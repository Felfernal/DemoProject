from django.urls import path
from . import views

app_name = 'shopping_app'

urlpatterns = [

    path('', views.allProdCateg, name='allProdCateg'),
    path('<slug:c_slug>/', views.allProdCateg, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetail, name='product_details')
]