from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category

class MarriedFilter(admin.SimpleListFilter):
    title='Women status'
    parameter_name='status'

    def lookups(self, request, model_admin):
        return[
            ('married', 'Married'),
            ('single', 'Not married')
        ]

    def queryset(self, request, queryset):
        if self.value()=='married':
            return queryset.filter(husband__isnull=False)
        elif self.value()=='single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenModel(admin.ModelAdmin):
    fields = ['title', 'content', 'photo', 'post_photo', 'slug', 'cat', 'husband', 'tags']
    readonly_fields = ['slug', 'post_photo']
    filter_horizontal = ['tags']
    list_display = ['title', 'post_photo', 'time_create', 'is_published', 'cat']
    list_display_links = ['title']
    ordering=['time_create', 'title']
    list_editable = ('is_published',)
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter,  'cat__name', 'is_published']

    @admin.display(description='Image', ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}' width=50")
        else:
            return "without photo"



    @admin.action(description='Publish')
    def set_published(self, request, queryset):
        count=queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f'{count} posts changed')

    @admin.action(description='Move to draft')
    def set_draft(self, request, queryset):
        count =queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f'{count} posts moved to draft', messages.WARNING)

@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']