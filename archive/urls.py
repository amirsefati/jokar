from django.urls import include,path
from . import views

urlpatterns = [
    
    path('delete/<group>',views.delete),
    
    path('daily/<group>',views.daily),
    path('daily_check/',views.daily_check),
    path('incomp/',views.incomp),
    path('incomp_count/',views.incomp_count),
    
    path('history/<group>/<start_time>/<end_time>/<name>',views.history),
    path('get_hisory_group/<group>/<start>/<end>',views.get_hisory_group),
    path('history_revamp/<start>/<end>',views.history_revamp),
    path('check_duplicate_data/<start_time>',views.check_duplicate_data),

    path('check_all_date/<start>/<end>',views.check_all_date),
    path('detail_day_namads/<date_namad>',views.detail_day_namads),
    
]
