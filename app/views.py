from django.shortcuts import render

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