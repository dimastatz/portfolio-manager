import time
import requests
import concurrent.futures

h = { 'apikey': '7575378a-446c-48df-aadc-c95c31b7ad92' }
url = 'https://data-collector-stage.video-data-platform-prod.aws.oath.cloud/batch'


start = time.time()
lst = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:
    for i in range(0, 10):
        lst.append(e.submit(requests.post, url, headers = h, data = '1'))

for x in concurrent.futures.as_completed(lst):
    print(x.result().status_code)
    raise Exception('failed ' + )

print(time.time() - start)
