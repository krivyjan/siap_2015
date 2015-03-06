__author__ = 'Jan'

import dexml
from dexml import fields

class Skolenie(dexml.Model):
    nazov = fields.String()
    priorita = fields.Integer(tagname="priorita")
    termin = fields.Integer(tagname="termin")