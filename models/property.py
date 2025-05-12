from odoo import models, fields, api

class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Real Estate Property'
    _inherit = ['mail.thread']

    name = fields.Char(required=True, tracking=True)
    description = fields.Text()
    price = fields.Float(tracking=True)
    status = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], default='new', tracking=True)
    property_type = fields.Selection([
        ('sale', 'For Sale'),
        ('rent', 'For Rent')
    ], default='sale')
    agent_id = fields.Many2one('res.users', string="Agent")
    offer_ids = fields.One2many('real.estate.offer', 'property_id', string="Offers")

class RealEstateOffer(models.Model):
    _name = 'real.estate.offer'
    _description = 'Property Offer'

    amount = fields.Float(required=True)
    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('real.estate.property', required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], default='new')
