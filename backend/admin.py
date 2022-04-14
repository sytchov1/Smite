from django.contrib import admin
from .models import WowClass, Armor, Weapon, Gem

# Register your models here.

admin.site.register(WowClass)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(Gem)