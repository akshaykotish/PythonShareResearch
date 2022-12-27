from requests import Session

S = Session()
time_out = 5
base_url = "https://www.nseindia.com/api"
page_url = "https://www.nseindia.com/get-quotes/equity?symbol=LT"
h = {
    "Host": "www.nseindia.com",
    "Referer": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
    "X-Requested-With": "XMLHttpRequest",
    "pragma": "no-cache",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
}

S.headers.update(h)
S.get(page_url)


def get(self, route, payload={}):
    url = base_url + "/quote-equity?symbol=SBIN"
    r = S.get(url)
    return r.json()


data = {"symbol": "LT"}
print(get("stock_quote", data))
