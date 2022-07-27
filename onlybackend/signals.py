from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from .models import User
from django.dispatch import receiver


@receiver(valid_ipn_received)
def valid_ipn_signal(sender, **kwargs):
    print('Ipn Valid')
    ipn_obj = sender
    if ipn_obj.payment_status == 'Completed':

        User.objects.create()

@receiver(invalid_ipn_received)
def invalid_ipn_signal(sender, **kwargs):
    print('Ipn invalid')
    ipn_obj = sender
    if ipn_obj.payment_status == 'Completed':

        User.objects.create()
      