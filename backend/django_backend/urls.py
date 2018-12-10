"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from django.contrib import admin
from api import urls as api_urls
from api import controllers, views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(api_urls)),
    url(r'^xss-example/', controllers.xss_example),
    url(r'^gallery/', views.GalleryPageView.as_view(), name='gallery'),
    url(r'^home/', views.HomePageView.as_view(), name='home'),
    url(r'^about/', views.AboutPageView.as_view(), name='about'),
    url(r'^productsview/', views.ProductsPageView.as_view(), name='about'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
