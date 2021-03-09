from BaseConfig.Models import UserModels, models, BaseModels


class UserModel(BaseModels):
    UserName = models.CharField(max_length=20, verbose_name='用户名', null=True)
    UserPwd = models.CharField(max_length=30, verbose_name='用户密码')
    phone = models.CharField(max_length=20, unique=True, verbose_name='用户的手机号密码')

    class Meta:
        db_table = 'uneatable'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name


class UserAnotherConfig(UserModels):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name="用户")
    UserBalance = models.DecimalField(max_length=10, max_digits=8, decimal_places=2, default=0.00, verbose_name="用户余额")

    class Meta:
        verbose_name_plural = verbose_name = "用户扩展"
