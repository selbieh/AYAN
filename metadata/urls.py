from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('metadata', views.MetadataView)
router.register('document', views.DocumentView)




urlpatterns = [
    path('',include(router.urls)),
]