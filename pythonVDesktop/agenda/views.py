from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all().order_by('date', 'time')
    return render(request, 'agenda/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    
    return render(request, 'agenda/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Récupère la tâche ou renvoie une erreur 404
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # Pré-remplit le formulaire avec la tâche existante
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirige vers la liste des tâches après modification
    else:
        form = TaskForm(instance=task)  # Pré-remplit le formulaire pour modification
    return render(request, 'agenda/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':  # Confirmation de suppression
        task.delete()
        return redirect('task_list')
    return render(request, 'agenda/delete_task.html', {'task': task})

def task_and_calendar_view(request):
    tasks = Task.objects.all()
    events = []

    # Transformer les tâches en événements pour FullCalendar
    for task in tasks:
        events.append({
            'title': task.title,
            'start': f"{task.date}T{task.time}",
            'end': f"{task.date}T{task.time}",
            'description': task.description,
        })

    return render(request, 'agenda/task_list.html', {'tasks': tasks, 'events': events})