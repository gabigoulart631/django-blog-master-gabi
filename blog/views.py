import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.template.response import TemplateResponse



from blog.models import Post

def post_show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post/detail.html', {'post': post})

# Create your views here.
def index(request):
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})

def ola(request):
    #return HttpResponse('Olá, Django')
    return render(request, 'home.html')
    posts = Post.objects.all()
    context = {'posts_list': posts }
    return render(request, 'posts.html', context) 

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'
    context_object_name = 'post'


def get_all_posts(request):
    posts = list(Post.objects.values('pk', 'body_text', 'pub_date'))
    data = {'success': True, 'posts': posts}
    json_data = json.dumps(data, indent=1, cls=DjangoJSONEncoder)
    response = HttpResponse(json_data, content_type='application/json')
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem

    return response

def get_post(request, post_id):
    post = Post.objects.filter(
            pk=post_id
        ).values(
            'pk', 'body_text', 'pub_date'
        ).first()

    data = {'success': True, 'post': post}
    status = 200
    if post is None:
        data = {'success': False, 'error': 'Post ID não existe.'}
        status=404
    response = HttpResponse(
        json.dumps(data, indent=1, cls=DjangoJSONEncoder),
        content_type="application/json",
        status=status
    )
    response['Access-Control-Allow-Origin'] = '*' # requisição de qualquer origem
    return response