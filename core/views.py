from django.contrib.auth.mixins import LoginRequireMixin
from django.views.generic.base import TempalateView

class IndexTemplateView(LoginRequireMixin, TemplateView):

	def get_template_names(self):
		template_name = "index.htnl"
		return template_name