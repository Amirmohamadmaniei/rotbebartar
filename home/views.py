from django.views import generic

from user.models import CustomUser


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['consultants'] = CustomUser.objects.filter(type='consultant')
        return context
