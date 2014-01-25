from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import resolve

from ft.utils import setup_view

from core.views import DashboardView

class DashboardViewTest(TestCase):

    def test_root_url_resolves_to_dashboard_view(self):
        view = resolve('/')
        self.assertEqual(view.func.func_name, DashboardView.__name__)

    def test_root_url_returns_dashboard_template(self):
        dashboard_request = RequestFactory().get('/')
        dashboard_view = DashboardView()
        view = setup_view(dashboard_view, dashboard_request)
        template_names = view.get_template_names()
        self.assertEqual(template_names, ['dashboard.html'])

    def test_dashboard_view_renders_successfully(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_view_template_extends_base(self):
        client = Client()
        response = client.get('/')
        self.assertTemplateUsed(response, 'base.html')
