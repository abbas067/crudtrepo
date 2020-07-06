import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudproject.settings')
django.setup()
from testapp.models import *
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1000,9999)
        fname=faker.name()
        fesal=randint(20000,40000)
        feaddr=faker.address()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fname,esal=fesal,eaddr=feaddr)
populate(30)
