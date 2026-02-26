from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from groups.views import StudyGroupViewSet

router = DefaultRouter()
router.register('groups', StudyGroupViewSet, basename='groups')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),   # /api/register/
    path('api/', include(router.urls)),    # /api/groups/
]