import random


def handle_response(message, username) -> str:
    p_message = message.lower()

    if username == "luxca_":
        print("detectado")
        if p_message.split(" ")[0] == "rolar":
            rollRequest = p_message.split(" ")
            rollRequest = rollRequest[1].split("d")
            if int(rollRequest[0]) != 1:
                results = []
                for i in range(0,int(rollRequest[0])):
                    results.append(random.randint(0,int(rollRequest[1])))
                return f'{username} rolou: {results}'
            else:
                result = random.randint(1,int(rollRequest[1]))
                return f'{username} rolou: **{result}**'    
            
        if p_message.split(" ")[0] == "rola":
            return 'hmmmm viadinho kkkk, rola?'

        if p_message == 'rolar 1d20':
            return f'@{username} rolou 1d20, \nresultado: **{random.randint(1,20)}**'
        
        # TESTES  MAGNUS <<<<----
        # ------------ TESTE DE PRESENÇA --------------------
        if p_message.lower() == 'teste de presença' or p_message.lower() == "tdp":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Magnus | Presença: **1**, Resultado: **{results}**"
        
        # ------------- TESTE DE AGILIDADE ------------------
        if p_message.lower() == 'teste de agilidade' or p_message.lower() == "tda":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Magnus | Agilidade: **1**, Resultado: **{results}**"
            
        # ------------ TESTE DE INTELIGENCIA -----------------
        if p_message.lower() == 'teste de inteligência' or p_message.lower() == "tdi":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Magnus | Inteligência: **1**, Resultado: **{results}**"
        
        # ------------ TESTE DE VIGOR -----------------
        if p_message.lower() == 'teste de vigor' or p_message.lower() == "tdv":
            results = []
            for i in range(0,4):
                    results.append(random.randint(1,20))
            return f"Magnus | vigor: **4**, Resultado: **{results}**"
        
        # ------------ TESTE DE FORÇA -----------------
        
        if p_message.lower() == 'teste de força' or p_message.lower() == "tdf":
            results = []
            for i in range(0,4):
                    results.append(random.randint(1,20))
            return f"Magnus | força: **4**, Resultado: **{results}**"
        
        # -------------- INICIATIVA ------------------
        if p_message.lower() == 'teste de iniciativa' or p_message.lower() == "tdini":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Magnus | bonus iniciativa: **5**, Resultado: **{results}**"
        
        # --------------- RESISTÊNCIA ----------------
        if p_message.lower() == 'teste de resistência' or p_message.lower() == "tdres":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            results.sort()
            return f"Magnus | Vontade: **10**, Dados: **{results}**\nResultado Final: {results[-1] + 10}"
        

        # ----------- DEBUG -------------------------
        if p_message.lower() == "teste":
             return f'Eca sai {username}, você nao é o meu deus gostoso **Lucas Fernandes**\n(desculpa, é que na real o lucas nao me programou para\nacessar os dados do seu personagem...)\n--Na proxima sessao quem sabe... S2'
        


    else:
        if p_message.split(" ")[0] == "rolar":
            if username != "luxca_":
                return f'Eca sai {username}, você nao é o meu deus gostoso **Lucas Fernandes**\n(desculpa, é que na real o lucas nao me programou para\nacessar os dados do seu personagem...)\n--Na proxima sessao quem sabe... S2'
        else:
            print("mensagem negada")
    

    """
    # TESTES  LUCIO <<<<----
        # ------------ TESTE DE PRESENÇA --------------------
        if p_message.lower() == 'teste de presença' or p_message.lower() == "tdp":
            results = []
            for i in range(0,4):
                    results.append(random.randint(1,20))
            return f"Lucio | Presença: **4**, Resultado: **{results}**"
        
        # ------------- TESTE DE AGILIDADE ------------------
        if p_message.lower() == 'teste de agilidade' or p_message.lower() == "tda":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Lucio | Agilidade: **4**, Resultado: **{results}**"
            
        # ------------ TESTE DE INTELIGENCIA -----------------
        if p_message.lower() == 'teste de inteligência' or p_message.lower() == "tdi":
            results = []
            for i in range(0,4):
                    results.append(random.randint(1,20))
            return f"Lucio | Inteligência: **4**, Resultado: **{results}**"
        
        # ------------ TESTE DE VIGOR -----------------
        if p_message.lower() == 'teste de vigor' or p_message.lower() == "tdv":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Lucio | vigor: **1**, Resultado: **{results}**"
        
        # ------------ TESTE DE FORÇA -----------------
        
        if p_message.lower() == 'teste de força' or p_message.lower() == "tdf":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Lucio | força: **1**, Resultado: **{results}**"
        
        if p_message.lower() == 'teste de iniciativa' or p_message.lower() == "tdini":
            results = []
            for i in range(0,1):
                    results.append(random.randint(1,20))
            return f"Lucio | bonus iniciativa: **0**, Resultado: **{results}**"
        
        if p_message.lower() == 'teste de resistência' or p_message.lower() == "tdres":
            results = []

            for i in range(0,4):
                    results.append(random.randint(1,20))
            results.sort()

            return f"Lucio | Vontade = 10: **0**, Dados: **{results}**\nResultado Final: {results[-1] + 10}"
    
    """
    
    # # CHECAR
    # if p_message.split(" ")[0] == "rolar":
    #     rollRequest = p_message.split(" ")
    #     rollRequest = rollRequest[1].split("d")
    #     if int(rollRequest[0]) != 1:
    #         results = []
    #         for i in range(0,int(rollRequest[0])):
    #             results.append(random.randint(0,int(rollRequest[1])))
    #         return f'{username} rolou: {results}'
    #     else:
    #         result = random.randint(1,int(rollRequest[1]))
    #         return f'{username} rolou: **{result}**'
    
    
    # else:
    #     print(f'{username} disse: p_message')
    #  return 'Yeah, I don\'t know. Try typing "!help".'
