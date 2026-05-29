from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import (
    Cidade, Paciente, Clinica, Psicologo, Emocao, RegistroDiario,
    CategoriaRisco, AnaliseComportamental, Alerta, Consulta,
    Tratamento, Medicamento, Notificacao, RelatorioEmocional, HistoricoAcompanhamento
)

# 1. Página Inicial
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

# 2. RF01 - Gerenciar pacientes
class PacienteView(View):
    def get(self, request, *args, **kwargs):
        pacientes = Paciente.objects.all()
        return render(request, 'paciente.html', {'pacientes': pacientes})

# 3. RF02 - Gerenciar psicólogos
class PsicologoView(View):
    def get(self, request, *args, **kwargs):
        psicologos = Psicologo.objects.all()
        return render(request, 'psicologo.html', {'psicologos': psicologos})

# 4. RF03 - Gerenciar clínicas psicológicas
class ClinicaView(View):
    def get(self, request, *args, **kwargs):
        clinicas = Clinica.objects.all()
        return render(request, 'clinica.html', {'clinicas': clinicas})

# 5. RF04 - Gerenciar emoções registradas
class EmocaoView(View):
    def get(self, request, *args, **kwargs):
        emocoes = Emocao.objects.all()
        return render(request, 'emocao.html', {'emocoes': emocoes})

# 6. RF05 - Gerenciar registros diários
class RegistroDiarioView(View):
    def get(self, request, *args, **kwargs):
        registros = RegistroDiario.objects.all()
        return render(request, 'registro_diario.html', {'registros': registros})

# 7. RF06 - Gerenciar análises comportamentais
class AnaliseComportamentalView(View):
    def get(self, request, *args, **kwargs):
        analises = AnaliseComportamental.objects.all()
        return render(request, 'analise_comportamental.html', {'analises': analises})

# 8. RF07 - Gerenciar alertas psicológicos
class AlertaView(View):
    def get(self, request, *args, **kwargs):
        alertas = Alerta.objects.all()
        return render(request, 'alerta.html', {'alertas': alertas})

# 9. RF08 - Gerenciar consultas
class ConsultaView(View):
    def get(self, request, *args, **kwargs):
        consultas = Consulta.objects.all()
        return render(request, 'consulta.html', {'consultas': consultas})

# 10. RF09 - Gerenciar tratamentos
class TratamentoView(View):
    def get(self, request, *args, **kwargs):
        tratamentos = Tratamento.objects.all()
        return render(request, 'tratamento.html', {'tratamentos': tratamentos})

# 11. RF10 - Gerenciar medicamentos
class MedicamentoView(View):
    def get(self, request, *args, **kwargs):
        medicamentos = Medicamento.objects.all()
        return render(request, 'medicamento.html', {'medicamentos': medicamentos})

# 12. RF11 - Gerenciar notificações
class NotificacaoView(View):
    def get(self, request, *args, **kwargs):
        notificacoes = Notificacao.objects.all()
        return render(request, 'notificacao.html', {'notificacoes': notificacoes})

# 13. RF12 - Gerenciar cidades
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

# 14. RF13 - Gerenciar relatórios emocionais
class RelatorioEmocionalView(View):
    def get(self, request, *args, **kwargs):
        relatorios = RelatorioEmocional.objects.all()
        return render(request, 'relatorio_emocional.html', {'relatorios': relatorios})

# 15. RF14 - Gerenciar categorias de risco
class CategoriaRiscoView(View):
    def get(self, request, *args, **kwargs):
        categorias = CategoriaRisco.objects.all()
        return render(request, 'categoria_risco.html', {'categorias': categorias})

# 16. RF15 - Gerenciar histórico de acompanhamento
class HistoricoAcompanhamentoView(View):
    def get(self, request, *args, **kwargs):
        historicos = HistoricoAcompanhamento.objects.all()
        return render(request, 'historico_acompanhamento.html', {'historicos': historicos})

# --- FUNÇÕES ADICIONAIS DO NEUROLINK (DELETE E EDIT) ---

class DeletePacienteView(View):
    def get(self, request, id, *args, **kwargs):
        # Busca o paciente pelo ID e deleta do banco
        paciente = Paciente.objects.get(id=id)
        paciente.delete()
        messages.success(request, 'Paciente excluído com sucesso!')
        return redirect('paciente') # Redireciona de volta para a lista

class EditarPacienteView(View):
    template_name = 'editar_paciente.html'

    def get(self, request, id, *args, **kwargs):
        paciente = get_object_or_404(Paciente, id=id)
        # Passamos os dados atuais do paciente para os campos da tela
        return render(request, self.template_name, {'paciente': paciente})

    def post(self, request, id, *args, **kwargs):
        paciente = get_object_or_404(Paciente, id=id)
        
        # Captura os dados atualizados vindos do formulário da tela
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.email = request.POST.get('email')
        paciente.save() # Salva as alterações no banco de dados
        
        messages.success(request, 'As edições foram salvas com sucesso.')
        return redirect('paciente')