# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pandas as pd
from patientregister.models import pactientaccount
from medicalproviders.models import medicalproviders
from doctor.models import doctor , Bookedsession

# Create your views here.

def reception(request,email):
    data1 = 'patient'
    data = pactientaccount.objects.filter(first_name=email)
    if data :
        name = data[0].first_name
    else:
        data1 = medicalproviders.objects.filter(first_name=email)
        data1 = data1[0].choosemedicalprovider
        data = medicalproviders.objects.filter(first_name=email)
        name = data[0].first_name
        dataaa = medicalproviders.objects.filter(first_name=email)
        bookedse = Bookedsession.objects.filter(email_recep =dataaa[0].email )
    return render(request,'reception/index.html',{'doctor':data[0] ,'medical':data1,'rs':email , 'email_res':data[0].email,'bookedse':bookedse})