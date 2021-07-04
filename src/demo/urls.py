from django.urls import path, include
from rest_framework import routers
from .views import DemoViewSet

router = routers.DefaultRouter()
router.register('all', DemoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
