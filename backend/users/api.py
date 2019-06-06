from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import (
    FakeAddress,
    FakeCompany,
    FakeGeo,
    FakeUser
)

from users.serializers import (
    FakeAddressSerializer,
    FakeCompanySerializer,
    FakeGeoSerializer,
    FakeUserSerializer
)

class FakeUserApi(ModelViewSet):
    queryset = FakeUser.objects.all()
    serializer_class = FakeUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FakeAddressApi(ModelViewSet):
    queryset = FakeAddress.objects.all()
    serializer_class = FakeAddressSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FakeGeoApi(ModelViewSet):
    queryset = FakeGeo.objects.all()
    serializer_class = FakeGeoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FakeCompanyApi(ModelViewSet):
    queryset = FakeCompany.objects.all()
    serializer_class = FakeCompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]