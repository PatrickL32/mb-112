from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_view = "pages/home.html"

class AboutPageView( TemplateView):
    template_name = "pages/about.html"