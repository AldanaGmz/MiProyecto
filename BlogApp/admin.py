from django.contrib import admin
from .models import Categoria, Post

# Register your models here.

"""class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=("created", "updated")


class PostAdmin(admin.Model.admin):
    readonly_fields=("created", "updated")"""


admin.site.register(Categoria)
admin.site.register(Post)





