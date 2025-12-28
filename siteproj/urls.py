"""
URL configuration for siteproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve as static_serve
from django.views.generic.base import RedirectView
from organic_theme.views import home as organic_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin', RedirectView.as_view(url='/admin/', permanent=False)),
    path('', include('organic_theme.urls')),
]

# Development-only static serving for existing folders referenced by index.html
if settings.DEBUG:
	urlpatterns += static('/css/', document_root=settings.BASE_DIR / 'css')
	urlpatterns += static('/js/', document_root=settings.BASE_DIR / 'js')
	urlpatterns += static('/images/', document_root=settings.BASE_DIR / 'images')
	urlpatterns += [
		path('style.css', static_serve, {'document_root': settings.BASE_DIR, 'path': 'style.css'}),
	]

# Catch-all: send non-static, non-admin paths to homepage to avoid 404s on UI links
urlpatterns += [
	# Exclude admin (with or without trailing slash) and asset prefixes
	re_path(r'^(?!(?:admin(?:/|$)|css/|js/|images/|style\.css$)).+$', organic_home),
]
