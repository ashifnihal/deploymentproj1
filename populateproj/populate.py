import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','populateproj.settings')
import django
django.setup()
from testapp.models import CarDataModel
import faker

import random
fakegen=faker.Faker()
class Populate:
    def mobileno(self):
        startswith=random.randint(6,9)
        fullnum=''
        for num in range(9):
            endswith=random.randint(0,9)
            fullnum+=str(endswith)
        mno=str(startswith)+fullnum
        self.mno=mno


    # mobileno()
    # print(mobileno())
    def fmodels(self):

        fsno=fakegen.random.randint(500,600)
        fbrands=random.choice(['vw','audi','skoda'])
        vwmodels=random.choice(['polo','vento','Tiaugon','jetta'])
        audimodels=random.choice(['A4','Q7','A9',])
        skodamodels=random.choice(['Kodiaq','laura','fabia'])
        ffuel=random.choice(['PETROL','DIESEL'])
        fyear=random.randint(2011,2019)
        fcc=random.randint(1,3)
        if fbrands=='vw':
            models=vwmodels
        elif fbrands=='audi':
            models=audimodels
        elif fbrands=='skoda':
            models=skodamodels
        print(fsno,fbrands,ffuel,fyear,fcc,models,self.mno)
        CarDataModel.objects.get_or_create(sno=int(fsno),brand=fbrands,model=models,fuel=ffuel,cc=float(fcc),year=fyear,mobileno=int(self.mno))

for x in range(50):
    n=Populate()
    n.mobileno()
    n.fmodels()
