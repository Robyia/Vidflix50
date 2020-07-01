"""vidflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from django.contrib.auth import views as auth_views
from paygate.views import paymentMode

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cource/<slug>/', views.lessonList, name='lessonName'),
    path('lesson/<slug>/', views.courseVideos, name='courseName'),
    path('login', views.loginView.as_view(), name="login"),
    path('signup', views.signupView.as_view(), name="signup"),
    path('language/<int:pk>', views.languagefilter, name = "language"),
    path('category/<int:pk>', views.categoryfilter, name = "category"),
    path('logout/', views.logoutView.as_view(), name='logout'),
    path('showprice/', views.showprice),
    path('showpaytm/', paymentMode, name='paytm'),
    path('showcontact', views.showcontact, name='contact'),
    path('showabout', views.showabout, name='about'),
    path('showterms', views.showterms, name='terms and conditions'),
    path('search', views.search, name='search'),
    path('mostwatched', views.mostwatched, name='mostwatched'),
    path('single', views.single, name='single'),
    path('showpassword', views.showpassword),
    path('showactivate', views.showactivate, name='activate'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_done.html'),
         name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),

    #path('membership/', include('membership.urls', namespace='membership')),
    #path('course/', include('course.urls', namespace='course')),
    #path('accounts/', include('allauth.urls')),
    #path('membershippayment/',views.membershippayment, name='membershippayment')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
