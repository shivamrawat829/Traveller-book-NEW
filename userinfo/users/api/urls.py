from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PostViewset,UserViewSet
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomAuthToken

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns = [
                path('',include(router.urls)),
                path(r'api-token-auth/', CustomAuthToken.as_view())
            ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)