from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.template import loader
from .models import Post, Calc, Image
from .forms import ImageForm, PostCreateForm


def home(request):
    context = {
        'posts': Post.objects.all(),
        'images': Image.objects.all(),
    }

    return render(request, 'dealership_site/home.html', context)


def calcs(request):
    context = {
        'calcs': Calc.objects.all()
    }
    return render(request, "dealership_site/all_calculations", context)


class PostListView(ListView):
    model = Post
    template_name = 'dealership_site/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 9


class UserPostListView(ListView):
    model = Post
    template_name = 'dealership_site/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content', 'price', 'odo', 'capacity', 'power', 'year', 'image', 'status']
#     success_url = '/'
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


def create_post(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            for i in files:
                Image.objects.create(post=f, image=i)
            messages.success(request, "Offer created successfully")
            return HttpResponseRedirect("/")
    else:
        form = PostCreateForm()
        imageform = ImageForm
    return render(request, "dealership_site/post_form.html", {"form": form, "imageform": imageform})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'price', 'odo', 'capacity', 'fuel', 'power', 'year', 'image', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class CalculatorView(LoginRequiredMixin, CreateView):
    model = Calc
    template_name = 'dealership_site/calculator.html'
    fields = ['title', 'buy_price', 'exchange', 'transport_cost', 'vat']
    success_url = '/calculation/'


def about(request):
    return render(request, 'dealership_site/about.html', {'title': 'About'})


def calculate_costs():
    latest = Calc.objects.last()
    bp = float(latest.buy_price)
    vt = float(latest.vat)
    exh = float(latest.exchange)
    tc = float(latest.transport_cost)

    cst = round(bp * vt * exh/100 + tc, 2)
    context = {
        'cst': cst
    }
    calculate = Calc.objects.get(title=latest.title)
    calculate.overall_price = cst
    calculate.save()
    return context


# class CalculationView(LoginRequiredMixin, ListView):
#     extra_context = calculate_costs()
#     model = Calc
#     template_name = 'dealership_site/calculation.html'


def calculation(request):
    template = loader.get_template('dealership_site/calculation.html')
    calc_costs = calculate_costs()
    return HttpResponse(template.render(calc_costs, request))


class CalcListView(LoginRequiredMixin, ListView):
    model = Calc
    template_name = 'dealership_site/all_calculations.html'
    context_object_name = 'calcs'
    ordering = ['-date_posted']
    paginate_by = 9


