from django.urls import path
from .viewsets import CompanyViewSet

urlpatterns = [
    path('', CompanyViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'put': 'update', 'delete': 'destroy'}))
]
