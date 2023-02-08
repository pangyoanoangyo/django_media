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
    # return redirect('mylist:main',{
    #     'profiles':profile
    #     })
    
def profile(request):
    profile=Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})


def upload(request):
    return render(request,'upload.html')

def upload_create(request):
    form=Profile_add() #폼은 모델을 불러온다.
    form.title=request.POST['title'] #폼의 title에 POST로 받은 title을 넣는다.
    form.content=request.POST['content'] #폼의 content에 POST로 받은 content를 넣는다.
    form.etc=request.POST['etc']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('mylist:main') 

