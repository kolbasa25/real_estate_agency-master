from django.contrib import admin
from .models import Flat, Complaint, Owner

class FlatOwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner',)
    extra = 0

class FlatAdmin(admin.ModelAdmin):
    inlines = (FlatOwnersInline,)
    fields = (
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
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        'likes_count',
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
        'author',
        'flat',
        'text',
        'created_at',
    )
    search_fields = (
        'author__username',
        'author__email',
        'flat__address',
        'text',
    )
    list_filter = (
        'created_at',
        'author',
    )
    readonly_fields = ('created_at',)
    raw_id_fields = ('author', 'flat',)
    fields = ('author', 'flat', 'text',)

class OwnerAdmin(admin.ModelAdmin):
    fields = (
        'full_name',
        'phonenumber',
        'pure_phone',
        'flats',
    )
    search_fields = (
        'full_name',
        'phonenumber',
        'pure_phone',
    )
    
    list_display = (
        'full_name',
        'phonenumber',
        'pure_phone',
        'flats_count',
    )
    list_filter = ('flats',)
    raw_id_fields = ('flats',)
    filter_horizontal = ('flats',)
    
    def flats_count(self, obj):
        return obj.flats.count()
    flats_count.short_description = 'Количество квартир'

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)