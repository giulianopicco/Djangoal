from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from teams import models
from teams import forms
# Create your views here.
from teams.mixins import PageTitleMixin


def dashboard(request):
    return render(request, 'dashboard.html')

class HomeView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["games_today"] = 6
        return context


def teamLists(request):
    teams = models.Team.objects.all()
    return render(request, 'teams/list.html', {'teams': teams})


class TeamListView(LoginRequiredMixin, CreateView, ListView):
    model = models.Team
    fields = ('name', 'couch', 'location', 'photo')
    template_name = 'teams/list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.model.objects.filter(couch=self.request.user)
        return self.model.objects.all()


def teamDetail(request, team_pk):
    team = get_object_or_404(models.Team, id=team_pk)
    return render(request, 'teams/detail.html', {'team': team})


class TeamDetailView(DetailView, UpdateView):
    model = models.Team
    fields = ('name', 'couch', 'location', 'photo')
    context_object_name = 'team'
    template_name = 'teams/detail.html'
    pk_url_kwarg = 'team_pk'


class TeamCreateView(LoginRequiredMixin, PageTitleMixin, CreateView):
    model = models.Team
    template_name = 'teams/create.html'
    fields = ('name', 'couch', 'location', 'photo')
    # from PageTitleMixin
    page_title = 'Create new Team'


    def get_initial(self):
        initial = super().get_initial()
        if self.request.user.is_authenticated:
            initial['couch'] = self.request.user.pk
        return initial


class TeamUpdateView(LoginRequiredMixin, PageTitleMixin, UpdateView):
    model = models.Team
    pk_url_kwarg = 'team_pk'
    template_name = 'teams/create.html'
    fields = ('name', 'couch', 'location', 'photo')

    def get_page_title(self):
        obj = self.get_object()
        return 'Update Team: {}'.format(obj.name)


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Team
    success_url = reverse_lazy('teams:list')