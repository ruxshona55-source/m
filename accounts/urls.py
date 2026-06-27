from accounts import views
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

router.register('auth',views.AuthViewSet,basename='auth')

router.register('auth-with-token',views.AuthViewSet,basename='auth-toke')

urlpatterns = [
    path('token/','auth-with-token',name='api-token'),
    path('',include(router.urls)),
]

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView, # Login → access+refresh
#     TokenRefreshView,   # Refresh → yangi access
#     TokenBlacklistView, # Logout → blacklist
# )


# urlpatterns = router.urls

# urlpatterns = [
#     path('login_jwt/', TokenObtainPairView.as_view()),
#     path('refresh/', TokenRefreshView.as_view()),
#     path('logout/', TokenBlacklistView.as_view()),
#
# ] +router.urls