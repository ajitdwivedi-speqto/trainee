
from django.urls import path,include
from ecom import views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')


urlpatterns = [
    path('', views.product_list, name='home'),
    path('add/', views.add_product, name='add_product'),
    path('edit<int:id>/', views.edit_product, name='edit_product'),
    path('buy<int:id>/', views.buy_product, name='buy_product'),

    # # ! API endpoints
    # path('api/products/', views.product_api, name='api_product_list'),
    # path('api/products<int:id>/', views.product_detail_api, name='api_product_detail'),
    path('api/', include(router.urls)),  # API endpoints
]


