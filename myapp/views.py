from django.shortcuts import render
from .models import Notification


def post_list(request):
    notifications = Notification.objects.order_by('created_datetime')
    return render(request, 'post_list.html', {'notifications':notifications})
