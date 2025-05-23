from django.contrib import admin

from .models import Advertisement, FavoriteAdvertisement

admin.site.register(Advertisement)
admin.site.register(FavoriteAdvertisement)


