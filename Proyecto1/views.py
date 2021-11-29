import datetime
from django.http import HttpResponse
from django.http.response import JsonResponse

def HelloWorld(request):

  return HttpResponse('Hello World')

def GoodByeWorld(request):
  data = request
  print(data.GET)
  return HttpResponse('GoodBye World')

def getTime(request):
  #get the current time in format '%H:%M:%S'
  current_time = datetime.datetime.now().strftime('%H:%M:%S')
  return HttpResponse(current_time)

def calculateMyFutureAge( request , age , year ):
  period = year - datetime.date.today().year
  futureAge = age + period
  return HttpResponse(f"En el año {year} tendras la edad de: {futureAge}")
