__author__ = 'Jan'

import dexml
from dexml import fields


class course(dexml.Model):
    #nazov = fields.String()
    nazov = fields.String(tagname="name")
    priorita = fields.Integer(tagname="priority")
    termin = fields.Integer(tagname="date")


class courses(dexml.Model):
    skolenie = fields.List(course)

