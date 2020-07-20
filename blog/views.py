from django.utils import timezone
from .models import Post, Category, Tag, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect



def category_list(request):
	categories=Category.objects.all()
	return render(request, 'blog/category_list.html', {'categories':categories})

def category_detail(request,slug):
	category = get_object_or_404(Category, slug=slug)
	print(category)
	posts= Post.objects.filter(category=category)
	print(posts)
	return render(request, 'blog/category_detail.html', {'posts': posts, 'category':category})

def category_edit(request, slug):
	category = get_object_or_404(Category, slug=slug)
	if request.method == "POST":
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			category = form.save(commit=False)
			category.created_date = timezone.now()
			category.save()
			return redirect('blog:category_detail', slug=category.slug)
	else:
		form = CategoryForm(instance=category)
	return render(request, 'blog/category_edit.html', {'form': form})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post_details.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_list')
		
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_detail', slug=post.slug)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def tag_list(request):
	tags= Tag.objects.all()
	print(tags)
	return render(request, 'blog/tag_list.html', {'tags':tags})


def tag_details(request, slug):
	tag = get_object_or_404(Tag, slug=slug)
	print(tag)
	posts=Post.objects.filter(tag__slug=tag)
	return render(request, 'blog/tag_details.html', {'tag':tag, 'posts': posts})

def add_comment_to_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			parent_obj = None
			try:
				parent_id =int(request.Post.get('parent_id'))
			except:
				parent_id=None
			if parent_id:
				parent_obj=Comment.objects.get(id=comment.id)
				print(comment.id)
				if parent_obj:
					replay_comment=form.save(commit=False)
					replay_comment.parent=parent_obj
			new_comment=form.save(commit=False)
			new_comment.post=post
			new_comment.save()
			return redirect('blog:post_detail', slug=post.slug)

	else:
		form = CommentForm()
	return render(request, 'blog/add_comment_to_post.html', {'form': form, 'post':post})


def cmnt(request, slug):
	post= get_object_or_404(Post, slug=slug)
	cmnt= Post.cmnt.filter(slug=post.slug)
	return cmnt



	




	






	

