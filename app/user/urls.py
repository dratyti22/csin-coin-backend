from django.urls import path
from .views import CreateUserView, AvtivateUserView, LoginUserView, LogoutUserView, ProfileUserView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name="create"),
    path("activate/<str:uid64>/<str:token>/", AvtivateUserView.as_view(), name="activate"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("logout/", LogoutUserView.as_view(), name="logout"),
    path("profile/", ProfileUserView.as_view(), name="profile"),
]
