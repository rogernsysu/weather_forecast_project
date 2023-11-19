from django.shortcuts import render
from .models import WeatherForecast
import requests
import datetime
import matplotlib.pyplot as plt
import io
import base64

def Homepages(request):
    context = {
        # Add any context data you want to pass to the template
    }
    return render(request, 'weather/Homepages.html', context)


def fetch_weather_data(city_name):
    api_key = 'd4981c8c1e59eebc2fe96e1c72006f63'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        rain = data.get('rain', {}).get('1h', 0)  # 获取1小时降雨量，单位毫米
        humidity = data.get('main', {}).get('humidity', 0)
        country_code = data['sys']['country']  # 获取国家代码
        country_names = {
            'CN': 'China',
            'US': 'USA',
            'GB': 'UK',
            'TW': 'Taiwan',
            'SG': 'Singapore',
            'JP': 'Japan',
            'AU': 'Australia',
            'DE': 'Germany',
            'FR': 'France',
            'NO': 'Norway',
            'CA': 'Canada',
            'NL': 'Netherlands',
            'TH': 'Thailand',
            'ID': 'Indonesia',
            'IN': 'India',
            'KR': 'Korea',  # Added for Seoul
            'IT': 'Italy',        # Added for Rome
            'AE': 'UAE',  # Added for Dubai
            'RU': 'Russia',       # Added for Moscow
            'TR': 'Turkey'        # Added for Istanbul
            # Add mappings for other countries as needed
        }
        country_name = country_names.get(country_code, country_code)  # 获取国家全名或默认为国家代码
        
        return {
            'name': data['name'],
            'country': country_name,
            'dt': data['dt'],
            'main': data['main'],
            'weather': data['weather'],
            'coord': data['coord'],
            'rainfall': rain,  # 将降雨量添加到数据中
            'humidity':humidity
        }
    else:
        print(f"Error: {response.status_code}")
        print(response.content)
        return None

def forecast_list(request):
    WeatherForecast.objects.all().delete()
    for city_name in ['Taipei', 'Kaohsiung', 'Taichung', 'Tainan', 'Hanoi', 'Singapore', 'Tokyo', 'Yokohama', 'Osaka', 'Kyoto', 'Kobe', 'Nagoya', 'Fukuoka', 'Seoul', 'New York', 'Houston', 'Phoenix', 'Honolulu', 'Los Angeles', 'San Francisco', 'Seattle', 'Chicago', 'Boston', 'Miami', 'London', 'Paris', 'Berlin', 'Lisbon', 'Barcelona', 'Cairo', 'Shanghai', 'Beijing', 'Hong Kong', 'Sydney', 'Canberra', 'Melbourne', 'Wellington', 'Auckland', 'New Delhi', 'Mumbai', 'Jakarta', 'Bangkok', 'Manila', 'Toronto', 'Ottawa', 'Vancouver', 'Amsterdam', 'Oslo', 'Copenhagen', 'stockholm', 'Helsinki', 'Dubai', 'Moscow', 'Istanbul', 'Zurich', 'Bern', 'Geneva', 'Athens', 'Warsaw', 'Vienna', 'Prague', 'Jerusalem']:
        data = fetch_weather_data(city_name)
        forecast = WeatherForecast(
            city=data['name'],
            country=data['country'],
            date=datetime.datetime.fromtimestamp(data['dt']),
            temperature=round(data['main']['temp']),
            description=data['weather'][0]['description'],
            lat=data['coord']['lat'],
            lon=data['coord']['lon'],
            rainfall = data['rainfall'],  # 将降雨量存储到数据库
            humidity = data['humidity']
        )
        forecast.save()
    forecasts = WeatherForecast.objects.all()
    return render(request, 'weather/forecast_list.html', {'forecasts': forecasts})

def plot_view(request):
    # Create a matplotlib plot
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Sample Plot')
    
    # Save the plot to a byte stream
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()
    
    # Encode the byte stream as a base64 string
    image_base64 = base64.b64encode(image_stream.getvalue()).decode()

    context = {'image_base64': image_base64}
    return render(request, 'weather/plot_template.html', context)    
