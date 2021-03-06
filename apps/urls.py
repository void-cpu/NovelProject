from rest_framework.routers import DefaultRouter

from apps.NovelApp.views import NovelClassViewSets, NovelViewSets, AuthorViewSets, InfoViewSets, ChapterViewSets

routers = DefaultRouter()
routers.register("Author", AuthorViewSets, basename="作者信息管理")
routers.register("NovelClass", NovelClassViewSets, basename="小说类型信息管理")
routers.register("Novel", NovelViewSets, basename="小说信息管理")
routers.register("Info", InfoViewSets, basename="内容信息管理")
routers.register("Chapter", ChapterViewSets, basename="章节信息管理")
