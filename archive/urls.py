from django.urls import include,path
from . import views

urlpatterns = [
    
    path('delete/<group>',views.delete),
    
    path('daily/<group>',views.daily),
    path('daily_check/',views.daily_check),
    path('incomp/',views.incomp),
    path('incomp_count/',views.incomp_count),
    path('get_daily_co',views.get_daily_co),
    #views
    path('get_daily_namad/',views.get_daily_namad),

    path('history/<group>/<start_time>/<end_time>/<name>',views.history),
    path('get_hisory_group/<group>/<start>/<end>',views.get_hisory_group),
    path('history_revamp/<start>/<end>',views.history_revamp),
    path('check_duplicate_data/<start_time>',views.check_duplicate_data),

    path('check_all_date/<start>/<end>',views.check_all_date),
    path('detail_day_namads/<date_namad>',views.detail_day_namads),
    
    path('edit_namad_new/<date_start>',views.edit_namad_new),

    path('history_new_method',views.history_new_method),

    #views
    path('get_history_namad',views.get_history_namad),
    path('get_history_group',views.get_history_group),
    path('revamp_history_view',views.revamp_history_view),
    path('edit_duplicate_history_view',views.edit_duplicate_history_view),


] 