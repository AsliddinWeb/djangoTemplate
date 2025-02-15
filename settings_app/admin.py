from django.contrib import admin

# User model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

# Django unfold
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

from .models import SeoSettings, SiteSettings, SocialNetworks, TelegramBotConfig

# Unfold auth_models
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

# Model unfold register
@admin.register(SeoSettings)
class SeoSettingsAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = ('phone_number', 'email', 'address')
    search_fields = ('phone_number', 'email', 'address')

@admin.register(SocialNetworks)
class SocialNetworksAdmin(ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ('title', 'link')

@admin.register(TelegramBotConfig)
class TelegramBotConfigAdmin(ModelAdmin):
    list_display = ('username', 'admins')
    search_fields = ('username', 'admins')
