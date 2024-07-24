# home/admin.py

from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from tinymce.widgets import TinyMCE
from .models import About, Slide, DetailedAbout, Saint, SaintDetail, Member, NewsItem, FAQ, Obituary

@admin.register(About)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        # Check if there's already an instance
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

# Your existing SlideAdmin registration here
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    readonly_fields = ('preview_image',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'preview_image', 'order', 'is_active')
        }),
    )

    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
    thumbnail.short_description = 'Thumbnail'

    def preview_image(self, obj):
        return format_html('<img src="{}" width="300" height="200" style="object-fit: cover;" />', obj.image.url)
    preview_image.short_description = 'Image Preview'

    class Media:
        css = {
            'all': ('home/admin/css/thumbnail.css',)
        }


@admin.register(DetailedAbout)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('Images', {
            'fields': ('detailed_image1', 'detailed_image2', 'detailed_image3')
        }),
        ('Content', {
            'fields': ('detailed_content1', 'detailed_content2', 'detailed_content3', 'detailed_content4', 'detailed_content5')
        }),
    )



class SaintDetailInline(admin.StackedInline):
    model = SaintDetail

@admin.register(Saint)
class SaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    inlines = [SaintDetailInline]

@admin.register(SaintDetail)
class SaintDetailAdmin(admin.ModelAdmin):
    list_display = ('saint',)




@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    search_fields = ('name',)




from .models import School, Contact, Facility

class ContactInline(admin.StackedInline):
    model = Contact
    can_delete = False
    verbose_name_plural = 'Contact Information'

class FacilityInline(admin.TabularInline):
    model = School.facilities.through
    extra = 1

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'standard', 'year_established', 'num_students', 'num_teachers', 'location', 'website_link', 'is_active')
    list_filter = ('standard', 'is_active', 'year_established')
    search_fields = ('name', 'location')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ContactInline, FacilityInline]
    actions = ['make_active', 'make_inactive']
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'standard', 'year_established', 'description')
        }),
        ('Statistics', {
            'fields': ('num_students', 'num_teachers')
        }),
        ('Web Presence', {
            'fields': ('website', 'is_active')
        }),
        ('Location', {
            'fields': ('location',)
        }),
    )

    def website_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.website, obj.website)
    website_link.short_description = 'Website'

    @admin.action(description='Mark selected schools as active')
    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} schools were successfully marked as active.')

    @admin.action(description='Mark selected schools as inactive')
    def make_inactive(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} schools were successfully marked as inactive.')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_schools')
    search_fields = ('name', 'schools__name')

    def get_schools(self, obj):
        return ", ".join([school.name for school in obj.schools.all()])
    get_schools.short_description = 'Schools'



@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'featured', 'created_at')
    list_filter = ('date', 'created_at', 'featured')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)
    search_fields = ('question', 'answer')



@admin.register(Obituary)
class ObituaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date')
    list_filter = ('death_date',)
    search_fields = ('name',)

# constitution
from .models import Chapter

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

#photo album
from .models import Album, Photo

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified', 'is_visible')
    list_filter = ('is_visible', 'created', 'modified')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'created', 'modified')
    list_filter = ('album', 'created', 'modified')
    search_fields = ('title', 'description', 'album__title')
    prepopulated_fields = {'slug': ('title',)}