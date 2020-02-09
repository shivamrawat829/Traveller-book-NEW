from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api2/', include(router.urls)),  
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('posts.api.urls')),
    path('accounts/', include('allauth.urls')),
    path('info/', include('users.api.urls')),

    # path(r'^$', views.post_list),
    # path(r'^tag/(?P<tag_slug>[-\w]+/$)', views.post_list,name='post_list_by_tag_name'),
    # path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    #  views.post_detail_view,name='post_detail'),
    # path(r'^(?P<id>\d+)/share/$',views.mail_send_view)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
