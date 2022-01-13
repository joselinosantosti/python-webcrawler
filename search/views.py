from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Urls

class IndexView(TemplateView):
	template_name = 'index.html'

class SearchPagesView(ListView):
	model = Urls
	template_name = 'pages.html'
	paginate_by = 10
	context_object_name = 'pages'
	
	def get_queryset(self):
		search = self.request.GET.get('busca')
		if search:
			qs = super().get_queryset()
			qs = qs.order_by('url').filter(url__icontains=search)
			return qs
		else:
			print('Nenhum resultado encontrado')
