from ferias_agent import FeriasAIAgent

agent = FeriasAIAgent()

resultado = agent.analisar_funcionario(
    nome="João Silva",
    salario=3500,
    faltas=3,
    data_admissao="2023-01-10"
)

print(resultado)
