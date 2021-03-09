from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .Pagination import *
from .Serializers import *


class AuthorViewSets(ModelViewSet):
    """
    作者信息管理
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pagination_class = AuthorPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'title': ['icontains', 'iexact'],
        'desc': ['icontains', 'iexact']
    }


class NovelClassViewSets(ModelViewSet):
    """
    小说类型信息管理
    """
    queryset = NovelClass.objects.all()
    serializer_class = NovelClassSerializers
    pagination_class = NovelClassPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'title': ['icontains', 'iexact']
    }


class NovelViewSets(ModelViewSet):
    """
    小说信息管理
    """
    queryset = Novel.objects.all()
    serializer_class = NovelSerializers
    pagination_class = NovelPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'title': ['icontains', 'iexact'],
        "desc": ['icontains', 'iexact'],
        "Author": ["exact"],
        "NovelClass": ["exact"]
    }


class InfoViewSets(ModelViewSet):
    """
    内容信息管理
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializers
    pagination_class = InfoPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'content': ['icontains']
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(words=len(request.data['content']))
        return Response(serializer.data)


class ChapterViewSets(ModelViewSet):
    """
    章节信息管理
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializers
    pagination_class = ChapterPagination
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'title': ['icontains'],
        "Novel": ["exact"]
    }
