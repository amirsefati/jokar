from django.contrib import admin
#1-16
from .models import Archive,agriculture,coal,oil_gas,metal_ores
from .models import other_mines,textiles,wood,paper
from .models import printz,pet_products,plastic,elec_computer
from .models import basic_metal,metal_products,equipment,electrical
#17-32
from .models import comm_devices,cars,sugar,multidisciplinary
from .models import supply_elec_gas,food,drug,chemical
from .models import contracting,wholesale,retail,tile
from .models import cement,non_metal,hotel,investments
#33-47
from .models import banks,other_financial,transportation,water_transportation
from .models import financial,insurance,auxiliary,etf
from .models import financing_bonds,estate,engineering,app_computer
from .models import information,technical_services,artistic


admin.site.register(Archive)

#1-4
admin.site.register(agriculture)
admin.site.register(coal)
admin.site.register(oil_gas)
admin.site.register(metal_ores)

#5-8
admin.site.register(other_mines)
admin.site.register(textiles)
admin.site.register(wood)
admin.site.register(paper)

#9-12
admin.site.register(printz)
admin.site.register(pet_products)
admin.site.register(plastic)
admin.site.register(elec_computer)

#13-16
admin.site.register(basic_metal)
admin.site.register(metal_products)
admin.site.register(equipment)
admin.site.register(electrical)

#17-20
admin.site.register(comm_devices)
admin.site.register(cars)
admin.site.register(sugar)
admin.site.register(multidisciplinary)

#21-24
admin.site.register(supply_elec_gas)
admin.site.register(food)
admin.site.register(drug)
admin.site.register(chemical)

#25-28
admin.site.register(contracting)
admin.site.register(wholesale)
admin.site.register(retail)
admin.site.register(tile)

#29-32
admin.site.register(cement)
admin.site.register(non_metal)
admin.site.register(hotel)
admin.site.register(investments)

#33-36
admin.site.register(banks)
admin.site.register(other_financial)
admin.site.register(transportation)
admin.site.register(water_transportation)

#37-40
admin.site.register(financial)
admin.site.register(insurance)
admin.site.register(auxiliary)
admin.site.register(etf)

#41-44
admin.site.register(financing_bonds)
admin.site.register(estate)
admin.site.register(engineering)
admin.site.register(app_computer)

#45-47
admin.site.register(information)
admin.site.register(technical_services)
admin.site.register(artistic)
