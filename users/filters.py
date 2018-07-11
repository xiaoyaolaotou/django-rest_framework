import django_filters
from django.contrib.auth.models import User
from django.db.models import Q

class UsersFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(method="search_hostname") #通过哪个字段具体搜索

    def search_hostname(self,queryset,name,value):
        return queryset.filter(Q(username__icontains=value)|Q(email__icontains=value))
    class Meta:
        model = User
        fields = ['username',] #这个username就等于上面定义的按数据库中的哪个字段搜索，保持一致