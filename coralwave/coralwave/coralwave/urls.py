from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("store.urls")),
    path('api/', include('api_shop.urls')),
    path('api-auth/', include('rest_framework.urls'))
]

# Обслуживание статических файлов в development режиме
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
