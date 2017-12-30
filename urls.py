# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('/addbooks', views.add_books, name="add-books"),
    path('/deletebooks', views.delete_books, name="delete-books"),
    path('/updatebooks', views.update_books, name="update-books"),
    path('/displaybooks', views.display_books, name="display-books"),
]