# TODO: More synergy between django's "official" class-based view interface

class View(object):
    """ Defines an object which django can make use of as a view. """
    
    def __init__(self, **kwargs):
        for kwarg in kwargs:
            setattr(self, kwarg, kwargs[kwarg])

    def __call__(self, *args, **kwargs):
        if hasattr(self, 'requested'):
            return self.requested(*args, **kwargs)

    @classmethod
    def as_view(cls, *args, **kwargs):
        """ A factory that attempts to help simulate django 1.3's silly as_view
        interface for object-oriented / class-based views. It simply acts as
        a factory that wraps to the view class's constructor in order to
        instantiate a view object.

        """

        return cls(*args, **kwargs)

class TemplateView(View):
    """ A simple view that abstracts template rendering. """

    template_name = None

    def __call__(self, request, *args, **kwargs):
        """ Performs abstraction of template rendering. """

        if self.template_name is None:
            error = 'The {0} class derives from TemplateView, but does '       \
                    'not implement the required attribute: template_name'      \
                    .format(self.__class__.__name__)

            raise NotImplementedError(error)

        context_data = super(TemplateView, self).__call__(request, *args, **kwargs)

        from django.shortcuts import render_to_response
        from django.template import RequestContext

        return render_to_response(self.template_name, context_data,
                                 context_instance=RequestContext(request))

class Home(TemplateView):
    """ A simple view which is used in order to render a homepage. This doubles
    as an example view to help describe the use of the View object.

    """

    def requested(self, request):
        """ renders home.html """

        return {}
