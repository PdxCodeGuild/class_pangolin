import pprint, time
import win32com.client as w32c
import config

report = {'as_owner': 'Microsoft Corporation',
 'asn': 8075,
 'continent': 'NA',
 'country': 'US',
 'detected_downloaded_samples': [],
 'detected_referrer_samples': [],
 'detected_urls': [7, 88],
 'https_certificate_date': 1573060489,
 'last_https_certificate': {'cert_signature': {'signature': '6880368aa42b13940a533881fbf476ee51a06de51ce1c7af2f56cd3a3d3a8baa625b8f4cf71383724130cb373bedaed2ea9e5681a592687c1346edc60966c56de205325f82bcb161fd5ed727457877aea5882a80cc463fa0a3a4d193acb0f3c7fe9c12cf1f1d44da3b64489b63766034c3f6715130b844694f75addc8f4be9d4e217c2f214d1d33005d87ae8dc12ed47a44acaf192c21db35858f5e966c6c9b25206c7740dd0f78bd96ff176fa07dea95c0b8a6deb7f9f50935c2d0156e766f34bac832c40d871dd37a5070960d9ce1312c2ad178dfe9b9f6d82fc3263c240f1eef2d3558844d9509eae3579c86f0867fe26f34de786d95f15ef6071feb3dbdc2f7724189bd28116f3ba173048f1aa866b9a90e43e1a11a4fffce7298bb9c0d99e5f0a310366311f4fc6d4f49519dd5e8cbc1188265ef29f412c5606109dbcc722a675bca08c8f9305463570137d5a36585684aa8f976bfdcc324b8fe69f49c6dd7df3187e26b3394302e8e516772e86990ad98f2bdcffa1691267178196b06554d88b1d1d5597737c6005dc62ed768515fc605c583bfadc0c786c0b5ab9fe59fdbb5641f1873923900aed561e6c7f26a916b1d07e08681d1e21317a8308df9c633052c2c4b5da6e1a518408d8c66b61168462cb65f808bd42dcb9d589a02498a6aa6d66a16815f067945689eeafd279e0aa01595e9fc6a0b2497c693e2fa408',
                                               'signature_algorithm': 'sha256RSA'},
                            'extensions': {'1.3.6.1.4.1.311.21.10': '3018300a06082b06010505070302300a06082b06010505070301',
                                           '1.3.6.1.4.1.311.21.7': '302f06272b060104018237150887da867583eed90182c9851b81b59e6185f4eb',
                                           'authority_key_identifier': {'keyid': '08fe259f74ea8704c2bcbb8ea8385f33c6d16c65'},
                                           'ca_information_access': {'CA Issuers': 'http://www.microsoft.com/pki/mscorp/Microsoft%20IT%20TLS%20CA%205.crt',
                                                                     'OCSP': 'http://ocsp.msocsp.com'},
                                           'certificate_policies': ['1.3.6.1.4.1.311.42.1'],
                                           'crl_distribution_points': ['http://mscrl.microsoft.com/pki/mscorp/crl/Microsoft%20IT%20TLS%20CA%205.crl'],
                                           'extended_key_usage': ['clientAuth',
                                                                  'serverAuth'],
                                           'key_usage': ['digitalSignature',
                                                         'keyEncipherment',
                                                         'dataEncipherment'],
                                           'subject_alternative_name': ['*.wns.windows.com'],
                                           'subject_key_identifier': '4d6cb09f31a7439e2baac8129f95d60df7d1aeda',
                                           'tags': []},
                            'issuer': {'C': 'US',
                                       'CN': 'Microsoft IT TLS CA 5',
                                       'L': 'Redmond',
                                       'O': 'Microsoft Corporation',
                                       'OU': 'Microsoft IT',
                                       'ST': 'Washington'},
                            'public_key': {'algorithm': 'RSA',
                                           'rsa': {'exponent': '010001',
                                                   'key_size': 2048,
                                                   'modulus': '00bfe1ffba04706b6761d8c9c142a12d465233aaca120fff611df72ff8fa70e29692ae17d255330a812e42f0f679a759c827b2ae8cd7078383d14b643ef1436df3d22fe171f5a97a833527f96e25ec1ce9e832dcebcddc9bc68ff4a7f813c3f3d5ae1b676be76d203b79f015339e40979ac710931cfdf5ac08bcfb902ea8412f9cf87835bd34723c03152d91750d20ba64c42d566b143fceb588ed23cba3ec7910b31bebf075455e627a5bb56b8df5f80fd29010ef43b2ef6f43b1bf22c6ab69f13a6d0ada774e2450f35aa83a1ecf3f8757cf94dc2b8af66b75bb579a9cf4edf0d644885c60a399a3074e656b34ecbac9a160420e530d9743410f06f5a7cbb66d'}},
                            'serial_number': '2d00024dc8bcaf57a4b922db66000000024dc8',
                            'signature_algorithm': 'sha256RSA',
                            'size': 1720,
                            'subject': {'CN': '*.wns.windows.com'},
                            'tags': [],
                            'thumbprint': 'dde1a145906b170592295775e121eb52521b9586',
                            'thumbprint_sha256': '016ecae37caf154e8416109eaf689762f10f2b22019c4bea557810b4990d7694',
                            'validity': {'not_after': '2020-03-13 22:31:32',
                                         'not_before': '2018-03-14 22:31:32'},
                            'version': 'V3'},
 'network': '52.140.0.0/14',
 'resolutions': [{'hostname': 'americas1.notify.windows.com.akadns.net',
                  'last_resolved': '2019-10-25 02:09:31'},
                 {'hostname': 'americas2.notify.windows.com.akadns.net',
                  'last_resolved': '2019-09-14 20:26:16'},
                 {'hostname': 'client.wns.windows.com',
                  'last_resolved': '2019-11-12 03:29:14'},
                 {'hostname': 'dm3p.wns.notify.windows.com.akadns.net',
                  'last_resolved': '2019-11-11 18:23:10'},
                 {'hostname': 'dm3p.wns.windows.com',
                  'last_resolved': '2019-10-26 12:41:39'},
                 {'hostname': 'skydrive.wns.windows.com',
                  'last_resolved': '2019-10-23 08:21:57'},
                 {'hostname': 'wns.notify.windows.com.akadns.net',
                  'last_resolved': '2019-11-09 18:12:08'},
                 {'hostname': 'wns.windows.com',
                  'last_resolved': '2019-11-05 15:14:30'}],
 'response_code': 1,
 'undetected_downloaded_samples': [],
 'undetected_referrer_samples': [{'date': '2019-11-06 17:09:00',
                                  'positives': 0,
                                  'sha256': 'e720901073c69cdd9454e7d2b7aaed4fc45e2125ede7ff24ac65d4d81697b23f',
                                  'total': 72},
                                 {'date': '2019-11-01 04:47:51',
                                  'positives': 0,
                                  'sha256': '76ff0110bf5d3b41be15c7027d58b3f2ad68e9ce7e120eb682fe2f5e5d874d34',
                                  'total': 73},
                                 {'date': '2019-10-09 02:17:02',
                                  'positives': 0,
                                  'sha256': '24e81bd3da955ec1c80ae9acafcf334ec0ce7abe88cc6985c26e0201a9ee7bb1',
                                  'total': 71}],
 'undetected_urls': [['https://client.wns.windows.com/',
                      '52d315778174f9b14cdfc82db611b5b9aca668c9d7eddbfed1887c18ce139b60',
                      0,
                      71,
                      '2019-11-12 12:31:15'],
                     ['http://client.wns.windows.com/',
                      '6c15c919fa2497c0bc72468d58550af7978c056492fa16b8a9eeeec7364278a6',
                      0,
                      71,
                      '2019-11-12 03:28:41'],
                     ['https://wns.windows.com/',
                      '08a29d3323468d83a1815c9ad6e097ce5097b7d2be1d38de54db7caf36053aa7',
                      0,
                      71,
                      '2019-10-30 01:00:24'],
                     ['http://52.141.217.125/',
                      '371ac5b483ae1a549ef505d653035777a0b66e3039e0969a33dbef31c927f425',
                      0,
                      71,
                      '2019-10-28 16:50:30'],
                     ['http://skydrive.wns.windows.com/',
                      '1b2476c19f163e7d7bcc45e507e7725f50a75fec0b91250c5f058b814887b19f',
                      0,
                      71,
                      '2019-10-25 17:23:00']],
 'verbose_msg': 'IP address in dataset',
 'whois': 'NetRange: 52.132.0.0 - 52.143.255.255\n'
          'CIDR: 52.136.0.0/13, 52.132.0.0/14\n'
          'NetName: MSFT\n'
          'NetHandle: NET-52-132-0-0-1\n'
          'Parent: NET52 (NET-52-0-0-0-0)\n'
          'NetType: Direct Assignment\n'
          'OriginAS: \n'
          'Organization: Microsoft Corporation (MSFT)\n'
          'RegDate: 2015-11-24\n'
          'Updated: 2017-06-12\n'
          'Ref: https://rdap.arin.net/registry/ip/52.132.0.0\n'
          'OrgName: Microsoft Corporation\n'
          'OrgId: MSFT\n'
          'Address: One Microsoft Way\n'
          'City: Redmond\n'
          'StateProv: WA\n'
          'PostalCode: 98052\n'
          'Country: US\n'
          'RegDate: 1998-07-09\n'
          'Updated: 2017-01-28\n'
          'Comment: To report suspected security issues specific to traffic '
          'emanating from Microsoft online services, including the '
          'distribution of malicious content or other illicit or illegal '
          'material through a Microsoft online service, please submit reports '
          'to:\n'
          'Comment: * https://cert.microsoft.com. \n'
          'Comment: \n'
          'Comment: For SPAM and other abuse issues, such as Microsoft '
          'Accounts, please contact:\n'
          'Comment: * abuse@microsoft.com. \n'
          'Comment: \n'
          'Comment: To report security vulnerabilities in Microsoft products '
          'and services, please contact:\n'
          'Comment: * secure@microsoft.com. \n'
          'Comment: \n'
          'Comment: For legal and law enforcement-related requests, please '
          'contact:\n'
          'Comment: * msndcc@microsoft.com\n'
          'Comment: \n'
          'Comment: For routing, peering or DNS issues, please \n'
          'Comment: contact:\n'
          'Comment: * IOC@microsoft.com\n'
          'Ref: https://rdap.arin.net/registry/entity/MSFT\n'
          'OrgAbuseHandle: MAC74-ARIN\n'
          'OrgAbuseName: Microsoft Abuse Contact\n'
          'OrgAbusePhone: +1-425-882-8080 \n'
          'OrgAbuseEmail: abuse@microsoft.com\n'
          'OrgAbuseRef: https://rdap.arin.net/registry/entity/MAC74-ARIN\n'
          'OrgTechHandle: MRPD-ARIN\n'
          'OrgTechName: Microsoft Routing, Peering, and DNS\n'
          'OrgTechPhone: +1-425-882-8080 \n'
          'OrgTechEmail: IOC@microsoft.com\n'
          'OrgTechRef: https://rdap.arin.net/registry/entity/MRPD-ARIN\n',
 'whois_timestamp': 1572779591}



# def replace(a):
#         return a.replace("'", '')
print(report['resolutions'])


resolutions_list = []
for i in range(len(report['resolutions'])):
        resolutions_list.append(report['resolutions'][i]['hostname'])
        resolutions = f"Top Resolutions: {resolutions_list[0]}"
print(resolutions)

# address_owner = f"\nAddress Owner: {a['as_owner']}"
# country_of_origin = f"Country of Origin: {a['country']}\n"
# whois_timestamp = f"Whois: {time.strftime('Date: %m-%d-%Y',time.localtime(a['whois_timestamp']))}"
# resolutions = f"Top Resolutions: {'; '.join(resolutions_list[0:2])}"

# print(address_owner)
# print(country_of_origin)s
# print(whois_timestamp)
# print(resolutions)

# message_subject_preamble = f"Warning: {len(ip_list)} Connection Reports in Queue."
# message_body_preamble = f"\nRemote Connections:\n\n>    {connection_rows}"

# def format_and_send_preamble_email(connections_dict):
#         ip_list = list(connections_dict.keys())
#         connection_rows = '\n>    '.join(ip_list)
#         message_subject_preamble = f"Warning: {len(ip_list)} Connection Reports in Queue."
#         message_body_preamble = f"\nRemote Connections:\n\n>    {connection_rows}"
#         return send_outlook_mail(config.to_email,message_subject_preamble, message_body_preamble)

# def format_and_send_report_email(report):
#         ''' This function formats the report email and calls the send_outlook_email() functions to deliver a report '''
#         address_owner = f"\nAddress Owner: {report['as_owner']}"
#         country_of_origin = f"Country of Origin: {report['country']}\n"
#         whois_timestamp = f"Whois {time.strftime('Date: %m-%d-%Y',time.localtime(report['whois_timestamp']))}"
#         # Retreives and stores the 2 most recent DNS resolutions for the given ip
#         resolutions_list = []
#         for i in range(len(report['resolutions'])):
#                 resolutions_list.append(report['resolutions'][i]['hostname'])
#                 resolutions = f"Top Resolutions: {'; '.join(resolutions_list[0:2])}"
#         # If there is a detection associated with the ip an alert subject line is sent
#         try:
#                 if len(list(report['detected_downloaded_samples'])) > 0 or len(list(report['detected_urls'])) > 0:
#                         message_subject_report = 'ALERT Suspicious Connection'
#                 else:
#                         message_subject_report = 'Connection report'
#         except KeyError:
#                 print('Key Error Raised')
#         # Email body message output
#         message_body_report = f"{address_owner}\n{country_of_origin}\n{whois_timestamp}\n{resolutions}"
#         return send_outlook_mail(config.to_email,message_subject_report, message_body_report)


# def send_outlook_mail(to_email, subject, body ):
#     ''' Function to send out an email message from the local outlook system account '''
#     outlook = w32c.Dispatch('outlook.application')
#     mail = outlook.CreateItem(0)
#     mail.To = to_email
#     mail.Subject = subject
#     mail.Body = body #mail.HTMLBody = '<h2></h2>'; attachment  = "Path to the attachment"; mail.Attachments.Add(attachment)
#     return mail.Send()

# format_and_send_report_email(report)
