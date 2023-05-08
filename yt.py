import requests

def youtube_subscribe(link):
    id = link.split('/')[-2]
    import requests

    cookies = {
        'DEVICE_INFO': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G',
        'VISITOR_INFO1_LIVE': 'Fh49y7MNqUM',
        'PREF': 'tz=Africa.Cairo',
        'LOGIN_INFO': 'AFmmF2swRQIgBE6tB9HFLC8vpwmsXVKlNPu_awMQPxVOxOF4-rlqNGACIQCnthLOYasZsZQmk1BZnzQwE-2Yu4LANl_D1AA6seTJIw:QUQ3MjNmeGlteEM4SVpuS0ZLTkFkVWRtNXF3NHNya2k5Qy1aQm9Sb2lHT3VsQ1BsakgzUXlqV0lDd1hucjdwUWNjRXB2VHRQX1Bza19VRTNJX0F6NHJyaHNhS1hxNXFWVXdnUTlqQVFZUndtX3lLSzVzRkdJbmVHMndXcmQyRmVqc1RVd21JX3MtSGlESG5sYm1VU2FzaVdtdmQtOGxJSS1zYURXM1ZESy1OS2pPcVB2RmMydUV0RzA0VFExWnIxZjBJYkFwSUoyQ1BhaUtpQU10VmlNWmF3dEhnNndlSnBhUQ==',
        'SID': 'WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lDv-SBzrxcD7zWJnd_rg4_EQ.',
        '__Secure-1PSID': 'WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD8hLB7BJR8rcJ9c7ug5Kfwg.',
        '__Secure-3PSID': 'WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD2IQICxV7OI6F1RnkYP3WXA.',
        'HSID': 'As-YstmRuz3H3Luq7',
        'SSID': 'ACc9YjcVC3ES0HAoe',
        'APISID': 'E6KNVlV2EcA8DBqj/AYAN2GzYLaqs3RSoB',
        'SAPISID': 'FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG',
        '__Secure-1PAPISID': 'FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG',
        '__Secure-3PAPISID': 'FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG',
        'YSC': 'szLD4Eyjw1k',
        'CONSISTENCY': 'ACeCFAXP1EphhXWKb6w5O8siXhb6FS968IlyymCHcwAs8msdqnG86049lSSs2NITNH1avbQ-6n0Swbnz-dBOgR1wTcR0He5WsPJC27naFil6vw9RSBYabnfg4H8',
        'SIDCC': 'AP8dLtzKuqZctPEgskZTDNH1ekeeNyFj4fMAe0DbJ4ZFc3lW1w1MpIRVOnendd1okeLdWvI0Hg',
        '__Secure-1PSIDCC': 'AP8dLtx77zCuBaEOOUu7y02bfgyCEYOwmwuiDMItPDlEtDwziRjKOKkttUpGvoZXtNcmxsqzr1A',
        '__Secure-3PSIDCC': 'AP8dLtwGUrB4fNwbVa5NYwJYNu2alUmW36VBFehF6lJ3XmlEX23KXH838S5sf993pCohJpc6Rg',
    }

    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'en,en-US;q=0.9,ar;q=0.8',
        'authorization': 'SAPISIDHASH 1683534876_7b09cf9e97c358c4f46f47c54a919ae07c92f006',
        'content-type': 'application/json',
        # 'cookie': 'DEVICE_INFO=ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G; VISITOR_INFO1_LIVE=Fh49y7MNqUM; PREF=tz=Africa.Cairo; LOGIN_INFO=AFmmF2swRQIgBE6tB9HFLC8vpwmsXVKlNPu_awMQPxVOxOF4-rlqNGACIQCnthLOYasZsZQmk1BZnzQwE-2Yu4LANl_D1AA6seTJIw:QUQ3MjNmeGlteEM4SVpuS0ZLTkFkVWRtNXF3NHNya2k5Qy1aQm9Sb2lHT3VsQ1BsakgzUXlqV0lDd1hucjdwUWNjRXB2VHRQX1Bza19VRTNJX0F6NHJyaHNhS1hxNXFWVXdnUTlqQVFZUndtX3lLSzVzRkdJbmVHMndXcmQyRmVqc1RVd21JX3MtSGlESG5sYm1VU2FzaVdtdmQtOGxJSS1zYURXM1ZESy1OS2pPcVB2RmMydUV0RzA0VFExWnIxZjBJYkFwSUoyQ1BhaUtpQU10VmlNWmF3dEhnNndlSnBhUQ==; SID=WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lDv-SBzrxcD7zWJnd_rg4_EQ.; __Secure-1PSID=WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD8hLB7BJR8rcJ9c7ug5Kfwg.; __Secure-3PSID=WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD2IQICxV7OI6F1RnkYP3WXA.; HSID=As-YstmRuz3H3Luq7; SSID=ACc9YjcVC3ES0HAoe; APISID=E6KNVlV2EcA8DBqj/AYAN2GzYLaqs3RSoB; SAPISID=FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG; __Secure-1PAPISID=FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG; __Secure-3PAPISID=FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG; YSC=szLD4Eyjw1k; CONSISTENCY=ACeCFAXP1EphhXWKb6w5O8siXhb6FS968IlyymCHcwAs8msdqnG86049lSSs2NITNH1avbQ-6n0Swbnz-dBOgR1wTcR0He5WsPJC27naFil6vw9RSBYabnfg4H8; SIDCC=AP8dLtzKuqZctPEgskZTDNH1ekeeNyFj4fMAe0DbJ4ZFc3lW1w1MpIRVOnendd1okeLdWvI0Hg; __Secure-1PSIDCC=AP8dLtx77zCuBaEOOUu7y02bfgyCEYOwmwuiDMItPDlEtDwziRjKOKkttUpGvoZXtNcmxsqzr1A; __Secure-3PSIDCC=AP8dLtwGUrB4fNwbVa5NYwJYNu2alUmW36VBFehF6lJ3XmlEX23KXH838S5sf993pCohJpc6Rg',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/@AJpluskibreet/about',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"113.0.5672.64"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.64", "Chromium";v="113.0.5672.64", "Not-A.Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client-data': 'CI+2yQEIo7bJAQjEtskBCKmdygEIrO3KAQiUocsBCP+GzQEI7Z7NAQiFoM0BCNGizQEIn6TNAQiHps0BCNamzQEI3KbNAQiLp80BCJCqzQEIpKrNAQjHqs0BCNerzQEImqzNAQifrc0BCM+uzQEIn4StAg==',
        'x-goog-authuser': '0',
        'x-goog-pageid': '101857047718780115111',
        'x-goog-visitor-id': 'CgtGaDQ5eTdNTnFVTSiI0uWiBg%3D%3D',
        'x-origin': 'https://www.youtube.com',
        'x-youtube-bootstrap-logged-in': 'true',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20230508.00.00',
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
                'remoteHost': '156.219.211.50',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'CgtGaDQ5eTdNTnFVTSiI0uWiBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20230508.00.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://www.youtube.com/watch?v=P9ZNSfe6gLU',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CIjS5aIGEOf3rgUQouyuBRCJ6K4FEMyu_hIQvbauBRDUoa8FENubrwUQqrL-EhClma8FELCfrwUQtaavBRDuoq8FEPOorwUQ4tSuBRDM9a4FEKC3_hIQ06yvBRC4i64FEMzfrgUQy7f-EhDks_4SEMK3_hIQ1_-uBRCbnq8F',
                },
                'timeZone': 'Africa/Cairo',
                'browserName': 'Chrome',
                'browserVersion': '113.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EIjS5aIGGJfCpZ8G',
                'screenWidthPoints': 1072,
                'screenHeightPoints': 937,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 180,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '8000000',
                'mainAppWebInfo': {
                    'graftUrl': 'https://www.youtube.com/@AJpluskibreet/about',
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
                        'encryptedTokenJarContents': 'ACeCFAXP1EphhXWKb6w5O8siXhb6FS968IlyymCHcwAs8msdqnG86049lSSs2NITNH1avbQ-6n0Swbnz-dBOgR1wTcR0He5WsPJC27naFil6vw9RSBYabnfg4H8',
                        'expirationSeconds': '600',
                    },
                ],
                'internalExperimentFlags': [],
            },
            'clientScreenNonce': 'MC40MDE2MjA2NzAzMTIyNDMxMw..',
            'clickTracking': {
                'clickTrackingParams': 'CBcQmysiEwjjtMrR1ub-AhUBHwYAHYOUCZkyCWNoYW5uZWxzNA==',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1683534344708',
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
                        'value': '7',
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
                'bid': 'ANyPxKpi5q8VRkDTtVF2lEq_f2N48rOHHXCUGeEa4sU-pRwFwfqfskaZg27Z5ovxFu-W-rErHGUdBAH5bb_rFWBOetFFkd7oJQ',
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

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"context":{"client":{"hl":"ar","gl":"EG","remoteHost":"156.219.211.50","deviceMake":"","deviceModel":"","visitorData":"CgtGaDQ5eTdNTnFVTSiI0uWiBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20230508.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/watch?v=P9ZNSfe6gLU","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CIjS5aIGEOf3rgUQouyuBRCJ6K4FEMyu_hIQvbauBRDUoa8FENubrwUQqrL-EhClma8FELCfrwUQtaavBRDuoq8FEPOorwUQ4tSuBRDM9a4FEKC3_hIQ06yvBRC4i64FEMzfrgUQy7f-EhDks_4SEMK3_hIQ1_-uBRCbnq8F"},"timeZone":"Africa/Cairo","browserName":"Chrome","browserVersion":"113.0.0.0","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EIjS5aIGGJfCpZ8G","screenWidthPoints":1072,"screenHeightPoints":937,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":180,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/@AJpluskibreet/about","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"consistencyTokenJars":[{"encryptedTokenJarContents":"ACeCFAXP1EphhXWKb6w5O8siXhb6FS968IlyymCHcwAs8msdqnG86049lSSs2NITNH1avbQ-6n0Swbnz-dBOgR1wTcR0He5WsPJC27naFil6vw9RSBYabnfg4H8","expirationSeconds":"600"}],"internalExperimentFlags":[]},"clientScreenNonce":"MC40MDE2MjA2NzAzMTIyNDMxMw..","clickTracking":{"clickTrackingParams":"CBcQmysiEwjjtMrR1ub-AhUBHwYAHYOUCZkyCWNoYW5uZWxzNA=="},"adSignalsInfo":{"params":[{"key":"dt","value":"1683534344708"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"180"},{"key":"u_his","value":"7"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1040"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"937"},{"key":"biw","value":"1055"},{"key":"brdim","value":"0,0,0,0,1920,0,1920,1040,1072,937"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKpi5q8VRkDTtVF2lEq_f2N48rOHHXCUGeEa4sU-pRwFwfqfskaZg27Z5ovxFu-W-rErHGUdBAH5bb_rFWBOetFFkd7oJQ"}},"channelIds":[f"{id}"],"params":"EgIIAhgA"}'
    #response = requests.post(
    #    'https://www.youtube.com/youtubei/v1/subscription/subscribe',
    #    params=params,
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    #)
    if response.status_code == 200:
     print(' successful!')
    else:
     print(' failed.')
