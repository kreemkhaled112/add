import requests

def youtube_subscribe(link):
    id = link.split('/')[-2]
    cookies = {
        'HSID': 'AQnxYIRF6p56Qpav1',
        'SSID': 'AJ2cYUtv4soIRdWsr',
        'APISID': 'OKYt2RSJZ7FBwCHW/Aku6aBgrT0EyIBA8y',
        'SAPISID': 'DVwgccRFcJvwXgfj/AFhOotICPpHTSXgZy',
        '__Secure-1PAPISID': 'DVwgccRFcJvwXgfj/AFhOotICPpHTSXgZy',
        '__Secure-3PAPISID': 'DVwgccRFcJvwXgfj/AFhOotICPpHTSXgZy',
        'LOGIN_INFO': 'AFmmF2swRQIgMvhKrD17c4nIsIhxJKonntP1vO5dT0vvXO0VuOaxanECIQCbnRM7rWV2VFJPG1xMubP4UoTk3u-3azQNeix4KKF_WQ:QUQ3MjNmeEFFX1I3T2p5R0ZwaVIxT1Q2Z3g4MXdyalgzRDVnUlE5TkZ3eUZ2bTJhSmJFbnVwU0NMbDZzQTk2WmtmREt3anVnLV9CZUtRcEk5SnNWSkRJUGRoYWlMWDVTU2dNOG05ZHozU21DTkdtNTJsd2dMWUUwRVlMQS1DWi1wYmVkOEdXNkJLR1NWVUliSUVEWVl2bFZfckVQQXNJLTZR',
        'DEVICE_INFO': 'ChxOekU1T1RZeU9EY3hNak14TnpjNU1qZzNNUT09EKvwqJ8GGKvwqJ8G',
        'VISITOR_INFO1_LIVE': 'IlZdTwFpZ4Y',
        'PREF': 'tz=Africa.Cairo&f6=400&f7=100&f5=30000',
        'SID': 'VwjhMbUI5ygXazMRZrFS-SWGmRHRaYpptmvak3ZGkalFxyj5vI7BRyG2Rx8bIMXoU_K7qg.',
        '__Secure-1PSID': 'VwjhMbUI5ygXazMRZrFS-SWGmRHRaYpptmvak3ZGkalFxyj5F2_E8YBWt_FJRHyFtg28ww.',
        '__Secure-3PSID': 'VwjhMbUI5ygXazMRZrFS-SWGmRHRaYpptmvak3ZGkalFxyj572o9nFN0RY0pPQArpO8hOw.',
        'YSC': 'kpEomEthq-o',
        'CONSISTENCY': 'ACeCFAVWmLybgUQvsvKdB1Ap-X5kdYnEQs-uv3R0aWTStAc15FKckz4j2H5a5ku-Yhmaz1fzlfCCnq8H9zJHfYivg5vYizc_1_yPMVaTVVzvUq1ULhzEr48pikQ',
        'SIDCC': 'AP8dLtyzG1_lD9WzMATX2sunuP3L6CpGVZCk0YHa2dDNFSm0B1C27s4ZgGZQRGGkdDiIGurytq0',
        '__Secure-1PSIDCC': 'AP8dLtzb3FHs790UkeZF3qyHswr5uOTlCDJBpdQmdpkXtHFskYJKwoVMnu3yiveFE_xTvvxY0Z4',
        '__Secure-3PSIDCC': 'AP8dLtxPbjrGZ57fvvRzuZIzKr--O2Hq048rUBSiOnC9GDccnTeGj-T9FbS-xtnoQUkSCKszMg',
    }

    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8,ar-EG;q=0.7',
        'authorization': 'SAPISIDHASH 1683180410_51c86aa2851eac77d4d033c39068e487ab29f653',
        'content-type': 'application/json',
        # 'cookie': 'HSID=AQnxYIRF6p56Qpav1; SSID=AJ2cYUtv4soIRdWsr; APISID=OKYt2RSJZ7FBwCHW/Aku6aBgrT0EyIBA8y; SAPISID=DVwgccRFcJvwXgfj/AFhOotICPpHTSXgZy; __Secure-1PAPISID=DVwgccRFcJvwXgfj/AFhOotICPpHTSXgZy; __Secure-3PAPISID=DVwgccRFcJvwXgfj/AFhOotICPpHTSXgZy; LOGIN_INFO=AFmmF2swRQIgMvhKrD17c4nIsIhxJKonntP1vO5dT0vvXO0VuOaxanECIQCbnRM7rWV2VFJPG1xMubP4UoTk3u-3azQNeix4KKF_WQ:QUQ3MjNmeEFFX1I3T2p5R0ZwaVIxT1Q2Z3g4MXdyalgzRDVnUlE5TkZ3eUZ2bTJhSmJFbnVwU0NMbDZzQTk2WmtmREt3anVnLV9CZUtRcEk5SnNWSkRJUGRoYWlMWDVTU2dNOG05ZHozU21DTkdtNTJsd2dMWUUwRVlMQS1DWi1wYmVkOEdXNkJLR1NWVUliSUVEWVl2bFZfckVQQXNJLTZR; DEVICE_INFO=ChxOekU1T1RZeU9EY3hNak14TnpjNU1qZzNNUT09EKvwqJ8GGKvwqJ8G; VISITOR_INFO1_LIVE=IlZdTwFpZ4Y; PREF=tz=Africa.Cairo&f6=400&f7=100&f5=30000; SID=VwjhMbUI5ygXazMRZrFS-SWGmRHRaYpptmvak3ZGkalFxyj5vI7BRyG2Rx8bIMXoU_K7qg.; __Secure-1PSID=VwjhMbUI5ygXazMRZrFS-SWGmRHRaYpptmvak3ZGkalFxyj5F2_E8YBWt_FJRHyFtg28ww.; __Secure-3PSID=VwjhMbUI5ygXazMRZrFS-SWGmRHRaYpptmvak3ZGkalFxyj572o9nFN0RY0pPQArpO8hOw.; YSC=kpEomEthq-o; CONSISTENCY=ACeCFAVWmLybgUQvsvKdB1Ap-X5kdYnEQs-uv3R0aWTStAc15FKckz4j2H5a5ku-Yhmaz1fzlfCCnq8H9zJHfYivg5vYizc_1_yPMVaTVVzvUq1ULhzEr48pikQ; SIDCC=AP8dLtyzG1_lD9WzMATX2sunuP3L6CpGVZCk0YHa2dDNFSm0B1C27s4ZgGZQRGGkdDiIGurytq0; __Secure-1PSIDCC=AP8dLtzb3FHs790UkeZF3qyHswr5uOTlCDJBpdQmdpkXtHFskYJKwoVMnu3yiveFE_xTvvxY0Z4; __Secure-3PSIDCC=AP8dLtxPbjrGZ57fvvRzuZIzKr--O2Hq048rUBSiOnC9GDccnTeGj-T9FbS-xtnoQUkSCKszMg',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/@shelbyscanada6774',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"112.0.5615.138"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-client-data': 'CI+2yQEIo7bJAQjEtskBCKmdygEIrO3KAQiWocsBCP+GzQEI7Z7NAQiFoM0BCL6izQEI0aLNAQifpM0BCIemzQEI1qbNAQjcps0BCIunzQEIkKrNAQikqs0BCNerzQEIn63NAQifhK0C',
        'x-goog-authuser': '0',
        'x-goog-visitor-id': 'CgtJbFpkVHdGcFo0WSiI4MqiBg%3D%3D',
        'x-origin': 'https://www.youtube.com',
        'x-youtube-bootstrap-logged-in': 'true',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20230502.04.00',
    }

    params = {
        'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'prettyPrint': 'false',
    }

    json_data = {
        'context': {
            'client': {
                'hl': 'ar',
                'gl': 'EG',
                'remoteHost': '156.219.238.176',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'CgtJbFpkVHdGcFo0WSiI4MqiBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20230502.04.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://www.youtube.com/@shelbyscanada6774',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CIjgyqIGENf_rgUQsJ-vBRC4i64FEKC3_hIQzPWuBRCi7K4FEKWZrwUQqrL-EhDMrv4SEIKdrwUQ4tSuBRDn964FELSVrwUQzN-uBRCRqa8FENShrwUQieiuBRDzqK8FEMK3_hIQ25uvBRDuoq8FEKKjrwUQ5LP-EhC9tq4FEMy3_hIQyJ2vBRCIi68FEJrargU%3D',
                },
                'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                'timeZone': 'Africa/Cairo',
                'browserName': 'Chrome',
                'browserVersion': '112.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekU1T1RZeU9EY3hNak14TnpjNU1qZzNNUT09EIjgyqIGGKvwqJ8G',
                'screenWidthPoints': 1365,
                'screenHeightPoints': 937,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 180,
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '4000000',
                'mainAppWebInfo': {
                    'graftUrl': 'https://www.youtube.com/@shelbyscanada6774',
                    'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                    'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                    'isWebNativeShareAvailable': True,
                },
            },
            'user': {
                'lockedSafetyMode': False,
            },
            'request': {
                'useSsl': True,
                'internalExperimentFlags': [],
                'consistencyTokenJars': [
                    {
                        'encryptedTokenJarContents': 'ACeCFAVWmLybgUQvsvKdB1Ap-X5kdYnEQs-uv3R0aWTStAc15FKckz4j2H5a5ku-Yhmaz1fzlfCCnq8H9zJHfYivg5vYizc_1_yPMVaTVVzvUq1ULhzEr48pikQ',
                        'expirationSeconds': '600',
                    },
                ],
            },
            'clientScreenNonce': 'MC4xNzk5NjUyNzcxNjY5MzM3OA..',
            'clickTracking': {
                'clickTrackingParams': 'CBcQmysiEwiGqsy069n-AhUnMvEFHZM_BjgyCWNoYW5uZWxzNA==',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1683180176321',
                    },
                    {
                        'key': 'flash',
                        'value': '0',
                    },
                    {
                        'key': 'frm',
                        'value': '0',
                    },
                    {
                        'key': 'u_tz',
                        'value': '180',
                    },
                    {
                        'key': 'u_his',
                        'value': '4',
                    },
                    {
                        'key': 'u_h',
                        'value': '1080',
                    },
                    {
                        'key': 'u_w',
                        'value': '1920',
                    },
                    {
                        'key': 'u_ah',
                        'value': '1040',
                    },
                    {
                        'key': 'u_aw',
                        'value': '1920',
                    },
                    {
                        'key': 'u_cd',
                        'value': '24',
                    },
                    {
                        'key': 'bc',
                        'value': '31',
                    },
                    {
                        'key': 'bih',
                        'value': '937',
                    },
                    {
                        'key': 'biw',
                        'value': '1348',
                    },
                    {
                        'key': 'brdim',
                        'value': '0,0,0,0,1920,0,1920,1040,1365,937',
                    },
                    {
                        'key': 'vis',
                        'value': '1',
                    },
                    {
                        'key': 'wgl',
                        'value': 'true',
                    },
                    {
                        'key': 'ca_type',
                        'value': 'image',
                    },
                ],
            },
        },
        'channelIds': [
            f'{id}',
        ],
        'params': 'EgIIAhgA',
    }

    response = requests.post(
        'https://www.youtube.com/youtubei/v1/subscription/subscribe',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
def youtube_like(link):
    id  = link.split('=')[1]

    cookies = {
        'DEVICE_INFO': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G',
        'VISITOR_INFO1_LIVE': 'Fh49y7MNqUM',
        'PREF': 'tz=Africa.Cairo',
        'SID': 'VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZjZQCujawfWu8Sxwt8sFP7Q.',
        '__Secure-1PSID': 'VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZ3IzIymNrZYg0jB4kbEW62A.',
        '__Secure-3PSID': 'VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZsukbZI68-qDkTKtSZRmFGA.',
        'HSID': 'A6LM4sZXbd7a7TBYw',
        'SSID': 'AX6c-hKAlNZiFhN3O',
        'APISID': 'Qfby6_ycdhS_cHlS/AzFNyTQUj92jDPx8A',
        'SAPISID': 'Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v',
        '__Secure-1PAPISID': 'Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v',
        '__Secure-3PAPISID': 'Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v',
        'YSC': 'uvkywVYtodw',
        'LOGIN_INFO': 'AFmmF2swRQIhAO_fRn6f1fCzUbvd2yfFOvzOetYg8Xp62j8N2vCPn3-9AiAPrmwUVS9LZ0pvOFf_ISgG-s8ZKMiHqRdfo54H1d78xg:QUQ3MjNmeWk5Zng3SXpUWGF2UWtiZjB4UFVDRi1NNEhOVmxHcnFCd1BvR2tEdUJwYkhmTERuT2RFeXF1NWdjelh4X2RjdnRfYm5pZ0lIdzZWaG5aZGg4NXJmSnU0aTFsOUtNdTV3dGRHNDN3WVhaLUJ2VmZwM0RRSnRwZlR3ai10aS0za2E1ekhmZFN2Qzd5a0Z4MUJ1MmNMLXRIT3ZUVGtWSUVmV0M5bE9hcHl1bWRZNF9tWFFRSlYzdmlXS3NSaTFvV2x3aG1pVVNpanl5ZkdCUFppOGFtRjNqN3FQa2pMQQ==',
        'CONSISTENCY': 'ACeCFAUivGb4KpS4KbCN9lZidv6-tdhDuFwobIdR-RXaBIRomZDmyvPdndbtT-0TyZxvfvPT--qmlhooDkB2XWhAZX5arwkJ3NUNKWgC76Enf1l2YxZw5whljP8',
        'SIDCC': 'AP8dLtyysMI5od9AQkUn4LdeBfihztofBQfrwlanWqFeQMHaM_DQ7M871WZOHcq-jD2phZEZiA',
        '__Secure-1PSIDCC': 'AP8dLtyzmqdejIQSBnsogBx4jX6k1mWr5ObpWrHzyitc4nPGDywSV1ZZY_nVLTmV4fOR3RMvJg8',
        '__Secure-3PSIDCC': 'AP8dLtz86lnVhJbxn5hN4TeMDVxe960tN5anpNJVtq4Gn85FOPI2_EWV9pXeUiqXcLLqZ_1NSA',
    }

    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8',
        'authorization': 'SAPISIDHASH 1683187546_0875b70a306d32269a0d9c0203e800c3f9682d84',
        'content-type': 'application/json',
        # 'cookie': 'DEVICE_INFO=ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G; VISITOR_INFO1_LIVE=Fh49y7MNqUM; PREF=tz=Africa.Cairo; SID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZjZQCujawfWu8Sxwt8sFP7Q.; __Secure-1PSID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZ3IzIymNrZYg0jB4kbEW62A.; __Secure-3PSID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZsukbZI68-qDkTKtSZRmFGA.; HSID=A6LM4sZXbd7a7TBYw; SSID=AX6c-hKAlNZiFhN3O; APISID=Qfby6_ycdhS_cHlS/AzFNyTQUj92jDPx8A; SAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; __Secure-1PAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; __Secure-3PAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; YSC=uvkywVYtodw; LOGIN_INFO=AFmmF2swRQIhAO_fRn6f1fCzUbvd2yfFOvzOetYg8Xp62j8N2vCPn3-9AiAPrmwUVS9LZ0pvOFf_ISgG-s8ZKMiHqRdfo54H1d78xg:QUQ3MjNmeWk5Zng3SXpUWGF2UWtiZjB4UFVDRi1NNEhOVmxHcnFCd1BvR2tEdUJwYkhmTERuT2RFeXF1NWdjelh4X2RjdnRfYm5pZ0lIdzZWaG5aZGg4NXJmSnU0aTFsOUtNdTV3dGRHNDN3WVhaLUJ2VmZwM0RRSnRwZlR3ai10aS0za2E1ekhmZFN2Qzd5a0Z4MUJ1MmNMLXRIT3ZUVGtWSUVmV0M5bE9hcHl1bWRZNF9tWFFRSlYzdmlXS3NSaTFvV2x3aG1pVVNpanl5ZkdCUFppOGFtRjNqN3FQa2pMQQ==; CONSISTENCY=ACeCFAUivGb4KpS4KbCN9lZidv6-tdhDuFwobIdR-RXaBIRomZDmyvPdndbtT-0TyZxvfvPT--qmlhooDkB2XWhAZX5arwkJ3NUNKWgC76Enf1l2YxZw5whljP8; SIDCC=AP8dLtyysMI5od9AQkUn4LdeBfihztofBQfrwlanWqFeQMHaM_DQ7M871WZOHcq-jD2phZEZiA; __Secure-1PSIDCC=AP8dLtyzmqdejIQSBnsogBx4jX6k1mWr5ObpWrHzyitc4nPGDywSV1ZZY_nVLTmV4fOR3RMvJg8; __Secure-3PSIDCC=AP8dLtz86lnVhJbxn5hN4TeMDVxe960tN5anpNJVtq4Gn85FOPI2_EWV9pXeUiqXcLLqZ_1NSA',
        'origin': 'https://www.youtube.com',
        'referer': f'https://www.youtube.com/watch?v={id}',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"112.0.5615.138"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-client-data': 'CI+2yQEIo7bJAQjEtskBCKmdygEIrO3KAQiUocsBCOiyzAEI/4bNAQjtns0BCIWgzQEIvqLNAQjRos0BCJ+kzQEIh6bNAQjXps0BCNymzQEIi6fNAQiQqs0BCKSqzQEI16vNAQifrc0BCM+uzQEIn4StAg==',
        'x-goog-authuser': '0',
        'x-goog-pageid': '109918954354469557451',
        'x-goog-visitor-id': 'CgtGaDQ5eTdNTnFVTSizmcuiBg%3D%3D',
        'x-origin': 'https://www.youtube.com',
        'x-youtube-bootstrap-logged-in': 'true',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20230502.04.00',
    }

    params = {
        'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'prettyPrint': 'false',
    }

    json_data = {
        'context': {
            'client': {
                'hl': 'ar',
                'gl': 'EG',
                'remoteHost': '156.219.238.176',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'CgtGaDQ5eTdNTnFVTSizmcuiBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20230502.04.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': f'https://www.youtube.com/watch?v={id}',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CLOZy6IGEKC3_hIQ7qKvBRDUoa8FEKqy_hIQieiuBRC4i64FEKWZrwUQ25uvBRDCt_4SEMu3_hIQ5_euBRDzqK8FEJGprwUQouyuBRDks_4SEMz1rgUQ4tSuBRC9tq4FEMzfrgUQzK7-EhDX_64F',
                },
                'timeZone': 'Africa/Cairo',
                'browserName': 'Chrome',
                'browserVersion': '112.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09ELOZy6IGGJfCpZ8G',
                'screenWidthPoints': 1072,
                'screenHeightPoints': 937,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 180,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '4000000',
                'mainAppWebInfo': {
                    'graftUrl': f'https://www.youtube.com/watch?v={id}',
                    'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                    'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                    'isWebNativeShareAvailable': True,
                },
            },
            'user': {
                'lockedSafetyMode': False,
            },
            'request': {
                'useSsl': True,
                'consistencyTokenJars': [
                    {
                        'encryptedTokenJarContents': 'ACeCFAUivGb4KpS4KbCN9lZidv6-tdhDuFwobIdR-RXaBIRomZDmyvPdndbtT-0TyZxvfvPT--qmlhooDkB2XWhAZX5arwkJ3NUNKWgC76Enf1l2YxZw5whljP8',
                    },
                ],
                'internalExperimentFlags': [],
            },
            'clickTracking': {
                'clickTrackingParams': 'CMUDEJhNIhMIwM2O4Iba_gIVP1tPBB2D2QUd',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1683187512314',
                    },
                    {
                        'key': 'flash',
                        'value': '0',
                    },
                    {
                        'key': 'frm',
                        'value': '0',
                    },
                    {
                        'key': 'u_tz',
                        'value': '180',
                    },
                    {
                        'key': 'u_his',
                        'value': '5',
                    },
                    {
                        'key': 'u_h',
                        'value': '1080',
                    },
                    {
                        'key': 'u_w',
                        'value': '1920',
                    },
                    {
                        'key': 'u_ah',
                        'value': '1040',
                    },
                    {
                        'key': 'u_aw',
                        'value': '1920',
                    },
                    {
                        'key': 'u_cd',
                        'value': '24',
                    },
                    {
                        'key': 'bc',
                        'value': '31',
                    },
                    {
                        'key': 'bih',
                        'value': '937',
                    },
                    {
                        'key': 'biw',
                        'value': '1055',
                    },
                    {
                        'key': 'brdim',
                        'value': '0,0,0,0,1920,0,1920,1040,1072,937',
                    },
                    {
                        'key': 'vis',
                        'value': '1',
                    },
                    {
                        'key': 'wgl',
                        'value': 'true',
                    },
                    {
                        'key': 'ca_type',
                        'value': 'image',
                    },
                ],
                'bid': 'ANyPxKo_PS3oPoXlLAKXvmbW-JcUVfjFBIFN04XiKQCl6Bzy8SeKRRYiqmBYigeK54GPIRfRoljX7-V2zVdOpth2-1qbVyaDxw',
            },
        },
        'target': {
            'videoId': f'{id}',
        },
        'params': 'Cg0KC283R3lGYTkwa2xnIAAyCwi0mcuiBhDjwI1l',
    }

    response = requests.post(
        'https://www.youtube.com/youtubei/v1/like/like',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    
    if response.status_code == 200:
     print(' successful!')
    else:
     print(' failed.')
