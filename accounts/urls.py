from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import TokenObtainPairView, TokenRefreshView, SignupAPIView, UserViewSet

app_name = 'accounts'

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = []

urlpatterns += [
    path('api/', include(router.urls)),
    path("api/signup/", SignupAPIView.as_view(), name="signup"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_view"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]