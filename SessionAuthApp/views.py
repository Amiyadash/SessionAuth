from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Stud
from django.contrib.auth import authenticate,login
from .serializers import StudSerializer
# Create your views here.
def login_form(request):
    return render(request,'login.html')
def login_user(request):
    username=request.POST['txtName']
    password=request.POST['txtPwd']
    userid=authenticate(username=username,password=password)
    if userid is not None:
        login(request,userid)
        return  redirect('/api')
    else:
        return redirect('/login')
class StudViewSet(viewsets.ModelViewSet):
    queryset =Stud.objects.all()
    serializer_class =StudSerializer
