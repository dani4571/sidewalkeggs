from django.urls import include, path, re_path

from . import views

from rest_framework_nested import routers

from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

app_name = 'unpolitical'
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', views.IndexView.as_view(), name='index'),
]

