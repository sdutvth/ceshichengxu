from django.urls import path
from .views import PermCRUD

urlpatterns = [
    path('test/', PermCRUD.as_view())
]
