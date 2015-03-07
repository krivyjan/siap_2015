#coding: utf-8
__author__ = 'Jan'

import dexml
from dexml import fields

from data.skolenie import courses

class application(dexml.Model):
    titul = fields.String(tagname="degree")
    meno = fields.String(tagname="first_name")
    priezvysko = fields.String(tagname="last_name")
    firma = fields.String(tagname="company")
    pobocka = fields.String(tagname="division")
    pozicia = fields.String(tagname="position")
    email = fields.String(tagname="e_mail")
    cislo = fields.String(tagname="phone")
    stat = fields.String(tagname="state")
    obec = fields.String(tagname="city")
    psc = fields.String(tagname="postal_code")
    skolenia = fields.List(courses)
