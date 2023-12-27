from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    tg_id = fields.IntField()

class ReferalProgram(Model):
    id = fields.IntField(pk=True)
    tg_id_ref = fields.IntField()
    tg_un_ref = fields.CharField(max_length=255)
    sell_invited = fields.IntField()

class BaseRegistration(Model):
    id = fields.IntField(pk=True)
    tg_id_user = fields.IntField()
    tg_un_user = fields.CharField(max_length=255)
    name = fields.CharField(max_length=255)
    sphere = fields.CharField(max_length=255)
    born_date = fields.CharField(max_length=255)
    born_time = fields.CharField(max_length=255)
    born_city = fields.CharField(max_length=255)
    subject_type_id = fields.IntField()
    personal_line_id = fields.IntField()
    design_line_id = fields.IntField()
    profile_id = fields.IntField()
    subject_authority_id = fields.IntField()
    subject_type_name = fields.CharField(max_length=500)
    personal_line_name = fields.CharField(max_length=500)
    design_line_name = fields.CharField(max_length=500)
    profile_name = fields.CharField(max_length=500)
    subject_authority_name = fields.CharField(max_length=500)

class TypePersonal_Money(Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=100)
    description = fields.CharField(max_length=4000)
    home_work = fields.CharField(max_length=4000)
    congratulation = fields.CharField(max_length=4000)

class AuthorityInBusiness_Money(Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=100)
    description = fields.CharField(max_length=4000)
    home_work = fields.CharField(max_length=4000)
    congratulation = fields.CharField(max_length=4000)

class StrategyProfiles_Money(Model):
    id = fields.IntField(pk=True)
    key = fields.CharField(max_length=100)
    name = fields.CharField(max_length=200)
    description = fields.CharField(max_length=4000)
    home_work = fields.CharField(max_length=4000)
    congratulation = fields.CharField(max_length=4000)

class Products(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    price = fields.FloatField()
    description = fields.CharField(max_length=4000)
