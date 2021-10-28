from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('bsc-csit', views.bsccsit, name='bsccsit'),
    path('semester', views.semester, name='semester'),
    path('subject', views.subject, name='subject'),
    path('model-questions', views.model_questions, name='model-questions'),
    path('refrenced-books', views.refrenced_books, name='refrenced-books'),
    path('tech-news', views.tech_news, name='tech-news'),

    # ========================= PROGRAMMING URLS============================

    path('programming/' , views.programming , name = "programming"),
    path('learnhtml/' , views.learnhtml , name = 'learnhtml'),
    path('learncss/' , views.learncss , name = 'learncss'),
    path('learnbootstrap/' , views.learnbootstrap , name = 'learnbootstrap'),
    path('learnjavascript/' , views.learnjavascript , name = 'learnjavascript'),
    path('learnjquery/' , views.learnjquery , name = 'learnjquery'),
    path('learnphp/' , views.learnphp , name = 'learnphp'),
    path('learnpython/' , views.learnpython , name = 'learnpython'),
    path('learndjango/' , views.learndjango , name = 'learndjango'),
    path('learnsql/' , views.learnsql , name = 'learnsql'),
    path('intro/' , views.intro , name = "intro")

]
