from django.db import models

# Create your models here.


class User(models.Model):
    """

    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=20, verbose_name="用户密码")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    # content = models.CharField(max_length=200)

    def __str__(self):
        """
        通过魔法方法自定义返回对象
        """
        return self.username


    class Mete:
        verbose_name_plural = "个人资料"  # 设置数据模型的别名，尽量使用复数别名；如果没有使用复数别名，系统会自动转化成复数别名-->系统会自动 + "s"
    



