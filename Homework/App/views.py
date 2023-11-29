from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"] # получаем данные браузера
    ip = request.META["REMOTE_ADDR"]

    return HttpResponse(f"""
        <p style="font-size: 24px;">Host: {host}</p>
        <p style="font-size: 24px;">User-agent: {user_agent}</p>
        <p style="font-size: 24px;">IP client: {ip}</p>
    """)

def error(request):
    return HttpResponse("К сожалению произошла ошибка", status=400, reason="Incorrect data")

def user(request, login="Undefined", name_folder="Undefined", number_post=0):
    return HttpResponse(f'<p style="font-size: 24px;">Логин: {login} <br> Имя папки: {name_folder} <br> Номер поста: {number_post}</p>')