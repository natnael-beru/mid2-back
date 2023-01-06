from django.urls import path
from . import views

urlpatterns = [
    path('employlist',views.employlist.as_view()),
    path('empdel/<int:pk>',views.employdel.as_view())
]
