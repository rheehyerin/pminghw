from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'posting_hw/post_list.html',{'post_list':post_list})

def post_detail(request, pk):
    post_ob = Post.objects.get(pk=pk)
    comments = post_ob.comment_set.all()
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentModelForm()
            return render(request, 'posting_hw/post_detail.html',{'post_ob':post_ob, 'comment_form':form, 'comments':comments})
        else:
            return render(request, 'posting_hw/post_detail.html',{'post_ob':post_ob, 'comment_form':form, 'comments':comments})
    else:
        form = CommentModelForm()
        return render(request, 'posting_hw/post_detail.html',{'post_ob':post_ob, 'comment_form':form, 'comments':comments})
    return render(request, 'posting_hw/post_detail.html',{'post_ob':post_ob, 'comment_form':form, 'comments':comments})

def post_write(request):

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return post_list(request)
    else:
        form = PostModelForm()

        return render(request, 'posting_hw/post_write.html',{'post_form':form})
