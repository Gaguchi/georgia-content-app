# content/views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Content
from .serializers import ContentSerializer
from .services import generate_content
from django.utils import timezone

class ContentListCreateView(generics.ListCreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Content.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        prompt = serializer.validated_data.get('prompt')
        content_type = serializer.validated_data.get('content_type')
        generated = generate_content(prompt, content_type)
        serializer.save(user=self.request.user, generated_content=generated)

class ContentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Content.objects.filter(user=self.request.user)
