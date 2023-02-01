from django.urls import path
from .views import home, order, update_pizza


urlpatterns = [
    path('', home, name="home"),
    path('order/', order, name="order"),
    path('order/<int:id>/', update_pizza, name='update'),
]