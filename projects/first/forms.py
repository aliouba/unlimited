from django.forms import ModelForm
from first.models import Clients
class ArticleForm(ModelForm):
	class Meta:
		model = Clients
		fields = ['nom', 'prenom', 'adresse', 'code']
