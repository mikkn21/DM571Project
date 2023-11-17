
from django.shortcuts import redirect
import website.views as views

def require_login(view_func):
    """
        Redirect to login page if the user is not logged in
    """
    def _decorated(request, *args, **kwargs):
        if "member" not in request.session:
            return redirect(views.login_page)

        context = {"member": request.session["member"]}

        return view_func(request, context, *args, **kwargs)

    return _decorated

def require_super_login(view_func):
    """
        Redirect to the index page if the user is not logged in as a super
    """
    @require_login
    def _decorated(request, *args, **kwargs):
        if "is_super" not in request.session["member"] or request.session["member"]["is_super"] == False:
            return redirect(views.index)

        return view_func(request, *args, **kwargs)

    return _decorated

