import requests
import os

def liveness_check():
    try:
        response = requests.get('http://localhost:3000/status')
        if response.status_code == 200:
            body = response.json()
            if len(list(body["dead_readers"].keys())) == 0:
                return True
        return False
    except Exception:
        return False

if __name__ == '__main__':
    if liveness_check():
        print('Service is up and running')
        os._exit(0)
    else:
        print('Service is down')
        os._exit(1)
    