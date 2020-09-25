from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def taskstring(request):
    result = 'Rest API string!'
    return HttpResponse(result, content_type="text/plain")

def taskxml(request):
    result = '''<employees>
                <employee><firstName>John</firstName> <lastName>Doe</lastName></employee>
                <employee><firstName>Anna</firstName> <lastName>Smith</lastName></employee>
                </employees>'''
    return HttpResponse(result, content_type='text/xml')

def taskjson(request):
    result = {"employees":[{"firstName":"John", "lastName":"Doe"},
                           {"firstName":"Anna", "lastName":"Smith"},
                           {"firstName":"Peter", "lastName":"Jones"}]}
    return JsonResponse(result)

def openweatherget(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=fd3121df45fa165283b9f3fe57b82b19'
    cities = ['London', "Seoul"]
    for city in cities:
        return city
    c = url.format(city)
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    res = requests.get(url=c, headers=headers)
    res.raise_for_status()
    rt_dict = json.loads(res.content)
    return JsonResponse(rt_dict)

    #depts = {'name':[{'f':'moon'},{'s':'seob'}]}
    #print(depts['name'][0]['f'])
    #output(moon)