from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from .models import DocsEditables, FormularioInscripcion,  UsuarioAdmin, DocContables, DocumentosEje,Cuestionarios,Reuniones


class FormIncripcion(forms.ModelForm):
    class Meta:
        model = FormularioInscripcion
        fields=[
            'IDusuario',
            'edad',
            'sexo',
            'IDDepartamentos',
            'dMunicipio',
            'Direccion',
            'profe',
            'fotografiaPersonal',
            'cartaRecomendacion',
            'cartaLaboral',
            'tituloyDiplomas',
            'CUI',
            'fotografiaDPI',
            'fotografiaRTU',
            'antecedentespenales',
            'antecedentespoliciacos',

            
            

        ]
        labels ={
            'IDusuario':'Usuario',
            'edad':'Edad',
            'sexo':'Sexo',
            'IDDepartamentos':'Departamento',
            'dMunicipio':'Municipio',
            'Direccion':'Direccion',
            'profe':'Profesion',
            'fotografiaPersonal':'Fotografia Personal',
            'cartaRecomendacion':'Carta de Recomendacion',
            'cartaLaboral':'Carta Laborar',
            'tituloyDiplomas':'Titulos y/o Diplomas',
            'CUI':'CUI',
            'fotografiaDPI':'Fotografia de DPI',
            'fotografiaRTU':'Fotografia de RTU',
            'antecedentespenales':'Antecedentes Penales',
            'antecedentespoliciacos':'Antecedentes Policiacos',

            
            
        }


class FormUser(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True, widget=forms.TextInput(attrs={
        "class":"input form-control","type":"first_name","placeholder":"Ingrese su nombre"
    }))
    last_name = forms.CharField(max_length=140, required=False, widget=forms.TextInput(attrs={
        "class":"input form-control","type":"last_name","placeholder":"ingrese su apellido"
    }))
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
    #     "class":"input form-control","type":"email","placeholder":"Ingrese su correo"
    # }))
    class Meta:
        model = User
        fields=(
            'username',
            # 'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
        labels ={
            'username':'Correo',
            # 'email':'correo2',
            'first_name':'Nombre',
            'last_name':'apellido',
            'password1':'Contraseña',
            'password2':'Validar Contraseña',

            
        }
     

class FormAdmin(forms.ModelForm):
    class Meta:
        model =UsuarioAdmin  
        fields=[
            'nombre',
            'apellido',
            'contraseña',
            'email',
            'puesto',
            

        ]
        labels ={
            
            'nombre':'Nombres',
            'apellido':'Apellidos',
            'contraseña':'Contraseña',
            'email':'Correo',
            'puesto':'Puesto',
        }

class FormEditables(forms.ModelForm):
    class Meta:
        model =DocsEditables  
        fields=[
            'Contenido',
            'Tipo',
            'Descripcion',
           
            

        ]
        labels ={
            
            'Contenido':'Contenido',
            'Tipo':'Tipo',
            'Descripcion':'Descripcion',
            
        }

class dcform(forms.ModelForm):
    class Meta:
        model=DocContables
        fields = '__all__'

class dejeform(forms.ModelForm):
    class Meta:
        model=DocumentosEje
        fields = '__all__'

class cuestform(forms.ModelForm):
    class Meta:
        model=Cuestionarios
        fields = '__all__'

class reuform(forms.ModelForm):
    class Meta:
        model=Reuniones
        fields =[
            'motivo',
            'tipo',
            'link',
            'horaRegisto',
            'horaReunion', 
        ]
        labels ={
            'motivo':'motivo',
            'tipo':'tipo',
            'link':'link',
            'horaRegisto':'horaReunion',
            'horaReunion':'horaReunion',
        } 