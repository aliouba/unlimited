from django import forms
from django.forms import ModelForm
from first.models import Clients
class ArticleForm(ModelForm):
	class Meta:
		model = Clients
		fields = ['nom', 'prenom', 'adresse','pays','region', 'code']
		widgets = {
                      "nom":forms.TextInput(attrs={'placeholder':'Name','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
                      "prenom":forms.TextInput(attrs={'placeholder':'description','name':'description','id':'common_id_for_imputfields','class':'input-class_name'}),
        }
