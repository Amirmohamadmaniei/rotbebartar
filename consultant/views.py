from datetime import datetime, timedelta
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from consultant.forms import CommentForm
from user.models import CustomUser


class ConsultantListView(generic.ListView):
    template_name = 'consultant/consultant_list.html'
    queryset = CustomUser.objects.filter(type='consultant')
    paginate_by = 2


class ConsultantDetailView(generic.View):
    def get(self, request, slug):
        form = CommentForm()
        consultant = CustomUser.objects.get(slug=slug)
        return render(request, 'consultant/consultant_detail.html',
                      {'object': consultant, 'form': form})

    def post(self, request, slug):
        form = CommentForm(self.request.POST)
        consultant = CustomUser.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.studentprofile
            comment.consultant = consultant.consultantprofile
            comment.save()
        return render(request, 'consultant/consultant_detail.html', {'object': consultant, 'form': form})


class SelectConsultantView(generic.View):
    def get(self, request, *args, **kwargs):
        consultant_pk = request.GET.get('consultant_pk')
        days = request.GET.get('days')
        consultant = CustomUser.objects.get(pk=consultant_pk)
        student = CustomUser.objects.get(id=request.user.id)

        student.studentprofile.consultant = consultant.consultantprofile
        student.studentprofile.time_consultation = days
        student.studentprofile.time_end = datetime.today().date() + timedelta(days=int(days))
        student.studentprofile.save()
        return redirect(reverse('consultant:consultant_detail', kwargs={'slug': consultant.slug}))


class SearchConsultantView(generic.View):
    def get(self, request):
        q = self.request.GET.get('q')
        object_list = CustomUser.objects.filter(
            Q(type='consultant') & Q(first_name__icontains=q) | Q(last_name__icontains=q) |
            Q(consultantprofile__major_university__icontains=q))
        return render(request, 'consultant/consultant_list.html', {'object_list': object_list})


class FilterConsultantView(generic.ListView):
    template_name = 'consultant/consultant_list.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FilterConsultantView, self).get_context_data(**kwargs)
        context['filter'] = True
        return context

    def get_queryset(self):
        consultant_name = self.request.GET.get('consultant_name')
        major = self.request.GET.get('major')

        object_list = CustomUser.objects.filter(Q(type='consultant') & Q(last_name__icontains=consultant_name) &
                                                Q(consultantprofile__major_university__icontains=major))
        return object_list
