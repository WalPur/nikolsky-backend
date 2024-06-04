from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Post
from .serializers import PostSerializer


class PostViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Post.objects.all().order_by("-date_created")
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        article = self.get_object()
        article.views += 1
        article.save()
        return super().retrieve(request, *args, **kwargs)
