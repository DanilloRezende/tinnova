from app.apps.api import router as teste_tinnova
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI(
    title="Teste Tinnova",
    version="1.0",
)

api.add_router("/teste_tinnova/", teste_tinnova)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', api.urls),
]