from django.http import HttpResponse


def ping_view(_):
    return HttpResponse('pong')