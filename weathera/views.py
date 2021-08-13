from django.shortcuts import render
import json 
import urllib.request

def index(request):
    
    if request.method =="POST":
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=656c70d9b920cb085d83c16b2a9d20a0').read()
        json_load = json.loads(res)

        data = {
            'country_code': str(json_load['sys']['country']),
            'coordinate' : str(json_load['coord']['lon'])+' ' +str(json_load['coord']['lat']),
            'temp':str(json_load['main']['temp']) + 'k',
            'pressure': str(json_load['main']['pressure']),
            'humidity' : str(json_load['main']['humidity']),
        }

    else:
        city = ''
        data = {}

    return render(request, 'index.html', {'city':city, 'data':data})