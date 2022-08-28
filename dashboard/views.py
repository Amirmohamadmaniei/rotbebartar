from django.views import generic


class DashBoardHomeView(generic.TemplateView):
    template_name = 'dashboard/dashboard_index.html'


class DashBoardStatisticsView(generic.TemplateView):
    template_name = 'dashboard/statistics.html'
