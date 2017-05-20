from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime

def index(request):
    date = datetime.now().strftime('%B %d, %Y')
    time = datetime.now().strftime('%H:%M %p')
    context = {
        'date': date,
        'time': time
    }
    return render(request, 'timeDisplay_app/index.html', context)
