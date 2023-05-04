import requests

def youtube_subscribe(link):
    id = link.split('/')[-2]
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
        'YSC': 'GNBvYYOjaDc',
        'CONSISTENCY': 'ACeCFAUvc-j8GzvAbZrFPxyTt3bo-jMazJ3ts3PjBwh_7gh0GS2ZGADOc-BPwUN2rfeGnYUW7Z_cTCBq_pztKzUEYymv4sbV2Dw1Bdnrlbuo_7gbufz7m44kNAE',
        'LOGIN_INFO': 'AFmmF2swRQIgRigljwkTHLhSUlxnCLoYxqxrweqg2Fz7VZ8ZeHirwwoCIQDe8SBJWZpey0WfJF6yb1b5VBkg7CZ7VO-irpH-WfslHQ:QUQ3MjNmd2VEQ2M4T09VcS1HTDN4amwzYnFFMjBheFpIekNvN19wWkFFRTZyUnZ3SGgzemVGVnN1dGoySU4tcXRwTGE1Ty1rMUl1Y1B4Rk44LXlYSVVmWjJwcXRwR0YzWFhuZjhRWjVHc0ZCMTQ3MDQwaGxNRjNjNzVMU0U5R1QyYnhSLVpUanAzaGRCRDJYdlNHaG12VmRWQ3ItYlRYUFVlS2p0bThNZ2dPdmp6a09MZU9BMXpGV09LcWltdFlUbFBJcDZxbTBuWVBKci04RE9Pa043VlZXT2F4MW9pZE1kQQ==',
        'SIDCC': 'AP8dLtzNz2B9qXlrGbrZc2UJ_HQgM-m2Ir4lzHg3mNl_i_27w4R0OLNo7Kr06o0kLBSRhATuWA',
        '__Secure-1PSIDCC': 'AP8dLtzr57qtI2fLDMgtIHECNusBVV0YoWPIO2r71odLNV0LJLta5o-bZ0uCpZrjBIuVRddy5nQ',
        '__Secure-3PSIDCC': 'AP8dLtyEMzP1_EgayqzZQl6TPNMqib1lPpPwVnVnc-bPsA6FPr9XdAX__cAqfMJdWTkOlUqlFA',
    }

    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8',
        'authorization': 'SAPISIDHASH 1683189445_9e1c3cd7d8e0ec39e4164b7faea8dd09e1b5e2a0',
        'content-type': 'application/json',
        # 'cookie': 'DEVICE_INFO=ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G; VISITOR_INFO1_LIVE=Fh49y7MNqUM; PREF=tz=Africa.Cairo; SID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZjZQCujawfWu8Sxwt8sFP7Q.; __Secure-1PSID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZ3IzIymNrZYg0jB4kbEW62A.; __Secure-3PSID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZsukbZI68-qDkTKtSZRmFGA.; HSID=A6LM4sZXbd7a7TBYw; SSID=AX6c-hKAlNZiFhN3O; APISID=Qfby6_ycdhS_cHlS/AzFNyTQUj92jDPx8A; SAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; __Secure-1PAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; __Secure-3PAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; YSC=GNBvYYOjaDc; CONSISTENCY=ACeCFAUvc-j8GzvAbZrFPxyTt3bo-jMazJ3ts3PjBwh_7gh0GS2ZGADOc-BPwUN2rfeGnYUW7Z_cTCBq_pztKzUEYymv4sbV2Dw1Bdnrlbuo_7gbufz7m44kNAE; LOGIN_INFO=AFmmF2swRQIgRigljwkTHLhSUlxnCLoYxqxrweqg2Fz7VZ8ZeHirwwoCIQDe8SBJWZpey0WfJF6yb1b5VBkg7CZ7VO-irpH-WfslHQ:QUQ3MjNmd2VEQ2M4T09VcS1HTDN4amwzYnFFMjBheFpIekNvN19wWkFFRTZyUnZ3SGgzemVGVnN1dGoySU4tcXRwTGE1Ty1rMUl1Y1B4Rk44LXlYSVVmWjJwcXRwR0YzWFhuZjhRWjVHc0ZCMTQ3MDQwaGxNRjNjNzVMU0U5R1QyYnhSLVpUanAzaGRCRDJYdlNHaG12VmRWQ3ItYlRYUFVlS2p0bThNZ2dPdmp6a09MZU9BMXpGV09LcWltdFlUbFBJcDZxbTBuWVBKci04RE9Pa043VlZXT2F4MW9pZE1kQQ==; SIDCC=AP8dLtzNz2B9qXlrGbrZc2UJ_HQgM-m2Ir4lzHg3mNl_i_27w4R0OLNo7Kr06o0kLBSRhATuWA; __Secure-1PSIDCC=AP8dLtzr57qtI2fLDMgtIHECNusBVV0YoWPIO2r71odLNV0LJLta5o-bZ0uCpZrjBIuVRddy5nQ; __Secure-3PSIDCC=AP8dLtyEMzP1_EgayqzZQl6TPNMqib1lPpPwVnVnc-bPsA6FPr9XdAX__cAqfMJdWTkOlUqlFA',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/@LukesEnglishPodcast',
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
        'x-goog-pageid': '100706374690481630592',
        'x-goog-visitor-id': 'CgtGaDQ5eTdNTnFVTSitqMuiBg%3D%3D',
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
                'visitorData': 'CgtGaDQ5eTdNTnFVTSitqMuiBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20230502.04.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://www.youtube.com/@LukesEnglishPodcast',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CK2oy6IGEL22rgUQ25uvBRDMt_4SEKqy_hIQsJ-vBRCJ6K4FELiLrgUQzPWuBRDyqK8FEMyu_hIQtuCuBRDn964FEJGprwUQoLf-EhDCt_4SENShrwUQ4tSuBRDuoq8FEMzfrgUQouyuBRDX_64FEOSz_hIQgZ2vBRClma8FEKa-_hI%3D',
                },
                'timeZone': 'Africa/Cairo',
                'browserName': 'Chrome',
                'browserVersion': '112.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EK2oy6IGGJfCpZ8G',
                'screenWidthPoints': 1072,
                'screenHeightPoints': 937,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 180,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '4000000',
                'mainAppWebInfo': {
                    'graftUrl': 'https://www.youtube.com/@LukesEnglishPodcast',
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
                        'encryptedTokenJarContents': 'ACeCFAUvc-j8GzvAbZrFPxyTt3bo-jMazJ3ts3PjBwh_7gh0GS2ZGADOc-BPwUN2rfeGnYUW7Z_cTCBq_pztKzUEYymv4sbV2Dw1Bdnrlbuo_7gbufz7m44kNAE',
                    },
                ],
                'internalExperimentFlags': [],
            },
            'clientScreenNonce': 'MC4zNTkyMTYxNjY2MzY3ODQ4',
            'clickTracking': {
                'clickTrackingParams': 'CBcQmysiEwi61efwjdr-AhUyHAYAHUxSCZAyCWNoYW5uZWxzNA==',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1683189430809',
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
                        'value': '9',
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
                'bid': 'ANyPxKqh97F35xHOO_Ewlb_CEdGBsgJ_UkgnbA79oRRWhLMZEIUSHFB4pIOWebC9jc61RhjoAAWTdOdg91xQaUn6U-SnQe1tGA',
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
    print(id)
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
        'YSC': 'GNBvYYOjaDc',
        'LOGIN_INFO': 'AFmmF2swRQIhAJu0fyHEb_rBFdS2Yayi5izKdGotI-7FXtwRmOx8tHbaAiBT5vf8SUC8dVP-7vjnVgP0azsEC3OK5Y8jjJMSZTlQ7A:QUQ3MjNmeVBPcGd6emFKbHlKRnJhWmN6YTZnRHdIclpLM3RSbEM5c0ZyQzB5MzU4aF9hdF9fNTA4MUdtcjAxYk80SXRIN0t6QmRZWVkzTmhEcTk1bHY5Sm5qUEpKeXVoNU1KT3AwZnpEMmlBc1lMMjBWcjBtZUhWRXVpYXlyTFlNWkZhc2FsMzF6U215ak90RldKYVJLTWhCS2JGQ1AxNnZVVEFaRlFHYVJsTDFoQlEzLWtjWDJMb2pDZUNYS0lpbmp2QzhVZlBaLWpuZEYyQ09fQUg5NVlVSlp3YnNQV2twQQ==',
        'SIDCC': 'AP8dLtzC0w0hEo7YheXkIyPZ3pFvcmEDJT6Y4Gql2Hw6maLvUShYqgvfANwtSuq2HkClcgO_PA',
        '__Secure-1PSIDCC': 'AP8dLty0fH1YxUoWDHsT1gthvrDnEV91YsR8BxFpOyPpDhzhZZ6eW6z0wZajy_ssin3Wkfg0ymk',
        '__Secure-3PSIDCC': 'AP8dLtxfVZU40lGZjE7feW5frTPGlOW3K2aEXHSt8UWnEaVAX-Y0Se_mXW3bcgHPqFIU4LWfbQ',
    }

    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8',
        'authorization': 'SAPISIDHASH 1683188628_79a9c84926e21af220f9e93142e124e35f09bdd7',
        'content-type': 'application/json',
        # 'cookie': 'DEVICE_INFO=ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G; VISITOR_INFO1_LIVE=Fh49y7MNqUM; PREF=tz=Africa.Cairo; SID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZjZQCujawfWu8Sxwt8sFP7Q.; __Secure-1PSID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZ3IzIymNrZYg0jB4kbEW62A.; __Secure-3PSID=VwgwuAGQHNoj7X1EcV_EWXWTMkrjXHz95CpfUbQKT4l1E1sZsukbZI68-qDkTKtSZRmFGA.; HSID=A6LM4sZXbd7a7TBYw; SSID=AX6c-hKAlNZiFhN3O; APISID=Qfby6_ycdhS_cHlS/AzFNyTQUj92jDPx8A; SAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; __Secure-1PAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; __Secure-3PAPISID=Hmz-8IZ_DDXDQDwS/Ad9i3-e4T5VgFT95v; YSC=GNBvYYOjaDc; LOGIN_INFO=AFmmF2swRQIhAJu0fyHEb_rBFdS2Yayi5izKdGotI-7FXtwRmOx8tHbaAiBT5vf8SUC8dVP-7vjnVgP0azsEC3OK5Y8jjJMSZTlQ7A:QUQ3MjNmeVBPcGd6emFKbHlKRnJhWmN6YTZnRHdIclpLM3RSbEM5c0ZyQzB5MzU4aF9hdF9fNTA4MUdtcjAxYk80SXRIN0t6QmRZWVkzTmhEcTk1bHY5Sm5qUEpKeXVoNU1KT3AwZnpEMmlBc1lMMjBWcjBtZUhWRXVpYXlyTFlNWkZhc2FsMzF6U215ak90RldKYVJLTWhCS2JGQ1AxNnZVVEFaRlFHYVJsTDFoQlEzLWtjWDJMb2pDZUNYS0lpbmp2QzhVZlBaLWpuZEYyQ09fQUg5NVlVSlp3YnNQV2twQQ==; SIDCC=AP8dLtzC0w0hEo7YheXkIyPZ3pFvcmEDJT6Y4Gql2Hw6maLvUShYqgvfANwtSuq2HkClcgO_PA; __Secure-1PSIDCC=AP8dLty0fH1YxUoWDHsT1gthvrDnEV91YsR8BxFpOyPpDhzhZZ6eW6z0wZajy_ssin3Wkfg0ymk; __Secure-3PSIDCC=AP8dLtxfVZU40lGZjE7feW5frTPGlOW3K2aEXHSt8UWnEaVAX-Y0Se_mXW3bcgHPqFIU4LWfbQ',
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
        'x-goog-pageid': '101857047718780115111',
        'x-goog-visitor-id': 'CgtGaDQ5eTdNTnFVTSjnocuiBg%3D%3D',
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
                'visitorData': 'CgtGaDQ5eTdNTnFVTSjnocuiBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20230502.04.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': f'https://www.youtube.com/watch?v={id}',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'COehy6IGEL22rgUQy7f-EhCi7K4FEOf3rgUQoLf-EhDM364FEO6irwUQtaavBRCJ6K4FEKqy_hIQzK7-EhCRqa8FEOSz_hIQ86ivBRClma8FELiLrgUQ25uvBRDi1K4FEMK3_hIQsJ-vBRDUoa8FENf_rgUQzPWuBRCbnq8FEMvA_hI%3D',
                },
                'timeZone': 'Africa/Cairo',
                'browserName': 'Chrome',
                'browserVersion': '112.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EOehy6IGGJfCpZ8G',
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
                'internalExperimentFlags': [],
                'consistencyTokenJars': [],
            },
            'clickTracking': {
                'clickTrackingParams': 'CM8DEJhNIhMI9sPm4Ira_gIV04tRCh36vQLL',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1683188594350',
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
                        'value': '6',
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
                'bid': 'ANyPxKqcLbXTEOK6riYRr3echnocMybvXiBwvwzoe006ZgOJNJa5gwxeWPHOJc3DKKZvlMgWYVMi4p-hJcQCn1EWoHxQV74fYQ',
            },
        },
        'target': {
            'videoId': f'{id}',
        },
        'params': 'Cg0KC2h1aW9fTzA4R3dzIAAyDAjnocuiBhDL1r2dAg%3D%3D',
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

