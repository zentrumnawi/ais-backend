from django.contrib import admin

from .models import Find, FormalAspect, Ware


class FormalAspectInline(admin.StackedInline):
    model = FormalAspect


class WareInline(admin.StackedInline):
    model = Ware


class FindModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    inlines = [
        FormalAspectInline,
        WareInline
    ]


admin.site.register(FormalAspect, admin.ModelAdmin)
admin.site.register(Ware, admin.ModelAdmin)
admin.site.register(Find, FindModelAdmin)
