from django.http import HttpRequest, HttpResponse


def contact_view(reqeust: HttpRequest) -> HttpResponse:
    return HttpResponse('salom')
