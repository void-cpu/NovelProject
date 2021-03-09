from rest_framework.routers import DefaultRouter

from apps.NovelApp.views import NovelClassViewSets, NovelViewSets, AuthorViewSets, InfoViewSets, ChapterViewSets
from apps.user.views import UserViewSets, UserAnotherViewSet

routers = DefaultRouter()
routers.register("Author", AuthorViewSets, basename="作者信息管理")
routers.register("NovelClass", NovelClassViewSets, basename="小说类型信息管理")
routers.register("Novel", NovelViewSets, basename="小说信息管理")
routers.register("Info", InfoViewSets, basename="内容信息管理")
routers.register("Chapter", ChapterViewSets, basename="章节信息管理")
routers.register("User", UserViewSets, basename="用户管理")
routers.register("UserAnother", UserAnotherViewSet, basename="用户扩展")
