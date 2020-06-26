from django.urls import include,path
from . import views

urlpatterns = [
    
    path('daily/<group>',views.daily),

]
