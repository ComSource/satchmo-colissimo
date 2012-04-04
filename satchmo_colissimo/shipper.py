"""
Colissimo from LaPoste (France) Shipping Module for Satchmo

author: Julien Maupetit (twitter @julienmaupetit)
"""

# Note, make sure you use decimal math everywhere!
from decimal import Decimal
from django.utils.translation import ugettext as _
from shipping.modules.base import BaseShipper
from livesettings import config_get_group

from colissimo.models import Recommanded, Rate
from config import SHIP_MODULE_NAME

import logging

log = logging.getLogger('satchmo_colissimo.shipper')

class Shipper(BaseShipper):

    def __init__(self, cart=None, contact=None):

        self._calculated = False
        self.cart = cart
        self.contact = contact

        self.id = u'colissimo'
        
        if cart or contact:
            self.calculate(cart, contact)
            
    def __str__(self):
        """
        This is mainly helpful for debugging purposes
        """
        return "Colissimo"
        
    def description(self):
        """
        A basic description that will be displayed to the user when selecting their shipping options
        """
        return _('La Poste Colissimo')

    def cost(self):
        """
        Complex calculations can be done here as long as the return value is a decimal figure
        """
        assert(self._calculated)
        return(Decimal(self.charges))

    def method(self):
        """
        Describes the actual delivery service (Mail, FedEx, DHL, UPS, etc)
        """
        return _("Colissimo")

    def expectedDelivery(self):
        """
        Can be a plain string or complex calcuation returning an actual date
        """
        return _("3 - 4 business days")

    def valid(self, order=None):
        """
        Can do complex validation about whether or not this option is valid.
        For example, may check to see if the recipient is in an allowed country
        or location.
        """
        return self.is_valid

    def calculate( self, cart, contact ):
        """
        Calculates rates according to colissimo 2012 rates (see
        django-colissimo app)
        """
        
        self.cart = cart
        self.contact = contact
        
        log.debug("Starting LaPoste Colissimo calculations")
        
        self.is_valid = False

        settings = config_get_group( SHIP_MODULE_NAME )
        
        # Compute cart total weight
        total_weight = float(settings.BOX_DEFAULT_WEIGHT.value)
        for product in cart.get_shipment_list():
            try:
                total_weight += float( product.smart_attr('weight') )
            except TypeError:
                log.debug( "Pass: " + str( product.smart_attr('weight') )  )
                pass
            log.debug( "Updated total weight to " + str(total_weight) )
        
        rate = Rate()
        rs = rate.get_rates( contact.shipping_address.country.name, total_weight )
        # Quick and dirty (enought for my customer...)
        level = settings.RECOMMANDED_DEFAULT_LEVEL.value
        if level > 5:
            level = 0

        log.debug( "Rates: %s - Level %s - Rate: %.2f (weight: %.2f price: %.2f)" % (str(rs), level, rs[ level ].price, total_weight, cart.total ) )
        
        self.charges = Decimal( rs[ level ].price )
        
        self.is_valid = True
        self._calculated = True
