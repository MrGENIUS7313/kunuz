from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import Category, Tags, News
from hitcount.models import HitCount
# Register your models here.
admin.site.register(Tags)
admin.site.register(Category)

class NewsAdmin(admin.ModelAdmin):
    readonly_fields = ['view_count', ]
    ordering = ['-create_at', ]
    list_display = ['title', 'create_at', 'user', 'is_active']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Create or get HitCount object
        hit_count, created = HitCount.objects.get_or_create(
            content_type_id=ContentType.objects.get_for_model(obj).id,
            object_pk=obj.pk
        )

admin.site.register(News, NewsAdmin)