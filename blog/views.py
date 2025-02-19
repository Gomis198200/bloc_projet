from django.shortcuts import get_object_or_404, render

from	django.shortcuts	import	render
from	.models	import	Post
def	post_list(request):
	posts	=	Post.objects.all().order_by('-created_at')
	return	render(request,	'blog/post_list.html',	{'posts':	posts})
def	detail_post(request,id):
	return	render(request,	'blog/posts_detail.html',{'id':id})

def posts_detail(request,id):
    post = get_object_or_404 (post,id=id)
    print('#***',40)
    print(post) 
    print('#***',40)
    return render ( request, 'blog/posts_detail.html',{'post':post})
def home(request):
    return render (request,'blog/index.html')
def blog(request):
    return render (request,'blog/blog.html')



# Create your views here.
