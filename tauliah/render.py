from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.conf import settings
import os
from django.contrib.staticfiles import finders


class Render:

    @staticmethod
    def render(filename: str ,path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response , link_callback=Render.link_callback)
        if not pdf.err:
            newPDF = HttpResponse(response.getvalue(), content_type='application/pdf')
            newPDF['Content-Disposition'] = 'attachment; filename="'+filename+'"'
            newPDF['Content-Length'] = len(response.getbuffer())
            newPDF['Len'] = len(response.getbuffer())
            #return HttpResponse(response.getvalue(), content_type='application/pdf')
            return newPDF
        else:
            return HttpResponse("Error Rendering PDF", status=400)

    def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path