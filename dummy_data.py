import os
import django
from django.conf import settings


from faker import Faker

import Faker

from job.models import company, category, job
import random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()
fake = Faker()


def create_category(n):
    fake = Faker()
    for i in range(n):
        category.objects.create(
            name=fake.name()
        )
    print(f'{n} category was added successfully')


def create_company(n):
    fake = Faker()
    images = ['job-list1.png', 'job-list2.png',
              'job-list3.png', 'job-list4.png']
    for i in range(n):
        company.objects.create(
            name=fake.company(),
            logo=f'cmpany/{images[random.randint(0,3)]}',
            subtitle=fake.text(),
            website=fake.url(),
            email=fake.email(),

        )
    print(f'{n} company was added successfully')


def create_job(n):
    fake = Faker()
    jobType = ['full time', 'part time', 'remote', 'freelance']
    for i in range(n):
        job.objects.create(
            title=fake.name(),
            Company=company.objects.all().order_by('?')[0],
            vacancy=random.randint(1, 5),
            description=fake.sentence(),
            salary_start=random.randint(2000, 2500),
            salary_end=random.randint(7000, 10000),
            job_type=jobType[random.randint(0, 3)],
            # location=fake.city(),
            experience=random.randint(1, 10),
            category=category.objects.all().order_by('?')[0],
        )
    print(f'{n} job was added successfully')


create_category(2)
create_job(10)  # 2000
create_company(5)  # 100
