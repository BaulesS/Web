from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
	Anime,
    Blog,
	Review
)

from django.views import generic
from . forms import BlogForm, ContactForm, CreateUserForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect



def signupPage(request):
	if request.user.is_authenticated:
		return redirect("main:index")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Cuenta creada para ' + user)

				return redirect('main:login')

		context = {'form':form}
		return render(request, 'main/signup.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:index")
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:index")
			else:
				messages.info(request, 'Usuatio o contraseña incorrecto')

		context = {}
		return render(request, 'main/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('main:login')




class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["Anime"] = Anime
		context["Review"] = Review
		context["Blog"] = Blog

class AnimeView(generic.CreateView):
	model = Anime
	template_name = "main/categories.html"
	paginate_by = 12
	fields="__all__"
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class AnimeDetailView(generic.DetailView):
	model = Anime
	template_name = "main/anime-details.html"

class BlogView(generic.CreateView):
	model = Blog
	template_name = "main/blog.html"
	paginate_by = 12
	fields="__all__"
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class BlogAddInfo(generic.FormView):
	template_name= "main/blogaddinfo.html"
	form_class = BlogForm
	success_url= "/"

	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por sus contribusiones a la pagina: ')
		return super().form_valid(form)

class ReviewAddInfo(generic.FormView):
	template_name="main/reviewaddinfo.html"
	form_class = ReviewForm
	success_url= "/"

	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Gracias por sus contribusiones a la pagina ')
		return super().form_valid(form)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "main/blog-details.html"

class ReviewView(generic.CreateView):
	model = Review
	template_name = "main/review.html"
	paginate_by = 12
	fields="__all__"

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class ReviewDetailView(generic.DetailView):
	model = Review
	template_name = "main/review-detail.html"


# Create your views here.
