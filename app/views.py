from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from .forms import CustomerRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

# ===========course view===========
def courses(request):
    return render(request, 'app/courses.html')

# =============BSC CSIT================
def bsccsit(request):
    return render(request, 'app/bsc-csit.html')

# =============SEMESTER================
def semester(request):
    return render(request, 'app/semester.html')

# =============SUBJECT================
def subject(request):
    return render(request, 'app/subject.html')

# =============MODEL QUESTIONS================
def model_questions(request):
    return render(request, 'app/model-questions.html')

# =============REFRENCED BOOKS================
def refrenced_books(request):
    return render(request, 'app/refrenced-books.html')

# =============TECH NEWS================
def tech_news(request):
    return render(request, 'app/tech-news.html')

def sports(request):
    return render(request, 'app/sports.html')
#============= ALL PROGRAMMING VIEWS ================
def programming(request):
    return render(request , 'app/programming.html')
def learnhtml(request):
    return render(request , 'app/learnhtml.html')
def intro(request):
    return render(request , 'app/introduction.html')


def learncss(request):
    return render(request , 'app/learncss.html')

def learnbootstrap(request):
    return render(request , 'app/learnbootstrap.html')

def learnjavascript(request):
    return render(request , 'app/learnjavascript.html')

def learnjquery(request):
    return render(request , 'app/learnjquery.html')

def learnphp(request):
    return render(request , 'app/learnphp.html')

def learnpython(request):
    return render(request , 'app/learnpython.html')

def learndjango(request):
    return render(request , 'app/learndjango.html')

def learnsql(request):
    return render(request  , 'app/learnsql.html')

#====================END OF PROGRAMMING VIEWS ==============


#contact view
def contact(reqeust):
    return render(reqeust , 'app/contact.html')

# ======================REGISTRATION VIEW=================
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})
    
# ================LOGIN VIEW============================
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
