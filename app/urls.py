from app.apps.api import router as voting_router
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI(
    title="API de Votação",
    version="1.0",
    description="API para cálculo de votos"
)

api.add_router("/voting/", voting_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', api.urls),
]