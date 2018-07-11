from django.conf.urls import url,include
from django.contrib import admin
from idcs import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^idclist/$', views.IdcList.as_view()),
    url(r'^idclist/', views.IdcDetail.as_view()),
]


urlpatterns = [

    url(r'^idclist/$', views.IdcList_v4.as_view()),
    url(r'^idclist/(?P<id>(\d+))/$', views.IdcDetail.as_view()),
]


urlpatterns = [

    url(r'^idclist/$', views.IdcList_v5.as_view()),
    url(r'^idclist/(?P<id>(\d+))/$', views.IdcDetail_v5.as_view()),
]

########################
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from idcs.views import IdcListViewset
from users.views import UserViewset
from cabinet.views import CabinetViewset
from manufacturer.views import ManufacturerViewset,ProductModelViewset

from servers.views import ServerAutoReportViewset,NetworkDeviceViewset,IPViewset,ServerViewset

route = DefaultRouter()
route.register("idcs",IdcListViewset,base_name="idcs")
route.register("users",UserViewset,base_name="users")
route.register("cabinet",CabinetViewset,base_name="cabinet")
route.register("manufacturer",ManufacturerViewset,base_name="manufacturer")
route.register("productModel",ProductModelViewset,base_name="productModel")
route.register("server",ServerAutoReportViewset,base_name="server")
route.register("network",NetworkDeviceViewset,base_name="network")
route.register("ip",IPViewset,base_name="ip")
route.register("servers",ServerViewset,base_name="servers")


urlpatterns = [

    url(r'^',include(route.urls)),
    url(r'^api-auth/',include("rest_framework.urls",namespace="rest_framework")),
    url(r'^docs/',include_docs_urls("运维平台接口API文档"))
]