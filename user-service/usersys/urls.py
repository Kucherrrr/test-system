from django.contrib import admin
from django.urls import path
from testsession import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', views.start_test),
    path('answer/', views.submit_answer),
]