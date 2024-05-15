from django.urls import path
from rest_framework import routers
from retail.apps import RetailConfig
from retail.views import TraderDetailUpdateDeleteView, TraderListCreateView, NetworkViewSet, ProductViewSet

app_name = RetailConfig.name

router = routers.DefaultRouter()
router.register(r'network', NetworkViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    #  Модель звена торговой сети
    path('trader/', TraderListCreateView.as_view(), name='trader_list_create'),
    path('trader/<int:pk>/', TraderDetailUpdateDeleteView.as_view(), name='trader_detail_update_delete'),
]
urlpatterns += router.urls
