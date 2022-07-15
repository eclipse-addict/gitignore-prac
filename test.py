import requests
from bs4 import BeautifulSoup

KEY = 'xIjAko9er7vU2xq3pMQrm%2BKyEZcNjd1lzWD7Id4TVfyi80hsQg7J4udyaYZTTscLh7mRjsW8Pt3RwZ%2FCuH06GA%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0'

response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

if 150 < dust:
    status = '매우나쁨'
elif 80 < dust <= 150:
    status = '나쁨'
elif 30 < dust and dust <= 80:
    status = '보통'
else:
    status = '좋음'

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}, {status}입니다.')