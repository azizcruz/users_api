from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users import api


router = DefaultRouter()
router.register(r'users', api.FakeUserApi)
router.register(r'addresses', api.FakeAddressApi)
router.register(r'companies', api.FakeCompanyApi)
router.register(r'geos', api.FakeGeoApi)

urlpatterns = [
    path('', include(router.urls)),
]