from django.db import models

# RF12 - Gerenciar cidades
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome} - {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


# CLASSE BASE PARA HERANÇA (Abstrata, não vira uma tabela sozinha no banco)
class Pessoa(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")

    class Meta:
        abstract = True  # Define que esta classe serve apenas como herança


# RF01 - Gerenciar pacientes (Herdando de Pessoa)
class Paciente(Pessoa):
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    historico_clinico = models.TextField(verbose_name="Histórico Clínico", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


# RF03 - Gerenciar clínicas psicológicas
class Clinica(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da Clínica")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(max_length=100, verbose_name="E-mail")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Clínica Psicológica"
        verbose_name_plural = "Clínicas Psicológicas"


# RF02 - Gerenciar psicólogos (Herdando de Pessoa)
class Psicologo(Pessoa):
    crp = models.CharField(max_length=20, unique=True, verbose_name="CRP")
    especialidade = models.CharField(max_length=100, verbose_name="Especialidade")
    clinicas = models.ManyToManyField(Clinica, verbose_name="Clínicas", related_name="psicologos")

    def __str__(self):
        return f"{self.nome} (CRP: {self.crp})"

    class Meta:
        verbose_name = "Psicólogo"
        verbose_name_plural = "Psicólogos"


# RF04 - Gerenciar emoções registradas
class Emocao(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da Emoção")
    intensidade = models.IntegerField(verbose_name="Intensidade (1 a 10)")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return f"{self.nome} (Intensidade: {self.intensidade})"

    class Meta:
        verbose_name = "Emoção"
        verbose_name_plural = "Emoções"


# RF05 - Gerenciar registros diários
class RegistroDiario(models.Model):
    data = models.DateField(verbose_name="Data do Registro")
    humor = models.CharField(max_length=50, verbose_name="Humor")
    observacoes = models.TextField(verbose_name="Observações", blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    emocao = models.ForeignKey(Emocao, on_delete=models.CASCADE, verbose_name="Emoção Principal")

    def __str__(self):
        return f"Registro de {self.paciente.nome} em {self.data}"

    class Meta:
        verbose_name = "Registro Diário"
        verbose_name_plural = "Registros Diários"


# RF14 - Gerenciar categorias de risco
class CategoriaRisco(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da Categoria")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria de Risco"
        verbose_name_plural = "Categorias de Risco"


# RF06 - Gerenciar análises comportamentais
class AnaliseComportamental(models.Model):
    descricao = models.TextField(verbose_name="Descrição da Análise")
    nivel_risco = models.ForeignKey(CategoriaRisco, on_delete=models.PROTECT, verbose_name="Nível de Risco")
    data_analise = models.DateField(verbose_name="Data da Análise")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")

    def __str__(self):
        return f"Análise de {self.paciente.nome} - {self.data_analise}"

    class Meta:
        verbose_name = "Análise Comportamental"
        verbose_name_plural = "Análises Comportamentais"


# RF07 - Gerenciar alertas psicológicos
class Alerta(models.Model):
    descricao = models.TextField(verbose_name="Descrição do Alerta")
    data_envio = models.DateTimeField(verbose_name="Data/Hora de Envio")
    nivel_urgencia = models.CharField(max_length=50, verbose_name="Nível de Urgência")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, verbose_name="Psicólogo Notificado")

    def __str__(self):
        return f"Alerta para Dr(a). {self.psicologo.nome} sobre {self.paciente.nome}"

    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"


# RF08 - Gerenciar consultas
class Consulta(models.Model):
    data = models.DateField(verbose_name="Data da Consulta")
    horario = models.TimeField(verbose_name="Horário")
    observacoes = models.TextField(verbose_name="Observações", blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, verbose_name="Psicólogo")

    def __str__(self):
        return f"Consulta: {self.paciente.nome} com {self.psicologo.nome} em {self.data}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"


# RF09 - Gerenciar tratamentos
class Tratamento(models.Model):
    descricao = models.TextField(verbose_name="Descrição do Tratamento")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim", blank=True, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, verbose_name="Psicólogo Responsável")

    def __str__(self):
        return f"Tratamento de {self.paciente.nome} por {self.psicologo.nome}"

    class Meta:
        verbose_name = "Tratamento"
        verbose_name_plural = "Tratamentos"


# RF10 - Gerenciar medicamentos
class Medicamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Medicamento")
    dosagem = models.CharField(max_length=50, verbose_name="Dosagem")
    frequencia = models.CharField(max_length=100, verbose_name="Frequência de Uso")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    tratamento = models.ForeignKey(Tratamento, on_delete=models.CASCADE, verbose_name="Tratamento Associado", blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.dosagem}) - {self.paciente.nome}"

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"


# RF11 - Gerenciar notificações
class Notificacao(models.Model):
    mensagem = models.TextField(verbose_name="Mensagem")
    data_envio = models.DateTimeField(verbose_name="Data de Envio")
    status = models.CharField(max_length=50, verbose_name="Status (Lida/Não Lida)")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")

    def __str__(self):
        return f"Notificação para {self.paciente.nome} - {self.status}"

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"


# RF13 - Gerenciar relatórios emocionais
class RelatorioEmocional(models.Model):
    periodo = models.CharField(max_length=50, verbose_name="Período (Ex: Semanal)")
    media_humor = models.CharField(max_length=50, verbose_name="Média de Humor")
    observacoes = models.TextField(verbose_name="Observações")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")

    def __str__(self):
        return f"Relatório ({self.periodo}) - {self.paciente.nome}"

    class Meta:
        verbose_name = "Relatório Emocional"
        verbose_name_plural = "Relatórios Emocionais"


# RF15 - Gerenciar histórico de acompanhamento
class HistoricoAcompanhamento(models.Model):
    data = models.DateField(verbose_name="Data")
    descricao = models.TextField(verbose_name="Descrição do Progresso")
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, verbose_name="Psicólogo")

    def __str__(self):
        return f"Histórico de {self.paciente.nome} em {self.data}"

    class Meta:
        verbose_name = "Histórico de Acompanhamento"
        verbose_name_plural = "Históricos de Acompanhamento"