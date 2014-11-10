from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from docs import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'docs', views.DocumentViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
