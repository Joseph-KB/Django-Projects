from django.urls import path

from . import views

app_name='customer'
urlpatterns=[
    path('register/',views.registaration,name='customer_registration'),
    path('login/',views.user_login,name='customer_login'),
]