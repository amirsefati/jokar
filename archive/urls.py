from django.urls import include,path
from . import views

urlpatterns = [
    
    path('daily/<group>',views.daily),
    path('history/<group>/<start_time>/<end_time>/<name>',views.history),

]
