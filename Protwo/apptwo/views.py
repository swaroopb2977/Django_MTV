from django.shortcuts import render
from django.http import HttpResponse
from  apptwo.models import user
# Create your views here.

def index(request):
    return HttpResponse("<em>Mys second project</em>")

def users(request):
    user_list=user.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'apptwo/users.html',context=user_dict)

def help(request):
    helpdict={'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)
