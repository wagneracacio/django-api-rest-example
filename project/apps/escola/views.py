from django.http import HttpResponse, HttpRequest


def hello(request:HttpRequest) -> HttpResponse:
    return HttpResponse('hello world')

