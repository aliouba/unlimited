from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from first.forms import ArticleForm
def add_client(request):
    if request.method == 'POST':
        print "form valided"
        form = ArticleForm(request.POST)
        if form.is_valid():
            print "form valid"
            data = form.save(commit=False)		
            print "yes"
            return HttpResponseRedirect('/thanks/')
        else:
			print "non valid"        
    else:
        print "FALSE"
        print request.user.id
        form = ArticleForm()
    return render(request, 'first/add_client.html', {'add_client': form})
