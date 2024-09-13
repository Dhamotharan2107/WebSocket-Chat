from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display room names in the admin list view
    search_fields = ('name',)  # Add search functionality for room names

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'content', 'timestamp')  # Display message details
    list_filter = ('room', 'user')  # Filter messages by room and user
    ordering = ('timestamp',)  # Order messages by timestamp

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If viewing a specific message
            return ('room', 'user', 'timestamp')  # Make room, user, and timestamp readonly
        else:
            return ()
