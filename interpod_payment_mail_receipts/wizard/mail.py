import base64
import re

from odoo import _, api, fields, models, SUPERUSER_ID, tools
from odoo.tools import pycompat
from odoo.tools.safe_eval import safe_eval

class MailComposer(models.TransientModel):
    """ Generic message composition wizard. You may inherit from this wizard
        at model and view levels to provide specific features.

        The behavior of the wizard depends on the composition_mode field:
        - 'comment': post on a record. The wizard is pre-populated via ``get_record_data``
        - 'mass_mail': wizard in mass mailing mode where the mail details can
            contain template placeholders that will be merged with actual data
            before being sent to each recipient.
    """
    _name = 'tdt.payment.mail'
    _inherit = 'mail.message'
