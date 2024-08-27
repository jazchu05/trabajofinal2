from socket import fromshare
from django import forms 
from .models import Socios

class SociosForm(forms.ModelForm):
  class Meta:
        model=Socios
       #fields='__all__'
        fields=('DNI','nom','fechan',"dire","cp","tel")
        labels ={
             
            "DNI" : "DNI del socio" ,
            'nom': 'nombre y apellido del socio:',
            "fechan" : "fecha de nacimiento del socio" ,
            "dire" : "direccion del socio",
            "cp" : "codigo postal del socio",
            "tel" : "numero de telefono del socio",
          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(SociosForm,self).__init__(*args,**kwargs)
      #  self.fields['descripcion'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechan'].required=False
        