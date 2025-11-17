from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

@login_required
def notes_home_view(request):
    # Initialize form for GET
    form = NoteForm()

    if request.method =='POST':
        form = NoteForm(request.POST, request.FILES) #refill form with data
        if form.is_valid():
            note = form.save(commit=False)
            note.uploader = request.user  # Set the logged-in user as the uploader
            note.save()
            return redirect('notes_home')
        

    all_notes = Note.objects.all().order_by('-uploaded_at')

    context = {
        'form': form,
        'all_notes': all_notes,
    }

    return render(request, 'notes_home.html', context)

@login_required
def notes_delete_view(request, pk):
    #specific note we wish to delete
    note = get_object_or_404(Note, pk=pk)
    # Check if the logged-in user is the one who uploaded the note
    if note.uploader == request.user:
        # Only allow deletion if the request is a POST
        if request.method == 'POST':
            note.note_file.delete() #delete actual file from storage
            note.delete() #delete record from DB
            return redirect('notes_home')

    #If user is NOT the uploader, or if it is GET request, just send them back to the notes page.
    return redirect('notes_home')

    
# Create your views here.
