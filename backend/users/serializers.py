from rest_framework import serializers
from users.models import (
    FakeAddress,
    FakeCompany,
    FakeGeo,
    FakeUser
)

class FakeUserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = FakeUser
        fields = ('id', 'username', 'email', 'address', 'phone', 'website', 'company')
class FakeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = FakeAddress
        fields = '__all__'

class FakeGeoSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = FakeGeo
        fields = '__all__'

class FakeCompanySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = FakeCompany
        fields = '__all__'