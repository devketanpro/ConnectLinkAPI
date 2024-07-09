from django.urls import path
from connect_link.views import InterestCreateView, ReceivedInterestListView


urlpatterns = [
    path('interests/', InterestCreateView.as_view(), name='interest-create'),
    path('interests/received/', ReceivedInterestListView.as_view(), name='received-interests'),
]
