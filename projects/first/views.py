from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from first.forms import ArticleForm
def add_client(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
		form = ArticleForm()
		print "FALSE"
    return render(request, 'first/add_client.html', {'add_client': form})
