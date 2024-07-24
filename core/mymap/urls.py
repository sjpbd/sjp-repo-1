# mymap/urls.py

# from django.urls import path
# from .views import ministry_map

# app_name = 'mymap'

# urlpatterns = [
#     path('', ministry_map, name='ministry_map'),
# ]

# from django.urls import path
# from .views import ministry_map_view  # Adjust according to your view function

# app_name = 'mymap'

# urlpatterns = [
#     path('', ministry_map_view, name='ministry_map'),  # Ensure the URL pattern matches
#     # Other paths as needed
# ]

from django.urls import path
from .views import ministry_map_view  # Adjust according to your view function
from . import views

app_name = 'mymap'

urlpatterns = [
    path('', ministry_map_view, name='ministry_map'),  # Ensure the URL pattern matches
    # Other paths as needed
    path('map/', views.sjp_map_view, name='sjp_map_view'),
    path('calculate_distance/', views.calculate_distance, name='calculate_distance'),
]

