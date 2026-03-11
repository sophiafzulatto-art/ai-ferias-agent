# AI Férias Agent

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Agente inteligente em Python para calcular férias de funcionários com base nas regras da CLT brasileira.

---

## Funcionalidades

- Calcula dias de férias conforme faltas do funcionário
- Verifica elegibilidade após 12 meses de trabalho
- Calcula adicional de 1/3 constitucional
- Retorna valores aproximados para pagamento de férias

---

## Como usar

```python
from ferias_agent import FeriasAIAgent

agent = FeriasAIAgent()

resultado = agent.analisar_funcionario(
    nome="Maria Silva",
    salario=4000,
    faltas=2,
    data_admissao="2022-05-01"
)

print(resultado)
