from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    # return HttpResponse("<h1>Главная</h1>")
    # return HttpResponse("Hello METANIT.COM", headers={"SecretCode": "21234567"})
    # return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")
    # return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")
    return HttpResponse("<h2>Главная</h2>")

def user(request, name="Undefined", age=0):
    return HttpResponse(f"<h2>Имя: {name} <br> Возраст: {age}</h2>")

def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"] # получаем данные браузера
    path = request.path # получаем запрошенный путь

    return HttpResponse(f"""
        <p style="font-size: 24px;">Host: {host}</p>
        <p style="font-size: 24px;">Path: {path}</p>
        <p style="font-size: 24px;">User-agent: {user_agent}</p>
    """)


