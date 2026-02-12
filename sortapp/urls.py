from django.urls import path
from .views import sort_view

urlpatterns = [
    path('', sort_view, name='sort_view')
]
