from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from inventory.forms import FormFornesedor,SignUpForm
from django.shortcuts import render_to_response
from inventory.models import Produto,Employer
from .filters import ProdutoFilter,EmployerFilter
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return	render_to_response('index.html')
	pass

def registar(request):
	if request.method=='POST':
		form=FormFornesedor(reques.POST)
		if form.is_valid():
			pass
		else:
			form=FormFornesedor()
			return	render(request,'home.html',{'form':form})
	pass

def consultar(request):
	return	HttpResponse("Rejistar entradas")
	pass

def editar():
	pass

def requisitar():
	pass

def about():
	pass
def teste(request,pk):
	produtu=Produto.objects.get(pk=pk)
	context_dict={'produtu':produtu}
	return render_to_response('produto.html',context_dict,request)
def pesquisar(request):
	"""
	produtu1=Produto.objects.all()
	context_dict1={'produtu1':produtu1}
	return render_to_response('produto.html',context_dict1,request)
	kategoria_choices = (
        ('IT','IT Equipment' ),
        ( 'OT','Office Stationary'),
        ('OTS','Others' ),
    )
	deskrisaun=models.CharField(max_length=255)
	kategoria=models.CharField(max_length=10,choices=kategoria_choices,default="IT Equipment")
	
			produtu1=Produto.objects.filter(kw=kw)
			context_dict1={'produtu1':produtu1}
			return render_to_response('produto.html',context_dict1,request)
	"""
@login_required(login_url="login")
def produto(request):
	produto_list=Produto.objects.all()
	produto_filter=ProdutoFilter(request.GET,queryset=produto_list)
	return render(request, 'produtu_list.html', {'filter': produto_filter})
	pass
	
@login_required(login_url="login")
def employerlist(request):
	employer_list=Employer.objects.all()
	#employer_filter=EmployerFilter(request.GET,queryset=employerlist)
	return render(request, 'employer_list.html',{'employer_list':employer_list})
	pass

@login_required(login_url="login")
def employersearch(request):
	employer_search=Employer.objects.all()
	employer_filter=EmployerFilter(request.GET, queryset=employer_search)
	return render(request, 'employer_search.html', {'employer_filter':employer_filter})
	pass

def handler404(request):
	response=render_to_response('404.html', {},context_instance=RequestContext(request))
	response.status_code = 404
	return (response)
	pass


"""
Sign up  code 
"""

def signup(request):
	if request.method=='POST':
		form =UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			raw_pwd=form.cleaned_data.get('password')
			user=authenticate(username=username, password=raw_pwd)
			login(request,user)
			return HttpResponseRedirect('')
	else:
		form=UserCreationForm()
		return render(request, 'signup.html', {'form': form})
		pass
"""
def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=authenticate(username=username,password=password)

		if user:
			if user.is_activate:
				login(user,request)
				return HttpResponseRedirect('login.html')
			else:
				return render_to_response('login.html', {'disabled_account': True }, request)
		else:
			return render_to_response('login.html', {'bad_details': True }, request)
	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		return render_to_response('login.html', {}, request)


	pass
	"""