# mymap/views.py

# from django.shortcuts import render
# from .models import Ministry

# def ministry_map(request):
#     ministries = Ministry.objects.all()
#     return render(request, 'mymap/ministry_map.html', {'ministries': ministries})


# from django.shortcuts import render
# from .models import Ministry

# def ministry_map_view(request):
#     ministries = Ministry.objects.all()
#     context = {
#         'ministries_json': list(ministries.values())  # Serialize ministries to JSON
#     }
#     return render(request, 'mymap/ministry_map.html', context)


# mymap/views.py

# mymap/views.py
from django.shortcuts import render
from django.conf import settings
from .models import Ministry, Institution
import requests

def ministry_map_view(request):
    ministries = Ministry.objects.all()
    context = {
        'ministries': list(ministries.values()),
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,  # Consider using environment variables for security
    }
    return render(request, 'mymap/ministry_map.html', context)

def sjp_map_view(request):
    institutions = Institution.objects.all()
    context = {
        'institutions': institutions,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'mymap/map.html', context)

def calculate_distance(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')
    api_key = settings.GOOGLE_MAPS_API_KEY
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination}&key={api_key}"

    try:
        response = requests.get(url)
        distance_data = response.json()
        return render(request, 'mymap/distance.html', {'distance_data': distance_data})
    except requests.exceptions.RequestException as e:
        # Handle API request errors gracefully (e.g., display error message)
        return render(request, 'mymap/distance.html', {'error': str(e)})

