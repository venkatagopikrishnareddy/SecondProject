from django.shortcuts import render
def students1(request):
    return render(request,'SecondApp/student.html')
def employes1(request):
    return render(request,'SecondApp/employe.html')
def students2(request):
    return render(request,'SecondApp/students2.html')
def employes(request):
    return render(request,'SecondApp/employe2.html')
# Create your views here.
