from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_email_notification

class AuditoriumBooking(models.Model):
    user_email = models.EmailField()
    booking_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.user_email} at {self.booking_time}"

@receiver(post_save, sender=AuditoriumBooking)
def schedule_email_notification(sender, instance, created, **kwargs):
    if created:
        try:
            # Ensure booking_time is timezone-aware
            notification_time = instance.booking_time - timedelta(seconds=5)
            now_time = now()

            # Calculate countdown in seconds
            countdown = (notification_time - now_time).total_seconds()

            if countdown > 0:
                # Schedule the task using Celery
                send_email_notification.apply_async(
                    (instance.id,), 
                    countdown=countdown
                )
                print(f"Email notification scheduled in {countdown} seconds.")
            else:
                print("Notification time is in the past. Email will not be scheduled.")
        except Exception as e:
            print(f"Error scheduling email notification: {e}")
