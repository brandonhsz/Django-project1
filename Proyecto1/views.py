import datetime
from django.http import HttpResponse
from django.template import Template, Context

class Person(object):
  def __init__(self, name, lastName):
    self.name = name
    self.lastName = lastName

def Index(request):

  external_doc = open('Proyecto1/templates/index.html')
  template_content = Template(external_doc.read())
  external_doc.close()

  ctx = Context()

  return HttpResponse(template_content.render(ctx))

def HelloWorld(request):

  anyPerson = Person('Brandon', 'Hernandez')

  external_doc = open('Proyecto1/templates/hello.html')
  template_content = Template(external_doc.read())

  external_doc.close()

  ctx = Context({
    'name': anyPerson.name,
    'lastName': anyPerson.lastName
  })


  return HttpResponse(template_content.render(ctx))

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
