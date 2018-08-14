import requests

def send_request(tpl, url):
    payload = {'login':tpl[0],'password':tpl[1]}
    response = requests.post(url,payload)
    if (response.status_code == 200):
        print("successfully sent a fake combo")


    
