from django.urls import path, include

from .views import HomeView, CategoryViewSet, FavoriteViewSet, add_to_favorite
from rest_framework import routers

router_1 = routers.SimpleRouter()
router_1.register(r'category', CategoryViewSet)
router_2 = routers.SimpleRouter()
router_2.register(r'favorites', FavoriteViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('api/v1/', include(router_1.urls)),
    path('api/v1/', include(router_2.urls)),
    path('api/v1/', add_to_favorite),
]