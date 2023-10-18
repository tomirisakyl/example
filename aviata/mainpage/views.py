import os
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import (
    RegistrationForm,
    EditProfileForm
)
from django.forms import inlineformset_factory
from .models import  Ticket
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .forms import CustomCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import ExampleModel, UserProfile
from .forms import UploadForm, EditProfileForm
from .forms import ChangeForm, ItemsForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




@login_required(login_url='login')
def main(request):
    return render(request, "mainpage/main.html")



def register(request):
    form = RegistrationForm ()
    if request.method == 'POST':
        form = RegistrationForm (request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for')
            return redirect('login')
    context = {'form': form}
    return render(request, 'mainpage/register.html', context)

# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('accounts:home'))
#     else:
#         form = RegistrationForm()

#         args = {'form': form}
#         return render(request, 'accounts/reg_form.html', args)

def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request,'Username or password is incorrect')
    context = {}
    return render(request, 'mainpage/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('login')


def add(request):
    error = ''
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anywhere')
        else:
            error = 'Форма запоkнена неверно'

    form = ItemsForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'mainpage/foradmin/add.html', data)


def change(request, pk):
    error = ''
    item = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        delete = None
        if 'deler' in request.POST.keys():
            item.delete()
            return redirect('anywhere')
        else:
            item.company = request.POST['company']
            item.city1 = request.POST['city1']
            item.city2 = request.POST['city2']
            item.time1 = request.POST['time1']
            item.time2 = request.POST['time2']
            item.price = request.POST['price']
            item.save()
            return redirect('anywhere')
    data = {
        'error': error,
        'item': item,
    }

    return render(request, 'mainpage/foradmin/update.html', data)




def anywhere(request):
    items = Ticket.objects.all()
    context = {'items': items}
    return render(request, 'mainpage/anywhere.html', context)
def details(request, pk):
    items = Ticket.objects.get(pk=pk)
    context = {'items': items}
    return render(request, 'mainpage/details.html', context)

def media_example(request):
    instance = None

    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            instance = ExampleModel()
            instance.image_field = form.cleaned_data["image_upload"]
            instance.file_field = form.cleaned_data["file_upload"]
            instance.save()
    else:
        form = UploadForm()

    return render(request, "mainpage/formedia.html", {"form": form, "instance": instance})

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'mainpage/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('mainpage:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'mainpage/edit_profile.html', args)



    # if request.method == 'POST':
    #     save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_upload"].name)
    #     with open(save_path, "wb") as output_file:
    #         for chunk in request.FILES["file_upload"].chunks():
    #             output_file.write(chunk)
    # return render(request, 'mainpage/formedia.html')





