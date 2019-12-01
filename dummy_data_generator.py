import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','talent_management_system.settings')

import django
django.setup()

## FAKE POP script
import random
from talent_info_app.models import Person
from faker import Faker

fakegen = Faker()
skill_list = ['Data', 'Programming', 'Agile', 'Delivery', 'BA']

def populate(N=5):
    for entry in range(N):

        fake_name = fakegen.name()
        fake_orgnisation = fakegen.company()
        fake_email = fakegen.email()
        fake_skill = random.choice(skill_list)
        fake_skill_level = random.randint(1, 5)

        fake_person = Person.objects.get_or_create(name = fake_name,
                                                   orgnisation = fake_orgnisation,
                                                   email = fake_email,
                                                   skill = fake_skill,
                                                   skill_level = fake_skill_level
                                                   )

if __name__ == '__main__':
    print("populating scripts!")
    populate(20)
    print("populating complete!")
