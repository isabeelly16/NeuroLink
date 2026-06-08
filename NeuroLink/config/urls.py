from django.contrib import admin
from django.urls import path
from app.views import (
    IndexView, PacienteView, PsicologoView, ClinicaView, EmocaoView,
    RegistroDiarioView, AnaliseComportamentalView, AlertaView, ConsultaView,
    TratamentoView, MedicamentoView, NotificacaoView, CidadeView,
    RelatorioEmocionalView, CategoriaRiscoView, HistoricoAcompanhamentoView,
    DeletePacienteView, EditarPacienteView, alternar_usuario, 
    LoginView, logout_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', IndexView.as_view(), name='index'),
    
    # Rota de alternância: agora ao acessar, ele desloga e vai para o login
    path('alternar-usuario/<str:tipo>/', alternar_usuario, name='alternar_usuario'),
    
    path('paciente/', PacienteView.as_view(), name='paciente'),
    path('psicologo/', PsicologoView.as_view(), name='psicologo'),
    path('clinica/', ClinicaView.as_view(), name='clinica'),
    path('emocao/', EmocaoView.as_view(), name='emocao'),
    path('registro-diario/', RegistroDiarioView.as_view(), name='registro_diario'),
    path('analise-comportamental/', AnaliseComportamentalView.as_view(), name='analise_comportamental'),
    path('alerta/', AlertaView.as_view(), name='alerta'),
    path('consulta/', ConsultaView.as_view(), name='consulta'),
    path('tratamento/', TratamentoView.as_view(), name='tratamento'),
    path('medicamento/', MedicamentoView.as_view(), name='medicamento'),
    path('notificacao/', NotificacaoView.as_view(), name='notificacao'),
    path('cidade/', CidadeView.as_view(), name='cidade'),
    path('relatorio-emocional/', RelatorioEmocionalView.as_view(), name='relatorio_emocional'),
    path('categoria-risco/', CategoriaRiscoView.as_view(), name='categoria_risco'),
    path('historico-acompanhamento/', HistoricoAcompanhamentoView.as_view(), name='historico_acompanhamento'),
    
    # Rotas com parâmetros
    path('paciente/delete/<int:id>/', DeletePacienteView.as_view(), name='delete_paciente'),
    path('paciente/editar/<int:id>/', EditarPacienteView.as_view(), name='editar_paciente'),
]