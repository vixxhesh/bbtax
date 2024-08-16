# main urls.py
from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('userauth/', include('userauth.urls')),
    path('blog/', include('blog.urls')),
    path('toolkit/', include('tool_kit.urls')),
    path('appointments/', include('appointments.urls')),
    path('latest-posts/', views.latest_posts, name='latest_posts'),
    path('contact/', include('contact.urls')),
    path('adminp/', include('adminp.urls')),
    path('resources/', include('resource_store.urls')),
    path('implinks/', include('implinks.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
