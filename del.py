# a = {
#   'version': '0',
#   'id': 'cf38ec12-fd19-0340-54a0-9fca72584bbf',
#   'detail-type': 'AWS API Call via CloudTrail',
#   'source': 'aws.ec2',
#   'account': '464599248654',
#   'time': '2021-10-05T01:23:53Z',
#   'region': 'ap-south-1',
#   'resources': [
#
#   ],
#   'detail': {
#     'eventVersion': '1.08',
#     'userIdentity': {
#       'type': 'IAMUser',
#       'principalId': 'AIDAWYLCF54HM3NRISBCJ',
#       'arn': 'arn:aws:iam::464599248654:user/Avinash',
#       'accountId': '464599248654',
#       'accessKeyId': 'ASIAWYLCF54HJMBYQOM6',
#       'userName': 'Avinash',
#       'sessionContext': {
#         'sessionIssuer': {
#
#         },
#         'webIdFederationData': {
#
#         },
#         'attributes': {
#           'creationDate': '2021-10-04T23:52:59Z',
#           'mfaAuthenticated': 'false'
#         }
#       }
#     },
#     'eventTime': '2021-10-05T01:23:53Z',
#     'eventSource': 'ec2.amazonaws.com',
#     'eventName': 'RunInstances',
#     'awsRegion': 'ap-south-1',
#     'sourceIPAddress': '122.171.246.199',
#     'userAgent': 'console.ec2.amazonaws.com',
#     'requestParameters': {
#       'instancesSet': {
#         'items': [
#           {
#             'imageId': 'ami-0a23ccb2cdd9286bb',
#             'minCount': 1,
#             'maxCount': 1,
#             'keyName': 'avi-jes-mumbai'
#           }
#         ]
#       },
#       'instanceType': 't2.micro',
#       'blockDeviceMapping': {
#         'items': [
#           {
#             'deviceName': '/dev/xvda',
#             'ebs': {
#               'volumeSize': 8,
#               'deleteOnTermination': True,
#               'volumeType': 'gp2'
#             }
#           }
#         ]
#       },
#       'availabilityZone': 'ap-south-1b',
#       'tenancy': 'default',
#       'monitoring': {
#         'enabled': False
#       },
#       'disableApiTermination': False,
#       'disableApiStop': False,
#       'networkInterfaceSet': {
#         'items': [
#           {
#             'deviceIndex': 0,
#             'subnetId': 'subnet-10873c5c',
#             'description': 'Primary network interface',
#             'deleteOnTermination': True,
#             'associatePublicIpAddress': True,
#             'groupSet': {
#               'items': [
#                 {
#                   'groupId': 'sg-7ffedc12'
#                 }
#               ]
#             },
#             'ipv6AddressCount': 0,
#             'networkCardIndex': 0
#           }
#         ]
#       },
#       'ebsOptimized': False,
#       'hibernationOptions': {
#         'configured': False
#       },
#       'metadataOptions': {
#         'httpTokens': 'optional',
#         'httpPutResponseHopLimit': 1,
#         'httpEndpoint': 'enabled'
#       }
#     },
#     'responseElements': {
#       'requestId': '1884bf83-9c14-4c3d-9e81-1715200202e8',
#       'reservationId': 'r-0c5e9f48a02bf8c99',
#       'ownerId': '464599248654',
#       'groupSet': {
#
#       },
#       'instancesSet': {
#         'items': [
#           {
#             'instanceId': 'i-06619ac2c16e394fb',
#             'imageId': 'ami-0a23ccb2cdd9286bb',
#             'instanceState': {
#               'code': 0,
#               'name': 'pending'
#             },
#             'privateDnsName': 'ip-172-31-12-245.ap-south-1.compute.internal',
#             'keyName': 'avi-jes-mumbai',
#             'amiLaunchIndex': 0,
#             'productCodes': {
#
#             },
#             'instanceType': 't2.micro',
#             'launchTime': 1633397033000,
#             'placement': {
#               'availabilityZone': 'ap-south-1b',
#               'tenancy': 'default'
#             },
#             'monitoring': {
#               'state': 'disabled'
#             },
#             'subnetId': 'subnet-10873c5c',
#             'vpcId': 'vpc-e664488e',
#             'privateIpAddress': '172.31.12.245',
#             'stateReason': {
#               'code': 'pending',
#               'message': 'pending'
#             },
#             'architecture': 'x86_64',
#             'rootDeviceType': 'ebs',
#             'rootDeviceName': '/dev/xvda',
#             'blockDeviceMapping': {
#
#             },
#             'virtualizationType': 'hvm',
#             'hypervisor': 'xen',
#             'groupSet': {
#               'items': [
#                 {
#                   'groupId': 'sg-7ffedc12',
#                   'groupName': 'default'
#                 }
#               ]
#             },
#             'sourceDestCheck': True,
#             'networkInterfaceSet': {
#               'items': [
#                 {
#                   'networkInterfaceId': 'eni-0050a40c3e987b2aa',
#                   'subnetId': 'subnet-10873c5c',
#                   'vpcId': 'vpc-e664488e',
#                   'description': 'Primary network interface',
#                   'ownerId': '464599248654',
#                   'status': 'in-use',
#                   'macAddress': '0a:fd:14:7a:ee:52',
#                   'privateIpAddress': '172.31.12.245',
#                   'privateDnsName': 'ip-172-31-12-245.ap-south-1.compute.internal',
#                   'sourceDestCheck': True,
#                   'interfaceType': 'interface',
#                   'groupSet': {
#                     'items': [
#                       {
#                         'groupId': 'sg-7ffedc12',
#                         'groupName': 'default'
#                       }
#                     ]
#                   },
#                   'attachment': {
#                     'attachmentId': 'eni-attach-063fdecfbff1af10d',
#                     'deviceIndex': 0,
#                     'networkCardIndex': 0,
#                     'status': 'attaching',
#                     'attachTime': 1633397033000,
#                     'deleteOnTermination': True
#                   },
#                   'privateIpAddressesSet': {
#                     'item': [
#                       {
#                         'privateIpAddress': '172.31.12.245',
#                         'privateDnsName': 'ip-172-31-12-245.ap-south-1.compute.internal',
#                         'primary': True
#                       }
#                     ]
#                   },
#                   'ipv6AddressesSet': {
#
#                   },
#                   'tagSet': {
#
#                   }
#                 }
#               ]
#             },
#             'ebsOptimized': False,
#             'enaSupport': True,
#             'cpuOptions': {
#               'coreCount': 1,
#               'threadsPerCore': 1
#             },
#             'capacityReservationSpecification': {
#               'capacityReservationPreference': 'open'
#             },
#             'hibernationOptions': {
#               'configured': False
#             },
#             'enclaveOptions': {
#               'enabled': False
#             },
#             'metadataOptions': {
#               'state': 'pending',
#               'httpTokens': 'optional',
#               'httpPutResponseHopLimit': 1,
#               'httpEndpoint': 'enabled',
#               'httpProtocolIpv4': 'enabled',
#               'httpProtocolIpv6': 'disabled'
#             }
#           }
#         ]
#       }
#     },
#     'requestID': '1884bf83-9c14-4c3d-9e81-1715200202e8',
#     'eventID': 'f1b71119-09e0-48ba-8215-3f8a050cbafe',
#     'readOnly': False,
#     'eventType': 'AwsApiCall',
#     'managementEvent': True,
#     'recipientAccountId': '464599248654',
#     'eventCategory': 'Management'
#   }
# }
#
#
# print(a['detail']['responseElements']['instancesSet']['items'][0]['instanceId'])



b = {
  'Reservations': [
    {
      'Groups': [

      ],
      'Instances': [
        {
          'AmiLaunchIndex': 0,
          'ImageId': 'ami-0a23ccb2cdd9286bb',
          'InstanceId': 'i-04af8b6723bcbb237',
          'InstanceType': 't2.micro',
          'KeyName': 'avi-jes-mumbai',
          'Monitoring': {
            'State': 'disabled'
          },
          'Placement': {
            'AvailabilityZone': 'ap-south-1a',
            'GroupName': '',
            'Tenancy': 'default'
          },
          'PrivateDnsName': 'ip-172-31-24-183.ap-south-1.compute.internal',
          'PrivateIpAddress': '172.31.24.183',
          'ProductCodes': [

          ],
          'PublicDnsName': 'ec2-13-126-91-252.ap-south-1.compute.amazonaws.com',
          'PublicIpAddress': '13.126.91.252',
          'State': {
            'Code': 0,
            'Name': 'pending'
          },
          'StateTransitionReason': '',
          'SubnetId': 'subnet-1ad79d72',
          'VpcId': 'vpc-e664488e',
          'Architecture': 'x86_64',
          'BlockDeviceMappings': [
            {
              'DeviceName': '/dev/xvda',
              'Ebs': {
                'DeleteOnTermination': True,
                'Status': 'attaching',
                'VolumeId': 'vol-03bf0c8916f07bbed'
              }
            }
          ],
          'ClientToken': '',
          'EbsOptimized': False,
          'EnaSupport': True,
          'Hypervisor': 'xen',
          'NetworkInterfaces': [
            {
              'Association': {
                'IpOwnerId': 'amazon',
                'PublicDnsName': 'ec2-13-126-91-252.ap-south-1.compute.amazonaws.com',
                'PublicIp': '13.126.91.252'
              },
              'Attachment': {
                'AttachmentId': 'eni-attach-0f26c61f190c32050',
                'DeleteOnTermination': True,
                'DeviceIndex': 0,
                'Status': 'attaching',
                'NetworkCardIndex': 0
              },
              'Description': '',
              'Groups': [
                {
                  'GroupName': 'launch-wizard-5',
                  'GroupId': 'sg-077fb317eabbe4e1d'
                }
              ],
              'Ipv6Addresses': [

              ],
              'MacAddress': '02:97:91:4c:7e:5a',
              'NetworkInterfaceId': 'eni-036597032b5841400',
              'OwnerId': '464599248654',
              'PrivateDnsName': 'ip-172-31-24-183.ap-south-1.compute.internal',
              'PrivateIpAddress': '172.31.24.183',
              'PrivateIpAddresses': [
                {
                  'Association': {
                    'IpOwnerId': 'amazon',
                    'PublicDnsName': 'ec2-13-126-91-252.ap-south-1.compute.amazonaws.com',
                    'PublicIp': '13.126.91.252'
                  },
                  'Primary': True,
                  'PrivateDnsName': 'ip-172-31-24-183.ap-south-1.compute.internal',
                  'PrivateIpAddress': '172.31.24.183'
                }
              ],
              'SourceDestCheck': True,
              'Status': 'in-use',
              'SubnetId': 'subnet-1ad79d72',
              'VpcId': 'vpc-e664488e',
              'InterfaceType': 'interface'
            }
          ],
          'RootDeviceName': '/dev/xvda',
          'RootDeviceType': 'ebs',
          'SecurityGroups': [
            {
              'GroupName': 'launch-wizard-5',
              'GroupId': 'sg-077fb317eabbe4e1d'
            }
          ],
          'SourceDestCheck': True,
          'VirtualizationType': 'hvm',
          'CpuOptions': {
            'CoreCount': 1,
            'ThreadsPerCore': 1
          },
          'CapacityReservationSpecification': {
            'CapacityReservationPreference': 'open'
          },
          'HibernationOptions': {
            'Configured': False
          },
          'MetadataOptions': {
            'State': 'pending',
            'HttpTokens': 'optional',
            'HttpPutResponseHopLimit': 1,
            'HttpEndpoint': 'enabled'
          },
          'EnclaveOptions': {
            'Enabled': False
          }
        }
      ],
      'OwnerId': '464599248654',
      'ReservationId': 'r-094104d90308c6f27'
    }
  ],
  'ResponseMetadata': {
    'RequestId': 'a9363a46-c22d-43f6-9798-7e716abc6288',
    'HTTPStatusCode': 200,
    'HTTPHeaders': {
      'x-amzn-requestid': 'a9363a46-c22d-43f6-9798-7e716abc6288',
      'cache-control': 'no-cache, no-store',
      'strict-transport-security': 'max-age=31536000; includeSubDomains',
      'vary': 'accept-encoding',
      'content-type': 'text/xml;charset=UTF-8',
      'content-length': '7545',
      'date': 'Wed, 06 Oct 2021 00:00:05 GMT',
      'server': 'AmazonEC2'
    },
    'RetryAttempts': 0
  }
}


print(b['Reservations'][0]['Instances'][0]['BlockDeviceMappings'][0]['Ebs']['VolumeId'])