import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

def slug_name(a):
    l = a.split()
    s1 = '-'.join(l)
    return s1


def list_p():
    phone_object = Phone.objects.all()
    p = [f'{c.id},   {c.name}' for c in phone_object]
    print(p)

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)
        for phone in phones:
            model_phone = Phone(id=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'],
                                release_date=phone['release_date'], lte_exists=phone['lte_exists'],
                                slug=slug_name(phone['name']))
            model_phone.save()


