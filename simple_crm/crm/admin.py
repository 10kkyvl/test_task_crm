from django.contrib import admin

from .models import Client, Deal, Note


class DealInline(admin.TabularInline):
    model = Deal
    extra = 0


class NoteInline(admin.TabularInline):
    model = Note
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email", "created_at")
    search_fields = ("name", "phone", "email")
    inlines = [DealInline]

    readonly_fields = ("created_at",)


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "status", "amount", "created_at")
    list_filter = ("status",)
    search_fields = ("title", "client__name")
    inlines = [NoteInline]

    readonly_fields = ("created_at",)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("deal", "created_at")
    search = ("text",)

    readonly_fields = ("created_at",)
