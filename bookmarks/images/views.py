from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == "POST":
        # 表单被提交
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            # 表单验证通过
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # 将当前用户附加到数据对象上
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')
            # 重定向到新创建的数据对象的详情视图
            return redirect(new_item.get_absolute_url())
    else:
        # 根据GET请求传入的参数建立表单对象
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})