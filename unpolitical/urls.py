from django.urls import include, path, re_path

from . import views

from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

app_name = 'unpolitical'
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/login', LoginView.as_view(), name='login'),
    path('api/v1/auth/logout', LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
]

