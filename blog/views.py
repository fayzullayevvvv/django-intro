from django.http import HttpRequest, HttpResponse
from django.urls import reverse


def contact_view(reqeust: HttpRequest) -> HttpResponse:
    
    url = reverse('users:contact_page')
    
    return HttpResponse(f'URL: {url}')
