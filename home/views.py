from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Blog
from home.forms import ContactUsForm
from user.models import CustomUser


class HomeView(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['consultants'] = CustomUser.objects.filter(type='consultant')
        context['last_blogs'] = Blog.objects.filter(status=True).order_by('-created')[:2]
        context['popular_blog'] = Blog.objects.filter(status=True).annotate(
            count=Count('likes')).order_by('-count', '-created')[:1]
        print(context['popular_blog'])
        return context


class AboutUsView(generic.TemplateView):
    template_name = 'home/AboutUs.html'


class FaqView(generic.TemplateView):
    template_name = 'home/Faq.html'


class ContactUsView(generic.FormView):
    template_name = 'home/ContactUs.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('home:contact_us')

    def form_valid(self, form):
        form.save()
        return super(ContactUsView, self).form_valid(form)
