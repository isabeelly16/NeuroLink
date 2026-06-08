from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import (
    Cidade, Paciente, Clinica, Psicologo, Emocao, RegistroDiario,
    CategoriaRisco, AnaliseComportamental, Alerta, Consulta,
    Tratamento, Medicamento, Notificacao, RelatorioEmocional, HistoricoAcompanhamento
)

# --- LOGIN E AUTENTICAÇÃO ---

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def alternar_usuario(request, tipo):
    logout(request)
    messages.info(request, f'Por favor, faça login como {tipo.capitalize()}.')
    return redirect('login')

# --- CLASSES DE VIEW (DINÂMICAS) ---

@method_decorator(login_required(login_url='login'), name='dispatch')
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'titulo_pagina': 'Dashboard', 'icone_pagina': 'fa-tachometer-alt', 'descricao': 'Visão geral do sistema'})

@method_decorator(login_required(login_url='login'), name='dispatch')
class PacienteView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'paciente.html', {
            'pacientes': Paciente.objects.all(),
            'titulo_pagina': 'Gestão de Pacientes',
            'icone_pagina': 'fa-user-injured',
            'descricao': 'Lista de pacientes cadastrados no sistema.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class PsicologoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'psicologo.html', {
            'psicologos': Psicologo.objects.all(),
            'titulo_pagina': 'Corpo Clínico',
            'icone_pagina': 'fa-user-md',
            'descricao': 'Psicólogos ativos e profissionais da rede.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class ClinicaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'clinica.html', {
            'clinicas': Clinica.objects.all(),
            'titulo_pagina': 'Clínicas & Locais',
            'icone_pagina': 'fa-clinic-medical',
            'descricao': 'Unidades de atendimento registradas.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class EmocaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'emocao.html', {
            'emocoes': Emocao.objects.all(),
            'titulo_pagina': 'Monitoramento de Emoções',
            'icone_pagina': 'fa-grin-beam',
            'descricao': 'Registro e análise de estados emocionais.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class RegistroDiarioView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registro_diario.html', {
            'registros': RegistroDiario.objects.all(),
            'titulo_pagina': 'Registro Diário',
            'icone_pagina': 'fa-book',
            'descricao': 'Acompanhamento do progresso diário.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class AnaliseComportamentalView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'analise_comportamental.html', {
            'analises': AnaliseComportamental.objects.all(),
            'titulo_pagina': 'Análise Comportamental',
            'icone_pagina': 'fa-chart-line',
            'descricao': 'Relatórios detalhados de comportamento.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class AlertaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'alerta.html', {
            'alertas': Alerta.objects.all(),
            'titulo_pagina': 'Central de Alertas',
            'icone_pagina': 'fa-exclamation-triangle',
            'descricao': 'Notificações críticas e pendências.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class ConsultaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'consulta.html', {
            'consultas': Consulta.objects.all(),
            'titulo_pagina': 'Consultas',
            'icone_pagina': 'fa-calendar-alt',
            'descricao': 'Agenda de atendimentos médicos.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class TratamentoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tratamento.html', {
            'tratamentos': Tratamento.objects.all(),
            'titulo_pagina': 'Tratamentos',
            'icone_pagina': 'fa-pills',
            'descricao': 'Planos terapêuticos em curso.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class MedicamentoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'medicamento.html', {
            'medicamentos': Medicamento.objects.all(),
            'titulo_pagina': 'Medicamentos',
            'icone_pagina': 'fa-capsules',
            'descricao': 'Controle de medicação e posologia.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class NotificacaoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'notificacao.html', {
            'notificacoes': Notificacao.objects.all(),
            'titulo_pagina': 'Notificações',
            'icone_pagina': 'fa-bell',
            'descricao': 'Histórico de avisos do sistema.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cidade.html', {
            'cidades': Cidade.objects.all(),
            'titulo_pagina': 'Cidades Atendidas',
            'icone_pagina': 'fa-city',
            'descricao': 'Cobertura geográfica da rede.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class RelatorioEmocionalView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'relatorio_emocional.html', {
            'relatorios': RelatorioEmocional.objects.all(),
            'titulo_pagina': 'Relatórios Emocionais',
            'icone_pagina': 'fa-file-medical-alt',
            'descricao': 'Relatórios consolidados de saúde mental.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class CategoriaRiscoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'categoria_risco.html', {
            'categorias': CategoriaRisco.objects.all(),
            'titulo_pagina': 'Categorias de Risco',
            'icone_pagina': 'fa-biohazard',
            'descricao': 'Níveis de atenção clínica.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class HistoricoAcompanhamentoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'historico_acompanhamento.html', {
            'historicos': HistoricoAcompanhamento.objects.all(),
            'titulo_pagina': 'Histórico Geral',
            'icone_pagina': 'fa-history',
            'descricao': 'Todo o histórico de acompanhamento registrado.'
        })

@method_decorator(login_required(login_url='login'), name='dispatch')
class DeletePacienteView(View):
    def get(self, request, id, *args, **kwargs):
        Paciente.objects.get(id=id).delete()
        return redirect('paciente')

@method_decorator(login_required(login_url='login'), name='dispatch')
class EditarPacienteView(View):
    def get(self, request, id, *args, **kwargs):
        paciente = get_object_or_404(Paciente, id=id)
        return render(request, 'editar_paciente.html', {'paciente': paciente, 'titulo_pagina': 'Editar Paciente', 'icone_pagina': 'fa-edit', 'descricao': 'Modificar dados do paciente.'})

    def post(self, request, id, *args, **kwargs):
        paciente = get_object_or_404(Paciente, id=id)
        paciente.nome = request.POST.get('nome')
        paciente.cpf = request.POST.get('cpf')
        paciente.email = request.POST.get('email')
        paciente.save()
        return redirect('paciente')