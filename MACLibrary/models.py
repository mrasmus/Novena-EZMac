import re

from django.utils.translation import ugettext_lazy as _
from django.forms import fields
from django.db import models

#MAC Address Field code from https://djangosnippets.org/snippets/1337/
MAC_RE = r'^([0-9a-fA-F]{2}([:-]?|$)){6}$'
mac_re = re.compile(MAC_RE)

class MACAddressFormField(fields.RegexField):
    default_error_messages = {
        'invalid': _(u'Enter a valid MAC address.'),
    }

    def __init__(self, *args, **kwargs):
        super(MACAddressFormField, self).__init__(mac_re, *args, **kwargs)

class MACAddressField(models.Field):
    empty_strings_allowed = False
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 17
        super(MACAddressField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        defaults = {'form_class': MACAddressFormField}
        defaults.update(kwargs)
        return super(MACAddressField, self).formfield(**defaults)


class Address(models.Model):
    OPEN = 'OPN'
    PENDING = 'PND'
    ASSIGNED = 'ASS'
    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (PENDING, 'Pending'),
        (ASSIGNED, 'Assigned'),
    )
    status = models.CharField(max_length=3,
                              choices=STATUS_CHOICES,
                              default=OPEN,
                              blank=False,
                              null=False)
    mac = MACAddressField(blank=False,
                          null=False,
                          unique=True)
    serial = models.AutoField(primary_key=True)

    #def save(self, *args, **kwargs):
    #    if not self.serial:
    #        self.status = Address.OPEN
    #    super(Address, self).save(*args, **kwargs)


    def confirm_assignment(self):
        self.status = Address.ASSIGNED


    def __unicode__(self):
        return self.mac + ' | ' + str(self.serial) + ('' if self.status == Address.ASSIGNED else '(' + self.status + ')')


def get_available_address():
    addr = Address.objects.filter(status=Address.OPEN)[0]
    addr.status = Address.PENDING
    addr.save()
    return addr


def free_pending_addresses():
    addrs = Address.objects.filter(status=Address.PENDING)
    count = 0
    for addr in addrs:
        addr.status = Address.OPEN
        addr.save()
        count += 1
    return count
