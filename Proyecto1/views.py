import datetime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class Person(object):
  def __init__(self, name, lastName):
    self.name = name
    self.lastName = lastName

def Index(request):

  return render(request, 'index.html')

def HelloWorld(request):

  anyPerson = Person('Brandon', 'Hernandez')

  ctx = {
    'name': anyPerson.name,
    'lastName': anyPerson.lastName,
    'topics' : ['Templates', 'Models', 'Forms', 'Views']
  }

  return render(request, 'hello.html', ctx)

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
