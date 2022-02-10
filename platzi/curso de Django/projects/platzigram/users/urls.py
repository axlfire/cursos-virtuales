from users import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns=[
    path(
        route='logout/',
        view=views.logoutView.as_view(), name='logout'
    ),
    path(
        route='login/',
        view=views.loginView.as_view(),
        name='login'
    ),
    path(
        route='signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update'
    ),
    path(
    route='<str:username>/',
    view=views.UserDetailView.as_view(),
    name='detail'
    ),
]
