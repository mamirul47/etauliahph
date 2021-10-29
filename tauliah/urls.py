from django.urls import path
from . import views

urlpatterns = [

    #MAIN REDIRECT URL
    path('',views.main_page,name='main_page'),
    path('tauliah/<str:cawangan_list>',views.download_sijil_tauliah, name="sijil_tauliah"),
    path('tauliah/<str:cawangan_list>',views.download_sijil_kosong, name="sijil_kosong"),

]