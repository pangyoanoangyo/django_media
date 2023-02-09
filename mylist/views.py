from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.utils import IntegrityError

from django.contrib import auth
from django.contrib.auth.models import User #USEER DB접근 추가
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Profile, Profile_add


def main(request):
    
    profile=Profile_add.objects.all()
    # profile=Profile.objects.get(id=1)
    return render(request,'index.html',{'profile':profile})

def write(request):
    profile=Profile_add.objects.all()
    # profile=Profile.objects.get(id=1)
    return render(request,'write.html',{'profile':profile})

def detail(request, list_id):
    profile=Profile_add.objects.get(id=list_id)
    return render(request,'detail.html',{'profile':profile})

def delete(request, list_id):
    profile=Profile_add.objects.get(id=list_id)
    profile.delete()
    return redirect('mylist:main')
def modify(request, list_id):
    profile=Profile_add.objects.get(id=list_id)
    return render(request,'modify.html',{'profile':profile})
    
def profile(request):
    profile=Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})


def upload(request):
    return render(request,'upload.html')

def upload_create(request):
    form=Profile_add() #폼은 모델을 불러온다.
    form.title=request.POST['title'] #폼의 title에 POST로 받은 title을 넣는다.
    form.content=request.POST['content'] #폼의 content에 POST로 받은 content를 넣는다.
    form.person1=request.POST['person1']
    form.person_phone1=request.POST['person_phone1']
    form.address=request.POST['address']
    form.etc=request.POST['etc']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('mylist:main') 

def upload_modify(request, list_id):
    profile=Profile_add.objects.get(id=list_id)
    profile.title=request.POST['title'] #폼의 title에 POST로 받은 title을 넣는다.
    profile.content=request.POST['content'] #폼의 content에 POST로 받은 content를 넣는다.
    profile.person1=request.POST['person1']
    profile.person_phone1=request.POST['person_phone1']
    profile.address=request.POST['address']
    profile.etc=request.POST['etc']
    try:
        profile.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    profile.save()
    return redirect('mylist:main') 

## python manage.py runserver 8080
