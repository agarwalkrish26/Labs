from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# Use Django's built-in LoginView
class LoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

# Use Django's built-in LogoutView
class LogoutView(auth_views.LogoutView):
    template_name = 'registration/logout.html'
    next_page = reverse_lazy('login')

# For the registration view, you might need a custom view:
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    
# creating a function for homepage    
from django.shortcuts import render

def homepage(request):
    return render(request, 'registration/webpage.html')

