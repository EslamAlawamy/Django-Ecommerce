from django.shortcuts import render
from users.forms import RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}!')
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'],
                                    )
            login(request, new_user)
            return redirect('pages:index')
        else:
            form = RegisterForm()
            print('invalid')

    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'pages/login.html' , context)