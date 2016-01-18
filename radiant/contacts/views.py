from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from radiant.contacts.models import Contact


class ContactView(CreateView):
    template_name = 'contacts/contact-form.html'
    model = Contact
    fields = ['full_name', 'email', 'message']
    success_url = reverse_lazy('contact-us')

    def form_valid(self, form):
        messages.success(self.request, 'Your email has been sent successfully.')
        return super(ContactView, self).form_valid(form)
