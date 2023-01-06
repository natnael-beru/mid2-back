from django.urls import path
from . import views

urlpatterns = [
    path('studentlist',views.studentlist.as_view()),
    path('studentdel/<int:pk>',views.studentdel.as_view())
]