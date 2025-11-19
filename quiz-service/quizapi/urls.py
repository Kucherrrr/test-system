from django.contrib import admin
from django.urls import path
from questions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/question/<str:level>/', views.get_question_by_level),
]