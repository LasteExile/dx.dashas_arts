from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drawings/', include('drawings.urls')),
    path('', RedirectView.as_view(url='drawings/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
