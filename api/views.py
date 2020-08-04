from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.apps import apps
from datetime import date,timedelta
from dateutil.relativedelta import relativedelta

# Create your views here.

has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
   
def pl1(request,date_time):
    all_data = []
    
    past_week = date.today() + relativedelta(days=-7)
    week = {'day':[]}
    for n in range((date.today() - past_week).days):
        week['day'].append(past_week + timedelta(n))

    week_calculate = {}

    for item in has:
        for day_in_week in week['day']:
            data = (apps.get_model('archive',item).objects.filter(date=day_in_week.strftime("%Y-%m-%d")))
            for da in data:
                dta = {}
                if(len(str(da.data)) > 290):
                    dc = da.data.split("[")
                    dc = dc[1].replace("]}","")
                    dc = dc.split(",")
                    for db in dc:
                        db = db.replace("{","")
                        db = db.replace("}","")
                        db = db.split(":")
                        dta.__setitem__(db[0],db[1])                 
                    pe = dta[" 'value_t'"]
                    pi = dta[" 'vt'"]
                    vbs = dta[" 'vbs'"]
                    vss = dta[" 'vss'"]
                    if((int(pi.replace("'",""))) > 0):
                        calculate_d = ((((int(pe.replace("'","")))/(int(pi.replace("'",""))))/10)*(int(vbs.replace("'",""))-int(vss.replace("'",""))))/1000000000
                        if da.name in week_calculate:
                            new_data = week_calculate[da.name]
                            new_calculate = calculate_d + new_data
                            week_calculate.__setitem__(da.name,new_calculate)
                        else:
                            week_calculate.__setitem__(da.name,calculate_d)

    #return HttpResponse(week_calculate['سيمرغ'])   

    for item in has:
            data = (apps.get_model('archive',item).objects.filter(date=date_time))
            for da in data:  
                dta = {}
                if(len(str(da.data)) > 290):
                    dc = da.data.split("[")
                    dc = dc[1].replace("]}","")
                    dc = dc.split(",")
                    for db in dc:
                        db = db.replace("{","")
                        db = db.replace("}","")
                        db = db.split(":")
                        dta.__setitem__(db[0],db[1])
                    pe = dta[" 'value_t'"]
                    pi = dta[" 'vt'"]
                    vbs = dta[" 'vbs'"]
                    vss = dta[" 'vss'"]
                    if((int(pi.replace("'",""))) > 0):

                        calculate_d = ((((int(pe.replace("'","")))/(int(pi.replace("'",""))))/10)*(int(vbs.replace("'",""))-int(vss.replace("'",""))))/1000000000
                        all_data.append({"n":da.name,"g":item,"d":calculate_d,"w":week_calculate[da.name]})
  
    return JsonResponse(all_data,safe=False)
