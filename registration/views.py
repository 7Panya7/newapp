from django.shortcuts import render, redirect
from .forms import UsersForm, LoginForm
from .models import Users
from django.views.generic import CreateView

class NewCreateView(CreateView):
    model = Users
    template_name = 'registration/create_user.html'
    form_class = UsersForm

def logins(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid:
            user = Users.objects.get(login = input(form.Meta.model.login))
            if user != None:
                if user.password != input(form.Meta.model.password):
                    error = 'Введен не верный пароль'
            else:
                return redirect('home')
        else:
            error = 'Форма заполнена не корректно'  
    form = LoginForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/login.html', data)