from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


# Create your views here.
def home(request):
    all_post = Post.objects.all()
    return render(request, 'blog/index.html',{'posts':all_post})

def contact_us(request):
    return render(request, 'blog/contact.html')

def post_list(request, pk, slug):
    post = get_object_or_404(Post,id=pk, slug=slug)
    print("the val in post",post.title,post.author,post.publish)
    return render(request, 'blog/post.html',{'post':post})

def create_post(request):
    print("this funciton gets called")
    if request.method == 'POST':
        form = PostForm(request.POST)
        print("the vlaue in the form",form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PostForm()
            return render(request, 'blog/post_create.html',{'form':form})
    else:
        form = PostForm()
        return render(request, 'blog/post_create.html', {'form':form})


def update_post(request, pk):
    id = pk
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return redirect('home')
    posts = PostForm(request.POST or None, instance = post)
    if posts.is_valid():
       posts.save()
       return redirect('home')
    return render(request, 'blog/post_create.html', {'post':posts})

def delete_post(request, pk):
    id = pk
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return redirect('home')
    post.delete()
    return redirect('home')

def about_us(request):
    return render(request, 'blog/about.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "blog/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "blog/register.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "blog/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")
  