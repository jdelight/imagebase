# Testing utility functions

def setup_view(view, request, *args, **kwargs):
    """
    Mimics the as_view() class method and makes it easier to test class based views
    Doesn't call to dispatch like the real as_view method
    """
    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view