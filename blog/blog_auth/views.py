from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import CreateView, ListView
from .forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from blog_posts.models import Author, Post

User = get_user_model()


class Login(LoginView):
    template_name = 'blog_auth/login_page.html'
    success_url = reverse_lazy('posts_list')


class Register(CreateView):
    template_name = 'blog_auth/register_page.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        return super().form_valid(form)


class ProfileDetailView(generic.DetailView):
    model = Author
    template_name = 'blog_auth/profile_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        context['page_user'] = page_user
        user = self.request.user
        if user.is_authenticated:
            context['is_following'] = user in page_user.followers.all()
            context['followers'] = page_user.followers.count()
            context['following'] = user.following.count()
            context['latest_posts'] = Post.objects.filter(user=page_user).order_by('-post_date')[:4]
        return context


@login_required
def subscribe(request, pk):
    author_to_follow = get_object_or_404(Author, pk=pk)
    user = request.user
    if user == author_to_follow:
        return redirect('profile', pk=pk)
    user.following.add(author_to_follow)
    author_to_follow.followers.add(user)

    return redirect('profile', pk=pk)


@login_required
def unsubscribe(request, pk):
    author_to_unfollow = get_object_or_404(Author, pk=pk)
    user = request.user
    user.following.remove(author_to_unfollow)
    author_to_unfollow.followers.remove(user)

    return redirect('profile', pk=pk)


class ProfileEditView(LoginRequiredMixin, CreateView):
    model = User
    template_name = "blog_auth/edit_page.html"
    form_class = UserUpdateForm

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserUpdateForm(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect(reverse('profile', args=[pk]))
        return render(request, self.template_name, {'form': form})


def logout_page(request):
    logout(request)
    return redirect('posts_list')


class FollowingListView(ListView):
    model = Author
    template_name = 'blog_auth/following_list.html'
    context_object_name = 'following'

    def get_queryset(self):
        user = get_object_or_404(Author, pk=self.kwargs['pk'])
        return user.following.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Author, pk=self.kwargs['pk'])
        context['page_user'] = user
        return context


class FollowersListView(ListView):
    model = Author
    template_name = 'blog_auth/followers_list.html'
    context_object_name = 'followers'

    def get_queryset(self):
        user = get_object_or_404(Author, pk=self.kwargs['pk'])
        return user.followers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(Author, pk=self.kwargs['pk'])
        context['page_user'] = user
        return context
