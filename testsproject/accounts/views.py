from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import LoginForm, RegisterForm


# Create your views here.
def  register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('register')
    else:
        form = RegisterForm()
    template_name = 'accounts/register.html'
    context = {'form': form }
    return render(request, template_name, context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forloop')
        else:
            print("Invalid credentials !!!")
            messages.info(request, 'Invalides Credentials')
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', context = {'form': form})
        
