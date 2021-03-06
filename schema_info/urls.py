from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schema_info.views import SchemaViewSet
from rest_framework.routers import DefaultRouter
from schema_info.views import login_test, add_request

router = DefaultRouter()
router.register(r'mysql_schema', SchemaViewSet, basename='mysql_schema')


urlpatterns = [
    *router.urls,
    path('user/djlogin/loginAPI/', login_test),
    path('add/', add_request)
]
