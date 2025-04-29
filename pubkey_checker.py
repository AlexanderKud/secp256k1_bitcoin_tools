import requests
import time

addr_file = open('addresses.txt', "r")
pub_res = open('results.txt', 'a')
full_res = open('full_results.txt', 'a')
err_msg = '{"error":"not-found-or-invalid-arg","message":"Item not found or argument invalid"}'

for address in addr_file:
    link = f"https://blockchain.info/q/pubkeyaddr/{address}"
    f = requests.get(link)
    if f.text == err_msg:
        print(f'{address}has no pubkey')
    else:
        pub_res.write(f"{f.text}\n")
        full_res.write(f"{address}{f.text}\n")
        print(f'{address}{f.text}')
        #time.sleep(10)
        time.sleep(2)

addr_file.close()
pub_res.close()
full_res.close()

'''
address = '17s2b9ksz5y7abUm92cHwG8jEPCzK3dLnT'
err_msg = '{"error":"not-found-or-invalid-arg","message":"Item not found or argument invalid"}'
link = f"https://blockchain.info/q/pubkeyaddr/{address}"
f = requests.get(link)
if f.text == err_msg:
   print("No pubkey")
else:
   print(f.text)
'''
