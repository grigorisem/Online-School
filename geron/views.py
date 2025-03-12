from django.shortcuts import render,HttpResponse, redirect
from .forms import MembershipForm
from .models import Membership
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "index.html")

def lessons(request):
    if request.user.is_authenticated:
        return render(request, "lessons.html")
    else:
        return redirect("home")

@login_required
def lessons_view(request):
    if Membership.objects.filter(user=request.user).exists():
        return redirect('profile')
    
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            membership = form.save(commit=False)
            membership.user = request.user
            membership.save()
            return redirect('profile')
        form = MembershipForm()

    return render(request, 'lessons.html', {'form': form})

@login_required
def profile_view(request):
    memberships = Membership.objects.filter(user=request.user)
    
    return render(request, "profile.html", {
        'user': request.user,
        'memberships': memberships
    })