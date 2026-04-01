print("Bem-vindo ao sistema de controle de acesso - Desenvolvido por Valeria")


tipo_usuario = input("Você é membro ou visitante? ").strip().lower()


dia = input("Informe o dia da semana (ex: segunda, terca, sabado): ").strip().lower()
hora = int(input("Informe a hora atual (0 a 23): "))


acesso_permitido = False
motivo = ""


if 9 <= hora <= 18:
    
    
    if dia in ["segunda", "terca", "quarta", "quinta", "sexta"]:
        
        if tipo_usuario == "membro":
          
            acesso_permitido = True
        
        elif tipo_usuario == "visitante":
          
            tempo = int(input("Quantas horas deseja permanecer? "))
            
            if tempo <= 4:
                acesso_permitido = True
            else:
                motivo = "Visitantes só podem permanecer até 4 horas."
        
        else:
            motivo = "Tipo de usuário inválido."
    elif dia in ["sabado", "domingo"]:
        
        if tipo_usuario == "membro":
            acesso_permitido = True
        else:
            motivo = "Apenas membros têm acesso no fim de semana."

    else:
        motivo = "Dia da semana inválido."

else:
    motivo = "Fora do horário comercial (9h às 18h)."


if acesso_permitido:
    print("Acesso permitido. Seja bem-vindo!")
else:
    print("Acesso negado.")
    print("Motivo:", motivo)