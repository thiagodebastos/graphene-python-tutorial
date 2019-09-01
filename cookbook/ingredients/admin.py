# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from cookbook.ingredients.models import Category, Ingredient, Recipe

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
