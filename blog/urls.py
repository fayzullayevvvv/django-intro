from django.urls import path

from blog.views import contact_view


urlpatterns = [
    path("contact/", contact_view, name='contact_page'),
]
