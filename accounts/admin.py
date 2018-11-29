from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )

    search_fields = ['email', 'first_name', 'last_name']
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
