from django.urls import path, include
from rest_framework.routers import DefaultRouter
from schema_info.views import SchemaViewSet, call_add, query_result
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mysql_schema', SchemaViewSet, basename='mysql_schema')


urlpatterns = [
    *router.urls,
    path('add/', call_add),
    path('query_result/', query_result)
]
