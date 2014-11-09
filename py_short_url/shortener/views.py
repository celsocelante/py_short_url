from django.shortcuts import render
from django.http import *
from converter import *
from shortener.models import *
import urllib2

# View to redirect "compressed" url to original state
def index_view(request, offset):
    result = Urls.objects.get(id=toDecimal(offset))
    location = urllib2.unquote(result.url)

    res = HttpResponse(location, status=302)
    res['Location'] = location
    return res
    #else: raise Http404

# View to compress urls. Input need to be encoded
def api_view(request):
    #offset = urllib.unquote(offset)
    url = Urls(url=urllib2.quote(request.GET['url']),clicks=0)
    url.save()
    return HttpResponse(toString(int(url.id)))
