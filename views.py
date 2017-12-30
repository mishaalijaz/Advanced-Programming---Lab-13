
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def add_books(request):
    now = datetime.datetime.now()
    html = "<html><body>DISPLAY BOOKS.</body></html>"
    return HttpResponse(html)

def add_books(request):
    now = datetime.datetime.now()
    html = "<html><body>ADD BOOK.</body></html>"
    return HttpResponse(html)

def delete_books(request):
    now = datetime.datetime.now()
    html = "<html><body>DELETE BOOK.</body></html>"
    return HttpResponse(html)

def update_books(request):
    now = datetime.datetime.now()
    html = "<html><body>UPDATE BOOK.</body></html>"
    return HttpResponse(html)