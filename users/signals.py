from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group
from events.models import RSVP
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from users.models import UserProfile

@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_url = f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}/"

        subject = 'Please activate Your Account'
        message = f"Hello user {instance.username},\n\nIf you want to register,\n\nPlease activate your account by clicking the link below:\n{activation_url}\n\nThank You!"
        recipient_list = [instance.email]

        try:
            send_mail(subject, message,
                      settings.EMAIL_HOST_USER, recipient_list)
        except Exception as e:
            print(f"An error happened.Failed to send email to {instance.email}: {str(e)}")


@receiver(post_save, sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name='User')
        instance.groups.add(user_group)
        instance.save()


@receiver(post_save, sender=RSVP)
def send_rsvp_confirmation_email(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        event = instance.event
        if user.email:
            send_mail(
                subject="RSVP Confirmation",
                message=(
                    f"Hi {user.first_name},\n\n"
                    f"You've successfully RSVPed to the event: {event.name}!\n\n"
                    f"Event Date: {event.date}\n"
                    f"Location: {event.location}\n\n"
                    f"Thanks for responding!"
                ),
                from_email="easin21562050@gmail.com", 
                recipient_list=[user.email],
                fail_silently=False
            )

@receiver(post_save,sender=User)
def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
