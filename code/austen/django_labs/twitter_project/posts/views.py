from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Twitter, Tweet

class TweetListView(ListView):
    model = Twitter
    template_name = 'home_page.html'

class TweetDetailView(DetailView):
    model = Twitter
    template_name = 'post_detail.html'

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Twitter
    template_name = 'post_new_post.html'
    fields = ['title', 'body', 'my_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Twitter
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home_page')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author


class FollowView(View):
    def get(self, request, *args, **kwargs):
        content = {}
        if 'pk' in self.kwargs:
            user = request.user
            newuserobj = User.objects.get(id=self.kwargs['pk'])
            newuserobj.follower.add(user)
            newuserobj.save()
            return redirect(reverse('home_page'))
        content['users'] = User.objects.all().exclude(id=request.user.id)
        return render_to_response('home_page.html', content, {})
