from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.template import loader
from .models import Post, Calc




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'dealership_site/home.html', context)


class PostListView(LoginRequiredMixin, ListView):
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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'price', 'odo', 'capacity', 'power', 'year', 'image', 'status']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
    fields = ['buy_price', 'exchange', 'transport_cost', 'vat']
    success_url = '/calculation/'


def about(request):
    return render(request, 'dealership_site/about.html', {'title': 'About'})


def calculate_costs():
    latest = Calc.objects.last()
    bp = float(latest.buy_price)
    vt = float(latest.vat)
    exh = float(latest.exchange)
    tc = float(latest.transport_cost)

    cst = bp * vt * exh + tc
    context = {
        'cst': cst
    }
    return context


# class CalculationView(LoginRequiredMixin, ListView):
#     extra_context = calculate_costs()
#     model = Calc
#     template_name = 'dealership_site/calculation.html'


def calculation(request):
    template = loader.get_template('dealership_site/calculation.html')
    calc_costs = calculate_costs()
    return HttpResponse(template.render(calc_costs, request))





