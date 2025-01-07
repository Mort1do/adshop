from django.urls import path

from django.conf import settings                # TEST
from django.conf.urls.static import static      # TEST

from catalog import views

urlpatterns = [
    path("", views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # TEST