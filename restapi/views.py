from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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

def abc(request):
    pass