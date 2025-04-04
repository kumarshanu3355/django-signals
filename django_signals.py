from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def slow_signal_handler(sender, instance, **kwargs):
    print("Signal received, processing...")
    time.sleep(5)  # Simulate a slow operation
    print("Signal processing complete!")

# Creating a user to trigger the signal
new_user = User.objects.create(username="test_user", password="test123")
print("User creation complete!")
