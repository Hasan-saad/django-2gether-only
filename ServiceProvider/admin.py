from django.contrib import admin
from .models import *


admin.site.register(ServicProvider)
admin.site.register(Category)
admin.site.register(Reservation)
# admin.site.register(comments)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'serviceProvider', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('user', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


