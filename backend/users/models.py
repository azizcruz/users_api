from django.db import models

# Create your models here.
class FakeUser(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class FakeCompany(models.Model):
    user = models.ForeignKey('users.FakeUser', related_name='company', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)
    catchPhrase = models.CharField(max_length=255, blank=True, null=True)
    bs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class FakeAddress(models.Model):
    user = models.OneToOneField('users.FakeUser', related_name='address', on_delete=models.CASCADE, null=True, blank=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    suite = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.street

class FakeGeo(models.Model):
    address = models.OneToOneField('users.FakeAddress', related_name='geo', on_delete=models.CASCADE, null=True, blank=True)
    lat = models.CharField(max_length=255, blank=True, null=True)
    lng = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.address.street