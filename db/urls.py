from django.urls import path
from .views import get_db_health

urlpatterns = [
    path('db-health/', get_db_health, name='db_health'),
]
