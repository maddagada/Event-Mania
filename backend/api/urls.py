from django.conf.urls import include, url

#Django Rest Framework
from rest_framework import routers

from api import controllers,views
from django.views.decorators.csrf import csrf_exempt

#REST API routes
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'^session', csrf_exempt(controllers.Session.as_view())),
    url(r'^register', csrf_exempt(controllers.Register.as_view())),
    url(r'^products', csrf_exempt(controllers.Products.as_view())),
    url(r'^chairs', csrf_exempt(controllers.Chairs.as_view())),
    url(r'^lenins', csrf_exempt(controllers.Lenins.as_view())),
    url(r'^tables', csrf_exempt(controllers.Tables.as_view())),
    url(r'^lights', csrf_exempt(controllers.Lights.as_view())),
    url(r'^activateifttt', csrf_exempt(controllers.ActivateIFTTT.as_view())),
    url(r'^home', views.HomePageView.as_view()),
]
