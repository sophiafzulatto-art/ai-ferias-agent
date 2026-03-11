from regras_clt import calcular_dias_ferias, calcular_valor_ferias, data_elegivel


class FeriasAIAgent:

    def analisar_funcionario(self, nome, salario, faltas, data_admissao):

        elegivel = data_elegivel(data_admissao)

        if not elegivel:
            return {
                "funcionario": nome,
                "status": "Ainda não possui 12 meses trabalhados."
            }

        dias = calcular_dias_ferias(faltas)
        valores = calcular_valor_ferias(salario)

        return {
            "funcionario": nome,
            "dias_de_ferias": dias,
            "salario_base": valores["salario_base"],
            "adicional_1_3": valores["adicional_1_3"],
            "total_receber": valores["total_ferias"]
        }
