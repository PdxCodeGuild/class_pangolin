import psutil, config, requests, time, json, pprint, win32com.client as w32c

ip = '123'
message_subject = ''
message_body = ''

def remote_connections(connections):
    ''' Function that takes in a list of (IPv4, Port) connections and returns a (k, v) pair dictionary '''
    b = []
    for i in range(len(connections)):
        b.append(connections[i][4])
    return  dict(list(filter(None, b))) # Filter funciton removes empty (k, v) pairs in the list.

def virus_total(url, api_key, ip):
    ''' Function that sends an IP to through the Virus Total API and returns a python dict of the results. 
    public tier is 4 requests per minute '''
    params = {'apikey': api_key, 'ip':ip}
    return requests.get(url, params=params).json()

def send_outlook_mail(to_email, subject, body ):
    ''' Function to send out an email message from the local outlook system account '''
    outlook = w32c.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to_email
    mail.Subject = subject
    mail.Body = body #mail.HTMLBody = '<h2></h2>'; attachment  = "Path to the attachment"; mail.Attachments.Add(attachment)
    return mail.Send()


fetch_remote_system_connections = list(psutil.net_connections(kind='inet4'))
# Variable stores the remote connections (k, v) tupples as a dictionary
remote_connections_dict = remote_connections(fetch_remote_system_connections)
response = virus_total(config.virus_total_url, config.api_key, ip)
pprint.pprint((response['as_owner']))
send_outlook_mail(config.to_email, message_subject, message_body)