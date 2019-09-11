from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)  # 后台显示的字段
    list_filter = ('status', 'created', 'publish', 'author',)  # 后台管理右侧边栏用于筛选结果
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}  # slug字段会根据标题自动填充
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'  # 在搜索栏的下方，出现了时间层级导航条
    ordering = ('status', 'publish',)  # 默认通过Status和Publish字段进行排序