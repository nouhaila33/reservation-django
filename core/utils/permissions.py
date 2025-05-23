from django.core.exceptions import PermissionDenied

def utilisateur_est_admin(user):
    return hasattr(user, 'profilutilisateur') and user.profilutilisateur.role == 'admin'

def require_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not utilisateur_est_admin(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
def utilisateur_est_admin(user):
    return hasattr(user, 'profilutilisateur') and user.profilutilisateur.role == 'admin'

def require_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not utilisateur_est_admin(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def utilisateur_est_admin(user):
    return hasattr(user, 'profilutilisateur') and user.profilutilisateur.role == 'admin'

def require_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not utilisateur_est_admin(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def utilisateur_est_admin(user):
    return hasattr(user, 'profilutilisateur') and user.profilutilisateur.role == 'admin'

def require_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not utilisateur_est_admin(request.user):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
