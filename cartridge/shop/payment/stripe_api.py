from __future__ import unicode_literals
from future.builtins import int
from future.builtins import str
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext as _
from mezzanine.conf import settings

from cartridge.shop.checkout import CheckoutError

# Requires Stripe Library Module -- install from pypi.
try:
    import stripe
except ImportError:
    raise ImproperlyConfigured("stripe package must be installed")

try:
    stripe.api_key = settings.STRIPE_API_KEY
except AttributeError:
    raise ImproperlyConfigured("You need to define STRIPE_API_KEY "
                               "in your settings module to use the "
                               "stripe payment processor.")

class Process():

    def create_customer(request):
        try:
            customer = stripe.Customer.create(
                description="Customer for david.martin@example.com",
                source=request.POST['stripe_token'])
        except Exception as e:
            raise CheckoutError(_("A general error occured: ") + str(e))
        return customer.id
    
    def take_payment(order):
        """
        Payment handler for the stripe API.
        """
        try:
            response = stripe.Charge.create(
                amount=int((order.total * 100).to_integral()),
                currency=getattr(settings, "STRIPE_CURRENCY", "gbp"),
                customer=order.stripe_customer_id,)
        except stripe.CardError:
            raise CheckoutError(_("Transaction declined"))
        except Exception as e:
            raise CheckoutError(_("A general error occured: ") + str(e))
        return response.id
