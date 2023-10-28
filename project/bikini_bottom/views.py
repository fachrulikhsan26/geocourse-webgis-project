from django.shortcuts import render
from django.core.serializers import serialize
from .models import Facility
from django.http import HttpResponse, JsonResponse
import ast #untuk membuat format koordinat menjadi sebuah object

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def home_map_api(request):
    data = serialize('geojson', Facility.objects.all())
    return HttpResponse(data, content_type='json')

def custom_map_api(request):
    features = {
        'type': 'FeatureCollection',
        'crs': {
            'type': '',
            'properties': {
                'name': 'EPSG:4326'
            }
        },
        'features': []
    } 

    model =  Facility.objects.all() #untuk memanggil data facility
    for item in model: #dilakukan looping
        feature = {
            'type': 'Feature',
            'geometry': ast.literal_eval(item.location.json), #BEST PRACTICES
            'properties':{
                'nama': item.name,
                'tipe': item.types,
                'harga': item.price,
                'satuan_harga': item.price_unit,
            }
        } 
        features['features'].append(feature)
    return JsonResponse(features, safe=False) 