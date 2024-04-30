import sys
import os
from twocaptcha import TwoCaptcha
import requests
import random
import time

text_file = r"自己改"


api_key = '自己改'
url = '自己改'

proxies_pool = [
   '自己的代理'
]


def captcha():
    solver = TwoCaptcha(api_key)
    try:
        result = solver.recaptcha(
            sitekey='自己改',
            url='自己改',
            invisible=1)

    except Exception as e:
        sys.exit(e)

    else:

        reaptcha = result["code"]
        return reaptcha



if __name__ == '__main__':

    with open(text_file, 'r') as file:
        addresses = file.readlines()

    for address in addresses:
        print(address)

        for attempt in range(3):  # 尝试 1 次 + 重试 3 次 = 总共 4 次
            # 从代理池随机选择一个代理
            proxy = random.choice(proxies_pool)
            proxies = {'http': proxy, 'https': proxy}
            
            data = {
                "address": address,
                "tokenId": "自己改",
                "recaptchaToken": captcha()
            }

            try:
                res = requests.post(url, json=data, proxies=proxies)
                if res.json().get("status") == True:
                    print(f"Request successful for address {address}")
                    break
                else:
                    print(f"Request failed with response: {res.text}, retrying...")
            except Exception as e:
                print(f"An error occurred: {e}, retrying...")
            time.sleep(10 * attempt)
        else:
            print(f"Failed to process request for address {address} after 3 retries.")
