from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.apps import apps

# Create your views here.

has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
      
def pl1(request,date_time):
    all_data = {}
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
                pe = dta[" 'pe'"]
                pi = dta[" 'pi'"]
                vbs = dta[" 'vbs'"]
                vss = dta[" 'vss'"]
                calculate = ((((int(pe.replace("'",""))*7)+(int(pi.replace("'",""))*3))/10)*(int(vbs.replace("'",""))-int(vss.replace("'",""))))/10000000000
                all_data[da.name] = calculate
    return JsonResponse(all_data)
