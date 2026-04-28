from django.urls import path

from .views import register_view, login_view, logout_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name='register_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('foasdjkfoas/', logout_view, name='contact_page'),
]
