from django.shortcuts import render
from .forms import QForm
from .helpers import *

def search_page(request):
    qform = QForm()
    results = None
    url = ''
    if request.method == 'GET' and 'submit_flag' in request.GET:    #submit_flag distinguishes b/w first time loading or after 'submit'
        qform = QForm(request.GET)
        if qform.is_valid():
            results = get_results(dict(request.GET))
    url = request.get_full_path()
    url = re.sub(r'&page=\d+', '', url)     #cleaning up url to append new page numbers during pagination
    return render(request, 'search/search.html', {'form': qform, 'results': results, 'url': url})
