from django.contrib import admin
from members.models import Member
from cards.models import Card


class CardInline(admin.TabularInline):
    model = Card

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

    inlines = [
        CardInline,
    ]