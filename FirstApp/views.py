from django.shortcuts import render
def wishes(request):
    return render(request,'firstapp/wishes.html')
def helo(request):
    return render(request,'firstapp1/time.html')


import datetime;
import time;
def datetimefunction(request):
    date1=datetime.datetime.now()
    print(date1)
    date2=time.ctime()
    print(date2)
    dict1={'server_datetime':date1,'server_datetime2':date2}
    return render (request,'firstapp/datetime.html',context=dict1)


