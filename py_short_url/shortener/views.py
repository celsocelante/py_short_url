from django.shortcuts import render
from django.http import *
from converter import *
from shortener.models import *
import urllib

# View to redirect "compressed" url to original state
def index_view(request, offset):
    result = Urls.objects.get(id=toDecimal(offset))
    location = result.url

    res = HttpResponse(location, status=302)
    res['Location'] = location
    return res
    #else: raise Http404

# View to compress urls. Input need to be encoded
def api_view(request, offset):
    #value = toDecimal(offset)
    #offset = urllib.unquote(offset)
    url = Urls(url=urllib.quote_plus(offset),clicks=0)
    url.save()
    return HttpResponse(url.url)
