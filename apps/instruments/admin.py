from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from .models import Instrument

# Register your models here.

@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):

    change_list_template = 'instruments_admin.html'
    list_display = ['name']


    # Override parent default url handlers to add my own.
    def get_urls(self):
        default_urls = super().get_urls()
        
        custom_urls = [
            path('import-instruments/', self.import_instruments),
        ]
        
        #Since django does left-right (in-order) scanning of urls, it's important to put our custom ones first.
        return custom_urls + default_urls


    # Custom method to update instruments from instruments_list.py
    def import_instruments(self, request):

        # Easier to use a disjoint set algo here than query for every instrument.
        from .instruments_list import instruments
        container = {}
        
        db_instruments = Instrument.objects.all()
        
        # Store the db's instrument-names inside a hash table.
        for db_instrument in db_instruments:
            container[db_instrument.name] = 0

        # Rotate through the maintained list of instruments.
        for instrument_name in instruments:
            # If it's not in the hash table, make it in the DB.
            try:
                container[instrument_name] + 1
            except KeyError:
                Instrument.objects.create(name=instrument_name)
        
        # Rotate through the DB instruments in the hash table:
        for instrument_name in container:
            # Prune any remove instruments that are in the DB that don't match the maintained list.
            if instrument_name not in instruments:
                Instrument.objects.get(name=instrument_name).delete()
        
        return redirect('..')
                