from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView, View

# from .methods import do_something
from .models import Note
from .tasks import task_do_something


class NoteListView(ListView):
    model = Note
    template_name = "index.html"
    context_object_name = "notes"


class NoteDetailView(DetailView):
    model = Note
    template_name = "preview.html"
    context_object_name = "note"


class NoteCreateView(View):
    def get(self, request):
        return render(request, "form.html")

    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        # do_something()
        task_do_something() # jalan di background -> Queue (antrian)
        Note.objects.create(title=title, content=content, user=request.user)
        return redirect("index")
