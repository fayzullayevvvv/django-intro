from django.http import HttpRequest, HttpResponse


def register_view(reqeust: HttpRequest) -> HttpResponse:
    return HttpResponse("Register page")
    

def login_view(reqeust: HttpRequest) -> HttpResponse:
    return HttpResponse("Login page")


def logout_view(reqeust: HttpRequest) -> HttpResponse:
    return HttpResponse("Logout page")

