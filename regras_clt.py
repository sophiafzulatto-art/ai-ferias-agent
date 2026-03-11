from datetime import datetime

def calcular_dias_ferias(faltas):
    if faltas <= 5:
        return 30
    elif faltas <= 14:
        return 24
    elif faltas <= 23:
        return 18
    elif faltas <= 32:
        return 12
    else:
        return 0


def calcular_valor_ferias(salario):
    adicional = salario / 3
    total = salario + adicional
    return {
        "salario_base": salario,
        "adicional_1_3": adicional,
        "total_ferias": total
    }


def data_elegivel(data_admissao):
    hoje = datetime.today()
    admissao = datetime.strptime(data_admissao, "%Y-%m-%d")

    dias_trabalhados = (hoje - admissao).days

    return dias_trabalhados >= 365
