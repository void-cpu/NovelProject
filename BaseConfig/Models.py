from django.db import models


class BaseModels(models.Model):
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    endTime = models.DateTimeField(auto_now=True, verbose_name="最后编辑时间")

    class Meta:
        abstract = True


class DeleteBaseModels(BaseModels):
    is_delete = models.BooleanField(default=False, verbose_name="删除标记")

    class Meta:
        abstract = True
