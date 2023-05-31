from django.contrib import messages
from django.shortcuts import render , HttpResponseRedirect
from .forms import UserForm
from .models import User
import uuid
from django.core.mail import EmailMessage
# Create your views here.


def home(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.warning(request , "This email already exists! try another email!")
            else:
                obj = form.save(commit=False)
                custom_uuid = str(uuid.uuid4())
                obj.uuid = custom_uuid
                obj.save()
                return HttpResponseRedirect('')
    else:
        form = UserForm()
    context = {
        'form':form
    }

    return render(request , 'vpn_generator/home.html' , context)