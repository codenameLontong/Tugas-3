from django.shortcuts import render
from mywatchlist.models import Movies
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = Movies.objects.all()
    context = {
        'list' : data_watchlist,
        'nama': 'Jeremy Mervin',
        'id' : '2106654675',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Movies.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Movies.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")