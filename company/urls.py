from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import urls
from django.urls import reverse_lazy

app_name = 'company'

urlpatterns = [
    path('', views.all_companies, name='all_companies'),
    path('update', views.update_companies, name='update_companies'),
    # path('login/', views.custom_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_reset/", auth_views.PasswordResetView.as_view(
            success_url = reverse_lazy("company:password_reset_done")),
         name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            success_url = reverse_lazy("company:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("profile/", views.view_profile, name="profile"),
    path("good", views.good_companies, name="good_componies"),
    path("bad", views.bad_companies, name="bad_componies"),

]