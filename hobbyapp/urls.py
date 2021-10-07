"""hobbyapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
'''from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]'''


from django.contrib import admin
from django.urls import include, path, re_path
from . import views
  
urlpatterns = [
  path("admin/", admin.site.urls),
  path("data/", include('dataretrievalapi.urls')),
  #re_path(r"^$", render_react),
  path('account/login/', views.loginView, name ='loginsubmit'),
  path('account/logout/', views.logoutView, name ='logoutSubmit'),
  path('account/create-account/', views.createAccount, name ='createAccountSubmit'),
  path("login/", views.render_react_auth, name = "login"),
  path("logout/", views.render_react_auth, name = "logout"),
  path("create-account/", views.render_react_auth, name = "createAccount"),
  path('Recipes',views.render_react, name = "recipes"),
  path('', views.render_react, name = "homePage"),
  re_path(r"^(?:.*)/?$", views.render_react),
]