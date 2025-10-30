from accounts.models import Profile

def user_profile(request):
    if request.user.is_authenticated:
        username = request.user.username.lower()

        # Define department access per user
        department_access = {
            'kamal': ['salesmarketing', 'construction', 'finance'],
            'nayan': ['salesmarketing'],
            'salim': ['salesmarketing'],
        }

        try:
            profile = Profile.objects.get(user=request.user)
            departments = department_access.get(username, [profile.department])
            return {
                'user_profile': profile,
                'user_departments': departments,
            }
        except Profile.DoesNotExist:
            return {
                'user_departments': department_access.get(username, []),
            }

    return {}
