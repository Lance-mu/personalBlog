from django.contrib import admin

# Register your models here.

from .models import User

# admin.site.register(User)  # 绑定方法1
# 等同于下面装饰器：admin.site.regiseter(User, UserAdmin)

# username:lenovo  password:admin
# admin.ModelAdmin --> 模型管理类,只在后台显示
# admin管理后台绑定模型数据，通过admin.py文件进行后台内容管理；


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 设置列表显示字段, 列表里面的字段是根据模型里面定义的模型字段
    list_display = ["id", "username", "password", "create_time"]

    list_max_show_all = 10  # 页面最大显示数据
    list_per_page = 10  # 页面显示数据

    # 排序需要接受的是一个严格的元组对象：正序，是前面使用+、或者不适用，倒序使用-
    ordering = ("-id",)



