from django.contrib import admin
from members.models import Member
from cards.models import Card
from logs.models import Log


class CardInline(admin.TabularInline):
    model = Card
    extra = 1

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_per_page = 10

    inlines = [
        CardInline,
    ]