from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from MACLibrary.models import Address, mac_re

class Command(BaseCommand):
    args = '<filename>'
    help = 'Loads a file of MACs into the database (one per line)'

    def handle(self, *args, **options):
        count = 0
        f = open(args[0])
        for mac in f.readlines():
            mac = mac.strip()
            try:
                if not mac_re.match(mac):
                    raise Exception()
                new_address = Address(mac=mac)
                new_address.save()
                count += 1
            except IntegrityError:
                self.stdout.write('MAC "' + mac +'" already exists in DB.')
            except:
                self.stdout.write('Error with mac: "' + mac + '"')
        self.stdout.write('Finished loading new MAC address, added: ' + str(count))