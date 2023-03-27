from django.contrib import admin
from .models import Channel, Category, Country, Favorites, Users


# Register your models here.
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', 'telegram_link', 'tgstat_link', 'telemetr_link', 'subscribes_count']
    readonly_fields = ['subscribes_count']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    pass

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
