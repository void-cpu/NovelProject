from BaseConfig.Models import BaseModels, models, DeleteBaseModels


class Author(BaseModels):
    title = models.CharField("作者名", max_length=128, unique=True)
    desc = models.CharField("简介", max_length=256, default="暂无简介信息")

    class Meta:
        verbose_name_plural = verbose_name = "作者信息"
        ordering = ["-createTime", "-endTime"]

    def __str__(self):
        return self.title


class NovelClass(BaseModels):
    title = models.CharField("小说类型名", max_length=128, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = "小说类型"
        ordering = ["-createTime", "-endTime"]

    def __str__(self):
        return self.title


class Novel(DeleteBaseModels):
    title = models.CharField("小说名", max_length=128, unique=True)
    desc = models.CharField("简介", max_length=256, default="暂无简介信息")
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="作者")
    NovelClass = models.ForeignKey(NovelClass, on_delete=models.CASCADE, verbose_name="小说类型")

    class Meta:
        verbose_name_plural = verbose_name = "小说"
        ordering = ["-createTime", "-endTime"]

    def __str__(self):
        return f"{self.title}:{self.Author.title}:{self.NovelClass.title}"


class Info(BaseModels):
    content = models.TextField("章节内容", default="暂无章节内容")
    words = models.BigIntegerField("字数", default=0)

    class Meta:
        verbose_name_plural = verbose_name = "内容"
        ordering = ["-createTime", "-endTime"]

    def __str__(self):
        return self.content[:30]


class Chapter(DeleteBaseModels):
    title = models.CharField("章节标题", max_length=128)
    Novel = models.ForeignKey(Novel, on_delete=models.CASCADE, verbose_name="小说ID")
    Info = models.ForeignKey(Info, on_delete=models.PROTECT, verbose_name="文章内容id")

    class Meta:
        verbose_name_plural = verbose_name = "章节"
        ordering = ["-createTime", "-endTime"]

    def __str__(self):
        return f"{self.Novel.title}:{self.title}:{self.Info.content[:30]}"
