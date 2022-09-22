from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def survey(request):
    # html = '<html><body>企业概况</body></html>'
    # return HttpResponse(html)
    return render(request, 'survey.html', {'active_menu': 'about',})

def honor(request):
    # html = '<html><body>荣誉资质</body></html>'
    # return HttpResponse(html)
    return render(request, 'honor.html', {'active_menu': 'about'})