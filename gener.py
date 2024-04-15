import requests
from bs4 import BeautifulSoup

cookies = {
    '_d34e2': '9f1f84614f930ae4',
    'jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQ3MjMwNjEsImp0aSI6IjdqeGxheFUwZnQzS3FBaW9OejlrdGk4T0RteXBvdFJvdVlLR0xmRFZ6dWc9IiwiaWF0IjoxNzEzMTg3MDYxLCJpc3MiOiJER19HT19BUEkiLCJzdWIiOiIwIiwiVmVyc2lvbiI6MCwiU29jaWFsSW5mbyI6eyJEYXRlT2ZCaXJ0aCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIn0sIkZpcnN0TmFtZSI6IiIsIkxhc3ROYW1lIjoiIiwiUGhvbmUiOiIiLCJCaXJ0aGRheSI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwiTG9naW4iOiIiLCJFbWFpbCI6IiJ9.Sqkp9yo_1LjlhaLG1BzHwZylM1uGSGzwmPabbaknmls',
    'isAuthorized': 'false',
    '_9e402': 'b4d7ebccfc1671c7',
    'bannerAB': '47627',
    '_89bdc': 'ab870841fea66ef5',
    'tmr_lvid': '1e86cdef3d50d9d0fc9f6e3a6267a0a4',
    'tmr_lvidTS': '1713187060351',
    '_ym_uid': '1713187061199646216',
    '_ym_d': '1713187061',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'domain_sid': '4lRhtFcnZv6nUCNtioyW1%3A1713187060834',
    '_c15b1': '4d58ad2fc7df365',
    '_e6717': '537709f54bc20a94',
    '_d65e2': '88c11dfc706bf6a8',
    'tmr_detect': '0%7C1713187062667',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_d34e2=9f1f84614f930ae4; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDQ3MjMwNjEsImp0aSI6IjdqeGxheFUwZnQzS3FBaW9OejlrdGk4T0RteXBvdFJvdVlLR0xmRFZ6dWc9IiwiaWF0IjoxNzEzMTg3MDYxLCJpc3MiOiJER19HT19BUEkiLCJzdWIiOiIwIiwiVmVyc2lvbiI6MCwiU29jaWFsSW5mbyI6eyJEYXRlT2ZCaXJ0aCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIn0sIkZpcnN0TmFtZSI6IiIsIkxhc3ROYW1lIjoiIiwiUGhvbmUiOiIiLCJCaXJ0aGRheSI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwiTG9naW4iOiIiLCJFbWFpbCI6IiJ9.Sqkp9yo_1LjlhaLG1BzHwZylM1uGSGzwmPabbaknmls; isAuthorized=false; _9e402=b4d7ebccfc1671c7; bannerAB=47627; _89bdc=ab870841fea66ef5; tmr_lvid=1e86cdef3d50d9d0fc9f6e3a6267a0a4; tmr_lvidTS=1713187060351; _ym_uid=1713187061199646216; _ym_d=1713187061; _ym_isad=2; _ym_visorc=b; domain_sid=4lRhtFcnZv6nUCNtioyW1%3A1713187060834; _c15b1=4d58ad2fc7df365; _e6717=537709f54bc20a94; _d65e2=88c11dfc706bf6a8; tmr_detect=0%7C1713187062667',
    'dnt': '1',
    'referer': 'https://duckduckgo.com/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

params = {
    'SubjectId': '30',
}
a = [60036,57330,57195,60035,62508,54239,60043,50426,57331,54237,57194,54240,50433,60042,54238]
for i in a:
    response = requests.get(f'https://3.shkolkovo.online/catalog/4399/{i}', params=params, cookies=cookies, headers=headers)
    soup = response.content.decode('utf8').split('answer">')[1].split('</span>')[0]
    print(i, soup)