from django.shortcuts import render

# Create your views here.

def projects(request):
	page_info = {'test':'some test info'}
	
	return render(request, 'projects/projects.html', context=page_info)
