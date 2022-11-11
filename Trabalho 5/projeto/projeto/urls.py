from django.urls import path, include
import projeto
from projeto import views

urlpatterns = [
    path('', projeto.views,name='homepage.urls'),
]
