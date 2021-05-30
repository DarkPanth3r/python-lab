# More info on https://textbelt.com
#Script to send an SMS to a Mobile Phone
import requests

resp = requests.post('https://textbelt.com/text', {
  'phone': '00000000000',
  'message': 'Hello world',
  'key': 'textbelt',
})

print(resp.json())