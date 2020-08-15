
from django.contrib import admin
from django.urls import include, path
from  .views import SignUpView,CustomLogIn
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLogIn.as_view(), name='login'),
]