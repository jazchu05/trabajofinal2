from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('',views.inicio,name='inicio'),
    #path('socios/nosotros',views.nosotros,name='nosotros'),
    path('socios/listasocios',views.listasocios,name='listasocios'),
    path('socios/crear_editarSocio/<int:idSocio>/',views.crear_editarSocio,name='crear_editarSocio'),
    path('socios/eliminar/<int:idSocio>',views.eliminar,name='eliminar'),
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)