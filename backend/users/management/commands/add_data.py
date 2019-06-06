from django.core.management.base import BaseCommand
import requests
import json
from django.db.utils import IntegrityError
from time import time
from users.models import (
    FakeUser,
    FakeAddress,
    FakeCompany,
    FakeGeo
)

# Generate a list of instances.
class Command(BaseCommand):
    help = 'Add data to database.'

    def users_instance_generator(self, data):
        for d in data:
            # create the current user instance
            user = FakeUser(
                name = d['name'],
                username = d['username'],
                email = d['email'],
                phone = d['phone'],
                website = d['website']
            )
            # create the address and user to it
            if d['address']:
                address = FakeAddress(
                    street = d['address'].get('street', ''),
                    suite = d['address'].get('suite', ''),
                    city = d['address'].get('city', ''),
                    zipcode = d['address'].get('zipcode', '')
                )

                # create the geo and assign address to it
                geo = FakeGeo(
                    lat = d['address']['geo'].get('lat', ''),
                    lng = d['address']['geo'].get('lng', '')
                )
            # create company and assign user to it
            if d['company']:
                company = FakeCompany(
                    name = d['company'].get('name'),
                    catchPhrase = d['company'].get('catchPhrase', ''),
                    bs = d['company'].get('bs', '')
                )
            
            # Add data and their relationships
            try:
                user.save()
            except IntegrityError:
                self.stderr.write('Error: Duplicated unique users data')
                return False
            
            address.user = user
            company.user = user
            address.save()
            company.save()
            geo.address = address
            geo.save()
        return True

        


    def handle(self, *args, **kwargs):
        start_time = time()

        url = 'https://jsonplaceholder.typicode.com/users'
        users_data = requests.get(url).json()
        
        users_instances = self.users_instance_generator(users_data)

        if users_instances:
            duration = time() - start_time
            self.stdout.write(self.style.SUCCESS(f'Success, took {duration} seconds'))
