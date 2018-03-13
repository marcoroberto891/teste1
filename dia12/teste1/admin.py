from django.contrib import admin

# Register your models here.
from teste1.models import Pessoa, EventoCientifico, PessoaFisica, Evento, ArtigoCientifico, Autor, PessoaJuridica


admin.site.register(Pessoa)
admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Evento)
admin.site.register(Autor)
admin.site.register(EventoCientifico)
admin.site.register(ArtigoCientifico)
admin.site.register(Autor)