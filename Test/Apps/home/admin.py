from django.contrib import admin
from .models import Asistencia, Cuestionarios, Departamento,Usuario, DocContables, DocsEditables, DocumentosEje, FormularioInscripcion,  Profesion, Reuniones, UsuarioAdmin
# Register your models here.
admin.site.register(Departamento)

admin.site.register(Usuario)
admin.site.register(FormularioInscripcion)
admin.site.register(Profesion)
admin.site.register(UsuarioAdmin)
admin.site.register(Reuniones)
admin.site.register(Asistencia)
admin.site.register(DocContables)
admin.site.register(DocsEditables)
admin.site.register(DocumentosEje)
admin.site.register(Cuestionarios)