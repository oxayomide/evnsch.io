# events/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or home page
    else:
        form = EventForm()
    return render(request, 'events/event_edit.html', {'form': form})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_edit.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event_list')

@login_required
def event_list_api(request):
    events = Event.objects.filter(user=request.user).values('title', 'start_time', 'end_time')
    return JsonResponse(list(events), safe=False)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('event_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

