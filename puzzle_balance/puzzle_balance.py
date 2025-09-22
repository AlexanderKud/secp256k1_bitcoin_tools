import requests
import time
import json


with open('unsolved.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        idx = line.index(' ')
        address = line[idx+1:]
        link = f"https://blockchain.info/balance?active={address}"
        f = requests.get(link)
        data = json.loads(f.text)
        print(f'{line[0:idx]} {data}')
        time.sleep(2)
