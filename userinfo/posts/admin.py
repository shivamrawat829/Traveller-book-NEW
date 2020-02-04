from django.contrib import admin
from .models import Posts, Comments, Places


class PostAdmin(admin.ModelAdmin):
    pass
    # list_display=['title','slug','setting_id','body','publish','created','updated','status']
    # list_filter=('title','setting_id','created','publish')
    # search_fields=('title','body')
    # raw_id_fields=('setting_id',)
    # date_hierarchy='publish'
    # ordering=['status','publish']
    # prepopulated_fields={'slug':('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'created', 'post', 'updated']
    list_filter = ('created', 'updated')
    search_fields = ('comment', 'created')


admin.site.register(Comments, CommentAdmin)
admin.site.register(Places)
admin.site.register(Posts, PostAdmin)
