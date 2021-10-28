from django.contrib import admin
from django.urls import path
from .views import HomeView,InicioView,DocsView,FormsoView, ListarContables, ListarCuestionario, ListarEditables, ListarEje, LoginView,MeetView, RegistroAdminView, RegistroUserView, RegistroView, modificar_producto,editarcontables,editarejec,editcu,editreu,ListEditablesadm,ListEjeadm,ListContablesadm,ListCuestionarioadm,MeetViewadm
#app_name = 'app1' Esto va a servir para poder indicar y direccionar los archivos solo del al App Home 
#(ustedes deciden si la van a usar o no) :) :) :) ;) ;) ;)

urlpatterns = [
    path('index/', HomeView.as_view(), name='index'),
    path('home/', InicioView.as_view(), name='home'),
    path('documentos/', DocsView.as_view(), name='documentos'),
    path('reuniones/', MeetView.as_view(), name='reuniones'),
    path('formularios/', FormsoView.as_view(), name='formularios'),
    path('login/', LoginView.as_view(), name='login'), 
    path('registrar/', RegistroView.as_view(), name='registrar'),
    path('registrarAdmin/', RegistroAdminView.as_view(), name='registrarAdmin'),
    path('registrarUser/', RegistroUserView.as_view(), name='registrarUser'),
    path('login/', LoginView.as_view(), name='login'),
    path('ListarEditables/', ListarEditables.as_view(), name='ListarEditables'),
    path('ListarContable/', ListarContables.as_view(), name='ListarContable'),
    path('ListarEje/', ListarEje.as_view(), name='ListarEje'),
    path('ListarCuestionario/', ListarCuestionario.as_view(), name='ListarCuestionario'),

    path('adminEditables/', ListEditablesadm.as_view(), name='adminEditables'),
    path('adminContable/', ListContablesadm.as_view(), name='adminContable'),
    path('adminEje/', ListEjeadm.as_view(), name='adminEje'),
    path('adminCuestionario/', ListCuestionarioadm.as_view(), name='adminCuestionario'),
    path('reuadm/', MeetViewadm.as_view(), name='reuadm'),
    
    path('modificar_producto/<id>/', modificar_producto, name='modificar_producto'),
    path('dcedit/<pk>/', editarcontables.as_view(), name='dcedit'),
    path('dejedit/<pk>/', editarejec.as_view(), name='dejedit'),
    path('cuedit/<pk>/', editcu.as_view(), name='cuedit'),
    path('reuedit/<pk>/', editreu.as_view(), name='reuedit'),
    
]
