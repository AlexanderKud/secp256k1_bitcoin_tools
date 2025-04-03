import requests
import time
import json

addr_list = [
             "16RGFo6hjq9ym6Pj7N5H7L1NR1rVPJyw2v", \
             "1QKBaU6WAeycb3DbKbLBkX7vJiaS8r42Xo", \
             "19GpszRNUej5yYqxXoLnbZWKew3KdVLkXg", \
             "1MUJSJYtGPVGkBCTqGspnxyHahpt5Te8jy", \
             "1AoeP37TmHdFh8uN72fu9AqgtLrUwcv2wJ", \
             "1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv"
             ]
puzzle = 135
for address in addr_list:
    address = address.strip()
    link = f"https://blockchain.info/balance?active={address}"
    f = requests.get(link)
    data = json.loads(f.text)
    print(f'{puzzle}:{data}')
    time.sleep(1)
    puzzle += 5

input()
