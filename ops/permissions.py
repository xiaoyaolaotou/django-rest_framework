from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions

class Permission(DjangoModelPermissions):
    """
    自定义get权限
    """
    def get_custom_perms(self,view,method):
       if hasattr(view,"extra_perm_map"):
           if isinstance(view.extra_perm_map,dict):
              return view.extra_perm_map.get(method,[])
        #return []

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        perms.extend(self.get_custom_perms(view,request.method))
        return request.user.has_perms(perms)







    # perms_map = {
    #     'GET': ['%(app_label)s.add_%(model_name)s'],
    #     'OPTIONS': [],
    #     'HEAD': [],
    #     'POST': ['%(app_label)s.add_%(model_name)s'],
    #     'PUT': ['%(app_label)s.change_%(model_name)s'],
    #     'PATCH': ['%(app_label)s.change_%(model_name)s'],
    #     'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    # }












    # def has_permission(self, request, view):
    #     # Workaround to ensure DjangoModelPermissions are not applied
    #     # to the root view when using DefaultRouter.
    #     if getattr(view, '_ignore_model_permissions', False):
    #         return True
    #
    #     if not request.user or (
    #        not request.user.is_authenticated and self.authenticated_users_only):
    #         return False
    #
    #     queryset = self._queryset(view)
    #     perms = self.get_required_permissions(request.method, queryset.model)
    #
    #     return request.user.has_perms(perms)

