
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index" ),
    path('<int:month>', views.monthly_challages_by_number),
    path('<str:month>', views.monthly_challage ,name="monthly_challange"),
]