# -*- coding: utf-8 -*-
from odoo import models, fields, api, tools

class MultipleReceiptSender(models.TransientModel):
    _name = 'interpod.multiple.receipt'

    def send_receipts(self):
        context = self._context['active_ids']
        template = self.env.ref('interpod_payment_mail_receipts.multiple_mail_template_payment')
        for receipt in context:
            self.env['mail.template'].browse(template.id).send_mail(receipt, force_send=True)
            # self.env['mail.mail'].create(main_content).send()
            # def follow_up_date_scheduler_queue(self):
            #     today = fields.Date.context_today(self)
            #     tomorrow = fields.Date.from_string(today) + timedelta(days=1)
            #     identities = self.search([('follow_date', '=', tomorrow)])
            #     # Find the e-mail template
            #     template = self.env.ref('identity_check.email_template_for_identity_followup')
            #     for identity in identities:
            #         self.env['mail.template'].browse(template.id).send_mail(identity.id, force_send=True)
            #     # return mail_id
            #     return
        return