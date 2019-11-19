import pprint, time
import win32com.client as w32c
import config
import jsonpickle


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
a = str(report)
thawed = jsonpickle.decode(report)
print(thawed)


$ C:/Users/cloud/AppData/Local/Programs/Python/Python37-32/python.exe "c:/Users/cloud/Desktop/projects/class_pangolin/code/taylor/Project_01/malicious_connections copy.py"
{'as_owner': 'Fastly',
 'asn': 54113,
 'continent': 'NA',
 'country': 'US',
 'detected_communicating_samples': [{'date': '2019-09-21 22:30:24',
                                     'positives': 57,
                                     'sha256': '5accacb1064e53c3d6f9232ad2704311c8fb60c352740a648f661e91bd30b963',
                                     'total': 73},
                                    {'date': '2019-07-15 23:09:38',
                                     'positives': 15,
                                     'sha256': '39e678456c030bec2132919823a3cf817f51f7a967adf1cf2a521dc19cc76e52',
                                     'total': 69},
                                    {'date': '2019-07-03 23:39:59',
                                     'positives': 12,
                                     'sha256': '37492f5ccfa386198da11a00ecafb43543f65271a2b4a16fb24f05e8ddd15f70',
                                     'total': 71}],
 'detected_downloaded_samples': [],
 'detected_referrer_samples': [],
 'detected_urls': [],
 'https_certificate_date': 1573841816,
 'last_https_certificate': {'cert_signature': {'signature': '997ed62fce1ba615f515b3eff130c11f541092a48c43c0bcbda50d0053e242c1856fe5a7a941994b46115addfde8276997b63ca60e2a30db3353be83b0aa0889047e6635e55cb32c287fa7b1e527796d812689eaa055517010cbeb43596baa52b446fdd2ff89168a45da0ebf870d53ef8324c517ad12634074804dbda4c9dd74d9df1c61020a71b093242f2da9207a43864411588a459bd75ce266eba6c6f17ca7dcddaf278939f7c19a99c87f347ad9397383cb7375bc16b04ea1492d09128d4e3e63fff08871df50462ba5383ddb3808972964decbc7eb887059dd62dc16762d306ae3a32f40a5360fcc0576d5e06e04403d6a215fbf4ea3a86cd09821b9bd',
                                               'signature_algorithm': 'sha256RSA'},
                            'extensions': {'1.3.6.1.4.1.11129.2.4.2': '048201e101df007600a4b90990b418581487bb13a2cc67700a3c359804f91bdf',
                                           'CA': True,
                                           'authority_key_identifier': {'keyid': '5168ff90af0207753cccd9656462a212b859723b'},
                                           'ca_information_access': {'CA Issuers': 'http://cacerts.digicert.com/DigiCertSHA2HighAssuranceServerCA.crt',
                                                                     'OCSP': 'http://ocsp.digicert.com'},
                                           'certificate_policies': ['2.16.840.1.114412.1.1',
                                                                    '2.23.140.1.2.2'],
                                           'crl_distribution_points': ['http://crl3.digicert.com/sha2-ha-server-g5.crl',
                                                                       'http://crl4.digicert.com/sha2-ha-server-g5.crl'],
                                           'extended_key_usage': ['serverAuth',
                                                                  'clientAuth'],
                                           'key_usage': ['ff'],
                                           'subject_alternative_name': ['www.github.com',
                                                                        '*.github.com',
                                                                        'github.com',
                                                                        '*.github.io',
                                                                        'github.io',
                                                                        '*.githubusercontent.com',
                                                                        'githubusercontent.com'],
                                           'subject_key_identifier': '308229d86d4ce0d4a2c61048058087a8bcaae912',
                                           'tags': []},
                            'issuer': {'C': 'US',
                                       'CN': 'DigiCert SHA2 High Assurance '
                                             'Server CA',
                                       'O': 'DigiCert Inc',
                                       'OU': 'www.digicert.com'},
                            'public_key': {'algorithm': 'RSA',
                                           'rsa': {'exponent': '010001',
                                                   'key_size': 2048,
                                                   'modulus': '00c6d3f18a3bcfa445f2cb7067d7459fa1698a4d6ef9dd4bf63eeb033666a5c7fee6a85aa2e41a8ae315901d0812a7285e760b562175822461ed80555c93e0c101b1e21ec13aedec295756b69761a9a8d0854d4efb52ca0d543ff13f2c7793e70f5fdcbcaea8cc899077c6cd7328360191ca0156b03e88edf6dd89099822c45c23b63bb6f5b702c55a437031dedeee7b5ebb6b8232fc4da79420db63089f7dedd9e80c3df20353f4dc2837f26adcb9face85de0ce1ede2209ea3503744ffe5fa5a624a9dc7c8f6d500ec23217f09f4a9039a8a2ee865baef31ad46e7734322817ed54e14bd3db7f131243571041f6c6771a103494cd1f15eff994d70312828eee7'}},
                            'serial_number': '83a84592f77f2e7951bf887cedec966',
                            'signature_algorithm': 'sha256RSA',
                            'size': 1964,
                            'subject': {'C': 'US',
                                        'CN': 'www.github.com',
                                        'L': 'San Francisco',
                                        'O': 'GitHub, Inc.',
                                        'ST': 'California'},
                            'tags': [],
                            'thumbprint': 'ccaa484866460e91532c9c7c232ab1744d299d33',
                            'thumbprint_sha256': 'd25d74b6e9af00715a4e5db82670492a0a6b910dc2febaf6bfa860c71437548f',
                            'validity': {'not_after': '2020-05-13 12:00:00',
                                         'not_before': '2017-03-23 00:00:00'},
                            'version': 'V3'},
 'network': '151.101.0.0/16',
 'resolutions': [{'hostname': '3xp10it.cc',
                  'last_resolved': '2019-11-04 12:05:03'},
                 {'hostname': 'admb-project.org',
                  'last_resolved': '2019-09-12 09:57:15'},
                 {'hostname': 'akarctichost.org',
                  'last_resolved': '2018-08-23 19:48:48'},
                 {'hostname': 'asyncdisplaykit.org',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'ax5.io', 'last_resolved': '2017-05-16 00:00:00'},
                 {'hostname': 'base.professionallyevil.com',
                  'last_resolved': '2016-11-04 00:00:00'},
                 {'hostname': 'benbahrman.com',
                  'last_resolved': '2019-09-30 05:28:47'},
                 {'hostname': 'bestmian.com',
                  'last_resolved': '2019-09-17 16:35:18'},
                 {'hostname': 'casesandberg.github.io',
                  'last_resolved': '2016-09-30 00:00:00'},
                 {'hostname': 'chixu.me',
                  'last_resolved': '2019-10-02 06:15:02'},
                 {'hostname': 'cjred.net',
                  'last_resolved': '2017-05-03 00:00:00'},
                 {'hostname': 'codyhansen.me',
                  'last_resolved': '2019-10-24 05:17:58'},
                 {'hostname': 'compbio.bccrc.ca',
                  'last_resolved': '2017-10-23 00:00:00'},
                 {'hostname': 'cpanel.tommyyuwang.com',
                  'last_resolved': '2019-10-17 15:41:45'},
                 {'hostname': 'cularuiz.com',
                  'last_resolved': '2016-11-27 00:00:00'},
                 {'hostname': 'darrenandroid.com',
                  'last_resolved': '2017-05-19 00:00:00'},
                 {'hostname': 'desmondchchan.com',
                  'last_resolved': '2019-09-13 11:59:55'},
                 {'hostname': 'dhruvmadeka.com',
                  'last_resolved': '2019-10-04 00:55:17'},
                 {'hostname': 'eastnwise.com',
                  'last_resolved': '2017-05-16 00:00:00'},
                 {'hostname': 'educateyo-self.com',
                  'last_resolved': '2016-11-12 00:00:00'},
                 {'hostname': 'facebook.design',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'fbinfer.com',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'ffanzhang.com',
                  'last_resolved': '2017-06-29 00:00:00'},
                 {'hostname': 'flogo.io',
                  'last_resolved': '2019-09-01 08:15:05'},
                 {'hostname': 'forty6fifty.com',
                  'last_resolved': '2017-04-22 00:00:00'},
                 {'hostname': 'frescolib.org',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'ghostf.com',
                  'last_resolved': '2017-01-14 00:00:00'},
                 {'hostname': 'ghostf.xyz',
                  'last_resolved': '2017-05-29 00:00:00'},
                 {'hostname': 'gist.githubusercontent.com',
                  'last_resolved': '2018-06-09 12:00:56'},
                 {'hostname': 'github.map.fastly.net',
                  'last_resolved': '2018-06-04 09:03:22'},
                 {'hostname': 'graphql.org',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'grindler.design',
                  'last_resolved': '2019-11-05 03:08:42'},
                 {'hostname': 'guizishanren.com',
                  'last_resolved': '2016-11-26 00:00:00'},
                 {'hostname': 'hackhouse.ca',
                  'last_resolved': '2017-05-19 00:00:00'},
                 {'hostname': 'hacklang.org',
                  'last_resolved': '2016-09-27 00:00:00'},
                 {'hostname': 'hajunsoo.org',
                  'last_resolved': '2016-11-19 00:00:00'},
                 {'hostname': 'haotliutechblog.tech',
                  'last_resolved': '2019-11-13 03:52:35'},
                 {'hostname': 'hhvm.com',
                  'last_resolved': '2016-10-05 00:00:00'},
                 {'hostname': 'hongday.net',
                  'last_resolved': '2016-12-12 00:00:00'},
                 {'hostname': 'inarticulatemedia.com',
                  'last_resolved': '2016-10-17 00:00:00'},
                 {'hostname': 'ivanfont.com',
                  'last_resolved': '2019-08-10 08:25:17'},
                 {'hostname': 'jaeyoon.org',
                  'last_resolved': '2017-04-30 00:00:00'},
                 {'hostname': 'jiehuangwei.wiki',
                  'last_resolved': '2019-10-21 16:35:30'},
                 {'hostname': 'jscreations.ca',
                  'last_resolved': '2017-11-04 00:00:00'},
                 {'hostname': 'kimfeeley.com',
                  'last_resolved': '2017-04-05 00:00:00'},
                 {'hostname': 'laudanum.professionallyevil.com',
                  'last_resolved': '2016-10-03 00:00:00'},
                 {'hostname': 'legend-exp.org',
                  'last_resolved': '2019-07-06 02:00:07'},
                 {'hostname': 'makeitopen.com',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'marshallhavefun.com',
                  'last_resolved': '2016-08-11 00:00:00'},
                 {'hostname': 'martincamacho.me',
                  'last_resolved': '2018-08-10 01:18:06'},
                 {'hostname': 'milestoneteam.com',
                  'last_resolved': '2019-10-04 13:22:51'},
                 {'hostname': 'mobisec.professionallyevil.com',
                  'last_resolved': '2016-10-13 00:00:00'},
                 {'hostname': 'morganandjoe.com',
                  'last_resolved': '2018-06-03 21:56:44'},
                 {'hostname': 'moxleystratton.com',
                  'last_resolved': '2019-10-03 23:48:36'},
                 {'hostname': 'myrocks.io',
                  'last_resolved': '2017-03-29 00:00:00'},
                 {'hostname': 'notoriousventures.com',
                  'last_resolved': '2019-06-19 13:55:36'},
                 {'hostname': 'origami.design',
                  'last_resolved': '2016-10-27 00:00:00'},
                 {'hostname': 'philhsmith.com',
                  'last_resolved': '2019-10-25 01:41:23'},
                 {'hostname': 'professionallyevil.com',
                  'last_resolved': '2016-10-03 00:00:00'},
                 {'hostname': 'qi-qian.com',
                  'last_resolved': '2019-09-27 07:17:51'},
                 {'hostname': 'qingwalashi.xyz',
                  'last_resolved': '2016-11-27 00:00:00'},
                 {'hostname': 'ranwu.me',
                  'last_resolved': '2017-02-22 00:00:00'},
                 {'hostname': 'raw.githubusercontent.com',
                  'last_resolved': '2019-07-04 08:26:57'},
                 {'hostname': 'riskybeverages.com',
                  'last_resolved': '2019-09-27 16:28:37'},
                 {'hostname': 'rocksdb.org',
                  'last_resolved': '2016-09-17 00:00:00'},
                 {'hostname': 'sergeysharp.com',
                  'last_resolved': '2019-04-06 07:51:07'},
                 {'hostname': 'shafou.com',
                  'last_resolved': '2016-08-27 00:00:00'},
                 {'hostname': 'shahlab.ca',
                  'last_resolved': '2018-10-04 22:50:08'},
                 {'hostname': 'sixyou.com',
                  'last_resolved': '2018-09-07 05:35:00'},
                 {'hostname': 'sofoya.net',
                  'last_resolved': '2018-07-25 00:36:21'},
                 {'hostname': 'theschuyler.com',
                  'last_resolved': '2019-08-30 10:51:38'},
                 {'hostname': 'tommyyuwang.com',
                  'last_resolved': '2019-10-17 15:41:41'},
                 {'hostname': 'trahelyk.com',
                  'last_resolved': '2019-09-28 05:39:28'},
                 {'hostname': 'u-root.tk',
                  'last_resolved': '2017-05-13 00:00:00'},
                 {'hostname': 'vulnpryer.net',
                  'last_resolved': '2016-11-11 00:00:00'},
                 {'hostname': 'waxybody.us',
                  'last_resolved': '2016-11-23 00:00:00'},
                 {'hostname': 'webmail.tommyyuwang.com',
                  'last_resolved': '2019-10-17 15:41:39'},
                 {'hostname': 'wowx.info',
                  'last_resolved': '2016-10-11 00:00:00'},
                 {'hostname': 'wushuning.com',
                  'last_resolved': '2019-11-05 09:37:49'},
                 {'hostname': 'www.bestmian.com',
                  'last_resolved': '2019-09-17 16:35:23'},
                 {'hostname': 'www.chixu.me',
                  'last_resolved': '2018-05-21 06:45:32'},
                 {'hostname': 'www.darrenandroid.com',
                  'last_resolved': '2017-07-15 00:00:00'},
                 {'hostname': 'www.errorpath.com',
                  'last_resolved': '2016-10-21 00:00:00'},
                 {'hostname': 'www.notoriousventures.com',
                  'last_resolved': '2016-12-24 00:00:00'},
                 {'hostname': 'www.opensource-helpdesk.com',
                  'last_resolved': '2016-11-20 00:00:00'},
                 {'hostname': 'www.professionallyevil.com',
                  'last_resolved': '2016-10-03 00:00:00'},
                 {'hostname': 'www.qi-qian.com',
                  'last_resolved': '2018-06-13 05:34:20'},
                 {'hostname': 'www.shafou.com',
                  'last_resolved': '2016-08-27 00:00:00'},
                 {'hostname': 'www.tommyyuwang.com',
                  'last_resolved': '2019-10-17 15:41:51'},
                 {'hostname': 'www.wowx.info',
                  'last_resolved': '2017-11-30 00:00:00'},
                 {'hostname': 'xlv5.pw',
                  'last_resolved': '2016-12-13 00:00:00'},
                 {'hostname': 'yidawang.org',
                  'last_resolved': '2019-01-08 12:30:17'},
                 {'hostname': 'yourgreatnessawaits.com',
                  'last_resolved': '2018-10-06 22:24:49'},
                 {'hostname': 'yutu.cloud',
                  'last_resolved': '2017-09-27 00:00:00'},
                 {'hostname': 'yyszfed.com',
                  'last_resolved': '2019-09-29 07:49:21'},
                 {'hostname': 'zaf1ro.com',
                  'last_resolved': '2017-03-17 00:00:00'},
                 {'hostname': 'zhipengli.net',
                  'last_resolved': '2018-03-05 00:00:00'},
                 {'hostname': 'zuf.co.kr',
                  'last_resolved': '2017-05-19 00:00:00'}],
 'response_code': 1,
 'undetected_communicating_samples': [{'date': '2018-07-02 02:38:37',
                                       'positives': 0,
                                       'sha256': '746905bc43ec98f6196281cf88c8e409ff1438cd818abf1e54abc24a432918be',
                                       'total': 69},
                                      {'date': '2018-07-02 02:34:05',
                                       'positives': 0,
                                       'sha256': '70e4400153ce03fee546799d5c0ab319774ab322f37db8ed176315d6bf479871',
                                       'total': 0},
                                      {'date': '2018-07-02 01:04:05',
                                       'positives': 0,
                                       'sha256': '6aa204d11198f9d4779429f9c8ba5729b1b901f9d602e153e3078a980b4aec91',
                                       'total': 69},
                                      {'date': '2018-07-02 01:09:29',
                                       'positives': 0,
                                       'sha256': 'f86fa79fef9ba686e802690b6fa935779fb73e683d5e462553be608b177b6b1c',
                                       'total': 65},
                                      {'date': '2018-07-01 08:28:50',
                                       'positives': 0,
                                       'sha256': 'a39bec6746465359470bc1486d8c17490d5c39e671c2ce6824f3773aa53ccef4',
                                       'total': 0},
                                      {'date': '2018-06-23 15:04:19',
                                       'positives': 0,
                                       'sha256': 'bb43a5d80f96f0ec28c48c8d648bb579e9c33ddaa7abf5986a13932ea51c476b',
                                       'total': 71},
                                      {'date': '2018-06-04 08:54:41',
                                       'positives': 0,
                                       'sha256': 'f3dfcf3060cc8da74fcf3eabe4e645d1aebb11ec2225a16c60d6f4ccc47ce74e',
                                       'total': 70}],
 'undetected_downloaded_samples': [{'date': '2019-04-19 17:44:31',
                                    'positives': 0,
                                    'sha256': '41d999d3821b0f692e4c2f7c6fb11b063d866692cd5085ad5755cf6e90d8758b',
                                    'total': 60},
                                   {'date': '2017-10-23 13:20:30',
                                    'positives': 0,
                                    'sha256': '9d6744bdf1646e0f6264e1fcdacdb194cb0c6180d2f4c14cae01200f5e8fc893',
                                    'total': 55},
                                   {'date': '2017-05-19 04:15:29',
                                    'positives': 0,
                                    'sha256': 'e074af54b3cdb81f8987fe8476c87c75e0d38b831b98ddfcabbe553ae783ebe3',
                                    'total': 57},
                                   {'date': '2016-10-27 18:26:30',
                                    'positives': 0,
                                    'sha256': 'a7b4cb3db2cf3d417e8e69528fde70b5ed09686cbf54cb06e5dd993dfa452670',
                                    'total': 56}],
 'undetected_referrer_samples': [{'date': '2019-06-29 23:01:39',
                                  'positives': 0,
                                  'sha256': '2b7eb310612c4a9a9cdf8c8a7a5d930e783974d017793403a6b6e7510198ca40',
                                  'total': 68}],
 'undetected_urls': [['http://chixu.me/',
                      'dda5282c8690ba716fdad14c55403bb3400fffeaf8b150a3cd6518cede35c2d4',
                      0,
                      71,
                      '2019-10-02 06:14:55'],
                     ['http://qi-qian.com/',
                      'a971e7ae6ddb1b1653d0dc371c18c754d6c5fdee5fc6c2813ab2105b11ac3676',
                      0,
                      71,
                      '2019-09-03 16:17:31'],
                     ['http://dhruvmadeka.com/',
                      '6115bad42793245a8bfd879373c66768201e2c830522d0d80abbac8608e10fe2',
                      0,
                      71,
                      '2019-08-22 06:13:10'],
                     ['http://ivanfont.com/',
                      '68a09413b51025ee02bc2ee7f02a78623d0dd8ad3fe7f29aa3a1c84ed79c9ebb',
                      0,
                      71,
                      '2019-08-10 14:07:56'],
                     ['http://legend-exp.org/',
                      '85b59208507a545698287045816016fcb3ca642d837ecf91ffcb4671d9daa05e',
                      0,
                      70,
                      '2019-07-02 05:10:25'],
                     ['http://trahelyk.com/',
                      '36946e1f81c7310375af60c2afb7918425a425740d884ba2e73b81fcc950738c',
                      '2019-06-13 13:57:51']],
 'verbose_msg': 'IP address in dataset',
 'whois': 'NetRange: 151.101.0.0 - 151.101.255.255\n'
          'CIDR: 151.101.0.0/16\n'
          'NetName: SKYCA-3\n'
          'NetHandle: NET-151-101-0-0-1\n'
          'Parent: RIPE-ERX-151 (NET-151-0-0-0-0)\n'
          'NetType: Direct Assignment\n'
          'OriginAS: \n'
          'Organization: Fastly (SKYCA-3)\n'
          'RegDate: 2016-02-01\n'
          'Updated: 2016-02-01\n'
'Ref: https://rdap.arin.net/registry/ip/151.101.0.0\n'
          'OrgName: Fastly\n'
          'OrgId: SKYCA-3\n'
          'Address: PO Box 78266\n'
          'City: San Francisco\n'
          'StateProv: CA\n'
          'PostalCode: 94107\n'
          'Country: US\n'
          'RegDate: 2011-09-16\n'
          'Updated: 2019-07-11\n'
          'Ref: https://rdap.arin.net/registry/entity/SKYCA-3\n'
          'OrgNOCHandle: FNO19-ARIN\n'
          'OrgNOCName: Fastly Network Operations\n'
          'OrgNOCPhone: +1-415-404-9374 \n'
          'OrgNOCEmail: noc@fastly.com\n'
          'OrgNOCRef: https://rdap.arin.net/registry/entity/FNO19-ARIN\n'
          'OrgTechHandle: FRA19-ARIN\n'
          'OrgTechName: Fastly RIR Administrator\n'
          'OrgTechPhone: +1-415-404-9374 \n'
          'OrgTechEmail: rir-admin@fastly.com\n'
          'OrgTechRef: https://rdap.arin.net/registry/entity/FRA19-ARIN\n'
          'OrgAbuseHandle: ABUSE4771-ARIN\n'
          'OrgAbuseName: Abuse Account\n'
          'OrgAbusePhone: +1-415-496-9353 \n'
          'OrgAbuseEmail: abuse@fastly.com\n'
          'OrgAbuseRef: https://rdap.arin.net/registry/entity/ABUSE4771-ARIN\n',
 'whois_timestamp': 1573510117}

# def replace(a):
#         return a.replace("'", '')
# print(report['resolutions'])


# resolutions_list = []
# for i in range(len(report['resolutions'])):
#         resolutions_list.append(report['resolutions'][i]['hostname'])
#         resolutions = f"Top Resolutions: {resolutions_list[0]}"
# print(resolutions)

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
