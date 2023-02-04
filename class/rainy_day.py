class WeatherData:
    def __init__(self,date, day, weather):
        self.date=date
        self.day=day
        self.weather=weather
    
n=int(input())
arr=[input().split() for _ in range(n)]
datas=[WeatherData(date,day,weather) for date,day,weather in arr]

rain_date,rain_day='2100-12-31',''
for i in range(n):
    if datas[i].weather=='rain':
        if datas[i].date<rain_date:
            rain_date, rain_day=datas[i].date, datas[i].day

print(f'가장 최근에 비가 오는 날은 {rain_date} {rain_day}')
