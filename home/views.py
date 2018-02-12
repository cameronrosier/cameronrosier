from django.shortcuts import render

# Create your views here.
def index(request):
    page_headers = {'index_main_header': 'About Me'}
    return render(request, 'home/index.html', context=page_headers)
