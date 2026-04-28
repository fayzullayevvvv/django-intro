import json

from django.http import HttpRequest, HttpResponse


def register_view(reqeust: HttpRequest, pk: int) -> HttpResponse:
    params = reqeust.GET

    min_price = params.get('min_price')
    max_price = params.get('max_price')

    # data = json.loads(reqeust.body)
    # print(data)

    headers = reqeust.headers
    print(headers.get('Content-Type'))

    form_data = reqeust.POST
    print(form_data.get('email'))

    files = reqeust.FILES

    image = files.get('image')
    print(image.read())

    return HttpResponse(content=f"Register page: {pk}, {min_price}:{max_price}", status=400)
    

def login_view(reqeust: HttpRequest) -> HttpResponse:
    return HttpResponse("Login page")


def logout_view(reqeust: HttpRequest) -> HttpResponse:
    return HttpResponse("Logout page")

