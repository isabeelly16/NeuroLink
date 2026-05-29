from django.contrib import admin
from django.urls import path
# Importando as views específicas do NeuroLink que criamos no passo anterior
from app.views import (
    IndexView, PacienteView, PsicologoView, ClinicaView, EmocaoView,
    RegistroDiarioView, AnaliseComportamentalView, AlertaView, ConsultaView,
    TratamentoView, MedicamentoView, NotificacaoView, CidadeView,
    RelatorioEmocionalView, CategoriaRiscoView, HistoricoAcompanhamentoView,
    DeletePacienteView, EditarPacienteView  # <-- CORRIGIDO: Importação adicionada aqui!
)

urlpatterns = [
    # Rota para o painel de administração (Django Admin)
    path('admin/', admin.site.urls),
    
    # Rota para a Página Inicial
    path('', IndexView.as_view(), name='index'),
    
    # Rotas do Projeto NeuroLink (Mapeando os requisitos funcionais)
    path('paciente/', PacienteView.as_view(), name='paciente'),  # RF01
    path('psicologo/', PsicologoView.as_view(), name='psicologo'),  # RF02
    path('clinica/', ClinicaView.as_view(), name='clinica'),  # RF03
    path('emocao/', EmocaoView.as_view(), name='emocao'),  # RF04
    path('registro-diario/', RegistroDiarioView.as_view(), name='registro_diario'),  # RF05
    path('analise-comportamental/', AnaliseComportamentalView.as_view(), name='analise_comportamental'),  # RF06
    path('alerta/', AlertaView.as_view(), name='alerta'),  # RF07
    path('consulta/', ConsultaView.as_view(), name='consulta'),  # RF08
    path('tratamento/', TratamentoView.as_view(), name='tratamento'),  # RF09
    path('medicamento/', MedicamentoView.as_view(), name='medicamento'),  # RF10
    path('notificacao/', NotificacaoView.as_view(), name='notificacao'),  # RF11
    path('cidade/', CidadeView.as_view(), name='cidade'),  # RF12
    path('relatorio-emocional/', RelatorioEmocionalView.as_view(), name='relatorio_emocional'),  # RF13
    path('categoria-risco/', CategoriaRiscoView.as_view(), name='categoria_risco'),  # RF14
    path('historico-acompanhamento/', HistoricoAcompanhamentoView.as_view(), name='historico_acompanhamento'),  # RF15
    
    # Rotas Extras para Deletar e Editar Pacientes (Estudo Dirigido)
    path('paciente/delete/<int:id>/', DeletePacienteView.as_view(), name='delete_paciente'),
    path('paciente/editar/<int:id>/', EditarPacienteView.as_view(), name='editar_paciente'),
]