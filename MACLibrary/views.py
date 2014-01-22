import json
from mixins import *
from models import *
from django.http import HttpResponse
from django.views.generic import DetailView, ListView


class AddressListView(ListView):
    model = Address


class AddressDetailView(JSONDetailResponseMixin, DetailView):
    model = Address
    slug_field = 'mac'


class AssignAddressDetailView(AddressDetailView):
    def get_object(self, queryset=None):
        obj = super(AssignAddressDetailView, self).get_object(queryset)
        obj.status = Address.ASSIGNED
        obj.save()
        return obj


class OpenAddressDetailView(AddressDetailView):
    def get_object(self):
        return get_available_address()


def free_pending_addresses_view(request):
    return HttpResponse(str(free_pending_addresses()) + " pending addresses marked as free.")