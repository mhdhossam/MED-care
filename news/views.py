from datetime import datetime
from django.shortcuts import render
from .models import news
# Create your views here.

def new(request):
    now = datetime.today()
    d = list(
        news.objects.filter(timing=now)
    )
    data = d.pop()
    data2 = d.pop()
    data3 = d.pop()
    data4 = d.pop()
    data5 = d.pop()
    data6 = d.pop()
    data7 = d.pop()
    data8 = d.pop()
    data9 = d.pop()
    data10 = d.pop()
    return render(request,'news/index.html',{'new':data,
                                                   'new2':data2,'new3':data3,'new4':data4,'new5':data5,
                                                   'new6':data6,'new7':data7,'new8':data8,'new9':data9,
                                                   'new10':data10})
def detail(request,title):
    detailing = news.objects.get(title = title)
    return render(request,'news/iindex.html',{'newss':detailing})


# news registered
def newRE(request,email):
    now = datetime.today()
    d = list(
        news.objects.filter(timing=now)
    )
    data = d.pop()
    data2 = d.pop()
    data3 = d.pop()
    data4 = d.pop()
    data5 = d.pop()
    data6 = d.pop()
    data7 = d.pop()
    data8 = d.pop()
    data9 = d.pop()
    data10 = d.pop()
    return render(request,'news/index.html',{'new':data,
                                                   'new2':data2,'new3':data3,'new4':data4,'new5':data5,
                                                   'new6':data6,'new7':data7,'new8':data8,'new9':data9,
                                                   'new10':data10,'rs':email})
def detailRE(request,email,title):
    detailing = news.objects.get(title = title)
    return render(request,'news/iindex.html',{'newss':detailing,'rs':email})






