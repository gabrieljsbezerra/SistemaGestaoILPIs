import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.db.models import Count, Sum, F, ExpressionWrapper, FloatField
from visitas.models import Visita
from estoque.models import Remedio

def gerar_grafico_barras(dados, titulo, xlabel='', ylabel=''):
    fig, ax = plt.subplots(figsize=(10, 5))
    nomes = [d['nome'] for d in dados]
    valores = [d['valor'] for d in dados]

    ax.bar(nomes, valores)
    ax.set_title(titulo)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    imagem_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return imagem_base64

def dashboard_analises(request):
    # 1. Visitas por responsável
    visitas = Visita.objects.values('responsavel__nome').annotate(total=Count('id')).order_by('-total')
    dados_visitas = [{'nome': v['responsavel__nome'], 'valor': v['total']} for v in visitas]
    grafico_visitas = gerar_grafico_barras(dados_visitas, 'Visitas por Responsável')

    # 2. Volume de estoque por remédio
    estoque = Remedio.objects.values('nome').annotate(total=Sum('quantidade')).order_by('-total')
    dados_estoque = [{'nome': e['nome'], 'valor': e['total']} for e in estoque]
    grafico_estoque = gerar_grafico_barras(dados_estoque, 'Volume de Estoque por Remédio', ylabel='Quantidade')

    # 3. Custo total por remédio (preco_compra * quantidade)
    custo = Remedio.objects.annotate(
        custo_total=ExpressionWrapper(
            F('preco_compra') * F('quantidade'),
            output_field=FloatField()
        )
    ).values('nome', 'custo_total').order_by('-custo_total')
    dados_custo = [{'nome': c['nome'], 'valor': c['custo_total']} for c in custo]
    grafico_custo = gerar_grafico_barras(dados_custo, 'Custo Total por Remédio (R$)', ylabel='Valor (R$)')

    # 4. Quantidade de idosos por remédio
    idosos_por_remedio = Remedio.objects.annotate(total=Count('idosos_em_uso')).values('nome', 'total').order_by('-total')
    dados_idosos = [{'nome': i['nome'], 'valor': i['total']} for i in idosos_por_remedio]
    grafico_idosos = gerar_grafico_barras(dados_idosos, 'Quantidade de Idosos por Remédio', ylabel='Número de Idosos')

    return render(request, 'analises/dashboard.html', {
        'grafico_visitas': grafico_visitas,
        'grafico_estoque': grafico_estoque,
        'grafico_custo': grafico_custo,
        'grafico_idosos': grafico_idosos,
    })
