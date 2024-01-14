import requests

r = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
proxylist = r.text.split()

def getProxy():
      for i in range(len(proxylist)):
            try:
                  proxy = proxylist[i]

                  proxies = {

                        "http": proxy,
                        "https": proxy
                  }

                  url = 'https://httpbin.org/ip'
                  response = requests.get(url, proxies=proxies, timeout=5)
                  print(f'{i}. proxy is active! Status code: {response.status_code} and adress {proxy}')
            except:
                  print(f'{i}. proxy is passive.')

getProxy()
