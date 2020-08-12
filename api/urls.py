from django.urls import include,path
from . import views


urlpatterns = [
    path('daily_individual_cash_inflows',views.pl1),
    path('micro_entry_and_exit_throughout_the_market',views.pl2),
    path('per_capita',views.pl3),

]
    