from django.urls import path
from django.views.generic import TemplateView

from teams import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='dashboard'),
    path('list', views.TeamListView.as_view(), name='list'),
    path('create', views.TeamCreateView.as_view(), name='create'),
    path('update/<int:team_pk>', views.TeamUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.TeamDeleteView.as_view(), name='delete'),
    path('<int:team_pk>', views.TeamDetailView.as_view(), name='detail')
]