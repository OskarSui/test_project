from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog.class_views import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index-page'),
    path('accounts/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# 127.0.0.1:8000/posts - все посты
# 127.0.0.1:8000/posts/?category=slug - посты по определенной категории
