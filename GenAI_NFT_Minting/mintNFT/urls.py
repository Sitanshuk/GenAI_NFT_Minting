# yourappname/urls.py
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    # path('your-location-url/', your_location_view, name='your_location_view_name'),
    # path('location_plus_cuisine/', location_plus_cuisine, name='location_plus_cuisine'),
    #
    # # path('recommend_on_location/', recommend_on_location, name='recommend_on_location'),
    # path('process_selected_restaurant/', process_selected_restaurant, name='process_selected_restaurant'),
    # path('new_recommendations/', new_recommendations, name='new_recommendations'),
]
