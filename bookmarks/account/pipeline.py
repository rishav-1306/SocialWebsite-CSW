from .models import Profile


def create_profile(backend, user, response, *args, **kwargs):
    """
    Social auth pipeline function.
    Creates a Profile for new users who register via a social provider
    (e.g. Google OAuth2). Skips silently if the profile already exists.
    """
    Profile.objects.get_or_create(user=user)
