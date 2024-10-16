# content/urls.py

from django.urls import path
from .views import ContentListCreateView, ContentDetailView

urlpatterns = [
    path('', ContentListCreateView.as_view(), name='content_list_create'),
    path('<int:pk>/', ContentDetailView.as_view(), name='content_detail'),
]
