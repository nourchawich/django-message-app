from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Post
from .forms import PostForm


def posts_list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request=request, template_name='posts/list.html', context=context)


def posts_create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/posts/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    context = {
        'form': form
    }
    return render(request=request, template_name='posts/create.html', context=context)

# Todo (Mentee): After creating the campaigns app
# 1. Create views.py where you define views similar to the above
# 2. Create templates to list and create campaigns. Check `templates/posts/list.html` and `templates/posts/create.html`
