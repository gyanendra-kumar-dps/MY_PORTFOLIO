import requests
import aqi_api
def aqi_calc(data):
    if 0<=data and 50>=data:
        return ['Good','Air is clean; no risk','🟢']
    elif 51<=data and 100>=data:
        return ['Satisfactory','Acceptable; minor health impact','🟡']
    elif 101<=data and 200>=data:
        return ['Moderate','May affect sensitive groups','🟠']
    elif 201<=data and 300>=data:
        return ['Poor','Breathing discomfort on prolonged exposure','🔴']
    elif 301<=data and 400>=data:
        return ['Very Poor','Respiratory illness risk','🟣']
    else:
        return ['Severe','Serious health impacts; emergency level','⚫']
def temp(city):
    try:
        response=requests.get(f"http://api.weatherapi.com/v1/current.json?key=628952ebf11d46b4b4c141951241207&q={city}&days=6&aqi=yes&alerts=no",timeout=5)
        json=response.json()
        return {'city':str(city).upper(),'temp':f"{round(json['current']['temp_c'])}°C",'icon':[json['current']['condition']['text'],f"https:{json['current']['condition']['icon']}"],'wind_speed':f"{str(round(json['current']['wind_kph']))} kph",'wind_deg':str(json['current']['wind_degree']),'wind_dir':json['current']['wind_dir'],'pressure':f'{json['current']['pressure_mb']} mb','humidity':f'{json['current']['humidity']}%','feels_like':f"{str(round(json['current']['feelslike_c']))}°C",'gust':f"{str(round(json['current']['gust_kph']))} kph","aqi":[aqi_api.aqi_data(city),aqi_calc(aqi_api.aqi_data(city))]}
    except:
        return {'error':'invalid city'}
