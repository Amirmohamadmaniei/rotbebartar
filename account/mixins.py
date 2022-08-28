from django.shortcuts import redirect
from django.urls import reverse


class RequireSelfUser:
    def dispatch(self, request, *args, **kwargs):
        if self.kwargs['pk'] == request.user.id:
            return super(RequireSelfUser, self).dispatch(request, *args, **kwargs)
        return redirect(reverse('home:home'))
