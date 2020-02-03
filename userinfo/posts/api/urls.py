from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import (
    PostListView,
    PostsDetailView,
    PostsCreateView,
    PostsUpdateView,
    PostsDeleteView,
    CommentsListView,
    CommentsDetailView,
    CommentDeleteView,
    CommentUpdateView,
    CommentCreateView,
    ScrollablePosts,
    PlacesCreateView,
    PlacesListView,
    UserTokenInfo

)

urlpatterns = [
    path('user/info/<str:token>', UserTokenInfo.as_view()),
    path('posts', PostListView.as_view()),
    path('posts/<int:start>/<int:count>', ScrollablePosts.as_view()),
    path('posts/create/', PostsCreateView.as_view()),
    path('posts/<pk>', PostsDetailView.as_view()),
    path('posts/<pk>/update/', PostsUpdateView.as_view()),
    path('posts/<pk>/delete/', PostsDeleteView.as_view()),
    path('places/', PlacesListView.as_view()),
    path('places/create/', PlacesCreateView.as_view()),
    path('comments', CommentsListView.as_view()),
    path('comments/<pk>', CommentsDetailView.as_view()),
    path('comments/create/', CommentCreateView.as_view()),
    path('<pk>/comment/update/', CommentUpdateView.as_view()),
    path('<pk>/comment/delete/', CommentDeleteView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)