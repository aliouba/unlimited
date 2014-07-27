from django.shortcuts import render
from django.shortcuts import render_to_response
from first.forms import ArticleForm
def add_client(request):
    client_form = ArticleForm()
    return render_to_response('first/add_client.html', {'add_client' : client_form})
