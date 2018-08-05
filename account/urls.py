from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account import views

urlpatterns = [
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^sign_up_success/$', views.sign_up_success, name='sign_up_success'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]+-[0-9A-Za-z]+)/$',
        views.activate, name='activate'),
    url(r'^login/$', auth_views.login, {'template_name': 'account/sign_in.html'}, name='sign_in'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'home.html'}, name='sign_out'),
]