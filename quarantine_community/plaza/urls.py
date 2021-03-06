from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from plaza import views

app_name = "plaza"

urlpatterns = [
    path('notifications/', views.OfficialNotificationsView.as_view(), name='official-notifications'),
    path('special-request-form/', views.AddSpecialRequestView.as_view(), name='special-request-form'),
    path('supply-registration-form/', views.AddSupplyRegistrationView.as_view(), name='supply-registration-form'),
    path('drinking-water-registration-form/', views.AddDrinkingWaterRegistrationView.as_view(),
         name='drinking-water-registration-form'),
    path('bentobox-request-form/', views.AddBentoBoxRequestView.as_view(), name='bentobox-request-form'),
    path('quarantine-life-share/', views.QuarantineLifeShareView.as_view(), name='quarantine-life-share'),
]
