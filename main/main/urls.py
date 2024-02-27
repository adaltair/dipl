
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.project import views
from drf_spectacular.views import SpectacularAPIView ,SpectacularSwaggerView 
from main.project.views import AppRetrieveUpdateDelete, AppListView

router = DefaultRouter()
router.register(r"app", views.AppView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('apps', AppListView.as_view(), name= "Create-User-List"),
    path('app/<int:pk>/', AppRetrieveUpdateDelete.as_view(), name='app-Details')
]
