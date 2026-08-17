from concurrent.futures import ThreadPoolExecutor
import time

def fetch(url):
    time.sleep(0.2)
    return f"Response from {url}"

urls = [f"https://site{i}.com" for i in range(6)]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch, urls))

for r in results:
    print(r)

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(fetch, url) for url in urls[:3]]
    for f in futures:
        print(f.result())
