"""
Colissimo from LaPoste (France) Shipping Module for Satchmo

author: Julien Maupetit (twitter @julienmaupetit)
"""
from django.utils.translation import ugettext_lazy as _
from livesettings import *

SHIP_MODULE_NAME = "satchmo_colissimo"

SHIP_MODULES = config_get('SHIPPING', 'MODULES')
SHIP_MODULES.add_choice((SHIP_MODULE_NAME, 'Colissimo'))

SHIPPING_GROUP = ConfigurationGroup( SHIP_MODULE_NAME,
                                     _('Colissimo Shipping Settings'),
                                     requires = SHIP_MODULES,
                                     requiresvalue = SHIP_MODULE_NAME,
                                     ordering = 101 )

config_register_list(
    
    IntegerValue(SHIPPING_GROUP,
                 'RECOMMANDED_DEFAULT_LEVEL',
                 description=_("Colissimo Recommanded default level"),
                 help_text=_("Set the default recommanded level from 0 to 5 corresponding to R0-R5"),
                 default=0 ),
                 
    DecimalValue(SHIPPING_GROUP,
                 'BOX_DEFAULT_WEIGHT',
                 description=_("Colissimo box default weight"),
                 help_text=_("Set the default weight in Kg"),
                 default=0.2) )
