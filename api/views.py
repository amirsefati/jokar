from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.apps import apps
from datetime import date,timedelta,datetime
from dateutil.relativedelta import relativedelta
from archive.models import namadtomodel,Archive
from scipy import stats


has = ['agriculture','coal','oil_gas','metal_ores','other_mines','textiles','wood','paper','printz','pet_products','plastic','elec_computer','basic_metal','metal_products','equipment','electrical','comm_devices','cars','sugar','multidisciplinary','supply_elec_gas','food','drug','chemical','contracting','wholesale','retail','tile','cement','non_metal','hotel','investments','banks','other_financial','transportation','water_transportation','financial','insurance','auxiliary','etf','financing_bonds','estate','engineering','app_computer','information','technical_services','artistic','telecommunication','tanning']    
   
def plugina(request):
    all_data = []

    #دیتای 22 روز اخیر  
    past_22 = date.today() + relativedelta(days=-23)
    day_22 = {'day':[]}
    for n in range((date.today() - past_22).days):
        day_22['day'].append(date.today() - timedelta(n))
    
    data_22 = {}

    for item in has:
        for day_in_22 in day_22['day']:
            data = (apps.get_model('archive',item).objects.filter(date=day_in_22.strftime("%Y-%m-%d")))
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

                        if da.name in data_22:
                            
                            arr_2 = []
                            new_data = data_22[da.name]
                            for pre_data in new_data:
                                arr_2.append(pre_data)
                            
                            arr_2.append(calculate_d)
                            
                            data_22.__setitem__(da.name,arr_2)
                        else:
                            arr = []
                            arr.append(calculate_d)
                            data_22.__setitem__(da.name,arr)
                else:
                    if da.name in data_22:
                            
                        arr_2 = []
                        new_data = data_22[da.name]
                        for pre_data in new_data:
                            arr_2.append(pre_data)
                            
                        arr_2.append('c')
                            
                        data_22.__setitem__(da.name,arr_2)
                    else:
                        arr = []
                        arr.append('c')
                        data_22.__setitem__(da.name,arr)
    #جمع ماهانه دیتای هر نماد 
    past_month = date.today() + relativedelta(days=-20)
    month = {'day':[]}
    for n in range((date.today() - past_month).days):
        month['day'].append(date.today() - timedelta(n))
    month_calculate = {}

    for item in has:
        for day_in_month in month['day']:
            data = (apps.get_model('archive',item).objects.filter(date=day_in_month.strftime("%Y-%m-%d")))
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
                        if da.name in month_calculate:
                            new_data = month_calculate[da.name]
                            new_calculate = calculate_d + new_data
                            new_calculate = round(new_calculate,4)
                            month_calculate.__setitem__(da.name,new_calculate)
                        else:
                            month_calculate.__setitem__(da.name,calculate_d)

    #جمع هفتگی دیتای هر نماد 
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
    re_1 : {}
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
                            True
                        else:
                            week_calculate.__setitem__(da.name,calculate_d)
                        item_p = namadtomodel.objects.filter(model=item)
                        
                        all_data.append({"n":da.name,"g":item,"g_fa":item_p[0].namad,"d":calculate_d,'d_r':0,"w":week_calculate[da.name],'w_r':0,"m":month_calculate[da.name],"m_r":0,"cal":0,"r":0,"d_22":data_22[da.name],"d_22_r":0})
  
    return JsonResponse(all_data,safe=False)

def pluginb(request):

    all_data = []
    past_week = date(2020, 7, 12)
    tommorow = date.today() + timedelta(days=1)
    week = {'day':[]}
    for n in range((tommorow  - past_week).days):
        week['day'].append(past_week + timedelta(n))
    
    cumulative_month = []
    c_a = 0
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
                    if(int(vt.replace("'","")) > 0):
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
        if(cumulative_day != 0):
            c_a = c_a + cumulative_day
            
            cumulative_month.append([day_in_week.strftime("%Y-%m-%d"),cumulative_day,c_a])

    return JsonResponse(cumulative_month,safe=False)

def pluginc(request):

    all_data = []
    #جمع ماهانه دیتای هر نماد 
    past_month = date.today() + relativedelta(days=-20)
    month = {'day':[]}
    for n in range((date.today() - past_month).days):
        month['day'].append(date.today() - timedelta(n))
    month_calculate = {}

    for item in has:
        for day_in_month in month['day']:
            data = (apps.get_model('archive',item).objects.filter(date=day_in_month.strftime("%Y-%m-%d")))
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
                    vt = dta[" 'vt'"]
                    cs = dta[" 'cs'"]
                    sf = '50'
                    if(" 'sf'" in dta):
                        if (len(str(dta[" 'sf'"])) > 4):
                            sf = dta[" 'sf'"]
                    if(len(str(da.data)) > 290):
                        vbs = dta[" 'vbs'"]
                        vss = dta[" 'vss'"]
                    else:
                        vbs = dta["'vbs'"]
                        vss = dta[" 'vss'"]
                    if((int(vt.replace("'",""))) > 0):
                        calculate_d = ((((int(vbs.replace("'","")))-(int(vss.replace("'","")))))/(int(sf.replace("'",""))*int(cs.replace("'",""))))*10000
                        calculate_d = round(calculate_d,4)
                        if da.name in month_calculate:
                            new_data = month_calculate[da.name]
                            new_calculate = calculate_d + new_data
                            new_calculate = round(new_calculate,4)
                            month_calculate.__setitem__(da.name,new_calculate)
                        else:
                            month_calculate.__setitem__(da.name,calculate_d)

    #جمع هفتگی دیتای هر نماد 
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
                    vt = dta[" 'vt'"]
                    cs = dta[" 'cs'"]
                    sf = '50'
                    if(" 'sf'" in dta):
                        if (len(str(dta[" 'sf'"])) > 4):
                            sf = dta[" 'sf'"]
                    if(len(str(da.data)) > 290):
                        vbs = dta[" 'vbs'"]
                        vss = dta[" 'vss'"]
                    else:
                        vbs = dta["'vbs'"]
                        vss = dta[" 'vss'"]
                    if((int(vt.replace("'",""))) > 0):
                        calculate_d = ((((int(vbs.replace("'","")))-(int(vss.replace("'","")))))/(int(sf.replace("'",""))*int(cs.replace("'",""))))*10000
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
                    vt = dta[" 'vt'"]
                    cs = dta[" 'cs'"]
                    sf = '50'
                    if(" 'sf'" in dta):
                        if (len(str(dta[" 'sf'"])) > 4):
                            sf = dta[" 'sf'"]
                    if(len(str(da.data)) > 290):
                        vbs = dta[" 'vbs'"]
                        vss = dta[" 'vss'"]
                    else:
                        vbs = dta["'vbs'"]
                        vss = dta[" 'vss'"]
                    if((int(vt.replace("'",""))) > 0):
                        calculate_d = ((((int(vbs.replace("'","")))-(int(vss.replace("'","")))))/(int(sf.replace("'",""))*int(cs.replace("'",""))))*10000
                        calculate_d = round(calculate_d,4)
                        if da.name in week_calculate:
                            True
                        else:
                            week_calculate.__setitem__(da.name,calculate_d)
                        item_p = namadtomodel.objects.filter(model=item)

                        all_data.append({"n":da.name,"g":item,"g_fa":item_p[0].namad,"d":calculate_d,'d_r':0,"w":week_calculate[da.name],'w_r':0,"m":month_calculate[da.name],"m_r":0,"cal":0,"r":0})
  
    return JsonResponse(all_data,safe=False)


def add_namad(request):
    all_data = []

    archive =  Archive.objects.all()

    for data in archive:
        url = data.url
        url = url.split("=")
        url = url[2]
        api = data.api
        api = api.split("=")
        api = api[2]
        api = api.replace("+","")
        all_data.append({url,api})
    return HttpResponse(all_data)
