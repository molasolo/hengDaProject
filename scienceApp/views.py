from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def science(request):
    # html = '<html><body>科研基地</body></html>'
    # return HttpResponse(html)
    return render(request, 'science.html', {'active_menu': 'science',})
