# Импортируем необходимые модули и функции Django
from django.contrib import admin
from django.urls import path, include

# Определяем переменную urlpatterns - список URL-маршрутов приложения
urlpatterns = [
    # URL-маршрут для административной панели Django
    path('admin/', admin.site.urls),

    # URL-маршрут, который включает URL-маршруты из приложения '.urls'
    path('', include('apps.youtube.urls'))
]
