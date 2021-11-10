
from django.db.models.base import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView,DetailView
from django.urls import reverse_lazy
from .forms import FormAdmin, FormEditables, FormIncripcion, dcform, dejeform,cuestform,reuform,FormUser
from .models import Cuestionarios, DocContables, DocsEditables, DocumentosEje, FormularioInscripcion, UsuarioAdmin,Reuniones,Usuario
from django.contrib.auth.views import LoginView
from django.forms import forms
# Create your views here.

class RegistroVer(DetailView):
    model =DocumentosEje
    template_name ="verRegistro.html"

class HomeView(TemplateView):
    template_name = 'index.html'

class InicioView(TemplateView):
    template_name = 'home.html'

class DocsView(TemplateView):
    template_name = 'documentos.html'

class admDocsView(TemplateView):
    template_name = 'documentosadm.html'    

class FormsoView(CreateView):
    model = FormularioInscripcion
    form_class = FormIncripcion
    template_name = 'formularios.html'
    success_url = reverse_lazy('home')

class MeetView(ListView):
    template_name = 'reuniones.html'
    model = Reuniones

    def get_queryset(self):
        return Reuniones.objects.all()

class LoginView(LoginView):
    template_name = 'login.html'

class RegistroView(TemplateView):
    template_name = 'registrar.html'

class RegistroAdminView(CreateView):
    model = UsuarioAdmin
    form_class = FormAdmin
    template_name = 'registrarAdmin.html'
    success_url = reverse_lazy('home')

class RegistroUserView(CreateView):
    model = Usuario
    form_class = FormUser
    template_name = 'registrarUsuario.html'
    success_url = reverse_lazy('home')


class ListarEditables(ListView):
    template_name = "ListarEditables.html"
    model = DocsEditables

    def get_queryset(self):
        return DocsEditables.objects.all()

class ListarEje(ListView):
    template_name = "ListarEjecutivos.html"
    model = DocumentosEje

    def get_queryset(self):
        return DocumentosEje.objects.all()

class ListarContables(ListView):
    template_name = "ListarContables.html"
    model = DocContables

    def get_queryset(self):
        return DocContables.objects.all()

class ListarCuestionario(ListView):
    template_name = "Listauestionario.html"
    model = Cuestionarios

    def get_queryset(self):
        return Cuestionarios.objects.all()

class ListEditablesadm(ListView):
    template_name = "ListarEditablesadm.html"
    model = DocsEditables

    def get_queryset(self):
        return DocsEditables.objects.all()

class ListEjeadm(ListView):
    template_name = "ListarEjecutivosadm.html"
    model = DocumentosEje

    def get_queryset(self):
        return DocumentosEje.objects.all()

class ListContablesadm(ListView):
    template_name = "ListarContablesadm.html"
    model = DocContables

    def get_queryset(self):
        return DocContables.objects.all()

class ListCuestionarioadm(ListView):
    template_name = "Listacuestionarioadm.html"
    model = Cuestionarios

    def get_queryset(self):
        return Cuestionarios.objects.all()



def modificar_producto(request, id):
    producto = get_object_or_404(DocsEditables, id=id)
    data = {
        'form': FormEditables(instance=producto)
    }

    if request.method == 'POST':
        formulario = FormEditables(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to = 'adminEditables')
        data["form"] = formulario

    return render(request, 'EditablesEdit.html', data)

class editarcontables(UpdateView):
    model = DocContables
    template_name = "dcedit.html"
    form_class = dcform
    success_url = reverse_lazy('adminContable')

class editarejec(UpdateView):
    model = DocumentosEje
    template_name = "dejedit.html"
    form_class = dejeform
    success_url = reverse_lazy('adminEje')

class editcu(UpdateView):
    model = Cuestionarios
    template_name = "cuestedit.html"
    form_class = cuestform
    success_url = reverse_lazy('adminCuestionario')

class MeetViewadm(ListView):
    template_name = 'reunionesadmin.html'
    model = Reuniones

    def get_queryset(self):
        return Reuniones.objects.all()

class crearmeet(CreateView):
    template_name = 'crearmeet.html'
    form_class = reuform
    success_url = reverse_lazy('reuadm')

class creareditable(CreateView):
    template_name = 'creareditable.html'
    form_class = FormEditables
    success_url = reverse_lazy('adminEditables')

class crearejecutivo(CreateView):
    template_name = 'crearejecutivo.html'
    form_class = dejeform
    success_url = reverse_lazy('adminEje')

class crearcontable(CreateView):
    template_name = 'crearcontable.html'
    form_class = dcform
    success_url = reverse_lazy('adminContable')

class crearcuestionario(CreateView):
    template_name = 'crearcuestionario.html'
    form_class = cuestform
    success_url = reverse_lazy('adminCuestionario')    

class editreu(UpdateView):
    model = Reuniones
    template_name = "reuedit.html"
    form_class = reuform
    success_url = reverse_lazy('reuadm')


