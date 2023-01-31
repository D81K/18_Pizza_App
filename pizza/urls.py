from django.urls import path
from .views import home, order


urlpatterns = [
    path('', home),
    path('order/', order),
]