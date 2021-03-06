from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.documentation import include_docs_urls

from NovelProject.settings import STATIC_ROOT
from apps.urls import routers

schema_view = get_schema_view(
    openapi.Info(
        title="Django-Rest-Framework API",  # 接口文档名称
        default_version='v4',  # 接口文档版本
        contact=openapi.Contact(email="3441292862@qq.com"),  # 开发者邮箱地址
        license=openapi.License(name="MIT License"),  # 许可证
    ),
    public=False,  # 是否公开
    permission_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(routers.urls)),
    path('doc_01/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('doc_02/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('doc_03/', include_docs_urls(title="接口文档", authentication_classes=[], permission_classes=[])),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
