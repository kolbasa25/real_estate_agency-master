from django.contrib import admin
from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    fields = (
        'owner',
        'owner_pure_phone',
        'owners_phonenumber',
        'address',
        'town',
        'town_district',
        'price',
        'new_building',
        'construction_year',
        'rooms_number',
        'living_area',
        'has_balcony',
        'floor',
        'description',
        'active',
        'created_at',
        'liked_by',
    )
    search_fields = ('town', 'address', 'owner','owner_pure_phone')
    readonly_fields = ('created_at',)
    
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'likes_count',
        'owner_pure_phone',
        'owners_phonenumber', 
    )
    
    list_editable = ('new_building',)

    list_filter = (
        'new_building',
        'rooms_number',
        'has_balcony',
        'town',
        'active',
    )

    raw_id_fields = ('liked_by',)
    
    def likes_count(self, obj):
        return obj.liked_by.count()
    likes_count.short_description = 'Количество лайков'

class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'flat',
        'text',
        'created_at',
    )
    search_fields = (
        'user__username',
        'user__email',
        'flat__address',
        'text',
    )
    list_filter = ('created_at', 'user')
    readonly_fields = ('created_at',)
    raw_id_fields = ('user', 'flat')
    fields = ('user', 'flat', 'text')

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)