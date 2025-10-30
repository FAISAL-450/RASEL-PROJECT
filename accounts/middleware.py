from accounts.models import Profile

class UserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile, _ = Profile.objects.get_or_create(user=request.user)
            request.user_profile = profile
        else:
            request.user_profile = None
        return self.get_response(request)




