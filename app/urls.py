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

]
