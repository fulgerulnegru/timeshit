from django.forms import Form

from timeshit.helpers.ajax import *

class ajax_handler:
    def __init__(self, FormClass = None, request_type = "POST", instance = None, **kwargs):
        self.FormClass = FormClass
        self.request_type = request_type
        self.kwargs = kwargs
        self.instance = instance

    def __call__(self, f):
        def newf(request, *args, **kargs):
            if request.method == self.request_type:
                if self.FormClass is not None:
                    if self.instance:
                        form = self.FormClass(getattr(request, self.request_type), request.FILES, self.instance, **self.kwargs)
                    else:
                        form = self.FormClass(getattr(request, self.request_type), request.FILES, **self.kwargs)
                    if form.is_valid():
                        return f(request, request.user, form, *args, **kargs)
                    return ajax_response("Form is not valid", serialize_form_errors(form), code = 1)
                return f(request, (hasattr(request.user, 'get_custom_class') and [request.user.get_custom_class()] or [None])[0], *args, **kargs)
            return ajax_response("No request", code = 1)
        return newf
