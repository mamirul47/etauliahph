from django.urls import path
from . import views

urlpatterns = [

    #MAIN REDIRECT URL
    path('',views.main_page,name='main_page'),
    path('cawangan/<str:cawangan_list>',views.senarai_kelas,name='senarai_kelas'),
    path('tauliah/<str:cawangan_list>/esijil',views.download_sijil_tauliah, name="sijil_tauliah"),
    path('tauliah/<str:cawangan_list>/esijil/<str:kelas_list>/kelas',views.download_sijil_tauliah_bykelas, name="download_sijil_tauliah_bykelas"),
    path('tauliah/<str:cawangan_list>/esijil/<str:kelas_list>/kelas_zip',views.download_sijil_tauliah_bykelas_zip, name="download_sijil_tauliah_bykelas_zip"),
    path('tauliah/<str:cawangan_list>/sijilkosong',views.download_sijil_kosong, name="sijil_kosong"),
    path('tauliah/<int:pk>/individu',views.download_sijil_individu, name="download_sijil_individu"),

]