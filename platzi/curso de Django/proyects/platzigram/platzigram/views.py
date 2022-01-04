#------------django
from django.http import HttpResponse
from django.http import JsonResponse
#-----------utils
from datetime import datetime
import pdb
#---------functions
def HelloWorld(request):
    #returns "helloworld
    #returns time

    #se le asigna un formato (respectivamente: month, day, year - hours, minutes)
    now=datetime.now().strftime('%b %dth,%Y - %H:%M hrs')
    return HttpResponse('hi,current Sv time is: {now}'.format(now=str(now)))

def hi(request):
    pdb.set_trace()
    return HttpResponse('hi')

def calc(request):
    #llama el debugger, se usa desde la consola
    # pdb.set_trace()
    numbers=request.GET['numbers']
    #se usa split para que se cree una lista
    numbers=numbers.split(",")
#---------------asi se poblaria usando un ciclo for una lista
    # ordernumbers=numbers.split(',')
    # lista=[]
    # for i in ordernumbers:
    #     lista.append(int(i))
#------------------------------------------------------------

    #esto es comprension de listas, hace lo mismo que el
    #de arriba, pero es mas facil de leer
    ordernumbers=[int(i) for i in numbers]
    # QUESTION: preguntarle a andres como se hace este filtro:
    #   ordernumbers=[i for i in numbers if i%2==0]

    ordernumbers.sort()
    info={
        'status':'ok',
        'content':

        ordernumbers,
        'message':'completed'

    }
    return JsonResponse(info,safe=False)
    #alternativa:
    #return HttpResponse(str(ordernumbers),content_type='application/json')

def menor(request,name,age):
    if age<18:
        return HttpResponse('hola {} tienes {}, por lo que no deberias estar aqui'.format(name,age))
    else:
        return HttpResponse('hola {} tienes {}, linda tarde'.format(name,age))
