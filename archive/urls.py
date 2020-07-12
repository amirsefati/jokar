from django.urls import include,path
from . import views

urlpatterns = [
    
    path('daily/<group>',views.daily),
    path('history/<group>/<start_time>/<end_time>/<name>',views.history),
    path('delete/<group>',views.delete),
    path('daily_check/',views.daily_check),
    path('incomp/',views.incomp),
    path('incomp_count/',views.incomp_count),


    path('check_all_date/<start>/<end>',views.check_all_date),
    path('detail_day_namads/<date_namad>',views.detail_day_namads),

]
