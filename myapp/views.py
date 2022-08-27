from django.http import HttpResponse
from django.template import Template, Context, loader
from myapp.models import Familia

def mi_familia (request):
    queryset = Familia.objects.all
    diccionario = {'flia':queryset}
    plantilla = loader.get_template('lista_flia.html')
    doc_html=plantilla.render(diccionario)

    return HttpResponse(doc_html)