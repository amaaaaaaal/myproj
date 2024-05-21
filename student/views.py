from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponseBadRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


def index (request):
    posts = Post.objects.all()
    return render(request, 'student/index.html', context={"posts": posts})



class PostListView(ListView):
    model = Post
    template_name = 'student/post_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(slug__isnull=False)


def post_detail(request, model_name, pk):
    model_map = {
        'post': Post,
        'reaction': Reaction,
        'recommandation': Recommandation,
        'transport': Transport,
        'logement': Logement,
        'stage': Stage,
        'event': Event,
        'evenclub': EvenClub,
        'evensocial': EvenSocial,
    }
    ModelClass = model_map.get(model_name.lower())
    if not ModelClass:
        raise ValueError(f"Invalid model name: {model_name}")  
    obj = get_object_or_404(ModelClass, pk=pk) 
    return render(request, 'student/post_detail.html', {'model_name': model_name, 'object': obj})


class PostDetailView(DetailView):
    model = Post
    template_name = 'student/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comment_set.all()
        context['likes'] = post.like_set.all()
        context['form'] = YourCommentForm()  
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ['image', 'slug', 'type', 'date']
    template_name = 'student/post_create.html'
    success_url = reverse_lazy('post_list')  

    def form_valid(self, form):
        form.instance.User = self.request.user
        return super().form_valid(form)
    


def stage_form(request):
    if request.method == 'POST':
        form = StageForm(request.POST)
        if form.is_valid():
            stage_form = form.save(commit=False)
            stage_form.save()
            return redirect('post_list')
    else:
        form = StageForm()
    return render(request, 'student/stage_form.html', {'form': form})



def transport_form(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  
    else:
        form = TransportForm()
    return render(request, 'transport_form.html', {'form': form})

def logement_form(request):
    if request.method == 'POST':
        form = LogementForm(request.POST)
        if form.is_valid():
            logement = form.save(commit=False)
            logement.save()
            return redirect('post_list')  
    else:
        form = LogementForm()
    return render(request, 'student/logement_form.html', {'form': form})



def stage_list(request):
    stages = Stage.objects.all()
    return render(request, 'student/stage_list.html', {'object_list': stages})


def transport_list(request):
    transports = Transport.objects.all()
    return render(request, 'student/transport_list.html', {'object_list': transports})



class PostUpdateView(UpdateView):
    model = Post
    fields = ['image', 'slug', 'type', 'date']
    template_name = 'student/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'student/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


class ReactionCreateView(CreateView):
    model = Reaction
    fields = ['like', 'comment']
    template_name = 'student/reaction_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

class EventListView(ListView):
    model = Event
    template_name = 'student/event_list.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'student/event_detail.html'

class StageListView(ListView):
    model = Stage
    template_name = 'student/stage_list.html'

class StageDetailView(DetailView):
    model = Stage
    template_name = 'student/stage_detail.html'

class LogementListView(ListView):
    model = Logement
    template_name = 'student/logement_list.html'

class LogementDetailView(DetailView):
    model = Logement
    template_name = 'student/logement_detail.html'

class TransportListView(ListView):
    model = Transport
    template_name = 'student/transport_list.html'

class TransportDetailView(DetailView):
    model = Transport
    template_name = 'student/transport_detail.html'




class LogementListView(ListView):
    model = Logement
    template_name = 'student/logement_list.html'
    context_object_name = 'logements'
    paginate_by = 10

    def get_queryset(self):
        return Logement.objects.all()
