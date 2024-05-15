from django.contrib import admin
from django.urls import path, include
from caps.router import router as cap_router
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include(cap_router.urls)),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
