from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, CreateView
from .forms import PostForm
from .models import Post
from blog_comments.forms import CommentForm
from blog_comments.models import Comment
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class BlogListView(ListView):
    model = Post
    paginate_by = 4
    context_object_name = 'posts'
    template_name = 'blog_posts/post_list.html'


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user in post.liked_by.all():
        post.liked_by.remove(user)
    else:
        post.liked_by.add(user)
    if user in post.disliked_by.all():
        post.disliked_by.remove(user)

    post.save()
    return redirect('post_detail', pk=pk)


def dislike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user in post.disliked_by.all():
        post.disliked_by.remove(user)
    else:
        post.disliked_by.add(user)
    if user in post.liked_by.all():
        post.liked_by.remove(user)

    post.save()
    return redirect('post_detail', pk=pk)


class BlogDetailView(DetailView, FormMixin):
    model = Post
    template_name = 'blog_posts/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.comments.filter(parent=None)
        context['comments'] = comments
        context['comment_form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.post = self.object
        parent_id = self.request.POST.get('parent_id')
        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            comment.parent = parent_comment
        comment.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return self.request.path


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog_posts/post_add.html'
    form_class = PostForm
    success_url = reverse_lazy('posts_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserReactionListView(ListView):
    model = User
    template_name = 'blog_posts/reacted_users.html'
    context_object_name = 'reacted_users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        reacted_users = post.liked_by.all() | post.disliked_by.all()
        context['post'] = post
        context['post_url'] = reverse('post_detail', args=[post.id])
        return context

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)
        reacted_users = post.liked_by.all() | post.disliked_by.all()
        return reacted_users


class SearchResultsView(ListView):
    template_name = 'blog_posts/search_posts.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        results = {'posts': [], 'users': []}

        if query:
            results['posts'] = Post.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            results['users'] = User.objects.filter(Q(username__icontains=query))

        return results
