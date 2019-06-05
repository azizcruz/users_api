from django.contrib import admin
from users.models import (
    FakeAddress,
    FakeCompany,
    FakeGeo,
    FakeUser
)
# Register your models here.
admin.site.register(FakeAddress)
admin.site.register(FakeCompany)
admin.site.register(FakeGeo)
admin.site.register(FakeUser)