from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Practice
from django.utils import timezone
from .forms import CreatePostForm

# Create your views here.


def index(request):
    blogs = Blog.objects
    practices = Practice.objects
    return render(request, 'blog/index.html',{'blogs':blogs,'practices':practices})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog_detail':blog_detail})

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            blog=form.save(commit=False)
            #commit=False는 아직 db상에 저장되지 않는다는 뜻
            blog.pub_date = timezone.datetime.now()
            blog.save()
            return redirect('/detail/' + str(blog.id))
        # print(request.POST)
        # #Post방식 : 입력이 들어올 때
        # blog = Blog()
        # blog.title = request.POST['title']
        # #ctrl + d  같은 단어 동시수정 가능
        # blog.body = request.POST['body']
        # blog.pub_date = timezone.datetime.now()
        # blog.save()
        # return redirect('/detail/' + str(blog.id))
    else:
        form = CreatePostForm()
        return render(request,'blog/create.html',{'form':form})
        #페이지만 바꿀 때
        # return render(request, 'create.html')

# def create_blog(request):
    # blog = Blog()
    # blog.title = request.GET['title']
    # blog.body = request.GET['body']
    # blog.pub_date = timezone.datetime.now()
    # blog.save()
    # return redirect('/detail/' + str(blog.id))

# ctrl + / => 주석처리

def update(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        form = CreatePostForm(request.POST, instance=blog)
        if form .is_valid():
            blog = form.save()
            return redirect('blog:information')
            # path의 name을 따라감
    else:
        form = CreatePostForm(instance=blog)
        return render(request, 'blog/create.html',{'form':form})

def delete(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect('blog:information')

def information(request):
    blogs = Blog.objects
    return render(request, 'blog/information.html',{'blogs':blogs})

