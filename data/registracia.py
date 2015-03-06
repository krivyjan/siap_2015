__author__ = 'Jan'

import dexml
from dexml import fields

from data.skolenie import Skolenie

class Registracia(dexml.Model):
    nazov = fields.String()
    titul = fields.String(tagname="titul")
    meno = fields.String(tagname="meno")
    priezvysko = fields.String(tagname="priezvysko")
    firma = fields.String(tagname="firma")
    pobocka = fields.String(tagname="pobocka")
    pozicia = fields.String(tagname="pozicia")
    email = fields.String(tagname="email")
    cislo = fields.String(tagname="cislo")
    stat = fields.String(tagname="stat")
    obec = fields.String(tagname="obec")
    psc = fields.String(tagname="psc")
    skolenia = fields.List(Skolenie)
