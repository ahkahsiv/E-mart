# from fastapi import FastAPI
# from tortoise.models import Model
# from tortoise import fields, Tortoise


# class Admin(Model):
#     id = fields.IntField(pk = True)
#     Full_name = fields.CharField(80)
#     mobile = fields.CharField(10 , unique = True)
#     email = fields.CharField(50, unique = True)
#     password = fields.TextField()
#     is_active = fields.BooleanField(default= True)
#     last_login = fields.DatetimeField(auto_now_add= True)
#     created_at = fields.DatetimeField(auto_now_add= True)

# Tortoise.init_models(['user.models'], 'models')