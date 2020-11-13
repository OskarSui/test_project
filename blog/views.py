# from django.http import Http404
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse
#
# from .forms import AddPostForm, EditPostForm
# from .models import Category, Post
#
#
# def index_page(request):
#     categories_list = Category.objects.all()
#     return render(request, 'blog/index.html', {'categories': categories_list})

# categories/slug/
# def category_details(request, slug):
#     category = Category.objects.get(slug=slug)
    # posts = Post.objects.filter(category=category)
    # posts = category.posts.all()
    # return render(request, 'blog/category_details.html', {'category': category, 'posts': posts})
    # return render(request=request, template_name='blog/category_details.html', context={'category': category, 'posts': posts})

# posts/?category='slug'
# /notebooks
# /notebooks/?disk=hdd&price_from=1000&price_to=10000
# request.GET -> {'disk': 'hdd', 'price_from': '1000', 'price_to': '10000'}
# def posts_list(request):
#     category_slug = request.GET.get('category')
#     posts = Post.objects.all()
#     if category_slug is not None:
#         posts = posts.filter(category__slug=category_slug)
#     return render(request, 'blog/posts_list.html', {'posts': posts})
#
# def post_details(request, pk):
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_details.html', {'post': post})
#



# Получение всех объектов модели: Model.objects.all()
# SELECT * FROM model;
# Получение объектов по условию: Model.objects.filter(условие)
# SELECT * FROM model WHERE условие;
# Исключение объектов из результата по условию: Model.objects.exclude(условие);
# .filter(age > 35) -> SELECT * FROM employee WHERE age > 35;
# .exclude(age > 35) -> SELECT * FROM employee WHERE NOT age > 35;
# Получение объекта по условию или id: Model.objects.get(условие)
# SELECT * FROM model WHERE условие;
# Получение первого объекта из списка: Model.objects.first() или Model.objects.filter().first()
# SELECT * FROM model [WHERE ...] [ORDER BY ...] LIMIT 1;
# Получение последнего объекта из списка: Model.objects.last() или Model.objects.filter().last()
# Создание объека: Model.objects.create()
# INSERT INTO model (поля) VALUES();
# Обновление объектов: Model.objects.update() или Model.objects.filter().update()
# UPDATE model SET ....WHERE;
# Удаление объектов: Model.objects.delete() или Model.objects.filter().delete()
# DELETE FROM model WHERE...;
# Получение количества объектов в запросе: Model.objects.count() или Model.objects.filter().count()
# SELECT COUNT(*) FROM model WHERE ...;

# get - возвращает только один объект
# order by - возвращает  QuerySet

# 9/11 2020:
# CRUD(CREATE, RETRIEVE, UPDATE, DELETE)
# GET(list, details), POST(create, update, delete)
# GET(list, details), POST(Create), PUT/PATCH(Updated), DELETE(delete)
#
# def add_post(request):
#     if request.POST:
#         post_form = AddPostForm(reques   t.POST, request.FILES)
#         if post_form.is_valid():
#             post = post_form.save()
#             return redirect(post.get_absolute_url())
#     else:
#         post_form = AddPostForm
#     return render(request, 'blog/add_post.html', {'post_form': post_form})
#
# def edit_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post_form = EditPostForm(request.POST or None, request.FILES or None, instance=post)
#     if post_form.is_valid():
#         post_form.save()
#         return redirect(post.get_absolute_url())
#     return render(request, 'blog/edit_post.html', {'post_form': post_form, 'post': post})
#
# def delete_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.POST:
#         post.delete()
#         return redirect(reverse('index-page'))
#     return render(request, 'blog/delete_post.html', {})

# Function-Based Views (FBV)
# Class-Based Views(CBV)


