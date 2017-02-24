from django.contrib import admin
from members.models import Member
from cards.models import Card
from logs.models import Log


class CardInline(admin.TabularInline):
    model = Card
    extra = 1


class LogInline(admin.TabularInline):
    model = Log
    extra = 0
    max_num = 10

    can_delete = False

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):
        result = list(set(
                [field.name for field in self.opts.local_fields] +
                [field.name for field in self.opts.local_many_to_many]
            ))
        result.remove('id')
        return result

# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_per_page = 50

    inlines = [
        CardInline,
        LogInline,
    ]