from django.contrib import admin
from .models import (
    Cidade, Paciente, Clinica, Psicologo, Emocao, RegistroDiario,
    CategoriaRisco, AnaliseComportamental, Alerta, Consulta,
    Tratamento, Medicamento, Notificacao, RelatorioEmocional, HistoricoAcompanhamento
)

# ==========================================
# DEFINIÇÃO DOS INLINES EXIGIDOS (Item 4)
# ==========================================

# iii) Pacientes e registros diários
class RegistroDiarioInline(admin.TabularInline):
    model = RegistroDiario
    extra = 1

# iv) Pacientes e análises comportamentais
class AnaliseComportamentalInline(admin.TabularInline):
    model = AnaliseComportamental
    extra = 1

# v) Pacientes e alertas
class AlertaInline(admin.TabularInline):
    model = Alerta
    extra = 1

# vi) Pacientes e consultas
class ConsultaInline(admin.TabularInline):
    model = Consulta
    extra = 1

# viii) Pacientes e relatórios emocionais
class RelatorioEmocionalInline(admin.TabularInline):
    model = RelatorioEmocional
    extra = 1

# ix) Pacientes, tratamentos e medicamentos (Medicamento aninhado indiretamente no paciente por meio do tratamento)
class MedicamentoInline(admin.TabularInline):
    model = Medicamento
    extra = 1

class TratamentoInline(admin.TabularInline):
    model = Tratamento
    extra = 1


class ClinicaInline(admin.TabularInline):
    model = Clinica
    extra = 1



@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    search_fields = ('nome',)
    inlines = [ClinicaInline]  


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'telefone', 'cidade')
    search_fields = ('nome', 'cpf')

    inlines = [
        RegistroDiarioInline,       
        AnaliseComportamentalInline, 
        AlertaInline,               
        ConsultaInline,            
        RelatorioEmocionalInline,   
        TratamentoInline,           
    ]


@admin.register(Tratamento)
class TratamentoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'paciente', 'psicologo', 'data_inicio')
    inlines = [MedicamentoInline]  


@admin.register(Clinica)
class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cidade')
    search_fields = ('nome',)


@admin.register(Psicologo)
class PsicologoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crp', 'email', 'especialidade')
    search_fields = ('nome', 'crp')
    filter_horizontal = ('clinicas',)  
admin.site.register(Emocao)
admin.site.register(CategoriaRisco)
admin.site.register(RegistroDiario)
admin.site.register(AnaliseComportamental)
admin.site.register(Alerta)
admin.site.register(Consulta)
admin.site.register(Medicamento)
admin.site.register(Notificacao)
admin.site.register(RelatorioEmocional)
admin.site.register(HistoricoAcompanhamento)