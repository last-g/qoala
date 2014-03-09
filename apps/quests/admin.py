from django.contrib import admin

from . import models
# Register your models here.

class QuestAdmin(admin.ModelAdmin):
    fields = (
        'shortname',
        ('category', 'score'),
        ('provider_type', 'provider_file'),
        ('is_simple', 'is_manual'),
        'open_for', 'provider_hash',
        ('created_at', 'updated_at')
    )
    readonly_fields = ('provider_type', 'provider_hash', 'category', 'score', 'created_at', 'updated_at')
    list_display = ('shortname', 'category', 'score')
    list_filter = ('category', 'score')
    list_select_related = ('category',)
    search_fields = ('shortname',)
    filter_horizontal = ('open_for',)


class QuestVariantAdmin(admin.ModelAdmin):
    fields = (('team', 'quest'),
              'timeout',
              ('is_valid', 'try_count'),
              'html',
              ('created_at', 'updated_at')
    )
    readonly_fields = ('html', 'created_at', 'updated_at')
    list_display = ('team', 'quest')
    list_filter = ('team', 'quest')
    list_select_related = ('quest', 'teams')
    search_fields = ('quest__shortname', 'team__name')


class QuestAnswerAdmin(admin.ModelAdmin):
    fields = ('quest_variant',
              ('score', 'is_checked', 'is_success'),
              'answer',
              'result',
              ('created_at', 'updated_at')
    )
    list_display = ('quest_name', 'team', 'is_checked', 'is_success', 'answer', 'score')
    list_filter = ('is_checked', 'is_success', 'quest_variant__quest', 'quest_variant__team')
    list_editable = ('is_checked', 'is_success', 'score')
    list_select_related = ('quest_variant',)
    search_fields = ('answer', 'quest_variant__quest__shortname')
    readonly_fields = ('created_at', 'updated_at')

    def quest_name(self, obj):
        return obj.quest_variant.quest

    quest_name.short_description = 'Quest'

    def team(self, obj):
        return obj.quest_variant.team

    team.short_description = 'Team'


admin.site.register(models.Quest, QuestAdmin)
admin.site.register(models.QuestVariant, QuestVariantAdmin)
admin.site.register(models.QuestAnswer, QuestAnswerAdmin)