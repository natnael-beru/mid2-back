from django.urls import path
from . import views

urlpatterns = [
    path('techlist',views.techlist.as_view()),
    path('techdel/<int:pk>',views.techdel.as_view())
]