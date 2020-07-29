from django.urls import include,path
from . import views


urlpatterns = [
    path('daily_individual_cash_inflows/<date_time>',views.pl1)
]
