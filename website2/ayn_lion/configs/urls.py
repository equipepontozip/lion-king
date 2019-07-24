from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

urlpatterns = [
    url('', include( 'lion_site.urls' ) ),
    url('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)