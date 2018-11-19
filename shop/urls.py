from django.urls import path, register_converter

from shop.converters import FourDigitYearConverter
from . import views

app_name = 'shop'


register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [

    path('article/<yyyy:year>', views.year_archive),
]
