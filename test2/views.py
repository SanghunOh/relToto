from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Community_post
from .forms import Community_PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import Signup_form, Login_form
from django.contrib.auth import login, authenticate

from django.http import HttpResponse

from .models import Member_info
from .models import My_role, My_under
from .models import Post

from .forms import Member_info_form
from .forms import Post_form

from django.contrib.auth import views as auth_views
####################################################################

def logout(request):
    # message user or whatever
    return auth_views.logout(request)



def friends_recommend(request):
    mem = Member_info.objects.all()
    my_roless = My_role.objects.all()
    friends = []
    follows = []
    for x in my_roless:
        if x.identity == request.user:
            break
    for y in x.my_roles.all():
        follows.append(y.identity.username)
    for x in mem:
        if x.identity == request.user or x.identity.username in follows:
            continue
        else:
            friends.append(x)
    return render(request, 'test2/compass.html', {'newfriends': friends,})



"""
def home(request):
    #users = User.objects.all()
    #posts = Post.objects.all()
    my_roless = My_role.objects.all()
    mem_info = Member_info.objects.get(identity= User.objects.get(username = request.user.username))
    follows = []
    for x in my_roless:
        if x.identity.username == request.user.username:
            break
    for y in x.my_roles.all():
        follows.append(y.identity.username)
    posts = Post.objects.all()
    real_forms = []
    for x in follows:
        for y in posts:
            if y.identity.username == x:
                real_forms.append(y)
    return render(request, 'test2/home.html', {'posts': real_forms, 'member_info': mem_info})
"""

def home(request):
    #users = User.objects.all()
    #posts = Post.objects.all()
    mem_info = Member_info.objects.get(identity=User.objects.get(username=request.user.username))
    my_roless = My_role.objects.all()
    follows = []
    if len(my_roless) != 0:
        for x in my_roless:
            if x.identity.username == request.user.username:
                break
        for y in x.my_roles.all():
            follows.append(y.identity.username)
        posts = Post.objects.all()
        real_forms = []
        for x in follows:
            for y in posts:
                if y.identity.username == x:
                    real_forms.append(y)
        return render(request, 'test2/home.html', {'posts': real_forms, 'member_info': mem_info})
    else:
        return render(request, 'test2/home.html', {})


def following(request, pk):
    my_roless = My_role.objects.all()
    for x in my_roless:
        if x.identity.username == request.user.username:
            x.my_roles.add(User.objects.get(username=request.user.username))
            break
    my_underss = My_under.objects.all()
    for x in my_underss:
        if x.identity.username == Post.objects.get(pk=pk).identity.username: #Post?, Member_info?
            x.my_unders.add(User.objects.get(username=request.user.username))
            break
    post = get_object_or_404(Post, pk=pk)
    return redirect('profile', pk)


"""
def profile(request, pk):
    user = User.objects.get(username=request.user.username)
    user_posts = Post.objects.filter(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username))
    member_inf = Member_info.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username))
    if len(My_role.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_roles.all()) > 0:
        my_roles_num = len(My_role.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_roles.all())
    else:
        my_roles_num = 0
    if len(My_under.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_unders.all()) > 0:
        my_unders_num = len(My_under.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_unders.all())
    else:
        my_unders_num = 0
    return render(request, 'test2/profile.html', {'user': user, 'user_posts': user_posts, 'member_infos': member_inf, 'my_roles_num': my_roles_num, 'my_unders_num': my_unders_num})
"""

def profile(request, pk):
    user = User.objects.get(username=request.user.username)
    user_posts = Post.objects.filter(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username))
    member_inf = Member_info.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username))
    if len(My_role.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_roles.all()) != 0:
        my_roles_num = len(My_role.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_roles.all())
    else:
        my_roles_num = 0
    if len(My_under.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_unders.all()) != 0:
        my_unders_num = len(My_under.objects.get(identity=User.objects.get(username=Post.objects.get(pk=pk).identity.username)).my_unders.all())
    else:
        my_unders_num = 0
    return render(request, 'test2/profile.html', {'user': user, 'user_posts': user_posts, 'member_infos': member_inf, 'my_roles_num': my_roles_num, 'my_unders_num': my_unders_num})

def  my_profile(request):
    posts = Post.objects.all()
    my_posts = []
    for x in posts:
        if x.identity.username == request.user.username:
            my_posts.append(x)
    # to my_posts
    member_infos = Member_info.objects.all()
    for x in member_infos:
        if x.identity.username == request.user.username:
            my_info = x
    return render(request, 'test2/my_profile.html', {'my_posts': my_posts, 'my_info': my_info})

def post_detail(request, pk):
    mem_info = Member_info.objects.get(identity=(Post.objects.get(pk= pk).identity))
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'test2/post_detail.html', {'post': post, 'member_info': mem_info})


#################################################


def signup(request):
    if request.method == "POST":
        form = Signup_form(request.POST)
        if form.is_valid():
            #new_user = User.objects.create_user(form.username, form.email, form.password)
            #new_user = User.objects.create_user(**form.cleaned_data)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user = User.objects.create_user(username, email, password)
            new_user.save
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('member_info')
    else:
        form = Signup_form()
    return render(request, 'test2/signup.html', {'form': form})


def member_info(request):
    if request.method == "POST":
        form = Member_info_form(request.POST, request.FILES)
        if form.is_valid():
            mem = form.save(commit=False)
            mem.identity = User.objects.get(username=request.user.username)
            mem.name = form.cleaned_data['name']
            mem.myinfo = form.cleaned_data['myinfo']
            mem.created_date = timezone.now()
            mem.save()
            return redirect('home')
    else:
        form = Member_info_form()
    return render(request, 'test2/member_info.html', {'form': form})


def member_info_edit(request, pk):
    mem = get_object_or_404(Member_info, pk=pk)
    if mem.identity.username == request.user.username:
        if request.method == "POST":
            form = Member_info_form(request.POST,  request.FILES, instance=mem)
            if form.is_valid():
                mem = form.save(commit=False)
                mem.identity = User.objects.get(username=request.user.username)
                mem.name = form.cleaned_data['name']
                mem.myinfo = form.cleaned_data['myinfo']
                #mem.my_photo = form.cleaned_data['my_photo']
                mem.created_date = timezone.now()
                mem.save()
                return redirect('home')
        else:
            form = Member_info_form(instance=mem)
        return render(request, 'test2/member_info.html', {'form': form})
    else:
        return HttpResponse('잘못된 접근입니다.')

"""
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
"""



def Login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패')
    else:
        form = Login_form()
        return render(request, 'test2/login.html', {'form': form})



def post_new(request):
    if request.method == 'POST':
        form = Post_form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.identity = request.user
            post.created_date = timezone.now()
            post.save()
            #new = form.save(commit=False)
            #new.user = request.user
            #new.save()
            return redirect('home')
    else:
        form = Post_form()
        return render(request, 'test2/post_new.html', {'form': form})










#######################################

def enter_sadari(request):
    return render(request, 'test2/sadari.html', {})

def enter_community(request):
    posts = Community_post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'test2/community.html', {'posts': posts})

def community_post_detail(request, pk):
    post = get_object_or_404(Community_post, pk=pk)
    return render(request, 'test2/community_post_detail.html', {'post': post})

def community_post_new(request):
    if request.method == "POST":
        form = Community_PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('community_post_detail', pk=post.pk)
    else:
        form = Community_PostForm()
    return render(request, 'test2/community_post_new.html', {'form':form})

def community_post_edit(request, pk):
    post = get_object_or_404(Community_post, pk=pk)
    if request.method == "POST":
        form = Community_PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('community_post_detail', pk=post.pk)
    else:
        form = Community_PostForm(instance=post)
    return render(request, 'test2/community_post_new.html', {'form': form})

def member_info_edit(request, pk):
    mem = get_object_or_404(Member_info, pk=pk)
    if mem.identity.username == request.user.username:
        if request.method == "POST":
            form = Member_info_form(request.POST, instance=mem)
            if form.is_valid():
                mem = form.save(commit=False)
                mem.identity = User.objects.get(username=request.user.username)
                mem.name = form.cleaned_data['name']
                mem.myinfo = form.cleaned_data['myinfo']
                mem.created_date = timezone.now()
                mem.save()
                return redirect('home')
        else:
            form = Member_info_form(instance=mem)
        return render(request, 'test2/member_info.html', {'form': form})
    else:
        return HttpResponse('잘못된 접근입니다.')
