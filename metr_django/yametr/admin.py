from django.contrib import admin
from yametr.models import Siteurl, Zapros, Zaproshistory, Pubdate, WordstatStat


class ZapHistAdmin(admin.ModelAdmin):
    list_display = ('zapros_name','zapros_value','views_value','fastrun_value','link','pub_date')
    list_filter = ['link','pub_date__pub_date']
    search_fields = ['link__link','zapros_name__zapros_name']
    date_hierarchy = 'pub_date__pub_date'
    def format_date(self, obj):
        return obj.pub_date.strftime('%d.%m.%Y')

admin.site.register(Zaproshistory,ZapHistAdmin)


class SiteurlAdmin(admin.TabularInline):
    model = Zaproshistory
    extra = 1

class UrlAdmin(admin.ModelAdmin):
    inlines = [SiteurlAdmin]
    list_display = ('link','count_sum')
    search_fields = ['link']
    

admin.site.register(Siteurl,UrlAdmin)

    
admin.site.register(Zapros)


admin.site.register(Pubdate)

class WordStAdmin(admin.ModelAdmin):
    list_display = ('zapros_name','pub_date','ws_stat_value', 'from_history')
    date_hierarchy = 'pub_date__pub_date'
    search_fields = ['zapros_name__zapros_name']
    list_filter = ['pub_date__pub_date','from_history']
    
admin.site.register(WordstatStat,WordStAdmin)