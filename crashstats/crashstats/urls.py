# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to
from django.conf import settings

from . import views


urlpatterns = patterns('',
    url(r'^products/(?P<product>\w+)/?$', views.products,
        name='crashstats.products'),
    url(r'^products/(?P<product>\w+)/versions/(?P<versions>[;\w\.()]+)/?$',
        views.products,
        name='crashstats.products'),
    url(r'^topcrasher/byversion/(?P<product>\w+)/?$',
        views.topcrasher,
        name='crashstats.topcrasher'),
    url(r'^topcrasher/byversion/(?P<product>\w+)/(?P<versions>[;\w\.()]+)/?$',
        views.topcrasher,
        name='crashstats.topcrasher'),
    url(r'^topcrasher/byversion/(?P<product>\w+)/(?P<versions>[;\w\.()]+)/(?P<days>\d+)$',
        views.topcrasher,
        name='crashstats.topcrasher'),
    url(r'^topcrasher/byversion/(?P<product>\w+)/(?P<versions>[;\w\.()]+)/(?P<days>\d+)/(?P<crash_type>\w+)$',
        views.topcrasher,
        name='crashstats.topcrasher'),
    url(r'^topcrasher/byos/(?P<product>\w+)/(?P<versions>[;\w\.()]+)/(?P<os_name>[\w\s]+)/(?P<days>\d+)/(?P<crash_type>\w+)$',
        views.topcrasher,
        name='crashstats.topcrasher'),
    url(r'^daily$', views.daily,
        name='crashstats.daily'),
    url(r'^products/(?P<product>\w+)/builds$',
        views.builds,
        name='crashstats.builds'),
    # note the deliberate omission of the ';' despite calling the regex variable 'versionS'
    url(r'^products/(?P<product>\w+)/versions/(?P<versions>[\w\.()]+)/builds$',
        views.builds,
        name='crashstats.builds'),
    url(r'^hangreport/byversion/(?P<product>\w+)/?$',
        views.hangreport,
        name='crashstats.hangreport'),
    url(r'^hangreport/byversion/(?P<product>\w+)/(?P<versions>[;\w\.()]+)$',
        views.hangreport,
        name='crashstats.hangreport'),
    url(r'^products/(?P<product>\w+)/topchangers$', views.topchangers,
        name='crashstats.topchangers'),
    url(r'^products/(?P<product>\w+)/versions/(?P<versions>[\w\.()]+)/topchangers$',
        views.topchangers,
        name='crashstats.topchangers'),
    url(r'^products/(?P<product>\w+)/versions/(?P<versions>[\w\.()]+)/topchangers/(?P<duration>\d+)/?$',
        views.topchangers,
        name='crashstats.topchangers'),
    url(r'^report/list$', views.report_list,
        name='crashstats.report_list'),
    url(r'^report/index/(?P<crash_id>.*)$', views.report_index,
        name='crashstats.report_index'),
    url(r'^query/?$', views.query,
        name='crashstats.query'),
    url(r'^query/query?$', redirect_to, {'url': '/query/?',
                                         'permanent': False,
                                         'query_string': True}),
    url(r'^buginfo/bug', views.buginfo,
        name='crashstats.buginfo'),
    url(r'^topcrasher/plot_signature/(?P<product>\w+)/(?P<versions>[;\w\.()]+)/(?P<start_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/(?P<end_date>[0-9]{4}-[0-9]{2}-[0-9]{2})/(?P<signature>.*)',
        views.plot_signature,
        name='crashstats.plot_signature'),
    url(r'^signature_summary/json_data$', views.signature_summary,
        name='crashstats.signature_summary'),
    # if we do a permanent redirect, the browser will "cache" the redirect and
    # it will make it very hard to ever change the DEFAULT_PRODUCT
    url(r'^$', redirect_to, {'url': '/products/%s' % settings.DEFAULT_PRODUCT,
                             'permanent': False}),
)
