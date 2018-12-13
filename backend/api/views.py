from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import base64
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "home.html"

class GalleryPageView(TemplateView):
    template_name = "gallery.html"

class AboutPageView(TemplateView):
    template_name = "contact.html"

class ProductsPageView(TemplateView):
    template_name = "ProductsInteraction.html"

class CheckoutPageView(TemplateView):
    template_name = "checkout.html"

class AddProductPage(TemplateView):
    template_name = "addproducts.html"
