from django.contrib import admin

from .models import Archive,agriculture,coal,oil_gas,metal_ores
from .models import other_mines,textiles,wood,paper
from .models import printz,pet_products,plastic,elec_computer
from .models import basic_metal,metal_products,equipment,electrical

from .models import comm_devices,cars,sugar,multidisciplinary


admin.site.register(Archive)

#4
admin.site.register(agriculture)
admin.site.register(coal)
admin.site.register(oil_gas)
admin.site.register(metal_ores)

#8
admin.site.register(other_mines)
admin.site.register(textiles)
admin.site.register(wood)
admin.site.register(paper)

#12
admin.site.register(printz)
admin.site.register(pet_products)
admin.site.register(plastic)
admin.site.register(elec_computer)

#16
admin.site.register(basic_metal)
admin.site.register(metal_products)
admin.site.register(equipment)
admin.site.register(electrical)

#20
admin.site.register(comm_devices)
admin.site.register(cars)
admin.site.register(sugar)
admin.site.register(multidisciplinary)
