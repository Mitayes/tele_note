from django.shortcuts import render
from . models import Topic
import os

api_token = os.getenv('api_token')


def index(requests):
    # Получаем логин залогинённого пользователя
    # user_name = requests.user.username
    # Получаем ИД залогинённого пользователя
    user_id = requests.user.pk
    # Получаем записи пользователя из БД
    data = Topic.objects.filter(owner=user_id)
    context = {
        'data': data,
    }
    return render(requests, 'index.html', context)
