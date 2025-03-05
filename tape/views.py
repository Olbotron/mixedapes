from django.shortcuts import render, get_object_or_404, redirect
from .models import Tape
from .forms import TapeForm

def home(request):
    return render(request, 'home.html')

def tape_list(request):
    tapes = Tape.objects.all()
    return render(request, 'tape/tape_list.html', {'tapes': tapes})

def tape_detail(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    return render(request, 'tape/tape_detail.html', {'tape': tape})

def tape_create(request):
    if request.method == "POST":
        form = TapeForm(request.POST)
        if form.is_valid():
            tape = form.save(commit=False)
            tape.user = request.user
            tape.save()
            return redirect('tape_detail', pk=tape.pk)
    else:
        form = TapeForm()
    return render(request, 'tape/tape_form.html', {'form': form})

def tape_update(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    if request.method == "POST":
        form = TapeForm(request.POST, instance=tape)
        if form.is_valid():
            tape = form.save(commit=False)
            tape.user = request.user
            tape.save()
            return redirect('tape_detail', pk=tape.pk)
    else:
        form = TapeForm(instance=tape)
    return render(request, 'tape/tape_form.html', {'form': form})

def tape_delete(request, pk):
    tape = get_object_or_404(Tape, pk=pk)
    tape.delete()
    return redirect('tape_list')