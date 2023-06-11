from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserForm
from .models import User
import uuid
from django.core.mail import EmailMessage
from .replacer import replace_new_uuid
import requests
from .credentials import IP_DESTINATION


def home(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.warning(request, "This email already exists! try another email!")
            else:
                # generate a uuid and add it to database
                obj = form.save(commit=False)
                custom_uuid = str(uuid.uuid4())
                obj.uuid = custom_uuid
                obj.save()

                # replace new uuid in client config file
                replace_new_uuid(obj.uuid)

                re = requests.get((IP_DESTINATION + obj.uuid))
                if re.status_code == 200:
                    # Send config to client
                    mail = EmailMessage("FreeInternet For everyone", "You can use this file and import it to any "
                                                                     "v2rayapp ", settings.EMAIL_HOST_USER, [email])
                    mail.attach_file("files/config.json")
                    mail.send()
                    return HttpResponseRedirect('successful')
                else:
                    return HttpResponseRedirect('unsuccessful')
    else:
        form = UserForm()
    context = {
        'form': form
    }

    return render(request, 'vpn_generator/home.html', context)


def successful(request):
    return render(request, 'vpn_generator/successful.html')


def unsuccessful(request):
    return render(request, 'vpn_generator/unsuccessful.html')
