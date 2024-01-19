from django.shortcuts import render

# Create your views here.
import datetime


def filters(request):
    dt=datetime.datetime.now()
    d={'data':'wE are NoT JoB EmpLoYeeS','date':dt,'c':0}
    return render(request,'filters.html',d)

def userDFilters(request):
    d1={'data':'DjaNgo almost ComplEteD'}
    return render(request,'userDFilters.html',d1)

