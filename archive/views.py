from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import datetime,time
import json
from django.apps import apps
from datetime import timedelta,date
from dateutil.relativedelta import relativedelta

from archive.models import Archive,namadtomodel,active_date,initial_public_offering

#4-16
from archive.models import agriculture,coal,oil_gas,metal_ores
from archive.models import other_mines,textiles,wood,paper
from archive.models import printz,pet_products,plastic,elec_computer
from archive.models import basic_metal,metal_products,equipment,electrical

#17-32
from archive.models import comm_devices,cars,sugar,multidisciplinary
from archive.models import supply_elec_gas,food,drug,chemical
from archive.models import contracting,wholesale,retail,tile
from archive.models import cement,non_metal,hotel,investments

#33-48
from archive.models import banks,other_financial,transportation,water_transportation
from archive.models import financial,insurance,auxiliary,etf
from archive.models import financing_bonds,estate,engineering,app_computer
from archive.models import information,technical_services,artistic,tanning

#49
from archive.models import telecommunication

has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    

def edit_namad_new(request,date_start):
    all_data = []
    str_date = date_start
    st_d = str_date.split(',')
    past_week = datetime.date(int(st_d[0]),int(st_d[1]),int(st_d[2])) + relativedelta(days=-30)
    week = {'day':[]}
    for n in range((datetime.date(int(st_d[0]),int(st_d[1]),int(st_d[2])) - past_week).days):
        week['day'].append(datetime.date(int(st_d[0]),int(st_d[1]),int(st_d[2])) - timedelta(n))
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
                    pe = dta[" 'pe'"]
                    vt = dta[" 'vt'"]
                    
                    if((int(vt.replace("'",""))) == 0):
                        if((int(pe.replace("'",""))) == 1000):
                            return HttpResponse([da.name])
                    
def revamp_history_view(request):
    return render(request,'revamp_history_view.html')

def edit_duplicate_history_view(request):
    return render(request,'edit_duplicate_history_view.html')

def get_history_group(request):
    nm = namadtomodel.objects.all()
    return render(request,'get_history_group.html',{"namad_model":nm})

def get_history_namad(request):
    nm = Archive.objects.all()
    return render(request,'get_history_namad.html',{"namad":nm})

def get_daily_co(request):
    import requests
    import time

    group = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']

    for data in group:
        address = "http://45.82.137.113:8000/data/daily/{}".format(data)
        requests.get(address)
        time.sleep(3)

def get_daily_namad(request):
    
    incom = {'name':[]}
    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    

    for item in has:
        today = apps.get_model('archive',item).objects.filter(date=datetime.date.today())
        for intodat in today :
            if(len(str(intodat.data)) > 30 and len(str(intodat.data)) < 330):
                incom['name'].append({intodat.name})

    return render(request,'get_daily_data.html',{'count':incom['name']})

def check_duplicate_data(request,start_time):
    start_time = start_time.split(',')
    start_date = date(int(start_time[0]),int(start_time[1]),int(start_time[2]))

    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']     
    data = []
    data2 = []
    for item in has:

        today = apps.get_model('archive',item).objects.filter(date=start_date.strftime("%Y-%m-%d"))
        for intodat in today:
            data.append(intodat.name)
    
    for item in has:
        for name_namad in data:
            if apps.get_model('archive',item).objects.filter(name=name_namad,date=start_date.strftime("%Y-%m-%d")).count() > 1:
                sm = apps.get_model('archive',item).objects.filter(name=name_namad,date=start_date.strftime("%Y-%m-%d"))
                apps.get_model('archive',item).objects.filter(id=sm[1].id).delete()
                
                
    return HttpResponse("done")

def history_revamp(request,start,end):

    export = {'e':[]}
    start_time = start.split(',')
    end_time = end.split(',')

    start_date = date(int(start_time[0]),int(start_time[1]),int(start_time[2]))
    end_date   = date(int(end_time[0]),int(end_time[1]),int(end_time[2]))

    incom = {'db':[]}
    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    
    step_day = {'day':[]}
    for n in range((end_date - start_date).days):
        step_day['day'].append(start_date + timedelta(n))

    for single_date in step_day['day']:
        for item in has:
            err_list = (apps.get_model('archive',item).objects.filter(date=single_date.strftime("%Y-%m-%d")))
            for item in err_list:
                if(len(str(item.data)) < 90):
                    incom['db'].append({"name":item.name,"date":single_date.strftime("%Y%m%d"),"date2":single_date.strftime("%Y-%m-%d")})

    for list_err in incom['db']:
        check = Archive.objects.filter(name=list_err['name'])
        name = list_err['name']
        url2 = check[0].history
        link = "{}{}".format(url2,list_err['date'])
        group_t1 = namadtomodel.objects.filter(namad=check[0].group)
        group = group_t1[0].model

        response = requests.get(link)
        data_d = response.text

        hiderow = re.compile("var\s+ClientTypeData=(.*)")
        hidden = hiderow.findall(data_d)

        end = re.compile("var\s+ClosingPriceData=(.*)")
        endprice = end.findall(data_d)
                    
        my_obj = {'data':[]}

        if(len(str(hidden)) > 50):
            if(len(str(endprice)) > 50):  
                p = re.compile("var\s+ClientTypeData=(.*)")
                b = p.findall(data_d) 
                for item in b :
                    item2 = item.split(',')
                    my_obj['data'].append({'vbs' : item2[4]}) 
                    my_obj['data'].append({'vbc' : item2[5]}) 
                    my_obj['data'].append({'vss' : item2[6]}) 
                    my_obj['data'].append({'vsc' : item2[7]}) 
                    my_obj['data'].append({'cbs' : item2[0]}) 
                    my_obj['data'].append({'cbc' : item2[1]}) 
                    my_obj['data'].append({'css' : item2[2]}) 
                    my_obj['data'].append({'csc' : item2[3]}) 
                            
                            #Get End Price
                    end = re.compile("var\s+ClosingPriceData=(.*)")
                    endprice = end.findall(data_d)

                    for item in endprice :
                        item5 = item.replace('[[','[')
                        item6 = item5.replace(']]',']')
                        item7 = item6.split('],[')
                        item8 = item7[-1]
                        item9 = item8.replace("'","")
                        item10 = item9.split(',')
                        my_obj['data'].append({'pi' : item10[2]}) 
                        my_obj['data'].append({'pe' : item10[3]}) 
                        my_obj['data'].append({'ct' : item10[8]}) 
                        my_obj['data'].append({'vt' : item10[9]}) 
                        my_obj['data'].append({'value_t' : item10[10]}) 

                        apps.get_model('archive',group).objects.filter(name=name,date=list_err['date2']).update(data=my_obj)
                        export['e'].append({list_err['name'],list_err['date2'], "DONE"})

            else:
                export['e'].append({list_err['name'],list_err['date2'],"ERR"})
        else:
            export['e'].append({list_err['name'],list_err['date2'],"ERR"})

        time.sleep(1)   
    return HttpResponse(export['e'])

def get_hisory_group(request,group,start,end):
    
    #has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    #for item in has:
        namad = namadtomodel.objects.filter(model=group)
        all_namad_in_group = Archive.objects.filter(group=namad[0].namad)
        for namad_in_group in all_namad_in_group:
            link = "http://45.82.137.113:8000/data/history/{}/{}/{}/{}".format(group,start,end,namad_in_group.name)
            requests.get(link)

def detail_day_namads(request,date_namad):
    
    date_namad = date_namad.split(',')
    date_namad = date(int(date_namad[0]),int(date_namad[1]),int(date_namad[2]))

    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    
    activedate = active_date.objects.filter(miladi=date_namad.strftime("%Y%m%d"))
    
    in_day = {'correct':[],'err':[],'all_data':[],'none':[]}

    if(len(str(activedate)) > 30):
        for item in has:
            all_inday_correct = (apps.get_model('archive',item).objects.filter(date=date_namad.strftime("%Y-%m-%d")))            
            for correct in all_inday_correct:
                in_day['correct'].append({item : correct.name})

            all_inday_err = (apps.get_model('archive',item).objects.filter(date=date_namad.strftime("%Y-%m-%d"),data='error_history'))
            for err in all_inday_err:
                in_day['err'].append({item : err.name})

    all_inday = Archive.objects.all()
    for all_data in all_inday:
        gp = namadtomodel.objects.filter(namad=all_data.group)
        for t in gp:
            in_day['all_data'].append({t.model:all_data.name})

    for none in in_day['all_data']:
        if none not in in_day['correct']:
                in_day['none'].append(none)

    return render(request,'check_on_day_history.html' , {'correct':in_day['correct'],'err':in_day['err'],'all_data':in_day['none']}) 

def check_all_date(request,start,end):
    
    start_time = start.split(',')
    end_time = end.split(',')

    start_date = date(int(start_time[0]),int(start_time[1]),int(start_time[2]))
    end_date = date(int(end_time[0]),int(end_time[1]),int(end_time[2]))

    incom = {'name':[]}
    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    
    step_day = {'day':[]}
    for n in range((end_date - start_date).days):
        step_day['day'].append(start_date + timedelta(n))
    
    ok = []
    err = []
    timer = []
    for single_date in step_day['day']:
        in_day = {'ok':[],'err':[]}
        activedate = active_date.objects.filter(miladi=single_date.strftime("%Y%m%d"))
        if(len(str(activedate)) > 30):

            for item in has:
                all_inday = (apps.get_model('archive',item).objects.filter(date=single_date.strftime("%Y-%m-%d")))
                all_inday_err = (apps.get_model('archive',item).objects.filter(date=single_date.strftime("%Y-%m-%d"),data='error_history'))

                for dt in all_inday:
                    in_day['ok'].append(dt.name)

                for dt in all_inday_err:
                    in_day['err'].append(dt.name)

            timer.append(single_date.strftime('%d %b %Y'))
            ok.append(len(in_day['ok']))
            err.append(len(in_day['err']))

    return render(request,'daily_icomp_all.html' , {'ok':ok,'err':err,'timer':timer}) 

def incomp_count(request):
    incom = {'name':[]}
    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    

    for item in has:
        #edit          datetime.date.today()
        today = apps.get_model('archive',item).objects.filter(date='2020-07-27')
        for intodat in today :
            if(len(intodat.data) > 5 and len(intodat.data) < 210):
                incom['name'].append({intodat.name})

    return render(request,'daily_icomp_all.html',{'inc':incom['name']}) 

def incomp(request):
    incom = {'name':[]}
    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    
    for item in has:
        #edit
        today = apps.get_model('archive',item).objects.filter(date=datetime.date.today())
        for intodat in today :
            if(len(intodat.data) > 30 and len(intodat.data) < 330):

                site = Archive.objects.filter(name=intodat.name)
                group = site[0].group

                url = site[0].url
                response = requests.get(url)
                plain_response = response.text
                in_page = re.compile("TopInst=(.*)")
                data_inpage = in_page.findall(plain_response)
                
                my_obj = {'data':[]}
            
                for data in data_inpage :
                    arr = data.split(',')
                    my_obj['data'].append({'vl' : arr[8].rsplit('=')[1]}) 
                    my_obj['data'].append({'cs' : arr[10].rsplit('=')[1]}) 
                    my_obj['data'].append({'avm' : arr[24].rsplit('=')[1].replace("'","")}) 
                    my_obj['data'].append({'sf' : arr[26].rsplit('=')[1].replace("'","")}) 

                url2 = site[0].api

                response2 = requests.get(url2)
                plain_api = response2.text

                in_api = re.compile("A.*")
                data_inapi = in_api.findall(plain_api)

                in_api_is = re.compile("IS.*")
                data_inapi_is = in_api_is.findall(plain_api)

                in_api_as = re.compile("AS.*")
                data_inapi_as = in_api_as.findall(plain_api)

                in_api_i = re.compile("I.*")
                data_inapi_i = in_api_i.findall(plain_api)

                if(len(str(data_inapi)) > 180):
                    
                    for data in data_inapi :
                        arr = data.split(',')
                        if(int(arr[7]) > 0):
                            my_obj['data'].append({"pi":arr[1]}) 
                            my_obj['data'].append({"pe":arr[2]}) 
                            my_obj['data'].append({"ct":arr[7]}) 
                            my_obj['data'].append({"vt":arr[8]}) 
                            my_obj['data'].append({"value_t":arr[9]}) 
                            if(group == 'etf'):
                                my_obj['data'].append({"da":arr[13]})
                                nav = arr[14].split(';') 
                                my_obj['data'].append({"nav":nav[0]}) 
                        
                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[2]
                                if(len(str(arr)) > 3): 

                                    arr = arr.split('@')               
                                    my_obj['data'].append({"bbv":arr[1]}) 
                                    my_obj['data'].append({"bbp":arr[2]}) 
                                    my_obj['data'].append({"sbp":arr[3]}) 
                                    my_obj['data'].append({"sbv":arr[4]}) 

                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[4]
                                arr = arr.split(',')
                                if(len(str(arr)) > 20):
                                    my_obj['data'].append({"vbs":arr[0]}) 
                                    my_obj['data'].append({"vbc":arr[1]}) 
                                    my_obj['data'].append({"vss":arr[3]}) 
                                    my_obj['data'].append({"vsc":arr[4]}) 

                                    my_obj['data'].append({"cbs":arr[5]}) 
                                    my_obj['data'].append({"cbc":arr[6]}) 
                                    my_obj['data'].append({"css":arr[8]}) 
                                    my_obj['data'].append({"csc":arr[9]}) 
                                
                                    we_model = namadtomodel.objects.filter(namad=group)
                                    apply_model = we_model[0].model
                                    apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
    
                        else:
                            my_obj=['Stopped stock']
                            we_model = namadtomodel.objects.filter(namad=group)
                            apply_model = we_model[0].model
                            apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                        

                elif((len(str(data_inapi_is)) > 180)):
                   
                        for data in data_inapi_is :
                            arr = data.split(',')
                            if(int(arr[7]) > 0):
                                my_obj['data'].append({"pi":arr[1]}) 
                                my_obj['data'].append({"pe":arr[2]}) 
                                my_obj['data'].append({"ct":arr[7]}) 
                                my_obj['data'].append({"vt":arr[8]}) 
                                my_obj['data'].append({"value_t":arr[9]}) 

                                for data in data_inapi_is :
                                    arr = data.split(';')
                                    arr = arr[2]
                                    if(len(str(arr)) > 3): 

                                        arr = arr.split('@')
                                            
                                        my_obj['data'].append({"bbv":arr[1]}) 
                                        my_obj['data'].append({"bbp":arr[2]}) 
                                        my_obj['data'].append({"sbp":arr[3]}) 
                                        my_obj['data'].append({"sbv":arr[4]}) 

                                for data in data_inapi_is :
                                    arr = data.split(';')
                                    arr = arr[4]
                                    if(len(str(arr)) > 20):

                                        arr = arr.split(',')
                                        my_obj['data'].append({"vbs":arr[0]}) 
                                        my_obj['data'].append({"vbc":arr[1]}) 
                                        my_obj['data'].append({"vss":arr[3]}) 
                                        my_obj['data'].append({"vsc":arr[4]}) 

                                        my_obj['data'].append({"cbs":arr[5]}) 
                                        my_obj['data'].append({"cbc":arr[6]}) 
                                        my_obj['data'].append({"css":arr[8]}) 
                                        my_obj['data'].append({"csc":arr[9]}) 
                            
                                        we_model = namadtomodel.objects.filter(namad=group)
                                        apply_model = we_model[0].model
                                        apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                        
                            else:
                                my_obj=['Stopped stock']
                                we_model = namadtomodel.objects.filter(namad=group)
                                apply_model = we_model[0].model
                                apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                        
                elif((len(str(data_inapi_as)) > 180)):
                   
                        for data in data_inapi_as :
                            arr = data.split(',')
                            if(int(arr[7]) > 0):
                                my_obj['data'].append({"pi":arr[1]}) 
                                my_obj['data'].append({"pe":arr[2]}) 
                                my_obj['data'].append({"ct":arr[7]}) 
                                my_obj['data'].append({"vt":arr[8]}) 
                                my_obj['data'].append({"value_t":arr[9]}) 

                                for data in data_inapi_as :
                                    arr = data.split(';')
                                    arr = arr[2]
                                    if(len(str(arr)) > 3): 

                                        arr = arr.split('@')
                                            
                                        my_obj['data'].append({"bbv":arr[1]}) 
                                        my_obj['data'].append({"bbp":arr[2]}) 
                                        my_obj['data'].append({"sbp":arr[3]}) 
                                        my_obj['data'].append({"sbv":arr[4]}) 

                                for data in data_inapi_as :
                                    arr = data.split(';')
                                    arr = arr[4]
                                    if(len(str(arr)) > 20):

                                        arr = arr.split(',')
                                        my_obj['data'].append({"vbs":arr[0]}) 
                                        my_obj['data'].append({"vbc":arr[1]}) 
                                        my_obj['data'].append({"vss":arr[3]}) 
                                        my_obj['data'].append({"vsc":arr[4]}) 

                                        my_obj['data'].append({"cbs":arr[5]}) 
                                        my_obj['data'].append({"cbc":arr[6]}) 
                                        my_obj['data'].append({"css":arr[8]}) 
                                        my_obj['data'].append({"csc":arr[9]}) 
                            
                                        we_model = namadtomodel.objects.filter(namad=group)
                                        apply_model = we_model[0].model
                                        apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                            else:
                                my_obj=['Stopped stock']
                                we_model = namadtomodel.objects.filter(namad=group)
                                apply_model = we_model[0].model
                                apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                        
                elif((len(str(data_inapi_i))  > 180)):
                   
                        for data in data_inapi_i :
                            arr = data.split(',')
                            if(int(arr[7]) > 0):
                                my_obj['data'].append({"pi":arr[1]}) 
                                my_obj['data'].append({"pe":arr[2]}) 
                                my_obj['data'].append({"ct":arr[7]}) 
                                my_obj['data'].append({"vt":arr[8]}) 
                                my_obj['data'].append({"value_t":arr[9]}) 

                                for data in data_inapi_i :
                                    arr = data.split(';')
                                    arr = arr[2]
                                    if(len(str(arr)) > 3): 

                                        arr = arr.split('@')
                                            
                                        my_obj['data'].append({"bbv":arr[1]}) 
                                        my_obj['data'].append({"bbp":arr[2]}) 
                                        my_obj['data'].append({"sbp":arr[3]}) 
                                        my_obj['data'].append({"sbv":arr[4]}) 

                                for data in data_inapi_i :
                                    arr = data.split(';')
                                    arr = arr[4]
                                    if(len(str(arr)) > 5):
                                        arr = arr.split(',')
                                        my_obj['data'].append({"vbs":arr[0]}) 
                                        my_obj['data'].append({"vbc":arr[1]}) 
                                        my_obj['data'].append({"vss":arr[3]}) 
                                        my_obj['data'].append({"vsc":arr[4]}) 

                                        my_obj['data'].append({"cbs":arr[5]}) 
                                        my_obj['data'].append({"cbc":arr[6]}) 
                                        my_obj['data'].append({"css":arr[8]}) 
                                        my_obj['data'].append({"csc":arr[9]}) 
                                    
                                        we_model = namadtomodel.objects.filter(namad=group)
                                        apply_model = we_model[0].model
                                        apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                            else:
                                my_obj=['Stopped stock']
                                we_model = namadtomodel.objects.filter(namad=group)
                                apply_model = we_model[0].model
                                apps.get_model('archive',apply_model).objects.filter(name=intodat.name,date=datetime.date.today()).update(data=my_obj)
                                        

    for item in has:
        #edit
        today = apps.get_model('archive',item).objects.filter(date=datetime.date.today())
        for intodat in today :
            if(len(intodat.data) > 30 and len(intodat.data) < 330):
                incom['name'].append({intodat.name})

    return render(request,'incomp.html',{'incom':incom['name']})
    
def daily_check(request):
    datain_archive = Archive.objects.all()
    all_namad = {'name':[]}
    for data in datain_archive:
        all_namad['name'].append({data.name})

    today_list = {'name':[]}
    has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
    for item in has:
        today = apps.get_model('archive',item).objects.filter(date=datetime.date.today())

        for today_namad in today:
            today_list['name'].append({today_namad.name})

    diff = []
    for arch in all_namad['name']:
        if arch not in today_list['name']:
            diff.append(arch)

    return render(request,'daily_check_namad.html',{"incom":diff})

def delete(request,group):
    apps.get_model('archive',group).objects.all().delete()
     
start_date = ''
end_date = ''

def history(request,group,start_time,end_time,name):

        start_time = start_time.split(',')
        end_time = end_time.split(',')
        start_date = date(int(start_time[0]),int(start_time[1]),int(start_time[2]))
        end_date = date(int(end_time[0]),int(end_time[1]),int(end_time[2]))

        check = Archive.objects.filter(name=name)
        url2 = check[0].history
        
        step_day = {'day':[]}
        for n in range((end_date - start_date).days):
            step_day['day'].append(start_date + timedelta(n))

        #model = apps.get_model('archive', group)
        ddd = {'d':[]}

        for single_date in step_day['day']: 

            activedate = active_date.objects.filter(miladi=single_date.strftime("%Y%m%d"))
            if(len(str(activedate)) > 30):

                hasnt = apps.get_model('archive',group).objects.filter(name=name,date=single_date.strftime("%Y-%m-%d"))

                if(len(str(hasnt)) < 40):

                    now = ''
                    now = single_date.strftime("%Y%m%d")

                    url = "{}{}".format(url2,now)
                    

                    response = requests.get(url)
                    data = response.text

                    hiderow = re.compile("var\s+ClientTypeData=(.*)")
                    hidden = hiderow.findall(data)

                    end = re.compile("var\s+ClosingPriceData=(.*)")
                    endprice = end.findall(data)
                    
                    my_obj = {'data':[]}

                    if(len(str(hidden)) > 100 and len(str(endprice)) > 100):   
                        
                        ddd['d'].append({single_date.strftime("%Y-%m-%d"),'OK'})

                      
                        p = re.compile("var\s+ClientTypeData=(.*)")
                        b = p.findall(data) 
                        for item in b :
                            item2 = item.split(',')
                            my_obj['data'].append({'vbs' : item2[4]}) 
                            my_obj['data'].append({'vbc' : item2[5]}) 
                            my_obj['data'].append({'vss' : item2[6]}) 
                            my_obj['data'].append({'vsc' : item2[7]}) 
                            my_obj['data'].append({'cbs' : item2[0]}) 
                            my_obj['data'].append({'cbc' : item2[1]}) 
                            my_obj['data'].append({'css' : item2[2]}) 
                            my_obj['data'].append({'csc' : item2[3]}) 
                        
                        #Get End Price
                        end = re.compile("var\s+ClosingPriceData=(.*)")
                        endprice = end.findall(data)

                        for item in endprice :
                            item5 = item.replace('[[','[')
                            item6 = item5.replace(']]',']')
                            item7 = item6.split('],[')
                            item8 = item7[-1]
                            item9 = item8.replace("'","")
                            item10 = item9.split(',')
                            my_obj['data'].append({'pi' : item10[2]}) 
                            my_obj['data'].append({'pe' : item10[3]}) 
                            my_obj['data'].append({'ct' : item10[8]}) 
                            my_obj['data'].append({'vt' : item10[9]}) 
                            my_obj['data'].append({'value_t' : item10[10]}) 

                            apps.get_model('archive',group).objects.create(name=name,kind=check[0].kind,date=single_date.strftime("%Y-%m-%d"),data=my_obj)

                    else:
                        apps.get_model('archive',group).objects.create(name=name,kind=check[0].kind,date=single_date.strftime("%Y-%m-%d"),data='error_history')

        return HttpResponse(ddd['d'])

def daily(request,group): 

    #1-4
    if(group == 'agriculture'):    
        data = Archive.objects.filter(group="زراعت و خدمات وابسته")
    elif(group == 'coal'):    
        data = Archive.objects.filter(group="استخراج ذغال سنگ")
    elif(group == 'oil_gas'):    
        data = Archive.objects.filter(group="استخراج نفت گاز و خدمات جنبی به جز اکتشاف")
    elif(group == 'metal_ores'):    
        data = Archive.objects.filter(group="استخراج کانه های فلزی")
    
    #5-8
    elif(group == 'other_mines'):    
        data = Archive.objects.filter(group="استخراج سایر معادن")
    elif(group == 'textiles'):    
        data = Archive.objects.filter(group="منسوجات")
    elif(group == 'wood'):    
        data = Archive.objects.filter(group="محصولات چوبی")
    elif(group == 'paper'):    
        data = Archive.objects.filter(group="محصولات کاغذی")
    
    #9-12
    elif(group == 'printz'):    
        data = Archive.objects.filter(group="انتشار چاپ تکثیر")
    elif(group == 'pet_products'):    
        data = Archive.objects.filter(group="فراورده های نفتی، کک و سوخت هسته ای")
    elif(group == 'plastic'):    
        data = Archive.objects.filter(group="لاستیک،پلاستیک")
    elif(group == 'elec_computer'):    
        data = Archive.objects.filter(group="تولیدات محصولات کامپیوتری و الکترونیکی نوری")
    
    #13-16
    elif(group == 'basic_metal'):    
        data = Archive.objects.filter(group="فلزات اساسی")
    elif(group == 'metal_products'):    
        data = Archive.objects.filter(group="ساخت محصولات فلزی")
    elif(group == 'equipment'):    
        data = Archive.objects.filter(group="ماشین آلات و تجهیزات")
    elif(group == 'electrical'):    
        data = Archive.objects.filter(group="ماشین آلات و دستگاه های برقی")
    
    #17-20
    elif(group == 'comm_devices'):    
        data = Archive.objects.filter(group="ساخت دستگاه ها و وسایل ارتباطی")
    elif(group == 'cars'):    
        data = Archive.objects.filter(group="خودرو و ساخت قطعات")
    elif(group == 'sugar'):    
        data = Archive.objects.filter(group="قند و شکر")
    elif(group == 'multidisciplinary'):    
        data = Archive.objects.filter(group="شرکت های چند رشته ای صنعتی")
    
    #21-24
    elif(group == 'supply_elec_gas'):    
        data = Archive.objects.filter(group="عرضه برق ، گاز، بخار و آب گرم")
    elif(group == 'food'):    
        data = Archive.objects.filter(group="محصولات غذایی و آشامیدنی به جز قند و شکر")
    elif(group == 'drug'):    
        data = Archive.objects.filter(group="مواد و محصولات دارویی")
    elif(group == 'chemical'):    
        data = Archive.objects.filter(group="محصولات شیمیایی")

    #25-28
    elif(group == 'contracting'):    
        data = Archive.objects.filter(group="پیمانکاری صنعتی")
    elif(group == 'wholesale'):    
        data = Archive.objects.filter(group="تجارت عمده فروشی به جز وسایل نقلیه موتوری")
    elif(group == 'retail'):    
        data = Archive.objects.filter(group="خرده فروشی به استثنای وسایل نقلیه موتوری")
    elif(group == 'tile'):    
        data = Archive.objects.filter(group="کاشی سرامیک")

    #29-32
    elif(group == 'cement'):    
        data = Archive.objects.filter(group="سیمان، آهک و گچ")
    elif(group == 'non_metal'):    
        data = Archive.objects.filter(group="سایر محصولات کانی غیر فلزی")
    elif(group == 'hotel'):    
        data = Archive.objects.filter(group="هتل و رستوران")
    elif(group == 'investments'):    
        data = Archive.objects.filter(group="سرمایه گذاری ها")

    #33-36
    elif(group == 'banks'):    
        data = Archive.objects.filter(group="بانک ها و موسسات اعتباری")
    elif(group == 'other_financial'):    
        data = Archive.objects.filter(group="سایر واسطه گریهای مالی")
    elif(group == 'transportation'):    
        data = Archive.objects.filter(group="حمل و نقل ، انبارداری و ارتباطات")
    elif(group == 'water_transportation'):    
        data = Archive.objects.filter(group="حمل و نقل آبی")

    #37-40
    elif(group == 'financial'):    
        data = Archive.objects.filter(group="واسطه گری های مالی و پولی")
    elif(group == 'insurance'):    
        data = Archive.objects.filter(group="بیمه و صندوق بازنشستگی به جز تامین اجتماعی")
    elif(group == 'auxiliary'):    
        data = Archive.objects.filter(group="فعالیت های کمکی به نهادهای مالی واسط")
    elif(group == 'etf'):    
        data = Archive.objects.filter(group="صندوق های سرمایه گذاری قابل معامله")

    #41-44
    elif(group == 'financing_bonds'):    
        data = Archive.objects.filter(group="اوراق تامین مالی")
    elif(group == 'estate'):    
        data = Archive.objects.filter(group="انبوه سازی، املاک، مستغلات")
    elif(group == 'engineering'):    
        data = Archive.objects.filter(group="فعالیت های مهندسی، تجزیه، تحلیل و آزمایش فنی")
    elif(group == 'app_computer'):    
        data = Archive.objects.filter(group="رایانه و فعالیت های وابسته به آن")

    #45-48
    elif(group == 'information'):    
        data = Archive.objects.filter(group="اطلاعات و ارتباطات")
    elif(group == 'technical_services'):    
        data = Archive.objects.filter(group="خدمات فنی و مهندسی")
    elif(group == 'artistic'):    
        data = Archive.objects.filter(group="فعالیت های هنری، سرگرمی و خلاقانه")
    elif(group == 'tanning'):    
        data = Archive.objects.filter(group="دباغی، پرداخت چرم و ساخت انواع پاپوش")
    
    #49
    elif(group == 'telecommunication'):    
        data = Archive.objects.filter(group="مخابرات")
    

    for address in data:
        #1-4
        if(group == 'agriculture'):  
            has = agriculture.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'coal'):    
            has = coal.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'oil_gas'):    
            has = oil_gas.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'metal_ores'):    
            has = metal_ores.objects.filter(name=address.name,date=datetime.date.today())

        #5-8
        elif(group == 'other_mines'):    
            has = other_mines.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'textiles'):    
            has = textiles.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'wood'):    
            has = wood.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'paper'):    
            has = paper.objects.filter(name=address.name,date=datetime.date.today())

        #9-12
        elif(group == 'printz'):    
            has = printz.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'pet_products'):    
            has = pet_products.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'plastic'):    
            has = plastic.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'elec_computer'):    
            has = elec_computer.objects.filter(name=address.name,date=datetime.date.today())
        
        #13-16
        elif(group == 'basic_metal'):    
            has = basic_metal.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'metal_products'):    
            has = metal_products.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'equipment'):    
            has = equipment.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'electrical'):    
            has = electrical.objects.filter(name=address.name,date=datetime.date.today())

        #17-20
        elif(group == 'comm_devices'):    
            has = comm_devices.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'cars'):    
            has = cars.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'sugar'):    
            has = sugar.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'multidisciplinary'):    
            has = multidisciplinary.objects.filter(name=address.name,date=datetime.date.today())

        #21-24
        elif(group == 'supply_elec_gas'):    
            has = supply_elec_gas.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'food'):    
            has = food.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'drug'):    
            has = drug.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'chemical'):    
            has = chemical.objects.filter(name=address.name,date=datetime.date.today())

        #25-28
        elif(group == 'contracting'):    
            has = contracting.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'wholesale'):    
            has = wholesale.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'retail'):    
            has = retail.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'tile'):    
            has = tile.objects.filter(name=address.name,date=datetime.date.today())

        #29-32
        elif(group == 'cement'):    
            has = cement.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'non_metal'):    
            has = non_metal.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'hotel'):    
            has = hotel.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'investments'):    
            has = investments.objects.filter(name=address.name,date=datetime.date.today())

        #33-36
        elif(group == 'banks'):    
            has = banks.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'other_financial'):    
            has = other_financial.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'transportation'):    
            has = transportation.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'water_transportation'):    
            has = water_transportation.objects.filter(name=address.name,date=datetime.date.today())

        #37-40
        elif(group == 'financial'):    
            has = financial.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'insurance'):    
            has = insurance.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'auxiliary'):    
            has = auxiliary.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'etf'):    
            has = etf.objects.filter(name=address.name,date=datetime.date.today())

        #41-44
        elif(group == 'financing_bonds'):    
            has = financing_bonds.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'estate'):    
            has = estate.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'engineering'):    
            has = engineering.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'app_computer'):    
            has = app_computer.objects.filter(name=address.name,date=datetime.date.today())

        #45-48
        elif(group == 'information'):    
            has = information.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'technical_services'):    
            has = technical_services.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'artistic'):    
            has = artistic.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'tanning'):    
            has = tanning.objects.filter(name=address.name,date=datetime.date.today())

        #49
        elif(group == 'telecommunication'):    
            has = telecommunication.objects.filter(name=address.name,date=datetime.date.today())

        if(len(has) == 0):
            url = address.url
            response = requests.get(url)
            plain_response = response.text
            in_page = re.compile("TopInst=(.*)")
            data_inpage = in_page.findall(plain_response)

            my_obj = {'data':[]}
        
            for data in data_inpage :
                arr = data.split(',')
                my_obj['data'].append({'vl' : arr[8].rsplit('=')[1]}) 
                my_obj['data'].append({'cs' : arr[10].rsplit('=')[1]}) 
                my_obj['data'].append({'avm' : arr[24].rsplit('=')[1].replace("'","")}) 
                my_obj['data'].append({'sf' : arr[26].rsplit('=')[1].replace("'","")}) 

            url2 = address.api
            response2 = requests.get(url2)
            plain_api = response2.text

            in_api = re.compile("A.*")
            data_inapi = in_api.findall(plain_api)

            in_api_is = re.compile("IS.*")
            data_inapi_is = in_api_is.findall(plain_api)

            in_api_i = re.compile("I.*")
            data_inapi_i = in_api_i.findall(plain_api)

            in_api_as = re.compile("AS.*")
            data_inapi_as = in_api_as.findall(plain_api)

            if(len(str(data_inapi)) > 300):
                for data in data_inapi :
                    arr = data.split(',')
                    if(int(arr[7]) > 0):

                        my_obj['data'].append({"pi":arr[1]}) 
                        my_obj['data'].append({"pe":arr[2]}) 
                        my_obj['data'].append({"ct":arr[7]}) 
                        my_obj['data'].append({"vt":arr[8]}) 
                        my_obj['data'].append({"value_t":arr[9]}) 
                        if(group == 'etf'):
                            my_obj['data'].append({"da":arr[13]})
                            nav = arr[14].split(';') 
                            my_obj['data'].append({"nav":nav[0]}) 
    
                        for data in data_inapi:
                            arr = data.split(';')
                            arr = arr[2]
                            if(len(str(arr)) > 3): 

                                arr = arr.split('@')
                                
                                my_obj['data'].append({"bbv":arr[1]}) 
                                my_obj['data'].append({"bbp":arr[2]}) 
                                my_obj['data'].append({"sbp":arr[3]}) 
                                my_obj['data'].append({"sbv":arr[4]}) 
                            
                        for data in data_inapi :
                            arr = data.split(';')
                            arr = arr[4]
                            if(len(str(arr)) > 5): 

                                arr = arr.split(',')
                                
                                my_obj['data'].append({"vbs":arr[0]}) 
                                my_obj['data'].append({"vbc":arr[1]}) 
                                my_obj['data'].append({"vss":arr[3]}) 
                                my_obj['data'].append({"vsc":arr[4]}) 

                                my_obj['data'].append({"cbs":arr[5]}) 
                                my_obj['data'].append({"cbc":arr[6]}) 
                                my_obj['data'].append({"css":arr[8]}) 
                                my_obj['data'].append({"csc":arr[9]}) 
                            else:
                                my_obj=['this_stock_need_incomp_update_retry']
                    else:
                        my_obj=['Stopped stock']

            elif(len(str(data_inapi_is)) > 300):
                in_api = re.compile("IS.*")
                data_inapi = in_api.findall(plain_api)
                for data in data_inapi :
                        arr = data.split(',')
                        if(int(arr[7]) > 0):
                            my_obj['data'].append({"pi":arr[1]}) 
                            my_obj['data'].append({"pe":arr[2]}) 
                            my_obj['data'].append({"ct":arr[7]}) 
                            my_obj['data'].append({"vt":arr[8]}) 
                            my_obj['data'].append({"value_t":arr[9]}) 

                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[2]
                                if(len(str(arr)) > 3): 

                                    arr = arr.split('@')
                                    
                                    my_obj['data'].append({"bbv":arr[1]}) 
                                    my_obj['data'].append({"bbp":arr[2]}) 
                                    my_obj['data'].append({"sbp":arr[3]}) 
                                    my_obj['data'].append({"sbv":arr[4]}) 


                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[4]
                                if(len(str(arr)) > 15):

                                    arr = arr.split(',')
                                    my_obj['data'].append({"vbs":arr[0]}) 
                                    my_obj['data'].append({"vbc":arr[1]}) 
                                    my_obj['data'].append({"vss":arr[3]}) 
                                    my_obj['data'].append({"vsc":arr[4]}) 

                                    my_obj['data'].append({"cbs":arr[5]}) 
                                    my_obj['data'].append({"cbc":arr[6]}) 
                                    my_obj['data'].append({"css":arr[8]}) 
                                    my_obj['data'].append({"csc":arr[9]}) 
                                else:
                                    my_obj=['this_stock_need_incomp_update_retry']
                        else:
                            my_obj=['Stopped stock']

            elif(len(str(data_inapi_i)) > 300):
                in_api = re.compile("I.*")
                data_inapi = in_api.findall(plain_api)
                for data in data_inapi :
                        arr = data.split(',')
                        if(int(arr[7]) > 0):
                            my_obj['data'].append({"pi":arr[1]}) 
                            my_obj['data'].append({"pe":arr[2]}) 
                            my_obj['data'].append({"ct":arr[7]}) 
                            my_obj['data'].append({"vt":arr[8]}) 
                            my_obj['data'].append({"value_t":arr[9]}) 

                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[2]
                                if(len(str(arr)) > 3): 

                                    arr = arr.split('@')
                                    
                                    my_obj['data'].append({"bbv":arr[1]}) 
                                    my_obj['data'].append({"bbp":arr[2]}) 
                                    my_obj['data'].append({"sbp":arr[3]}) 
                                    my_obj['data'].append({"sbv":arr[4]}) 


                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[3]
                                if(len(str(arr)) > 20):
                                    arr = arr.split(',')
                                    my_obj['data'].append({"vbs":arr[0]}) 
                                    my_obj['data'].append({"vbc":arr[1]}) 
                                    my_obj['data'].append({"vss":arr[3]}) 
                                    my_obj['data'].append({"vsc":arr[4]}) 

                                    my_obj['data'].append({"cbs":arr[5]}) 
                                    my_obj['data'].append({"cbc":arr[6]}) 
                                    my_obj['data'].append({"css":arr[8]}) 
                                    my_obj['data'].append({"csc":arr[9]}) 
                                else:
                                    my_obj=['this_stock_need_incomp_update_retry']
                        else:
                            my_obj=['Stopped stock']

            elif(len(str(data_inapi_as)) > 300):
                in_api = re.compile("AS.*")
                data_inapi = in_api.findall(plain_api)
                for data in data_inapi :
                        arr = data.split(',')
                        if(int(arr[7]) > 0):
                            my_obj['data'].append({"pi":arr[1]}) 
                            my_obj['data'].append({"pe":arr[2]}) 
                            my_obj['data'].append({"ct":arr[7]}) 
                            my_obj['data'].append({"vt":arr[8]}) 
                            my_obj['data'].append({"value_t":arr[9]}) 

                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[2]
                                if(len(str(arr)) > 3): 

                                    arr = arr.split('@')
                                    
                                    my_obj['data'].append({"bbv":arr[1]}) 
                                    my_obj['data'].append({"bbp":arr[2]}) 
                                    my_obj['data'].append({"sbp":arr[3]}) 
                                    my_obj['data'].append({"sbv":arr[4]}) 


                            for data in data_inapi :
                                arr = data.split(';')
                                arr = arr[4]
                                if(len(str(arr)) > 5):

                                    arr = arr.split(',')
                                    my_obj['data'].append({"vbs":arr[0]}) 
                                    my_obj['data'].append({"vbc":arr[1]}) 
                                    my_obj['data'].append({"vss":arr[3]}) 
                                    my_obj['data'].append({"vsc":arr[4]}) 

                                    my_obj['data'].append({"cbs":arr[5]}) 
                                    my_obj['data'].append({"cbc":arr[6]}) 
                                    my_obj['data'].append({"css":arr[8]}) 
                                    my_obj['data'].append({"csc":arr[9]}) 
                                else:
                                    my_obj=['this_stock_need_incomp_update_retry']
                                    
                        else:
                            my_obj=['Stopped stock']

    


            #1-4
            if(group == 'agriculture'):    
                agriculture.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'coal'):
                coal.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'oil_gas'):
                oil_gas.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'metal_ores'):
                metal_ores.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

            #5-8
            elif(group == 'other_mines'):
                other_mines.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'textiles'):
                textiles.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'wood'):
                wood.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'paper'):
                paper.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

            #9-12
            elif(group == 'printz'):
                printz.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'pet_products'):
                pet_products.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'plastic'):
                plastic.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'elec_computer'):
                elec_computer.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)


            #13-16
            elif(group == 'basic_metal'):
                basic_metal.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'metal_products'):
                metal_products.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'equipment'):
                equipment.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'electrical'):
                electrical.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

            #17-20
            elif(group == 'comm_devices'):
                comm_devices.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'cars'):
                cars.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'sugar'):
                sugar.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'multidisciplinary'):
                multidisciplinary.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #21-24
            elif(group == 'supply_elec_gas'):
                supply_elec_gas.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'food'):
                food.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'drug'):
                drug.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'chemical'):
                chemical.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #25-28
            elif(group == 'contracting'):
                contracting.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'wholesale'):
                wholesale.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'retail'):
                retail.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'tile'):
                tile.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #29-32
            elif(group == 'cement'):
                cement.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'non_metal'):
                non_metal.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'hotel'):
                hotel.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'investments'):
                investments.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #33-36
            elif(group == 'banks'):
                banks.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'other_financial'):
                other_financial.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'transportation'):
                transportation.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'water_transportation'):
                water_transportation.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #37-40
            elif(group == 'financial'):
                financial.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'insurance'):
                insurance.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'auxiliary'):
                auxiliary.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'etf'):
                etf.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #41-44
            elif(group == 'financing_bonds'):
                financing_bonds.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'estate'):
                estate.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'engineering'):
                engineering.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'app_computer'):
                app_computer.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

             #45-48
            elif(group == 'information'):
                information.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'technical_services'):
                technical_services.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'artistic'):
                artistic.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'tanning'):
                tanning.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

            #49
            elif(group == 'telecommunication'):
                telecommunication.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

    return HttpResponse(group)