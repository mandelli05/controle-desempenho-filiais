print("CONTROLE DE DESEMPENHO DE FILIAIS")
print("Matheus Mandelli")

filiais = ["Filial Domingos Martins", "Filial Vitoria", "Filial Vila Velha"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

faturamento = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

clientes = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

opcao = -1
while opcao != 0:
    print("""Escolha uma opção:
[1] Cadastrar dados
[2] Relatório de desempenho
[3] Atualizar dados financeiros
[4] Buscar dados
[0] Sair""")
    
    try:
        opcao_entrada = input("\nEscolha a opção desejada: ").strip()
        
        if opcao_entrada == "":
            print("Erro: Digite uma opção.\n")
            continue
        
        opcao = int(opcao_entrada)
        
        if opcao == 1:
            confirmacao = input("Isso vai sobrescrever os dados existentes. Continuar? (s/n): ")
            if confirmacao.lower() == 's':
                for i in range(3):
                    print(f"\n--- Cadastrando dados da {filiais[i]} ---")
                    for j in range(4):
                        valor_valido = False
                        while not valor_valido:
                            try:
                                valor = float(input(f"Faturamento da {filiais[i]} - {semanas[j]} (R$): "))
                                if valor < 0:
                                    print("Erro: Valor não pode ser negativo. Tente novamente.")
                                else:
                                    faturamento[i][j] = valor
                                    valor_valido = True
                            except ValueError:
                                print("Erro: Digite um número válido. Tente novamente.")
                        
                        qtd_valido = False
                        while not qtd_valido:
                            try:
                                qtd = int(input(f"Clientes da {filiais[i]} - {semanas[j]}: "))
                                if qtd < 0:
                                    print("Erro: Quantidade não pode ser negativa. Tente novamente.")
                                else:
                                    clientes[i][j] = qtd
                                    qtd_valido = True
                            except ValueError:
                                print("Erro: Digite um número inteiro válido. Tente novamente.")
                
                print("\nDados cadastrados com sucesso!\n")
            else:
                print("Cadastro cancelado.\n")
        
        elif opcao == 2:
            print("\n" + "="*60)
            print("RELATÓRIO DE DESEMPENHO")
            print("="*60)
            
            for i in range(3):
                print(f"\n{filiais[i]}")
                print("-" * 60)
                for j in range(4):
                    print(f"{semanas[j]:12} - Faturamento: R$ {faturamento[i][j]:10,.2f} - Clientes: {clientes[i][j]:3}")
            
            print("\n")
        
        elif opcao == 3:
            print("\n--- Atualizar Dados ---")
            
            matriz_valida = False
            while not matriz_valida:
                matriz_opcao = input("O que deseja atualizar? (1-Faturamento / 2-Clientes): ").strip()
                if matriz_opcao in ['1', '2']:
                    matriz = int(matriz_opcao)
                    matriz_valida = True
                else:
                    print("Erro: Digite 1 ou 2.\n")
            
            print("\nQual filial?")
            for i in range(3):
                print(f"[{i}] {filiais[i]}")
            
            linha_valida = False
            while not linha_valida:
                try:
                    linha = int(input("Escolha a filial: "))
                    if linha in [0, 1, 2]:
                        linha_valida = True
                    else:
                        print("Erro: Escolha entre 0, 1 ou 2.\n")
                except ValueError:
                    print("Erro: Digite um número inteiro válido.\n")
            
            print("\nQual semana?")
            for j in range(4):
                print(f"[{j}] {semanas[j]}")
            
            coluna_valida = False
            while not coluna_valida:
                try:
                    coluna = int(input("Escolha a semana: "))
                    if coluna in [0, 1, 2, 3]:
                        coluna_valida = True
                    else:
                        print("Erro: Escolha entre 0, 1, 2 ou 3.\n")
                except ValueError:
                    print("Erro: Digite um número inteiro válido.\n")
            
            if matriz == 1:
                novo_valido = False
                while not novo_valido:
                    try:
                        novo = float(input("Novo valor de faturamento (R$): "))
                        if novo < 0:
                            print("Erro: Valor não pode ser negativo. Tente novamente.")
                        else:
                            faturamento[linha][coluna] = novo
                            print("Faturamento atualizado com sucesso!\n")
                            novo_valido = True
                    except ValueError:
                        print("Erro: Digite um número válido. Tente novamente.")
            
            elif matriz == 2:
                novo_valido = False
                while not novo_valido:
                    try:
                        novo = int(input("Nova quantidade de clientes: "))
                        if novo < 0:
                            print("Erro: Quantidade não pode ser negativa. Tente novamente.")
                        else:
                            clientes[linha][coluna] = novo
                            print("Clientes atualizado com sucesso!\n")
                            novo_valido = True
                    except ValueError:
                        print("Erro: Digite um número inteiro válido. Tente novamente.")
        
        elif opcao == 4:
            meta_valida = False
            while not meta_valida:
                try:
                    meta = float(input("Mostrar semanas com faturamento acima de (R$): "))
                    if meta < 0:
                        print("Erro: Valor não pode ser negativo. Tente novamente.")
                    else:
                        meta_valida = True
                except ValueError:
                    print("Erro: Digite um número válido. Tente novamente.")
            
            print("\n" + "="*60)
            print(f"Filiais com faturamento acima de R$ {meta:,.2f}")
            print("="*60)
            
            encontrou = False
            for i in range(3):
                for j in range(4):
                    if faturamento[i][j] > meta:
                        print(f"{filiais[i]:30} - {semanas[j]:12} - R$ {faturamento[i][j]:,.2f}")
                        encontrou = True
            
            if not encontrou:
                print("Nenhum resultado encontrado.")
            
            print()
        
        elif opcao == 0:
            print("Programa encerrado. Até logo!")
        
        else:
            print("Erro: Opção inválida. Escolha entre 0 e 4.\n")
    
    except ValueError:
        print("Erro: Digite um número inteiro válido.\n")
    except Exception as erro:
        print(f"Erro inesperado: {erro}\n")
