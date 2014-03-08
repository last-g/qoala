from django.contrib import admin

from . import models
# Register your models here.

class QuestAdmin(admin.ModelAdmin):
    fields = (
        'shortname',
        ('provider_type', 'provider_file'),
        ('is_simple', 'is_manual')
    )
    list_display = ('shortname', 'category', 'score')
    list_filter = ('category', 'score')

class QuestVariantAdmin(admin.ModelAdmin):
    list_display = ('team', 'quest')
    list_filter = ('team', 'quest')

class QuestAnswerAdmin(admin.ModelAdmin):
    list_display = ('quest_name', 'team', 'is_checked', 'is_success')
    list_filter = ('quest_variant__quest', 'quest_variant__team', 'is_checked', 'is_success')
    def quest_name(self, obj):
        return obj.quest_variant.quest
    quest_name.short_description = 'Quest'

    def team(self, obj):
        return obj.quest_variant.team
    team.short_description = 'Team'

admin.site.register(models.Quest, QuestAdmin)
admin.site.register(models.QuestVariant, QuestVariantAdmin)
admin.site.register(models.QuestAnswer, QuestAnswerAdmin)