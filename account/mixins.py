from django.shortcuts import redirect
from django.urls import reverse


class RequireSelfUser:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('account:login'))

        return super(RequireSelfUser, self).dispatch(request, *args, **kwargs)


class NoLoginRequired:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home:home'))
        return super(NoLoginRequired, self).dispatch(request, *args, **kwargs)


class IsConsultant:
    def dispatch(self, request, *args, **kwargs):
        if request.user.type != 'consultant':
            return redirect('home:home')
        return super(IsConsultant, self).dispatch(request, *args, **kwargs)
