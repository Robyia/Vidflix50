from django.contrib import admin
from .models import course, Lesson, category, language

admin.site.register(course)
admin.site.register(Lesson)
admin.site.register(language)
admin.site.register(category)
class InLineLesson(admin.TabularInline):
    model = Lesson
    extra = 1
    max_num = 3

class CourseAdmin(admin.ModelAdmin):
    inlines = [InLineLesson]
    list_display = ('title', 'slug', 'description', 'combine_title_and_slug')
    list_display_links = ('title', 'combine_title_and_slug')
    list_editable = ('slug')
    list_filter = ('title', 'slug')
    search_fields = ('title', 'slug')
    fieldsets = (
        (None, {
            'fields':(
                'slug',
                'title',
                'description',
                'allowed_memberships'
            )
        })
    )

    def combine_title_and_slug(self, obj):
        return "{} - {}".format(obj.title, obj.slug)
