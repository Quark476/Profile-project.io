from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('create/', views.create_portfolio, name='create_portfolio'),
    path('list/', views.portfolio_list, name='portfolio_list'),
]