from uuid import uuid4

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def get_hello(request: WSGIRequest) -> HttpResponse:
    return HttpResponse("hello world")


# 12. Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#
#     a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#     b) zwróć listę jako JsonResponse


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return HttpResponse(f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids":uuids})

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f"X = {x}, Y = {y}, Z = {z}")


def get_arguments_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(int("a")))
    return HttpResponse(f"a = {a}, b = {b}, c = {c}")

# 15. Przygotuj funkcję drukująca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE

def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    query_type = "Unknown"
    if request.method == "GET":
        query_type = "This is GET"
    elif request.method == "POST":
        query_type = "This is POST"
    elif request.method == "This is PUT":
        query_type = "This is PUT"
    elif request.method == "This is DELETE":
        query_type = "This is DELETE"

    return HttpResponse(query_type)