from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,DestroyAPIView, UpdateAPIView
from .serializers import PostsSerializers
from .serializers import CommentsSerializers
from .serializers import PlacesSerializers
from posts.models import Posts
from posts.models import Comments
from posts.models import Places
from rest_framework.views import APIView
from rest_framework.response import Response


class DynamicViewData(APIView):
    serializer_class = PostsSerializers
    def get_queryset(self, start=None , count= None):
        if start and count is not None:
            data1 = Posts.objects.all().values()[start:count + start]
            return data1

    def get(self, request, start, count):
        if start and count:
            data = self.get_queryset(start, count)

        else:
            data = Posts.objects.all()
        return Response(data)


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


class PlacesListView(ListAPIView):
    queryset = Places.objects.all()
    serializer_class =PlacesSerializers



class PlacesCreateView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializers



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
