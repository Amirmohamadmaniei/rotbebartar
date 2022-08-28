from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from user.models import CustomUser


class ConsultantListView(generic.ListView):
    template_name = 'consultant/consultant_list.html'
    queryset = CustomUser.objects.filter(type='consultant')
    paginate_by = 1


class ConsultantDetailView(generic.DetailView):
    template_name = 'consultant/consultant_detail.html'
    queryset = CustomUser.objects.filter(type='consultant')



