from allauth.utils import get_user_model


def create_user():
    """Creates a test user."""
    user_model_class = get_user_model()
    return user_model_class.objects.create_user(
        username='testuser', password='testpass'
    )
