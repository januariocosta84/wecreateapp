from django.contrib.auth.models import User
from inventory.models import Produto,Employer
import django_filters


class ProdutoFilter(django_filters.FilterSet):
	"""docstring for UserFilter"""
	class Meta:
		model=Produto
		fields=['kategoria',]

class EmployerFilter(django_filters.FilterSet):
	"""docstring for ClassName"""
	class Meta:
		model=Employer
		fields=['naran',]


		