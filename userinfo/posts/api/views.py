from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,DestroyAPIView, UpdateAPIView
from .serializers import PostsSerializers
from .serializers import CommentsSerializers
from posts.models import Posts
from posts.models import Comments

class PostListView(ListAPIView):
    queryset = Posts.objects.all()
    serializer_class =PostsSerializers

class PostsDetailView(RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class =PostsSerializers

class PostsCreateView(CreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    # permission_classes = (permissions.IsAuthenticated, )

class PostsUpdateView(UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    # permission_classes = (permissions.IsAuthenticated, )


class PostsDeleteView(DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers
    # permission_classes = (permissions.IsAuthenticated, )




class CommentsListView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class =CommentsSerializers

class CommentsDetailView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class =CommentsSerializers


class CommentCreateView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = PostsSerializers
    # permission_classes = (permissions.IsAuthenticated, )


class CommentUpdateView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    # permission_classes = (permissions.IsAuthenticated, )


class CommentDeleteView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializers
    # permission_classes = (permissions.IsAuthenticated, )
