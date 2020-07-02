from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
import datetime
import json

#4-16
from archive.models import Archive,agriculture,coal,oil_gas,metal_ores
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
        data = Archive.objects.filter(group="فلزات اساسي")
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
                    
            if(len(str(data_inapi)) > 20):
                for data in data_inapi :
                    arr = data.split(',')
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
                in_api = re.compile("IS.*")
                data_inapi = in_api.findall(plain_api)
                if(len(str(data_inapi)) > 5):
                    
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
                else:
                    my_obj=['IS AND A NOT EXIST !!']

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