import requests

def youtube_subscribe(link):
    id = link.split('/')[-2]

    cookies = {
        'GPS': '1',
        'PREF': 'tz=Africa.Cairo',
        'CONSISTENCY': 'ACeCFAXWB5IL8Eey16bcSL16wINs9aDh6VVVdfps4QD1q_NSMquIPAJyjyhHtQs0RYudpFEufBHxCGaAkCM2l2LmAsRUDThULTOwH3L1HSF44SKvmjYdlEIXuktsYIObBhQMwBzT3_d_z393EttLQA',
        '__Secure-3PSID': 'WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD2IQICxV7OI6F1RnkYP3WXA.',
        'YSC': 'xGiDlTQx7E0',
        'SID': 'WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lDv-SBzrxcD7zWJnd_rg4_EQ.',
        'SAPISID': 'FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG',
        'SSID': 'ACc9YjcVC3ES0HAoe',
        'DEVICE_INFO': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G',
        '__Secure-1PAPISID': 'FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG',
        '__Secure-1PSID': 'WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD8hLB7BJR8rcJ9c7ug5Kfwg.',
        '__Secure-3PAPISID': 'FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG',
        'APISID': 'E6KNVlV2EcA8DBqj/AYAN2GzYLaqs3RSoB',
        'HSID': 'As-YstmRuz3H3Luq7',
        'VISITOR_INFO1_LIVE': 'Fh49y7MNqUM',
        'LOGIN_INFO': 'AFmmF2swRQIhAPzr-DWJ2M2NWrXshG45RVGS0_8mogJDJOYZO2FS5x0VAiA7cp5LZoOZ8xf1Y3jhYLIwd8ue4ksRAPtLQ8yOglpwbw:QUQ3MjNmeWVSUkdmb1dYME1tdFA5cmtZWVdKZmdOd3lrRzNSeFN2Z2pmMDZGSkNHRzl1d0xpcXZaeVdBOWF3QVNhRVRyZHFwdHEweWhyXzFHajhYYWNJZmRmMUlvNGtJZlk1aG9UcVVQZHpDcXNneEltVlVDS3VWM2VCaEdVU2Y5LTkwcWp1NUUwSExBVFlCd25FdFUzR0owSzVxVmZ4Z183WWxnQWN0Y3JCc0I1dWlfY3NkckJ0QlNlb01yenVyMzJ3R1FKZnpiMzdaM0EwM3JGSmJndzNndFU5bDBmVFRYdw==',
        'SIDCC': 'AP8dLtwEOzLpbZV2MMuQzaZVmSe6rQ6xF2r_ZV2Xme-PdXynpLr5_LETwZl9Kn1nVGJHQdxQ5w',
        '__Secure-1PSIDCC': 'AP8dLtxqcJkopGSgBSLlk9MbZhCQgD59OwJ-ORTzUac_yIXto5KiYzngzUYCY4CEX2R9pK7KSmw',
        '__Secure-3PSIDCC': 'AP8dLtwVSwGF3iR0vlkDEO2gnd6oyG9aDDCeeoCJaByjtaY9BajHUn7cihGHZms4fdHxU42RZw',
    }

    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'SAPISIDHASH 1683583770_a292c57e5eeeca6956408fbd365e70857f55e8bc',
        'content-type': 'application/json',
        # 'cookie': 'GPS=1; PREF=tz=Africa.Cairo; CONSISTENCY=ACeCFAXWB5IL8Eey16bcSL16wINs9aDh6VVVdfps4QD1q_NSMquIPAJyjyhHtQs0RYudpFEufBHxCGaAkCM2l2LmAsRUDThULTOwH3L1HSF44SKvmjYdlEIXuktsYIObBhQMwBzT3_d_z393EttLQA; __Secure-3PSID=WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD2IQICxV7OI6F1RnkYP3WXA.; YSC=xGiDlTQx7E0; SID=WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lDv-SBzrxcD7zWJnd_rg4_EQ.; SAPISID=FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG; SSID=ACc9YjcVC3ES0HAoe; DEVICE_INFO=ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EJfCpZ8GGJfCpZ8G; __Secure-1PAPISID=FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG; __Secure-1PSID=WQgwuNconjqOg9iETaQ5WbN-ixmeSag4tah-EZIiIdfQz3lD8hLB7BJR8rcJ9c7ug5Kfwg.; __Secure-3PAPISID=FpBS5mqypywwBAcI/AJ3XtwxyG6wOZ9bkG; APISID=E6KNVlV2EcA8DBqj/AYAN2GzYLaqs3RSoB; HSID=As-YstmRuz3H3Luq7; VISITOR_INFO1_LIVE=Fh49y7MNqUM; LOGIN_INFO=AFmmF2swRQIhAPzr-DWJ2M2NWrXshG45RVGS0_8mogJDJOYZO2FS5x0VAiA7cp5LZoOZ8xf1Y3jhYLIwd8ue4ksRAPtLQ8yOglpwbw:QUQ3MjNmeWVSUkdmb1dYME1tdFA5cmtZWVdKZmdOd3lrRzNSeFN2Z2pmMDZGSkNHRzl1d0xpcXZaeVdBOWF3QVNhRVRyZHFwdHEweWhyXzFHajhYYWNJZmRmMUlvNGtJZlk1aG9UcVVQZHpDcXNneEltVlVDS3VWM2VCaEdVU2Y5LTkwcWp1NUUwSExBVFlCd25FdFUzR0owSzVxVmZ4Z183WWxnQWN0Y3JCc0I1dWlfY3NkckJ0QlNlb01yenVyMzJ3R1FKZnpiMzdaM0EwM3JGSmJndzNndFU5bDBmVFRYdw==; SIDCC=AP8dLtwEOzLpbZV2MMuQzaZVmSe6rQ6xF2r_ZV2Xme-PdXynpLr5_LETwZl9Kn1nVGJHQdxQ5w; __Secure-1PSIDCC=AP8dLtxqcJkopGSgBSLlk9MbZhCQgD59OwJ-ORTzUac_yIXto5KiYzngzUYCY4CEX2R9pK7KSmw; __Secure-3PSIDCC=AP8dLtwVSwGF3iR0vlkDEO2gnd6oyG9aDDCeeoCJaByjtaY9BajHUn7cihGHZms4fdHxU42RZw',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/@_vector_/about',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"113.0.5672.93"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="113.0.5672.93", "Chromium";v="113.0.5672.93", "Not-A.Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-client-data': 'CI+2yQEIo7bJAQjEtskBCKmdygEIrO3KAQiTocsBCP+GzQEI7Z7NAQiFoM0BCNGizQEIn6TNAQiHps0BCNemzQEI3KbNAQiLp80BCJGqzQEIpKrNAQjHqs0BCNerzQEIn63NAQjQrs0BCJ+ErQI=',
        'x-goog-authuser': '0',
        'x-goog-pageid': '100706374690481630592',
        'x-goog-visitor-id': 'CgtGaDQ5eTdNTnFVTSij0-iiBg%3D%3D',
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
                'visitorData': 'CgtGaDQ5eTdNTnFVTSij0-iiBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20230508.00.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://www.youtube.com/',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CKPT6KIGENShrwUQgZ2vBRDi1K4FEKC3_hIQqrL-EhC4i64FEMzfrgUQzLf-EhCwn68FEKmurwUQ25uvBRDFuv4SEOSz_hIQzK7-EhDn964FEMz1rgUQwrf-EhDUrK8FEKWZrwUQouyuBRDyqK8FEL22rgUQ1_-uBRCArq8FEO6irwUQieiuBRCmvv4S',
                },
                'timeZone': 'Africa/Cairo',
                'browserName': 'Chrome',
                'browserVersion': '113.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EKPT6KIGGJfCpZ8G',
                'screenWidthPoints': 1365,
                'screenHeightPoints': 969,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 180,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '8000000',
                'mainAppWebInfo': {
                    'graftUrl': 'https://www.youtube.com/@_vector_/about',
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
                        'encryptedTokenJarContents': 'ACeCFAXWB5IL8Eey16bcSL16wINs9aDh6VVVdfps4QD1q_NSMquIPAJyjyhHtQs0RYudpFEufBHxCGaAkCM2l2LmAsRUDThULTOwH3L1HSF44SKvmjYdlEIXuktsYIObBhQMwBzT3_d_z393EttLQA',
                    },
                ],
                'internalExperimentFlags': [],
            },
            'clientScreenNonce': 'MC4wMTQzOTI4NTE3NjE2NjkzNzk.',
            'clickTracking': {
                'clickTrackingParams': 'CBcQmysiEwij7YXfjOj-AhUuwkkHHQoxDPkyCWNoYW5uZWxzNA==',
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1683583649889',
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
                        'value': '969',
                    },
                    {
                        'key': 'biw',
                        'value': '1349',
                    },
                    {
                        'key': 'brdim',
                        'value': '0,0,0,0,1920,0,1920,1040,1365,969',
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

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"context":{"client":{"hl":"ar","gl":"EG","remoteHost":"156.219.211.50","deviceMake":"","deviceModel":"","visitorData":"CgtGaDQ5eTdNTnFVTSij0-iiBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20230508.00.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CKPT6KIGENShrwUQgZ2vBRDi1K4FEKC3_hIQqrL-EhC4i64FEMzfrgUQzLf-EhCwn68FEKmurwUQ25uvBRDFuv4SEOSz_hIQzK7-EhDn964FEMz1rgUQwrf-EhDUrK8FEKWZrwUQouyuBRDyqK8FEL22rgUQ1_-uBRCArq8FEO6irwUQieiuBRCmvv4S"},"timeZone":"Africa/Cairo","browserName":"Chrome","browserVersion":"113.0.0.0","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOekU1T1RNNU1qSXpNVFUwTlRVME9URXdOZz09EKPT6KIGGJfCpZ8G","screenWidthPoints":1365,"screenHeightPoints":969,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":180,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/@_vector_/about","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":true}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"consistencyTokenJars":[{"encryptedTokenJarContents":"ACeCFAXWB5IL8Eey16bcSL16wINs9aDh6VVVdfps4QD1q_NSMquIPAJyjyhHtQs0RYudpFEufBHxCGaAkCM2l2LmAsRUDThULTOwH3L1HSF44SKvmjYdlEIXuktsYIObBhQMwBzT3_d_z393EttLQA"}],"internalExperimentFlags":[]},"clientScreenNonce":"MC4wMTQzOTI4NTE3NjE2NjkzNzk.","clickTracking":{"clickTrackingParams":"CBcQmysiEwij7YXfjOj-AhUuwkkHHQoxDPkyCWNoYW5uZWxzNA=="},"adSignalsInfo":{"params":[{"key":"dt","value":"1683583649889"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"180"},{"key":"u_his","value":"7"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1040"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"969"},{"key":"biw","value":"1349"},{"key":"brdim","value":"0,0,0,0,1920,0,1920,1040,1365,969"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"channelIds":[f"{id}"],"params":"EgIIAhgA"}'
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
