import psutil, config, requests, time, json, pprint, win32com.client as w32c

def remote_connections(connections):
    ''' Function that takes in a list of (IPv4, Port) connections and returns a (k, v) pair dictionary '''
    b = []
    for i in range(len(connections)):
        b.append(connections[i][4])
    return  dict(list(filter(None, b))) # Filter funciton removes empty (k, v) pairs in the list.

def virus_total(url, api_key, ip):
    ''' Virus Total API function, returns a python dict of the results '''
    params = {'apikey': api_key, 'ip':ip}
    report = requests.get(url, params=params).json()
    return format_and_send_report_email(report)

def time_virus_total_requests(ip_list):
    ''' Times the Virus Total API requests, 'Public Tier' is 4 calls per minute '''
    counter = len(ip_list)
    for i in range(len(ip_list)):
        virus_total(config.virus_total_url, config.api_key, ip_list[i])
        counter -= 1
        print('counter',counter)
        if counter == 0:
            break
        else:
            time.sleep(15)
            continue
def format_and_send_preamble_email(ip_list):

        connection_rows = '\n>    '.join(ip_list)
        message_subject_preamble = f"Warning: {len(ip_list)} Connection Reports in Queue."
        message_body_preamble = f"\nRemote Connections:\n\n>    {connection_rows}"
        return send_outlook_mail(config.to_email,message_subject_preamble, message_body_preamble)

def format_and_send_report_email(report):
        ''' This function formats the report email and calls the send_outlook_email() functions to deliver a report '''
        message_subject_report = f"Connection report {ip}"
        address_owner = f"\nAddress Owner: {report['as_owner']}"
        country_of_origin = f"Country of Origin: {report['country']}\n"
        # Retreives and stores the 2 most recent DNS resolutions for the given ip
        resolutions = 'None'
        whois_timestamp = 'None'
        try:
            whois_timestamp = f"Whois {time.strftime('Date: %m-%d-%Y',time.localtime(report['whois_timestamp']))}"
            resolutions_list = []
            for i in range(len(report['resolutions'])):
                resolutions_list.append(report['resolutions'][i]['hostname'])
                resolutions = f"Top Resolutions: {'; '.join(resolutions_list[0:2])}"
        except (KeyError, UnboundLocalError):
            print('Error1')
            resolutions = 'None'
            whois_timestamp = 'None'
            pass
        finally:

            pass
        try:
            print('samples length', len(list(report['detected_downloaded_samples'])))
            print('samples url length', len(list(report['detected_urls'])))
            if len(list(report['detected_downloaded_samples'])) > 0 or len(report['detected_urls']) > 0:
                message_subject_report = f"ALERT Suspicious Connection {ip}"
        except KeyError:
            print('Error2')
            pass
        finally:
            message_body_report = f"{address_owner}\n{country_of_origin}\n{whois_timestamp}\n{resolutions}"
            return send_outlook_mail(config.to_email,message_subject_report, message_body_report)

def send_outlook_mail(to_email, subject, body ):
    ''' Function to send out an email message from the local outlook system account '''
    outlook = w32c.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to_email
    mail.Subject = subject
    mail.Body = body #mail.HTMLBody = '<h2></h2>'; attachment  = "Path to the attachment"; mail.Attachments.Add(attachment)
    return mail.Send()


connections_dict = remote_connections(list(psutil.net_connections(kind='inet4')))
ip_list = list(connections_dict.keys())


format_and_send_preamble_email(ip_list)
time_virus_total_requests(ip_list)

