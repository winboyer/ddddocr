import json
import requests
import time


def test_captcha_service():
    # url = "http://172.30.4.220:2512/captcha/recognize"
    # url = "http://172.20.10.5:2512/captcha/recognize"
    # url = "http://172.30.65.194:2512/captcha/recognize"
    # url = "http://112.124.54.138:2512/captcha/recognize"
    url = "http://192.168.7.157:2512/captcha/recognize"
    
    response = requests.get(url, timeout=5)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")


if __name__ == "__main__":
    test_captcha_service()

