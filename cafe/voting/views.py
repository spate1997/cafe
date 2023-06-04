from django.shortcuts import render, redirect
from .models import Dessert
from .forms import VoteForm

def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            dessert = Dessert.objects.get(name=form.cleaned_data['name'])
            dessert.votes += 1
            dessert.save()
            return redirect('results')
    else:
        form = VoteForm()
    return render(request, 'vote.html', {'form': form})

def results(request):
    desserts = Dessert.objects.order_by('-votes')
    return render(request, 'results.html', {'desserts': desserts})
