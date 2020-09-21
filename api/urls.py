from django.urls import include,path
from . import views


urlpatterns = [
    path('daily_individual_cash_inflows',views.plugina),
    path('micro_entry_and_exit_throughout_the_market',views.pluginb),
    path('The_entry_and_exit_of_micro_floating_value',views.pluginc),

    path('all_namad',views.add_namad)

]
    