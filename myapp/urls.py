from django.urls import path
from myapp.views import mi_familia

urlpatterns = [
    path('', mi_familia),
]