from .models import TP
from .render import Render
from etauliahph.settings import BASE_DIR
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
# RUJUKAN :  https://codeburst.io/django-render-html-to-pdf-41a2b9c41d16
# RUJUKAN :  https://xhtml2pdf.readthedocs.io/en/latest/format_html.html

# Create your views here.
def main_page(request):
    context={}
    tp_list = TP.objects.all().order_by('cawangan','kelas','status')
    cawangan_list = TP.objects.all().values('cawangan').distinct()
    print(cawangan_list)
    context['cawangan_list'] = cawangan_list
    context['tp_list'] = tp_list
    return render(request , 'main_page.html' ,{'context':context})


def download_sijil_tauliah(request,cawangan_list):
    context = {}
    tp_list = TP.objects.filter(cawangan=cawangan_list).order_by('cawangan','kelas','status')
    context['list'] = tp_list
    context['BASE_DIR'] = BASE_DIR
    return Render.render(cawangan_list+'.pdf','sijil/sijil.html', context)

def download_sijil_kosong(request,cawangan_list):
    context = {}
    tp_list = TP.objects.filter(cawangan=cawangan_list).order_by('cawangan','kelas','status')
    context['list'] = tp_list
    context['BASE_DIR'] = BASE_DIR
    return Render.render(cawangan_list+'.pdf','sijil/sijil_kosong.html', context)