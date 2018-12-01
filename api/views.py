from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostSerializer
from posts.models import Post


@api_view()
def simple(requst):
    return Response({"message": "Hello, world!"})


class PostTitles(APIView):
    def get(self, request, format=None):
        """
        Return all posts titles.
        """
        titles = [post.title for post in Post.objects.all()]
        return Response(titles)

    def post(self, request, format=None):
        """
        Create a post and return its title.
        """
        title = request.data['title']
        text = request.data['text']
        author = request.data['author']
        post = Post.objects.create(title=title, text=text, author=author)
        return Response(post.title)


class Posts(APIView):
    def get(self, request, format=None):
        """
        Return serialized posts.
        """
        serializer = PostSerializer(instance=Post.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Create a post and return it.
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
