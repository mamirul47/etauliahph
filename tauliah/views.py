from .models import TP
from .render import Render
from etauliahph.settings import BASE_DIR
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import HttpResponse
import zipfile
from io import BytesIO

# RUJUKAN :  https://codeburst.io/django-render-html-to-pdf-41a2b9c41d16
# RUJUKAN :  https://xhtml2pdf.readthedocs.io/en/latest/format_html.html

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='/admin/login/?next=/admin/')
def main_page(request):
    context={}
    tp_list = TP.objects.all().order_by('cawangan','kelas','status')
    cawangan_list = TP.objects.all().values('cawangan').distinct()
    context['cawangan_list'] = cawangan_list
    context['tp_list'] = tp_list
    return render(request , 'main_page.html' ,{'context':context})

@login_required(login_url='/admin/login/?next=/admin/')
def senarai_kelas(request,cawangan_list):
    context = {}
    kelas_list = TP.objects.filter(cawangan=cawangan_list).values('kelas','cawangan').distinct()
    tp_list = TP.objects.filter(cawangan=cawangan_list).order_by('cawangan','kelas','status')
    context['kelas_list'] = kelas_list
    context['tp_list'] = tp_list
    return render(request , 'senarai_kelas.html' ,{'context':context})

@login_required(login_url='/admin/login/?next=/admin/')
def download_sijil_tauliah_bykelas(request,cawangan_list,kelas_list):
    context = {}
    tp_list = TP.objects.filter(kelas=kelas_list,cawangan=cawangan_list).order_by('cawangan','kelas','status')
    context['list'] = tp_list
    context['BASE_DIR'] = BASE_DIR
    return Render.render(kelas_list+'.pdf','sijil/sijil.html', context)


@login_required(login_url='/admin/login/?next=/admin/')
def download_sijil_tauliah(request,cawangan_list):
    context = {}
    tp_list = TP.objects.filter(cawangan=cawangan_list).order_by('cawangan','kelas','status')
    context['list'] = tp_list
    context['BASE_DIR'] = BASE_DIR
    return Render.render(cawangan_list+'.pdf','sijil/sijil.html', context)
    
@login_required(login_url='/admin/login/?next=/admin/')
def download_sijil_kosong(request,cawangan_list):
    context = {}
    tp_list = TP.objects.filter(cawangan=cawangan_list).order_by('cawangan','kelas','status')
    context['list'] = tp_list
    context['BASE_DIR'] = BASE_DIR
    return Render.render(cawangan_list+'.pdf','sijil/sijil_kosong.html', context)

@login_required(login_url='/admin/login/?next=/admin/')
def download_sijil_individu(request,pk):
    context = {}
    tp_list = TP.objects.filter(pk=pk)
    context['list'] = tp_list
    context['BASE_DIR'] = BASE_DIR
    return Render.render(tp_list[0].nama+'.pdf','sijil/sijil.html', context)


@login_required(login_url='/admin/login/?next=/admin/')
def download_sijil_tauliah_bykelas_zip(request,cawangan_list,kelas_list):
    context = {}
    tp_list = TP.objects.filter(kelas=kelas_list,cawangan=cawangan_list).order_by('cawangan','kelas','status')
    #context['list'] = tp_list
    #context['BASE_DIR'] = BASE_DIR

    files = []
    for q in tp_list:
        context = {}
        context['list'] = q
        context['BASE_DIR'] = BASE_DIR
        pdf = Render.render(q.nama+'.pdf','sijil/sijil_bundle.html', context)
        files.append((q.nama + '_' +q.status +'.pdf', pdf))
    full_zip_in_memory = generate_zip(files)
    
    response = HttpResponse(full_zip_in_memory, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(kelas_list+'.zip')
    return response
	
def generate_zip(files):
    mem_zip = BytesIO()
    zip_file = zipfile.ZipFile(mem_zip, "w",compression=zipfile.ZIP_DEFLATED)
    #with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
    for f in files:
        print(f[1])
            #zf.writestr(f[0], f[1])
        zip_file.writestr(f[0], f[1].getvalue())
    zip_file.close()
    return mem_zip.getvalue()