from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.apps import apps
from datetime import date,timedelta,datetime
from dateutil.relativedelta import relativedelta
from archive.models import namadtomodel
# Create your views here.

has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
   
def pl1(request):
    all_data = []
    
    past_week = date.today() + relativedelta(days=-7)
    week = {'day':[]}
    for n in range((date.today() - past_week).days):
        week['day'].append(date.today() - timedelta(n))
    week_calculate = {}

    for item in has:
        for day_in_week in week['day']:
            data = (apps.get_model('archive',item).objects.filter(date=day_in_week.strftime("%Y-%m-%d")))
            for da in data:
                dta = {}
                if(len(str(da.data)) > 230):
                    dc = da.data.split(": [")
                    dc = dc[1].replace("}]}","")
                    dc = dc.split(",")
                    for db in dc:
                        db = db.replace("{","")
                        db = db.replace("}","")
                        db = db.split(":")
                        dta.__setitem__(db[0],db[1])                 
                    value_t = dta[" 'value_t'"]
                    vt = dta[" 'vt'"]
                    if(len(str(da.data)) > 290):
                        vbs = dta[" 'vbs'"]
                        vss = dta[" 'vss'"]
                    else:
                        vbs = dta["'vbs'"]
                        vss = dta[" 'vss'"]
                    if((int(vt.replace("'",""))) > 0):
                        calculate_d = ((((int(value_t.replace("'","")))/(int(vt.replace("'",""))))/10)*(int(vbs.replace("'",""))-int(vss.replace("'",""))))/1000000000
                        calculate_d = round(calculate_d,4)
                        if da.name in week_calculate:
                            new_data = week_calculate[da.name]
                            new_calculate = calculate_d + new_data
                            new_calculate = round(new_calculate,4)
                            week_calculate.__setitem__(da.name,new_calculate)
                        else:
                            week_calculate.__setitem__(da.name,calculate_d)
    #section 2
    for item in has:
            data = (apps.get_model('archive',item).objects.filter(date=date.today().strftime("%Y-%m-%d")))
            for da in data:  
                dta = {}
                if(len(str(da.data)) > 230):
                    dc = da.data.split(": [")
                    dc = dc[1].replace("]}","")
                    dc = dc.split(",")
                    for db in dc:
                        db = db.replace("{","")
                        db = db.replace("}","")
                        db = db.split(":")
                        dta.__setitem__(db[0],db[1])
                    value_t = dta[" 'value_t'"]
                    vt = dta[" 'vt'"]
                    if(len(str(da.data)) > 290):
                        vbs = dta[" 'vbs'"]
                        vss = dta[" 'vss'"]
                    else:
                        vbs = dta["'vbs'"]
                        vss = dta[" 'vss'"]
                    if((int(vt.replace("'",""))) > 0):
                        calculate_d = ((((int(value_t.replace("'","")))/(int(vt.replace("'",""))))/10)*(int(vbs.replace("'",""))-int(vss.replace("'",""))))/1000000000
                        calculate_d = round(calculate_d,4)

                        if da.name in week_calculate:
                            print('')
                        else:
                            week_calculate.__setitem__(da.name,calculate_d)
                        item_p = namadtomodel.objects.filter(model=item)

                        all_data.append({"n":da.name,"g":item,"g_fa":item_p[0].namad,"d":calculate_d,"w":week_calculate[da.name]})
  
    return JsonResponse(all_data,safe=False)


def pl2(request):

    all_data = []

    past_week = date.today() + relativedelta(days=-15)
    week = {'day':[]}
    for n in range((date.today() - past_week).days):
        week['day'].append(date.today() - timedelta(n))
    
    cumulative_month = []
    
    for day_in_week in week['day']:
        cumulative_day = 0
        for item in has:
            data = (apps.get_model('archive',item).objects.filter(date=day_in_week.strftime("%Y-%m-%d")))
            for da in data:
                dta = {}
                if(len(str(da.data)) > 210):
                    dc = da.data.split(": [")
                    dc = dc[1].replace("]}","")
                    dc = dc.split(",")
                    for db in dc:
                        db = db.replace("{","")
                        db = db.replace("}","")
                        db = db.split(":")
                        dta.__setitem__(db[0],db[1])                 
                    value_t = dta[" 'value_t'"]
                    vt = dta[" 'vt'"]
                    if(len(str(da.data)) > 290):
                        vbs = dta[" 'vbs'"]
                        vss = dta[" 'vss'"]
                    else:
                        vbs = dta["'vbs'"]
                        vss = dta[" 'vss'"]
                    if((int(vt.replace("'",""))) > 0):
                        calculate_d = ((((int(value_t.replace("'","")))/(int(vt.replace("'",""))))/10)*(int(vbs.replace("'",""))-int(vss.replace("'",""))))/1000000000
                        calculate_d = round(calculate_d,4)
                        cumulative_day = cumulative_day + calculate_d
        if(cumulative_day > 0):
            cumulative_month.append({"d":day_in_week.strftime("%Y-%m-%d"),"c":cumulative_day})

    return JsonResponse(cumulative_month,safe=False)
