# """userinfo URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/2.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include  # add this
from rest_framework import routers  # add this
from django.conf import settings
from django.conf.urls.static import static
# from TravellerBuddies import views  # add this

router = routers.DefaultRouter()  # add this
# router.register(r'posts', views.PostsView, 'post')  # add this

urlpatterns = [
    path('admin/', admin.site.urls), path('api/', include(router.urls)),  # add this
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('posts.api.urls')),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.api.urls')),

    # path(r'^$', views.post_list),
    # path(r'^tag/(?P<tag_slug>[-\w]+/$)', views.post_list,name='post_list_by_tag_name'),
    # path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
    #  views.post_detail_view,name='post_detail'),
    # path(r'^(?P<id>\d+)/share/$',views.mail_send_view)

]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
