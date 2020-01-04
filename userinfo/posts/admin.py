from django.contrib import admin
# admin.site.register(Posts)

from .models import Posts,Comments
# Register your models here.
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
    list_display=['name','email','body','created','post','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')


admin.site.register(Comments,CommentAdmin)
admin.site.register(Posts,PostAdmin)