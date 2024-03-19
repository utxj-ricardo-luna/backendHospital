from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'nacimientos_bebes', views.nacimientos_bebesViewSet)
router.register(r'seguimiento_pediatria', views.seguimiento_pediatriaViewSet)

urlpatterns = [
	path('api/v1',include(router.urls))
]

