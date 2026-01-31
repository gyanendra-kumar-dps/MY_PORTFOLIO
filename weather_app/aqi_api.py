import requests
def aqi_data(name):
    api_key = "c4de83b301cf8de11962b4af04b2419789e00a47"
    url = f"https://api.waqi.info/feed/{name}/?token={api_key}"
    response = requests.get(url,timeout=5)
    data = response.json()
    print(data['status'])
    if data['status'] == 'ok':
        aqi = data['data']['aqi']
        return(aqi)
    else:
        return("Failed to fetch AQI data.")
