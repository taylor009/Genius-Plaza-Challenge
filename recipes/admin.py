from django.contrib import admin
from .models import Recipe, Step, Ingredient

# Register Models here.
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
