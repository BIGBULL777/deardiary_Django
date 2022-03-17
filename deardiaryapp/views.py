from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    entry = Diary.objects.all()
    form =  EntryForm()
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'entry':entry,'form':form}
    return render(request,'homebs.html',context)

def update_entry(request,pk):
    upadte_entry = Diary.objects.get(id = pk)
    form = EntryForm(request.POST,instance=upadte_entry)
    # if request.method == 'POST':
    #     form2 = form(request.POST) 
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form':form}
    return render(request,'update.html',context)


def Delete_entry(request,pk):
    Delete_entry = Diary.objects.get(id= pk)
    if request.method == 'POST':
        Delete_entry.delete()
        return redirect('home')
    context = {'Delete_entry':Delete_entry}
    return render(request,'delete.html',)




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)



def login_user(request):
    return redirect('/')

def logoutuser(request):
    logout(request)
    return redirect('/')