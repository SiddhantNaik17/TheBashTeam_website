from django.db.models.signals import post_save

from accounts.models import User, UserProfile


def create_user_profile(sender, instance, created, **kwargs):
    # Whenever a new user is created also create it's user profile
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
