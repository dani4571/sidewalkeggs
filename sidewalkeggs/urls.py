"""sidewalkeggs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.utils.translation import ugettext_lazy
from rest_framework_nested import routers

from . import views
from authentication.views import AccountViewSet, LoginView, LogoutView
from posts.views import AccountPostsViewSet, PostViewSet

admin.site.site_title = ugettext_lazy('Sidewalkeggs site admin')
admin.site.site_header = ugettext_lazy('Sidewalkeggs administration')
admin.site.index_title = ugettext_lazy('Sidewalkeggs administration')

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = [
    path('unpolitical/', include('unpolitical.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(accounts_router.urls)),
    path('api/v1/auth/login', LoginView.as_view(), name='login'),
    path('api/v1/auth/logout', LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
]
