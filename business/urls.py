from django.urls import path
from .views import ContactCreateAPIView

urlpatterns = [
    path('contacts/', ContactCreateAPIView.as_view(), name='contact-create'),
]
