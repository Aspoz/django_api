from django.shortcuts import render
from rest_framework import viewsets
from docs.models import Document
from docs.serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer