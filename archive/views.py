from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import datetime
import json

#4
from archive.models import Archive,agriculture,coal,oil_gas,metal_ores
from archive.models import other_mines,textiles,wood,paper
from archive.models import printz,pet_products,plastic,elec_computer
from archive.models import basic_metal,metal_products,equipment,electrical

#20
from archive.models import comm_devices,cars,sugar,multidisciplinary

def daily(request,group): 

    #4
    if(group == 'agriculture'):    
        data = Archive.objects.filter(group="زراعت و خدمات وابسته")
    elif(group == 'coal'):    
        data = Archive.objects.filter(group="استخراج ذغال سنگ")
    elif(group == 'oil_gas'):    
        data = Archive.objects.filter(group="استخراج نفت گاز و خدمات جنبی به جز اکتشاف")
    elif(group == 'metal_ores'):    
        data = Archive.objects.filter(group="استخراج کانه های فلزی")
    
    #8
    elif(group == 'other_mines'):    
        data = Archive.objects.filter(group="استخراج سایر معادن")
    elif(group == 'textiles'):    
        data = Archive.objects.filter(group="منسوجات")
    elif(group == 'wood'):    
        data = Archive.objects.filter(group="محصولات چوبی")
    elif(group == 'paper'):    
        data = Archive.objects.filter(group="محصولات کاغذی")
    
    #12
    elif(group == 'printz'):    
        data = Archive.objects.filter(group="انتشار چاپ تکثیر")
    elif(group == 'pet_products'):    
        data = Archive.objects.filter(group="فراورده های نفتی، کک و سوخت هسته ای")
    elif(group == 'plastic'):    
        data = Archive.objects.filter(group="لاستیک،پلاستیک")
    elif(group == 'elec_computer'):    
        data = Archive.objects.filter(group="تولیدات محصولات کامپیوتری و الکترونیکی نوری")
    
    #16
    elif(group == 'basic_metal'):    
        data = Archive.objects.filter(group="فلزات اساسي")
    elif(group == 'metal_products'):    
        data = Archive.objects.filter(group="ساخت محصولات فلزی")
    elif(group == 'equipment'):    
        data = Archive.objects.filter(group="ماشین آلات و تجهیزات")
    elif(group == 'electrical'):    
        data = Archive.objects.filter(group="ماشین آلات و دستگاه های برقی")
    
    #20
    elif(group == 'comm_devices'):    
        data = Archive.objects.filter(group="ساخت دستگاه ها و وسایل ارتباطی")
    elif(group == 'cars'):    
        data = Archive.objects.filter(group="خودرو و ساخت قطعات")
    elif(group == 'sugar'):    
        data = Archive.objects.filter(group="قند و شکر")
    elif(group == 'multidisciplinary'):    
        data = Archive.objects.filter(group="شرکت های چند رشته ای صنعتی")
    

    for address in data:

        #4
        if(group == 'agriculture'):  
            has = agriculture.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'coal'):    
            has = coal.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'oil_gas'):    
            has = oil_gas.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'metal_ores'):    
            has = metal_ores.objects.filter(name=address.name,date=datetime.date.today())

        #8
        elif(group == 'other_mines'):    
            has = other_mines.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'textiles'):    
            has = textiles.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'wood'):    
            has = wood.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'paper'):    
            has = paper.objects.filter(name=address.name,date=datetime.date.today())

        #12
        elif(group == 'printz'):    
            has = printz.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'pet_products'):    
            has = pet_products.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'plastic'):    
            has = plastic.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'elec_computer'):    
            has = elec_computer.objects.filter(name=address.name,date=datetime.date.today())
        
        #16
        elif(group == 'basic_metal'):    
            has = basic_metal.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'metal_products'):    
            has = metal_products.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'equipment'):    
            has = equipment.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'electrical'):    
            has = electrical.objects.filter(name=address.name,date=datetime.date.today())

        #20
        elif(group == 'comm_devices'):    
            has = comm_devices.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'cars'):    
            has = cars.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'sugar'):    
            has = sugar.objects.filter(name=address.name,date=datetime.date.today())
        elif(group == 'multidisciplinary'):    
            has = multidisciplinary.objects.filter(name=address.name,date=datetime.date.today())


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
                    
            if(len(str(data_inapi)) > 20):
                for data in data_inapi :
                    arr = data.split(',')
                    my_obj['data'].append({"pi":arr[1]}) 
                    my_obj['data'].append({"pe":arr[2]}) 
                    my_obj['data'].append({"ct":arr[7]}) 
                    my_obj['data'].append({"vt":arr[8]}) 
                    my_obj['data'].append({"value_t":arr[9]}) 
                
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
                my_obj=['Stopped stock']

            #4
            if(group == 'agriculture'):    
                agriculture.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'coal'):
                coal.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'oil_gas'):
                oil_gas.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'metal_ores'):
                metal_ores.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

            #8
            elif(group == 'other_mines'):
                other_mines.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'textiles'):
                textiles.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'wood'):
                wood.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'paper'):
                paper.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)

            #12
            elif(group == 'printz'):
                printz.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'pet_products'):
                pet_products.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'plastic'):
                plastic.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'elec_computer'):
                elec_computer.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)


            #16
            elif(group == 'basic_metal'):
                basic_metal.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'metal_products'):
                metal_products.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'equipment'):
                equipment.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'electrical'):
                electrical.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)


             #20
            elif(group == 'comm_devices'):
                comm_devices.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'cars'):
                cars.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'sugar'):
                sugar.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
            elif(group == 'multidisciplinary'):
                multidisciplinary.objects.create(name=address.name,kind=address.kind,date=datetime.date.today(),data=my_obj)
