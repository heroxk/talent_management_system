import os
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE','talent_management_system.settings')

import django
django.setup()

## FAKE POP script
import random
from talent_info_app.models import Person
from faker import Faker

fakegen = Faker()
skill_list = [
  'Java',
  '.NET',
  'NodeJS',
  'Spark',
  'Hadoop',
  'Power BI',
  'AWS',
  'Azure',
  'GCP'
]

def populate(N=5):

    cols = ['name', 'orgnisation', 'email', 'skill', 'skill_level']
    df_fake_person = pd.DataFrame(columns=cols)


    for entry in range(N):

        fake_name = fakegen.name()
        fake_orgnisation = fakegen.company()
        fake_email = fakegen.email()
        fake_skill = random.choice(skill_list)
        fake_skill_level = random.randint(1, 5)

        df2 = pd.DataFrame([[fake_name,
                            fake_orgnisation,
                            fake_email,
                            fake_skill,
                            fake_skill_level
                            ]], columns=cols)

        df_fake_person = df_fake_person.append(df2)

    df_fake_person.to_csv('data/talent_info.csv', index=False)


if __name__ == '__main__':
    print("populating scripts!")
    populate(100)
    print("populating complete!")
