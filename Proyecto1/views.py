import datetime
from django.http import HttpResponse
from django.template import loader

class Person(object):
  def __init__(self, name, lastName):
    self.name = name
    self.lastName = lastName

def Index(request):

  IndexTemplate = loader.get_template('index.html')

  render = IndexTemplate.render({})

  return HttpResponse(render)

def HelloWorld(request):

  anyPerson = Person('Brandon', 'Hernandez')

  # external_doc = open('Proyecto1/templates/hello.html')
  # template_content = Template(external_doc.read())
  # external_doc.close()

  HelloTemplate = loader.get_template('hello.html')

  ctx = {
    'name': anyPerson.name,
    'lastName': anyPerson.lastName,
    'topics' : ['Templates', 'Models', 'Forms', 'Views']
  }

  render = HelloTemplate.render(ctx)
  return HttpResponse(render)

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
