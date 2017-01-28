import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.views import generic

from .forms import PostingForm
from .models import Posting
from core import helpers


class PostingDetailView(generic.DetailView):
    model = Posting


class PostingCreateView(generic.CreateView):
    model = Posting
    fields = ('title', )
    template_name = 'core/posting_create.html'

    def get_success_url(self):
        return reverse('core:update', kwargs={'pk': self.object.pk})


class PostingUpdateView(generic.UpdateView):
    model = Posting
    form_class = PostingForm

    def get_initial(self):
        initial = super(PostingUpdateView, self).get_initial()
        current_data = helpers.flatten(self.object.context)
        initial.update(current_data)
        return initial

    def get_success_url(self):
        return reverse('core:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        for filefield in self.request.FILES:
            form.cleaned_data.pop(filefield)
        new_data = helpers.unflatten(form.cleaned_data)
        for field in new_data:
            if field not in self.model._meta.get_fields():
                self.object.context[field] = new_data[field]
        self.object.save()
        for field_name, f in self.request.FILES.items():
            helpers.handle_uploaded_file(
                f,
                os.path.join(settings.MEDIA_ROOT, str(self.object.pk),
                             field_name),
                f.name
            )
        return super(PostingUpdateView, self).form_valid(form)
