import urllib.request
import urllib.parse
import json
url = 'https://api.avgle.com/v1/search/{}/{}?limit={}'
query = str(input("關鍵字："))
page = 1
limit = int(input("數量："))

def v(query,limit):
    resp = json.loads(urllib.request.urlopen(url.format(urllib.parse.quote_plus(query), page, limit)).read().decode())
    videos = resp['response']['videos']
    video=dict(videos[0])
    print("標題：%s\n網址：%s\n預覽圖：%s\n----------------------------------------"%(video['title'],video['video_url'],video['preview_url']))
for i in range(1,limit+1):
    v(query,i)