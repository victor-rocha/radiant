from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic import CreateView, View

from radiant.contacts.models import Contact, Subscriber, Nominee


class ContactView(CreateView):
    template_name = 'contacts/contact-form.html'
    model = Contact
    fields = ['full_name', 'email', 'message']
    success_url = reverse_lazy('contact-us')

    def form_valid(self, form):
        messages.success(self.request, 'Your email has been sent successfully.')
        return super(ContactView, self).form_valid(form)


class SubscribeView(View):
    model = Subscriber
    http_method_names = ['post']

    def post(self, *args, **kwargs):
        email = self.request.POST.get('email', '')
        if email:
            subscribers = Subscriber.objects.filter(email=email)
            if subscribers.exists():
                msg = 'You are already a subscriber.'
            else:
                Subscriber(email=email).save()
                msg = 'Thank you for subscribing!'
            return HttpResponse(msg)
        return HttpResponseBadRequest()


class NominateView(CreateView):
    template_name = 'contacts/nominate-form.html'
    model = Nominee
    fields = ['radiant_nominee_name', 'your_name', 'your_email', 'description',
              'video']
    success_url = reverse_lazy('nominate')

    def form_valid(self, form):
        messages.success(self.request, 'Your nomination has been submitted')
        return super(NominateView, self).form_valid(form)
