from django import forms
from django.forms import ModelForm
from first.models import Clients
from first.models import Entreprises
class ArticleForm(ModelForm):
    code2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Verifier Mot de Passe','class':'form-control'}))
    class Meta:
        model = Clients
	widgets = {
                  "nom":forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}),
                 "prenom":forms.TextInput(attrs={'placeholder':'Prenom','class':'form-control'}),
                  "date_naissance":forms.TextInput(attrs={'placeholder':'Date de Naissance','class':'form-control'}),
                 "telephone":forms.TextInput(attrs={'placeholder':'Telephone','class':'form-control'}),
                  "email":forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}),
                 "pays":forms.TextInput(attrs={'placeholder':'Pays','class':'form-control'}),
                  "region":forms.TextInput(attrs={'placeholder':'Region','class':'form-control'}),
                 "ville":forms.TextInput(attrs={'placeholder':'Ville','class':'form-control'}),
                 "commune":forms.TextInput(attrs={'placeholder':'Commune','class':'form-control'}),
                  "adresse":forms.TextInput(attrs={'placeholder':'Adresse','class':'form-control'}),
                 "code":forms.TextInput(attrs={'placeholder':'Mot de Passe ','class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
	    super(ArticleForm, self).__init__(*args, **kwargs)
	    self.fields["entreprise"].initial=1
	    
