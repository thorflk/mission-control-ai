# Mission Control AI
### Sistema Inteligente de Monitoramento de Missão Espacial
**GS2026.1 — Pensamento Computacional e Automação com Python — FIAP**

---

## Descrição do Projeto

O **Mission Control AI** é um sistema desenvolvido em Python que simula o monitoramento inteligente de uma missão espacial experimental chamada **Prometheus IV**.

O sistema analisa dados de telemetria coletados em ciclos de monitoramento, classifica o estado de cada ciclo automaticamente, gera alertas e recomendações, e apresenta um relatório final completo com estatísticas e tendências da missão.

---

## Equipe

| Thor Ferreira Camargo | RM: 569543 |

| Gabriel Botelho Romão | RM: 570589 |

**Missão:** Prometheus IV
**Equipe:** Equipe Nebula

---

## Narrativa da Missão

A missão Prometheus IV passou por 6 ciclos de monitoramento com a seguinte progressão:

| Ciclo | Descrição | Classificação |
|-------|-----------|---------------|
| Ciclo 1 | Lançamento turbulento — missão já começa com problemas | MISSÃO CRÍTICA |
| Ciclo 2 | Piora inicial — situação se agrava ao máximo | MISSÃO CRÍTICA |
| Ciclo 3 | Recuperação parcial — equipe começa a estabilizar | MISSÃO EM ATENÇÃO |
| Ciclo 4 | Estabilidade — missão normalizada | MISSÃO ESTÁVEL |
| Ciclo 5 | Falha inesperada — novo problema crítico surge | MISSÃO CRÍTICA |
| Ciclo 6 | Colapso dos sistemas — situação insustentável | MISSÃO CRÍTICA |

---

## Métricas Monitoradas

Cada ciclo monitora 5 áreas da missão na seguinte ordem:

| Posição | Métrica | Unidade |
|---------|---------|---------|
| 0 | Temperatura interna | °C |
| 1 | Comunicação com a base | % |
| 2 | Sistema de energia (bateria) | % |
| 3 | Suporte de oxigênio | % |
| 4 | Estabilidade operacional | % |

---

## Regras de Alerta

### Temperatura
| Condição | Classificação | Pontuação |
|----------|---------------|-----------|
| Menor que 18°C | ATENÇÃO | 1 ponto |
| De 18°C a 30°C | NORMAL | 0 pontos |
| De 31°C a 35°C | ATENÇÃO | 1 ponto |
| Maior que 35°C | CRÍTICO | 2 pontos |

### Comunicação
| Condição | Classificação | Pontuação |
|----------|---------------|-----------|
| Menor que 30% | CRÍTICO | 2 pontos |
| De 30% a 59% | ATENÇÃO | 1 ponto |
| 60% ou mais | NORMAL | 0 pontos |

### Bateria
| Condição | Classificação | Pontuação |
|----------|---------------|-----------|
| Menor que 20% | CRÍTICO | 2 pontos |
| De 20% a 49% | ATENÇÃO | 1 ponto |
| 50% ou mais | NORMAL | 0 pontos |

### Oxigênio
| Condição | Classificação | Pontuação |
|----------|---------------|-----------|
| Menor que 80% | CRÍTICO | 2 pontos |
| De 80% a 89% | ATENÇÃO | 1 ponto |
| 90% ou mais | NORMAL | 0 pontos |

### Estabilidade
| Condição | Classificação | Pontuação |
|----------|---------------|-----------|
| Menor que 40% | CRÍTICO | 2 pontos |
| De 40% a 69% | ATENÇÃO | 1 ponto |
| 70% ou mais | NORMAL | 0 pontos |

---

## Pontuação e Classificação dos Ciclos

Cada métrica gera uma pontuação de risco. A soma das 5 métricas classifica o ciclo:

| Pontuação Total | Classificação |
|-----------------|---------------|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

## Funções do Sistema

O projeto contém 9 funções organizadas por responsabilidade:

| Função | Descrição |
|--------|-----------|
| `analisar_temperatura()` | Classifica a temperatura e retorna risco e descrição |
| `analisar_comunicacao()` | Classifica a comunicação e retorna risco e descrição |
| `analisar_bateria()` | Classifica a bateria e retorna risco e descrição |
| `analisar_oxigenio()` | Classifica o oxigênio e retorna risco e descrição |
| `analisar_estabilidade()` | Classifica a estabilidade e retorna risco e descrição |
| `classificar_ciclo()` | Recebe a pontuação total e retorna o status do ciclo |
| `gerar_recomendacao()` | Retorna uma recomendação baseada no status do ciclo |
| `processar_ciclos()` | Loop principal — percorre todos os ciclos e imprime os detalhes |
| `calcular_medias()` | Calcula a média aritmética de cada métrica sem bibliotecas externas |
| `analisar_tendencia()` | Compara o primeiro e último ciclo para identificar a tendência |
| `identificar_area_mais_afetada()` | Identifica a área com maior risco acumulado |
| `gerar_relatorio_final()` | Gera e imprime o relatório final completo |

---

## Como Executar

**Pré-requisitos:** Python 3.x instalado. Nenhuma biblioteca externa é necessária.

```bash
# Clone o repositório
git clone https://github.com/thorflk/mission-control-ai.git

# Entre na pasta
cd mission-control-ai

# Execute o programa
python mission_control.py
```

---

## Estrutura do Repositório

```
mission-control-ai/
├── README.md
└── mission_control.py
```

---

## Informações Acadêmicas

- **Instituição:** FIAP
- **Curso:** Ciência da Computação
- **Disciplina:** Pensamento Computacional e Automação com Python
- **Semestre:** 1º Semestre — GS2026.1

---

## Link Vídeo YouTube

- **Link:** https://youtu.be/qcOai7PDBOs
