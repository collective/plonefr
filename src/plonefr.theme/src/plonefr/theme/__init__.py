import logging
from zope.i18nmessageid import MessageFactory

MessageFactory = plonefrthemeMessageFactory = MessageFactory('plonefr.theme')
logger = logging.getLogger('plonefr.theme')
EXTENSION_PROFILES = ('plonefr.theme:default',)
SKIN = 'plonefr.skin'
PRODUCT_DEPENDENCIES = (
)


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


GLOBALS = globals()
