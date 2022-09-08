from user.models import CustomUser


class ConsultantCapacityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        consultants = CustomUser.objects.filter(type='consultant')
        for consultant in consultants:
            if consultant.consultantprofile.capacity <= consultant.consultantprofile.students.all().count():
                consultant.consultantprofile.status = False
                consultant.consultantprofile.save()
            else:
                consultant.consultantprofile.status = True
                consultant.consultantprofile.save()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
