# ============================================================
# MISSION CONTROL AI
# Sistema Inteligente de Monitoramento de Missão Espacial
# ============================================================
 
# --- IDENTIDADE DA MISSÃO ---
NOME_MISSAO = "Prometheus IV"
NOME_EQUIPE = "Equipe Nebula"
 
# --- ÁREAS MONITORADAS ---
# Cada índice corresponde a uma coluna da matriz dados_missao:
#   índice 0 → temperatura
#   índice 1 → comunicação
#   índice 2 → bateria
#   índice 3 → oxigênio
#   índice 4 → estabilidade
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]
 
# --- MATRIZ PRINCIPAL DE DADOS ---
# Cada linha = 1 ciclo | Cada coluna: [temp, com, bat, oxi, est]
#
# Ciclo 1 — Lançamento turbulento  → missão já começa com problemas
# Ciclo 2 — Piora inicial          → situação se agrava
# Ciclo 3 — Recuperação parcial    → equipe começa a estabilizar
# Ciclo 4 — Estabilidade           → missão normalizada
# Ciclo 5 — Falha inesperada       → novo problema crítico
# Ciclo 6 — Colapso dos sistemas   → situação insustentável
dados_missao = [
    [36, 45, 38, 85, 55],   # Ciclo 1 — turbulento
    [39, 27, 19, 79, 34],   # Ciclo 2 — crítico
    [31, 58, 52, 88, 65],   # Ciclo 3 — recuperando
    [25, 74, 78, 93, 82],   # Ciclo 4 — estável
    [38, 31, 22, 81, 42],   # Ciclo 5 — falha inesperada
    [41, 24, 15, 76, 30],   # Ciclo 6 — colapso
]
 
 
# ============================================================
# FUNÇÕES DE ANÁLISE INDIVIDUAL
# ============================================================
# Cada função retorna TRÊS valores agora:
#   1. classificação → "NORMAL", "ATENÇÃO" ou "CRÍTICO"
#   2. risco         → 0, 1 ou 2
#   3. descrição     → texto explicativo para o terminal
# ============================================================
 
def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura baixa demais"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"
 
def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"
 
def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"
 
def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"
 
def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"
 
 
# ============================================================
# FUNÇÕES DE CLASSIFICAÇÃO E PROCESSAMENTO
# ============================================================
 
def classificar_ciclo(pontuacao_total):
    if pontuacao_total <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao_total <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"
 
 
def gerar_recomendacao(classificacao_ciclo):
    if classificacao_ciclo == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."
    elif classificacao_ciclo == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."
 
 
def processar_ciclos():
    # Percorre cada linha da matriz, chama as funções de análise,
    # acumula os riscos por área e imprime o detalhamento de cada ciclo.
    #
    # Retorna:
    #   riscos_por_ciclo → pontuação total de cada ciclo
    #   riscos_por_area  → pontuação acumulada de cada área
 
    riscos_por_area  = [0, 0, 0, 0, 0]
    riscos_por_ciclo = []
 
    for numero, ciclo in enumerate(dados_missao, start=1):
 
        temperatura  = ciclo[0]
        comunicacao  = ciclo[1]
        bateria      = ciclo[2]
        oxigenio     = ciclo[3]
        estabilidade = ciclo[4]
 
        # Cada função retorna 3 valores: classificação, risco e descrição
        class_temp, risco_temp, desc_temp = analisar_temperatura(temperatura)
        class_com,  risco_com,  desc_com  = analisar_comunicacao(comunicacao)
        class_bat,  risco_bat,  desc_bat  = analisar_bateria(bateria)
        class_oxi,  risco_oxi,  desc_oxi  = analisar_oxigenio(oxigenio)
        class_est,  risco_est,  desc_est  = analisar_estabilidade(estabilidade)
 
        pontuacao_total = risco_temp + risco_com + risco_bat + risco_oxi + risco_est
 
        riscos_por_area[0] += risco_temp
        riscos_por_area[1] += risco_com
        riscos_por_area[2] += risco_bat
        riscos_por_area[3] += risco_oxi
        riscos_por_area[4] += risco_est
 
        riscos_por_ciclo.append(pontuacao_total)
 
        classificacao = classificar_ciclo(pontuacao_total)
        recomendacao  = gerar_recomendacao(classificacao)
 
        print(f"\nCICLO {numero}")
        print("-" * 60)
        print(f"Temperatura:  {temperatura}°C | {class_temp} | {desc_temp}")
        print(f"Comunicação:  {comunicacao}%  | {class_com} | {desc_com}")
        print(f"Bateria:      {bateria}%  | {class_bat} | {desc_bat}")
        print(f"Oxigênio:     {oxigenio}%  | {class_oxi} | {desc_oxi}")
        print(f"Estabilidade: {estabilidade}%  | {class_est} | {desc_est}")
        print(f"\nPontuação de risco do ciclo: {pontuacao_total}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {recomendacao}")
 
    return riscos_por_ciclo, riscos_por_area
 
 
# ============================================================
# FUNÇÕES DE CÁLCULO ESTATÍSTICO E TENDÊNCIA
# ============================================================
 
def calcular_medias():
    total_ciclos = len(dados_missao)
 
    media_temp = sum([ciclo[0] for ciclo in dados_missao]) / total_ciclos
    media_com  = sum([ciclo[1] for ciclo in dados_missao]) / total_ciclos
    media_bat  = sum([ciclo[2] for ciclo in dados_missao]) / total_ciclos
    media_oxi  = sum([ciclo[3] for ciclo in dados_missao]) / total_ciclos
    media_est  = sum([ciclo[4] for ciclo in dados_missao]) / total_ciclos
 
    return media_temp, media_com, media_bat, media_oxi, media_est
 
 
def analisar_tendencia(riscos_por_ciclo):
    # Compara o risco do primeiro ciclo com o do último
    # riscos_por_ciclo[-1] → índice -1 sempre aponta pro último elemento
    primeiro = riscos_por_ciclo[0]
    ultimo   = riscos_por_ciclo[-1]
 
    if ultimo > primeiro:
        return "A missão apresentou tendência de PIORA."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de MELHORA."
    else:
        return "A missão permaneceu ESTÁVEL em relação ao início."
 
 
def identificar_area_mais_afetada(riscos_por_area):
    # max() encontra o maior valor da lista
    # .index() encontra em qual posição esse valor está
    # areas_monitoradas[indice] busca o nome daquela área
    maior_risco = max(riscos_por_area)
    indice      = riscos_por_area.index(maior_risco)
    area        = areas_monitoradas[indice]
 
    return area, maior_risco
 
 
# ============================================================
# RELATÓRIO FINAL
# ============================================================
 
def gerar_relatorio_final(riscos_por_ciclo, riscos_por_area):
 
    medias                         = calcular_medias()
    tendencia                      = analisar_tendencia(riscos_por_ciclo)
    area_mais_afetada, pontos_area = identificar_area_mais_afetada(riscos_por_area)
 
    # --- Ciclo mais crítico ---
    maior_pontuacao = max(riscos_por_ciclo)
    ciclo_critico   = riscos_por_ciclo.index(maior_pontuacao) + 1
 
    # --- Risco médio da missão ---
    risco_medio = sum(riscos_por_ciclo) / len(riscos_por_ciclo)
 
    # --- Quantidade de ciclos críticos ---
    ciclos_criticos = 0
    for risco in riscos_por_ciclo:
        if risco >= 6:
            ciclos_criticos += 1
 
    # --- Classificação final baseada no risco médio ---
    classificacao_final = classificar_ciclo(risco_medio)
 
    # --- Conclusão automática baseada na classificação final ---
    if classificacao_final == "MISSÃO ESTÁVEL":
        conclusao = (
            "A missão transcorreu dentro dos parâmetros esperados. "
            "Todos os sistemas operaram de forma adequada e não foram "
            "registradas ocorrências críticas. Recomenda-se manter o "
            "monitoramento de rotina."
        )
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        conclusao = (
            "A missão apresentou instabilidade relevante durante a operação. "
            "Apesar de períodos de recuperação, ainda existem sistemas em "
            "atenção e a equipe deve manter o plano de contingência ativo."
        )
    else:
        conclusao = (
            "A missão operou em estado crítico durante parte significativa "
            "dos ciclos monitorados. A equipe deve acionar imediatamente os "
            "protocolos de emergência e priorizar o restabelecimento dos "
            "sistemas essenciais antes de retomar operações normais."
        )
 
    # --- Impressão do relatório ---
    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
 
    print(f"\nMissão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
 
    print(f"\nMédia de temperatura:  {medias[0]:.2f}°C")
    print(f"Média de comunicação:  {medias[1]:.2f}%")
    print(f"Média de bateria:      {medias[2]:.2f}%")
    print(f"Média de oxigênio:     {medias[3]:.2f}%")
    print(f"Média de estabilidade: {medias[4]:.2f}%")
 
    print(f"\nCiclo mais crítico:       Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_pontuacao}")
    print(f"Risco médio da missão:    {risco_medio:.2f}")
    print(f"Ciclos críticos:          {ciclos_criticos} de {len(dados_missao)}")
 
    print(f"\nTendência da missão:")
    print(f"  {tendencia}")
 
    print(f"\nPontuação acumulada por área:")
    for i in range(len(areas_monitoradas)):
        destaque = " ←" if areas_monitoradas[i] == area_mais_afetada else ""
        print(f"  {areas_monitoradas[i]}: {riscos_por_area[i]} pontos{destaque}")
 
    print(f"\nÁrea mais afetada:")
    print(f"  {area_mais_afetada} ({pontos_area} pontos)")
 
    print(f"\nClassificação final da missão:")
    print(f"  {classificacao_final}")
 
    print(f"\nConclusão:")
    print(f"  {conclusao}")
 
    print("\n" + "=" * 60)
 
 
# ============================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================
 
print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {NOME_MISSAO}")
print(f"Equipe: {NOME_EQUIPE}")
print(f"Ciclos analisados: {len(dados_missao)}")
 
riscos_por_ciclo, riscos_por_area = processar_ciclos()
 
gerar_relatorio_final(riscos_por_ciclo, riscos_por_area)