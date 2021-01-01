#must use Python3+


import requests

ap_sn = input("Enter Access Point SN: ") 
api_key = input("Enter API Key: ")

url = f"https://api.meraki.com/api/v1/devices/{ap_sn}/wireless/status?sn="

payload={}
headers = {
  'Accept': '*/*',
  'X-Cisco-Meraki-API-Key': api_key
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
