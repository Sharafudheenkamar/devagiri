from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import AuditoriumBooking

@shared_task
def send_email_notification(booking_id):
    try:
        print("send email")
        booking = AuditoriumBooking.objects.get(id=booking_id)
        send_mail(
            subject="Auditorium Booking Reminder",
            message=f"Reminder: Your auditorium booking is scheduled at {booking.booking_time}.",
            from_email="no-reply@example.com",
            recipient_list=[booking.user_email],
            fail_silently=False,
        )
    except AuditoriumBooking.DoesNotExist:
        pass
