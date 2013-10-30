from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from haystack.views import FacetedSearchView
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sqs = SearchQuerySet().facet('model_type').facet('sector').facet('sub_sector')

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'admin.views.site.home', name='home'),
    # url(r'^pursuite/', include('pursuite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('analytics.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^account/profile/', 'account.views.profile'),
    url(r'^account/', include('allauth.urls')),
    url(r'^search/$', FacetedSearchView(
        form_class=FacetedSearchForm,
        template='search-result.html',
        searchqueryset=sqs,
        results_per_page=10,
        ), name='haystack_search'),
    url(
        r'^occupational-standards/$',
        'admin.views.occupational_standard.view_occupational_standards',
        name="occupational_standards"
    ),
    url(
        r'^occupational-standard/(?P<code>[A-z]{3}/[NO]\d{4})/$',
        'admin.views.occupational_standard.view_occupational_standard',
        name="occupational_standard"
    ),
    url(
        r'^occupational-standard/(?P<code>[A-z]{3}/[NO]\d{4})/'
            '(?P<version>\d+\.\d+)/$',
        'admin.views.occupational_standard.view_occupational_standard',
        name="occupational_standard"
    ),
    url(
        r'^qualification-packs/$',
        'admin.views.qualification_pack.view_qualification_packs',
        name="qualification_packs"
    ),
    url(
        r'^qualification-pack/(?P<code>[A-z]{3}/Q\d{4})/$',
        'admin.views.qualification_pack.view_qualification_pack',
        name="qualification_pack"
    ),
    url(
        r'^qualification-pack/(?P<code>[A-z]{3}/Q\d{4})/(?P<version>\d+\.\d+)/\
            $', 'admin.views.qualification_pack.view_qualification_pack',
        name="qualification_pack"
    ),
    url(
        r'^wfmis-json/$', 'admin.views.common.wfmis_json', name="wfmis_json"
    ),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
