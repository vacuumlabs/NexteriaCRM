from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.novinky),
    url(r'^skolne/$', views.skolne),
    url(r'^skolne/(?P<id>[0-9]+)$', views.skolne_detail),
    url(r'^kredity/$', views.kredity),
    url(r'^kredity/(?P<id>[0-9]+)$', views.kredity_detail),

    url(r'^kontakty/$', views.kontakty),

    url(r'^aktivity/$', views.aktivity),
    url(r'^aktivity/(?P<id>[0-9]+)$', views.aktivita_detail, name='aktivita_detail'),
    url(r'^aktivity/(?P<id>[0-9]+)/prihlasovanie$', views.aktivita_prihlasovanie, name='aktivita_prihlasovanie'),
    url(r'^aktivity/(?P<id>[0-9]+)/odhlasovanie$', views.aktivita_odhlasovanie, name='aktivita_odhlasovanie'),

    url(r'parse_platba/$', views.parse_platba),

    url(r'^student-autocomplete/$', views.StudentAutocomplete.as_view(), name='student-autocomplete'),
    url(r'^lektor-autocomplete/$', views.LektorAutocomplete.as_view(), name='lektor-autocomplete'),

]