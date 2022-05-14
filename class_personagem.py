# ########### Personagem #############
import random

class Personagem:

    def __init__(self):
        self.informacoes_iniciais = {}
        self.atributos = {}
        self.vantagens = {}
        self.vida = []
        self.pericias = {}
        self.vantagem_magica = []
        self.equipamentos = []
        self.escolhas_iniciais()
        self.distribuicao_pontos()
        self.caminho_da_vida()
        self.info_profissao()
        self.pericias

    def escolhas_iniciais(self):
        # 1) Nome do Jogador
        nome_jogador = input("Nome do jogador: ")
        info_nome_jogador = {"Nome do jogador": nome_jogador}
        self.informacoes_iniciais.update(info_nome_jogador)

        # 2) Nome do Personagem
        nome_personagem = input("Nome do personagem: ")
        info_nome_personagem = {"Nome do personagem": nome_personagem}
        self.informacoes_iniciais.update(info_nome_personagem)

        # 3) Sexo
        escolhas_iniciais_a = int(input('Qual o sexo do seu personagem:\n'
                                        '1 - Masculino\n'
                                        '2 - Feminino.\n'
                                        '---> '))
        if escolhas_iniciais_a == 1:
            sexo = "Masculino"
        else:
            sexo = "Feminino"
        info_sexo = {"Sexo": sexo}
        self.informacoes_iniciais.update(info_sexo)

        # 4) Raça
        escolher_raca_a = int(input("Qual a raça do seu personagem:\n"
                                    "1 - Humano;\n"
                                    "2 - Elfo;\n"
                                    "3 - Anão;\n"
                                    "4 - Ananico;\n"
                                    "5 - Bruxo.\n"
                                    "---> "))
        if escolher_raca_a == 1:
            raca = "humano"
        elif escolher_raca_a == 2:
            raca = "elfo"
        elif escolher_raca_a == 3:
            raca = "anão"
        elif escolher_raca_a == 4:
            raca = "ananico"
        elif escolher_raca_a == 5:
            raca = "bruxo"
        info_raca = {"Raça": raca}
        self.informacoes_iniciais.update(info_raca)

        # 5) Vantagens - Raca
        dicio_vantagens = {
            "Confiável": "Em um mundo onde não-humanos não podem ser confiados, os humanos parecem mais confiáveis. "
                         "Os humanos têm +1 em testes de Carisma, Sedução e Persuação contra outros humanos.",
            "Ingenuidade": "Os humanos são inteligentes e, no geral, têm soluções brilhantes para problemas difíceis. "
                           "Os humanos ganham +1 em Dedução.",
            "Cegamente Teimoso": "Parte da grande força da raça humana é a sua interminável disposição de seguir em"
                                 " frente, mesmo em situações que verdadeiramente ameaçam a sua vida. Um humano pode "
                                 "invocar a sua coragem e jogar novamente uma jogada fracassada de Resistir Coerção "
                                 "ou Coragem por três vezes por sessão de jogo. Eles ficam com o resultado maior das "
                                 "duas jogadas, mas se ainda assim fracassarem, não podem usar novamente a habilidade"
                                 " para fazer a jogada.",
            "Artístico": "Os elfos tem um olho bom para beleza e um talento para empreitadas artísticas. Os elfos "
                         "ganham +1 em sua perícia Belas Artes.",
            "Atirador": "Anos de tradição e treino tornaram os elfos uns dos melhores arqueiros do mundo. Os elfos "
                        "ganham +2 em sua perícia Arcos e Flecha e podem sacar e colocar corda sem contar como uma "
                        "ação.",
            "Sintonia com a Natureza": "Os elfos têm uma ligação mágica profunda com a natureza. Os elfos não "
                                       "perturbam os animais, o que significa que qualquer fera encontrada é "
                                       "considerada amigável e não atacará, a menos que seja provocada. Os elfos também"
                                       " encontram automaticamente qualquer substância de planta com disponibilidade "
                                       "comum (ou menos) que eles estejam procurando, desde que a substância exista "
                                       "naturalmente no terreno em questão.",
            "Durão": "Ao passar muito do seu tempo nas montanhas e minas, os anões têm naturalmente uma pele dura. "
                     "Dessa maneira, a pele de um anão tem o poder de parada natural de 2. Esse PP é adicionado a "
                     "qualquer PP de armadura já existente e não pode sofrer dano de ablação.",
            "Forte": "Pelo seu porte compacto e gosto por profissões que exigem muito preparo físico, os anões ganham"
                     " +1 na perícia Físico e aumentam seu Fardo em 25.",
            "Olho de Artesão": "Com um olho para detalhes minuciosos e apreciação é difícil blefar com um anão. Os "
                               "anões têm +1 em sua perícia de Negócios.",
            "Ágil": "Os ananicos são naturalmente ágeis e habilidosos. Eles ganham +1 em sua perícia de Atletismo.",
            "Dedo Verde": "Os ananicos são atraídos geralmente para a agricultura, graças a anos de tradição e uma "
                          "aptidão aparentemente inata em criar animais. Eles ganham +2 em sua perícia de Sobrevivência"
                          " no Ermo e quando estão acalmando, adestrando, ou controlando animais.",
            "Resistência a Magia": "Por razões desconhecidas, os ananicos são resistentes a certas forças mágicas. Eles"
                                   " ganham +5 em sua perícia de Resistir a Magia e são capazes de jogar Resistir a "
                                   "Magia para negar os efeitos de quaisquer fetiços que afetariam a sua mente, mesmo "
                                   "se normalmente não gosse permitido. No entanto, poções de bruxo e outras poções "
                                   "máicas não afetam positivamente os ananicos (até mesmo se tiverem sucesso num "
                                   "teste de Tolerância).",
            "Sentidos Melhorados": "Por causa de seus sentidos avançados, os bruxos não sofrem penalidades em áreas de "
                                   "pouca luz e ganha +1 em sua perícia de Consciência e a habilidade de rastrear "
                                   "coisas somente através do cheiro.",
            "Mutação Resiliente": "Depois de todas as mutações necessárias para se tornar um bruxo, eles ficam imunes"
                                  " a doenças e são capazes de usar mutagênicos.",
            "Emoções Dessensibilizadas": "Graças a trauma e mutação. as emoções de um bruxo ficam dessensibilizadas. Os"
                                         " bruxos não precisam realizar testes de coragem contra Intimidação, mas eles"
                                         " tem um -4 em sua estatística de Empatia. Isso não pode levar a Empatia para "
                                         "menos do que 1.",
            "Reflexos Relâmpago": "Depois de treinamento intensivo e mutação, os bruxos ficam mais rápidos e mais ágeis"
                                  " do que humanos. Eles ganham um permanente +1 em seu Reflexo e Destreza que pode "
                                  "levar ambas as estatísticas para além de 10.",
        }
        raca_vantagens = raca
        if raca_vantagens == "humano":
            self.vantagens = {x: dicio_vantagens[x] for x in dicio_vantagens if x in ("Confiável",
                                                                                      "Ingenuidade",
                                                                                      "Cegamente Teimoso")}
        elif raca_vantagens == "elfo":
            self.vantagens = {x: dicio_vantagens[x] for x in dicio_vantagens if x in ("Artístico",
                                                                                      "Atirador",
                                                                                      "Sintonia com a Natureza")}
        elif raca_vantagens == "anão":
            self.vantagens = {x: dicio_vantagens[x] for x in dicio_vantagens if x in ("Durão",
                                                                                      "Forte",
                                                                                      "Olho de Artesão")}
        elif raca_vantagens == "ananico":
            self.vantagens = {x: dicio_vantagens[x] for x in dicio_vantagens if x in ("Ágil",
                                                                                      "Dedo Verde",
                                                                                      "Resistência a Magia")}
        elif raca_vantagens == "bruxo":
            self.vantagens = {x: dicio_vantagens[x] for x in dicio_vantagens if x in ("Sentidos Melhorados",
                                                                                      "Mutação Resiliente",
                                                                                      "Emoções Dessensibilizadas",
                                                                                      "Reflexos Relâmpago")}

        # 6) Profissão
        if raca == "bruxo":
            profissao = "bruxo"
            info_profissao = {"Profissão": profissao}
            self.informacoes_iniciais.update(info_profissao)
        else:
            prof = ["0", "bardo", "artesão", "criminoso", "doutor",
                    "mago", "homem de armas", "comerciante", "sacerdote", "nobre"]
            escolhas_iniciais_c = int(input("Qual a profissão do seu personagem:\n"
                                            "1 - Bardo;\n"
                                            "2 - Artesão;\n"
                                            "3 - Criminoso;\n"
                                            "4 - Doutor;\n"
                                            "5 - Mago;\n"
                                            "6 - Homem de Armas;\n"
                                            "7 - Comerciante;\n"
                                            "8 - Sacerdote;\n"
                                            "9 - Nobre.\n----> "))
            info_profissao = {"Profissão": prof[escolhas_iniciais_c]}
            self.informacoes_iniciais.update(info_profissao)

    def distribuicao_pontos(self):
        valor_3 = int(input("Como você gostaria de distribuir seus pontos?\n"
                            "1 - rolar dados para cada estatística;\n"
                            "2 - distribuir pontos manualmente.\n"
                            "---> "))
        if valor_3 == 1:
            inteligencia = random.randint(3, 10)
            info_inteligencia = {"Inteligência": inteligencia}
            self.atributos.update(info_inteligencia)

            reflexos = random.randint(3, 10)
            info_reflexos = {"Reflexos": reflexos}
            self.atributos.update(info_reflexos)

            destreza = random.randint(3, 10)
            info_destreza = {"Destreza": destreza}
            self.atributos.update(info_destreza)

            corpo = random.randint(3, 10)
            info_corpo = {"Corpo": corpo}
            self.atributos.update(info_corpo)

            velocidade = random.randint(3, 10)
            info_velocidade = {"Velocidade": velocidade}
            self.atributos.update(info_velocidade)

            empatia = random.randint(3, 10)
            info_empatia = {"Empatia": empatia}
            self.atributos.update(info_empatia)

            criar = random.randint(3, 10)
            info_criar = {"Criar": criar}
            self.atributos.update(info_criar)

            vontade = random.randint(3, 10)
            info_vontade = {"Vontade": vontade}
            self.atributos.update(info_vontade)

            sorte = random.randint(3, 10)
            info_sorte = {"Sorte": sorte}
            self.atributos.update(info_sorte)

        else:
            self.atributos = {}
            validacao_1 = False
            while not validacao_1:
                tipo_de_partida = int(input("Escolha um entre os seguintes tipos de personagem:\n"
                                            "1 - Comum, 2 - Habilidoso, 3 - Herói ou 4 - Lenda.\n"
                                            "---> "))
                if tipo_de_partida == 4:
                    pontos = 80
                elif tipo_de_partida == 3:
                    pontos = 75
                elif tipo_de_partida == 2:
                    pontos = 70
                else:
                    pontos = 60
                print(f"Total de pontos a distribuir: {pontos} totais.\nCada atributo pode ter no máximo 10 pontos.")
                inteligencia = int(input("Inteligência(1/9): Digite um valor de 1 a 10.\n---> "))
                if inteligencia > 10:
                    inteligencia = 10
                info_inteligencia = {"Inteligência": inteligencia}
                self.atributos.update(info_inteligencia)
                pontos -= inteligencia
                print(f"faltam {pontos} pontos.")
                reflexos = int(input("Reflexos(2/9): Digite um valor de 1 a 10.\n---> "))
                if reflexos > 10:
                    reflexos = 10
                info_reflexos = {"Reflexos": reflexos}
                self.atributos.update(info_reflexos)
                pontos -= reflexos
                print(f"faltam {pontos} pontos.")
                destreza = int(input("Destreza(3/9): Digite um valor de 1 a 10.\n---> "))
                if destreza > 10:
                    destreza = 10
                info_destreza = {"Destreza": destreza}
                self.atributos.update(info_destreza)
                pontos -= destreza
                print(f"faltam {pontos} pontos.")
                corpo = int(input("Corpo(4/9): Digite um valor de 1 a 10.\n---> "))
                if corpo > 10:
                    corpo = 10
                info_corpo = {"Corpo": corpo}
                self.atributos.update(info_corpo)
                pontos -= corpo
                print(f"faltam {pontos} pontos.")
                velocidade = int(input("Velocidade(5/9): Digite um valor de 1 a 10.\n---> "))
                if velocidade > 10:
                    velocidade = 10
                info_velocidade = {"Velocidade": velocidade}
                self.atributos.update(info_velocidade)
                pontos -= velocidade
                print(f"faltam {pontos} pontos.")
                empatia = int(input("Empatia(6/9): Digite um valor de 1 a 10.\n---> "))
                if empatia > 10:
                    empatia = 10
                info_empatia = {"Empatia": empatia}
                self.atributos.update(info_empatia)
                pontos -= empatia
                print(f"faltam {pontos} pontos.")
                criar = int(input("Criar(7/9): Digite um valor de 1 a 10.\n---> "))
                if criar > 10:
                    criar = 10
                info_criar = {"Criar": criar}
                self.atributos.update(info_criar)
                pontos -= criar
                print(f"faltam {pontos} pontos.")
                vontade = int(input("Vontade(8/9): Digite um valor de 1 a 10.\n---> "))
                if vontade > 10:
                    vontade = 10
                info_vontade = {"Vontade": vontade}
                self.atributos.update(info_vontade)
                pontos -= vontade
                print(f"faltam {pontos} pontos.")
                sorte = int(input("Sorte(9/9): Digite um valor de 1 a 10.\n---> "))
                if sorte > 10:
                    sorte = 10
                info_sorte = {"Sorte": sorte}
                self.atributos.update(info_sorte)
                pontos -= sorte

                if pontos < 0:
                    print("A quantidade de pontos distribuídos foi além do limite disponível.\n"
                          "Refaça a distribuição de pontos.")
                    validade_1 = False
                else:
                    validacao_2 = input(f"Inteligência: {inteligencia}\n"
                                        f"Reflexos: {reflexos}\n"
                                        f"Destreza: {destreza}\n"
                                        f"Corpo: {corpo}\n"
                                        f"Velocidade: {velocidade}\n"
                                        f"Empatia: {empatia}\n"
                                        f"Criar: {criar}\n"
                                        f"Vontade: {vontade}\n"
                                        f"Sorte: {sorte}\n"
                                        f"Faltam {pontos} pontos para distribuir.\n"
                                        f"Gostaria de redestribuí-los?\n"
                                        f"Digite 1-Sim ou 2-Não:\n ---> ")
                    if validacao_2 == "1":
                        validacao_1 = False
                    else:
                        validacao_1 = True
            

        valor_1 = int((corpo + vontade) / 2)
        pontos_de_vida = valor_1 * 5
        info_pontos_de_vida = {"Pontos de Vida": pontos_de_vida}
        self.atributos.update(info_pontos_de_vida)
        estamina = valor_1 * 5
        info_estamina = {"Estamina": estamina}
        self.atributos.update(info_estamina)
        recuperacao = valor_1
        info_recuperacao = {"Recuperação": recuperacao}
        self.atributos.update(info_recuperacao)
        atordoamento = valor_1
        info_atordoamento = {"Atordoamento": atordoamento}
        self.atributos.update(info_atordoamento)


        valor_2 = corpo
        if valor_2 == 1 or valor_2 == 2:
            soco = (1, "d6", -4)
            chute = (1, "d6", 0)
        elif valor_2 == 3 or valor_2 == 4:
            soco = (1, "d6", -2)
            chute = (1, "d6", 2)
        elif valor_2 == 5 or valor_2 == 6:
            soco = (1, "d6", 0)
            chute = (1, "d6", 4)
        elif valor_2 == 7 or valor_2 == 8:
            soco = (1, "d6", 2)
            chute = (1, "d6", 6)
        elif valor_2 == 9 or valor_2 == 10:
            soco = (1, "d6", 4)
            chute = (1, "d6", 8)
        elif valor_2 == 11 or valor_2 == 12:
            soco = (1, "d6", 6)
            chute = (1, "d6", 10)
        elif valor_2 == 13:
            soco = (1, "d6", 8)
            chute = (1, "d6", 12)
        info_soco = {"Soco": soco}
        self.atributos.update(info_soco)
        info_chute = {"Chute": chute}
        self.atributos.update(info_chute)

        fardo = corpo * 10
        info_fardo = {"Fardo": fardo}
        self.atributos.update(info_fardo)
        correr = velocidade * 3
        info_correr = {"Correr": correr}
        self.atributos.update(info_correr)
        salto = int(correr / 5)
        info_salto = {"Salto": salto}
        self.atributos.update(info_salto)

    def caminho_da_vida(self):
        dados_quando = [
            "1 a 2 anos de idade",
            "Primeira Infância ( entre 4 e 6 anos de idade)",
            "Infância Tardia ( entre 8 e 11 anos de idade)"
        ]
        dados_escola = [
            "A Escola do Lobo",
            "A Escola do Grifo",
            "A Escola do Gato",
            "A Escola da Víbora",
            "A Escola do Urso"
        ]
        dados_treinamento = [
            "Ferido no Desafio",
            "Conhecimento Roubado",
            "Fez um Rival",
            "Mutações Fáceis",
            "Tiro Pela Culatra Mágico",
            "Melhor da Sala",
            "Reação Ruim a Mutagênicos",
            "Fez Um Amigo",
            "Ferido pelo Pêndulo",
            "Pesquisa Extensiva"
        ]
        dados_testes = [
            "Quase Fatal",
            "Aceitação Ruim",
            "Mutações Suportáveis",
            "Mutações Extras"
        ]
        dados_evento = [
            "Recebeu Uma Criança Através da Lei da Surpresa. Em suas viagens, você invocou a Lei da Surpresa e "
            "recebeu uma criança. Se foi um menino, ele se transformou em um bruxo, e se foi uma menina, o destino"
            " dela ficou em suas mãos.",
            "Caçado por um Monstro Senciente. O jogo virou durante uma de suas caçadas. Monstros sencientes como "
            "bruxas sepulcrais e katakans podem ser alvos perigosos, e você acabou sendo perseguido durante uma "
            "noite estressante.",
            "Lutou ao Lado de um Cavaleiro. Você lutou ao lado de um nobre cavaleiro. Pode ter sido a sua escolha"
            " ou produto de um acidente, mas lutar ao lado do nobre mudou a sua visão sobre os cavaleiros e o seu"
            " trabalho como bruxo",
            "Capturado por um Mago para Testes. Os magos desejam ter os segredos de mutações dos bruxos. Em algum"
            " momento de sua vida, você foi capturado por um mago que o fez de cobaia numa tentativa de engenharia"
            " reversa.",
            "Trabalhou para um Nobre. Durante um tempo você trabalhou para um nobre. O salário era bom, mas era "
            "estranho e difícil esconder as suas ações para evitar que os segredos da família viessem"
            " a tona.",
            "Viajou Além das Fronteiras. Uma vez você viajou para além das fronteiras do Continente, depois das "
            "Montanhas do Dragão, Tir Tochair ou Montanhas Azuis, ou o Grande Mar. Você viu terras que são "
            "desconhecidas para muitos.",
            "Romance Importante. A maior parte dos bruxos fica neutro e evita relacionamentos sérios. No entanto, "
            "isso não foi o seu caso. Você se apaixonou e pensou de verdade em se estabelecer. Isso ocorre com "
            "você às vezes.",
            "Lutou por sua Fortaleza. Você lutou contra um cerco em sua fortaleza. Você estava em menor número e "
            "menor poder, mas ficou assim mesmo. Sobreviveu ao cerco com vários ferimentos, mas viu muitos dos "
            "seus morrerem à sua volta.",
            "Tornou-se Infame. Depois de ajudar uma cidade com um monstro, o povo ficou com medo e se voltou contra"
            " você. Até tentaram matá-lo. De qualquer forma, você percebeu o quanto pode receber em troca das "
            "pessoas.",
            "Tornou-se Famoso. Você foi bem-recebido numa cidade depois de ajudar com um monstro. Não esperava "
            "bebidas de graça ou mulheres com olhares lascivos, mas foi isso que você conseguiu. Nunca mais viu o "
            "mesmo carinho por aí, mas foi tocante."
        ]
        dados_agora = [
            "Tornou-se um Bruxo Particular",
            "Procurando um Trabalho",
            "Tornou-se Ermitão",
            "Tem uma vida Normal",
            "Tornou-se um Criminoso Perigoso"
        ]

        if self.informacoes_iniciais["Raça"] == "bruxo":
            rolagem_1 = random.randint(1, 10)
            if rolagem_1 == 1 or rolagem_1 == 2:
                rolagem_quando = dados_quando[0]
            elif rolagem_1 == 9 or rolagem_1 == 10:
                rolagem_quando = dados_quando[2]
            else:
                rolagem_quando = dados_quando[1]
            self.vida.append(rolagem_quando)
            rolagem_escola = dados_escola[random.randint(0, 4)]
            self.vida.append(rolagem_escola)
            rolagem_treinamento = dados_treinamento[random.randint(0, 9)]
            self.vida.append(rolagem_treinamento)
            if rolagem_quando == dados_quando[2] and rolagem_treinamento == dados_treinamento[3]:
                rolagem_2 = random.randint(4, 9)
            elif rolagem_quando == dados_quando[0] and rolagem_treinamento == dados_treinamento[6]:
                rolagem_2 = random.randint(0, 5)
            elif rolagem_quando == dados_quando[0] and rolagem_treinamento == dados_treinamento[3]:
                rolagem_2 = random.randint(0, 9)
            elif rolagem_quando == dados_quando[2] and rolagem_treinamento == dados_treinamento[6]:
                rolagem_2 = random.randint(0, 9)
            elif rolagem_quando == dados_quando[2] or rolagem_treinamento == dados_treinamento[3]:
                rolagem_2 = random.randint(2, 9)
            elif rolagem_quando == dados_quando[0] or rolagem_treinamento == dados_treinamento[6]:
                rolagem_2 = random.randint(0, 7)
            else:
                rolagem_2 = random.randint(0, 9)
            if rolagem_2 == 0:
                rolagem_testes = dados_testes[0]
            elif rolagem_2 == 1 or rolagem_2 == 2:
                rolagem_testes = dados_testes[1]
            elif rolagem_2 == 9:
                rolagem_testes = dados_testes[3]
            else:
                rolagem_testes = dados_testes[2]
            self.vida.append(rolagem_testes)
            rolagem_evento = dados_evento[random.randint(0, 9)]
            self.vida.append(rolagem_evento)
            rolagem_3 = random.randint(1, 10)
            if rolagem_3 == 1:
                rolagem_agora = dados_agora[0]
            elif rolagem_3 == 8:
                rolagem_agora = dados_agora[2]
            elif rolagem_3 == 9:
                rolagem_agora = dados_agora[3]
            elif rolagem_3 == 10:
                rolagem_agora = dados_agora[4]
            else:
                rolagem_agora = dados_agora[1]
            self.vida.append(rolagem_agora)

        else:
            origem_norte = ['Redânia', 'Kaedwen', 'Teméria', 'Aedirn', 'Lyria e Rívia', 'Kovir e Poviss', 'Skellige',
                            'Cidaris', 'Verden', 'Cintra']  # 10 total
            origem_nilfgaard = ['Nilfgaard', 'Vicovaro', 'Angren', 'Nazair', 'Mettina', 'Mag Turga', 'Geso', 'Ebbing',
                                'Maecht', 'Gemmera', 'Etólia']  # 11 total
            origem_terras_ancestrais = ['Dol Blathanna', 'Mahakam']  # 2 total
            bonus_norte = ['+1 Educação', '+1 Tolerância', '+1 Carisma', '+1 Criar itens', '+1 Resistir Coerção',
                           '+1 Negócios',
                           '+1 Coragem', '+1 Velejar', '+1 Sobrevivência no Ermo', '+1 Percepção Humana']
            bonus_nilfgaard = ['+1 Ludibriar', '+1 Educação', '+1 Sobrevivência no Ermo', '+1 Brigar', '+1 Cavalgar',
                               '+1 Tolerância', '+1 Furtividade', '+1 Dedução', '+1 Carisma', '+1 Intimidação',
                               '+1 Coragem']
            bonus_terras_ancestrais = ['+1 Etiqueta Social', '+1 Criar itens']

            if self.informacoes_iniciais["Raça"] == "humano":
                regiao = int(random.randint(1, 2))
                if regiao == 1:  # Reinos do Norte
                    cidade = random.randint(0, 9)
                    origem = "Norte"
                    terra_natal = origem_norte[cidade]
                    vantagem = bonus_norte[cidade]
                else:  # Nilfgaard
                    origem_b = int(random.randint(1, 10))
                    if origem_b <= 3:
                        origem = "Nilfgaard"
                        terra_natal = origem_nilfgaard[0]
                        vantagem = bonus_nilfgaard[0]
                    elif origem_b > 3:
                        cidade = int(random.randint(1, 10))
                        origem = "Nilfgaard"
                        terra_natal = origem_nilfgaard[cidade]
                        vantagem = bonus_nilfgaard[cidade]
                self.vida.append(origem)
                self.vida.append(terra_natal)
                # global vantagens
                background = {"vantagem background": vantagem}
                self.vantagens.update(background)
            elif self.informacoes_iniciais["Raça"] == "anão":
                origem = "Terras Ancestrais"
                terra_natal = origem_terras_ancestrais[1]
                vantagem = bonus_terras_ancestrais[1]
                self.vida.append(origem)
                self.vida.append(terra_natal)
                # global vantagens
                background = {"vantagem background": vantagem}
                self.vantagens.update(background)

            elif self.informacoes_iniciais["Raça"] == "elfo":
                origem = "Terras Ancestrais"
                terra_natal = origem_terras_ancestrais[0]
                vantagem = bonus_terras_ancestrais[0]
                self.vida.append(origem)
                self.vida.append(terra_natal)
                # global vantagens
                background = {"vantagem background": vantagem}
                self.vantagens.update(background)

            elif self.informacoes_iniciais["Raça"] == "ananico":
                origem_c = int(random.randint(1, 3))
                if origem_c == 1:  # Reinos do Norte
                    cidade = int(random.randint(0, 9))
                    origem = "Norte"
                    terra_natal = origem_norte[cidade]
                    vantagem = bonus_norte[cidade]
                elif origem_c == 2:  # Nilfgaard
                    cidade = int(random.randint(1, 10))
                    if cidade <= 3:
                        origem = "Nilfgaard"
                        terra_natal = origem_nilfgaard[0]
                        vantagem = bonus_nilfgaard[cidade]
                    elif cidade > 3:
                        cidade_a = int(random.randint(1, 10))
                        origem = "Nilfgaard"
                        terra_natal = origem_nilfgaard[cidade_a]
                        vantagem = bonus_nilfgaard[cidade_a]
                elif origem_c == 3:  # Terras Ancestrais
                    regiao = int(random.randint(1, 2))
                    if regiao == 1:
                        origem = "Terras Ancestrais"
                        terra_natal = origem_terras_ancestrais[1]
                        vantagem = bonus_terras_ancestrais[1]
                    elif regiao == 2:
                        origem = "Terras Ancestrais"
                        terra_natal = origem_terras_ancestrais[0]
                        vantagem = bonus_terras_ancestrais[0]
                self.vida.append(origem)
                self.vida.append(terra_natal)
                # global vantagens
                background = {"vantagem background": vantagem}
                self.vantagens.update(background)

            data_origem_d_familia_norte = ["Aristocracia. Você cresceu em uma mansão nobre com servos à sua" \
                                               " disposição, mas sempre esperaram que você se comportasse e causasse" \
                                               " uma boa impressão.",
                                               "Adotado por um mago. Você foi dado ainda criança para um mago. Viveu" \
                                               " com conforto, mas mal via o seu guardião, que estava sempre ocupado.",
                                               "Cavaleiros. Você cresceu em uma mansão onde aprendeu a ser uma" \
                                               " verdadeira dama ou um verdadeiro lorde. O seu destino foi formado" \
                                               " no seu nascimento.",
                                               "Família de Mercadores. Você cresceu entre mercadores e sempre foi" \
                                               " rodeado por gritaria, pregões e dinheiro.",
                                               "Família de Artesãos. Você cresceu em um atelier de artesão. Os seus" \
                                               " normalmente longos dias são recheados de sons incessantes de criação.",
                                               "Família de Artistas. Você cresceu com um bando de artistas. Você" \
                                               " pode ter viajado ou pode ter se apresentado em teatro.",
                                               "Família de Camponeses. Você cresceu numa fazenda no interior. Você" \
                                               " não teve nada no seu nome e sua vida era simples, mas perigosa.",
                                               "Um ou ambos seus pais foram mortos nas Guerras do Norte.",
                                               "Um ou ambos os seus pais o abandonaram no ermo, onde teve que " \
                                               "sobreviver sozinho. Talvez não conseguissem sustentá-lo. Talvez você" \
                                               "tenha sido um \"acidente\".",
                                               "Um ou ambos os seus pais foram amaldiçoados por um mago ou por causa" \
                                               " do intenso ódio de alguém que encontraram. A maldição virou a vida" \
                                               "deles.",
                                               "Um ou ambos os pais o venderam por dinheiro, ou talvez foi trocado" \
                                               " por bens e serviços. Os seus pais precisavam de dinheiro mais do" \
                                               "que você.",
                                               "Um ou ambos os seus pais se juntaram a uma gangue. Você via essa" \
                                               " gangue com frequência e por vezes, foi forçado a trabalhar para eles.",
                                               "Um ou ambos os seus pais foram mortos por monstros. É sua escolha" \
                                               " escolher de quais criaturas eles foram vítimas.",
                                               "Um ou ambos os seus pais foram executados sob falsa acusação. Eles" \
                                               " podem ter sido bode espiatório de alguma coisa ou simplesmente " \
                                               "estavam no lugar errado.",
                                               "Um ou ambos os seus pais foram mortos por uma praga. Não havia nada" \
                                               " a fazer a não ser tentar aliviar a dor deles.",
                                               "Um ou ambos os seus pais desertaram para Nilfgaard. Talvez tivessem" \
                                               " um acordo por troca de informações ou simplismente cruzaram a " \
                                               "fronteira.",
                                               "Um ou ambos os seus pais foram sequestrados por nobres. " \
                                               "Provavelmente sua mãe atraiu a atenção de um lorde local ou de seu" \
                                               " filho.",
                                               "A sua família foi dispersada pelas guerras e você não tem ideia de " \
                                               "onde a maioria deles estão.",
                                               "A sua família foi presa por crimes ou por acusações exageradas. " \
                                               "Somente você escapou. Você pode querer libertá-los... ou não.",
                                               "A sua família foi amaldiçoada e agora as plantações não crescem e os " \
                                               "espectros percorrem os corredores. Tornou-se muito perigoso ficar em " \
                                               "sua casa.",
                                               "Com tantas guerras, o sustento de sua família foi destruído. Para " \
                                               "sobreviver a sua família voltou-se para o crime.",
                                               "A sua família acumulou uma dívida enorme por causa de apostas ou favores" \
                                               " para outras pessoas. Você precisa muito de dinheiro.",
                                               "A sua família travou uma disputa com uma outra família. Você não " \
                                               "consegue nem lembrar do porquê desta rixa ter começado.",
                                               "Por causa de alguma ação ou inação, a sua família é odiada em sua " \
                                               "cidade natal e agora ninguém quer ter qualquer relação com ela.",
                                               "Um dia tudo o que você tinha foi roubado por bandidos. A sua família " \
                                               "foi massacrada, deixando você sozinho.",
                                               "A sua família tem um segredo profundo e sombrio que se descoberto " \
                                               "arruinaria a todos completamente. Você pode decidir qual será o segredo" \
                                               " ou o Mestre pode decidir.",
                                               "A sua família odeia uns aos outros. Ninguém se fala mais e você tem " \
                                               "sorte de conseguir um \"olâ\" de seus irmãos."
                                               ]
            data_origem_d_familia_nif = ["Aristocracia. Você cresceu em uma mansão e foi treinado a ser bem-" \
                                             "versado no mundo da corte. O luxo era apenas o seu incentivo.",
                                             "Alto Clero. Você foi criado entre o clero do Grande Sol. Cresceu " \
                                             "sendo devoto e consciente de que a Igreja iria guiá-lo.",
                                             "Cavaleiros. Você cresceu sabendo que o seu dever era dedicado ao " \
                                             "Imperador e que toda a sua riqueza era recompensa por um eventual " \
                                             "serviço.",
                                             "Família de Artesãos. Você cresceu num atelier de artesão, " \
                                             "aprendendo a criar produtos para venda no mundo todo. Você " \
                                             "aprendeu o valor da qualidade.",
                                             "Família de Mercadores. Você cresceu vendendo produtos por todo " \
                                             "o Império. Já viu todos os tipos de bens exóticos de todas as " \
                                             "partes do mundo.",
                                             "Servido na Servidão. Você nasceu na servidão e viveu em alojamentos" \
                                             " simples. Você não tinha muito e trabalhava sempre.",
                                             "Família de Camponeses. Você cresceu em uma das milhares de fazendas" \
                                             " espalhadas pelo Império. Teve poucas posses, mas a vida era simples.",
                                             "O seu pai morreu em uma das Guerras do Norte. Ele podia já ser " \
                                             "militar ou se alistou durante a guerra.",
                                             "Um ou ambos os seus pais foram envenenados. Pode ter sido o trabalho" \
                                             " de um profissional rival, ou pode ter sido uma forma de tirá-los " \
                                             "do caminho.",
                                             "A polícia secreta levou os seus pais (ou um deles) para " \
                                             "interrogatório. Na semana seguinte, seus corpos foram encontrados" \
                                             " nas ruas da cidade.",
                                             "Um ou ambos os pais foram mortos por um mago renegado. O mais" \
                                             " provável é que tentaram entregar este mago para o Império e " \
                                             "pagaram o preço.",
                                             "Um ou ambos os seus pais foram presos por fazerem magia ilegal. " \
                                             "Talvez eles realmente tenham cometido o crime ou talvez tenha sido" \
                                             " uma armação.",
                                             "Um ou ambos os seus pais foram exilados para o Deserto de Korath. " \
                                             "Provavelmente, cometeram um crime pesado, mas matá-los seria um " \
                                             "problema.",
                                             "Um ou ambos os seus pais foram amaldiçoados por um mago. " \
                                             "Provavelmente o mago tinha uma vendeta contra eles.",
                                             "Os seus pais simplesmente o abandonaram num dia. Você pode nem saber" \
                                             " o por quê. Um dia os seus pais simplesmente desapareceram.",
                                             "Um ou ambos os seus pais foram escravizados. Ou eles cometeram um " \
                                             "crime contra o Império ou sofreram de uma armação de um rival.",
                                             "Um ou ambos os seus pais foram enviados para o Norte como agentes " \
                                             "duplos. Provavelmente você nem sabe onde eles estão agora, mas " \
                                             "estão a serviço do Imperador.",
                                             "A sua família foi condenada por crimes contra o Império ou por " \
                                             "acusações exageradas. Somente você escapou.",
                                             "A sua família foi exilada para o Deserto de Korath e você passou a " \
                                             "maior parte de sua vida pregressa lutando para sobreviver no deserto" \
                                             " mortal.",
                                             "A sua família foi morta por um mago renegado que tinha uma vendeta " \
                                             "contra a sua família ou só porque queria ver sangue. De qualquer " \
                                             "forma, você está sozinho.",
                                             "A sua família desapareceu e você não tem ideia para onde eles foram. " \
                                             "Um dia ela simplismente foi embora.",
                                             "A sua família foi executada por traição contra o Império. Você foi o " \
                                             "único a escapar desse destino.",
                                             "A sua família foi destituída de seu título por alguma razão. Você foi " \
                                             "despejado de sua casa e abandonado na miséria para sobreviver entre os " \
                                             "deploráveis.",
                                             "O nome de sua família foi manchado por um parente que ostentou o dote " \
                                             "mágico da família desgraçadamente como um mago do Norte.",
                                             "Você desgraçou a sua família aos olhos do Império. Alguma coisa que " \
                                             "você fez ou deixou de fazer arruinou o seu nome e prejudicou a sua " \
                                             "família.",
                                             "A sua família tem um segredo profundo e sombrio que se descoberto " \
                                             "poderia destruir a todos e manchar seu nome para sempre. Você deve " \
                                             "proteger esse segredo com a sua vida.",
                                             "A sua família foi assassinada. Estavam no meio do plano de alguém ou " \
                                             "foram usados para chegar a alguém mais poderoso. De qualquer forma, a" \
                                             " sua família se foi."
                                             ]
            data_origem_d_familia_ances = ["Aristocracia. Você cresceu num palácio e era lembrado constantemente" \
                                               " da glória do passado. Esperavam que você fizesse jus ao seu legado.",
                                               "Nobre Guerreiro. Você cresceu como o filho de um nobre guerreiro," \
                                               " destinado a elevar a reputação da família e nunca desonrar a sua" \
                                               "herança.",
                                               "Mercadores. Você cresceu entre comerciantes viajantes. A vida é " \
                                               "difícil às vezes, mas o artesanato não-humano é sempre valorizado.",
                                               "Família de Escribas. Você cresceu como o filho de escribas, " \
                                               "registrando e protegendo a história do povo ancestral o máximo " \
                                               "possível.",
                                               "Artistas. Você cresceu cantando e apresentando peças. Você trabalhou" \
                                               " nos bastidores, ajudou a escrever canções e consertou instrumentos.",
                                               "Família de Artesãos. Você cresceu em uma família de artesãos," \
                                               " visitando palácios antigos em busca de inspiração, e gastando horas" \
                                               " todo dia em projetos.",
                                               "Família de Classe Inferior. Você cresceu numa família de classe " \
                                               "inferior, atendendo as mansões dos ricos ou fazendo trabalhos" \
                                               "pequenos em sua cidade natal.",
                                               "Um ou ambos os seus pais foram acusados de ser Scoia'tael. As " \
                                               "pessoas à sua volta olham feio para os seus pais.",
                                               "Um ou ambos os seus pais se voltaram contra o seu próprio povo e " \
                                               "venderam as raças ancestrais para os humanos. Seus pais não são " \
                                               "bem-vindos em sua terra natal.",
                                               "Um ou ambos os seus pais se mataram por causa do desespero. Sem " \
                                               "esperança de reconquistar a glória do passado, eles desistiram de " \
                                               "viver.",
                                               "Enquanto viajavam, um ou ambos os seus pais foram vítimas de " \
                                               "racismo humano. Eles morreram num pogrom e seus corpos foram " \
                                               "exibidos em estacas.",
                                               "Um ou ambos os seus pais ficaram obcecados em reconquistar a glória " \
                                               "passada de sua raça. Sacrificaram tudo por essa causa.",
                                               "Um ou ambos os seus pais foram exilados de sua terra natal. Há " \
                                               "muitas razões possíveis para isso, de crime a opiniões divergentes.",
                                               "Um ou ambos os seus pais foram amaldiçoado. Você pode decidir qual " \
                                               "foi a maldição ou deixar o Mestre decidir.",
                                               "Os seus pais o entregaram para outra família, para que pudesse " \
                                               "sobreviver, porque não podiam cuidar de você.",
                                               "Um ou ambos os seus pais se juntaram aos Scoia'tael numa tentativa " \
                                               "de conseguir vingança contra os humanos que eles pensam terem " \
                                               "arruinado as suas vidas.",
                                               "Um ou ambos os seus pais morreram num \"acidente\". Provavelmente " \
                                               "fizeram um inimigo poderoso que finalmente encontrou uma maneira de" \
                                               " se livrar deles.",
                                               "A sua família foi marcada como simpatizante de humanos e não é " \
                                               "bem-vista em sua terra natal.",
                                               "A sua família foi condenada ao ostracismo por ter opiniões contrárias" \
                                               " e agora o povo não interage com você ou sua família.",
                                               "A sua família morreu nas Guerras do Norte. Podem ter até lutado na " \
                                               "guerra, ou foram baixas inocentes.",
                                               "A sua família está numa disputa por séculos. Você pode não se lembrar" \
                                               " do motivo dessa rixa, mas é feia.",
                                               "A sua família foi destituída de seu título por alguma razão. Você foi " \
                                               "despejado de sua casa e abandonado às próprias custas.",
                                               "A sua família fazia assaltos a povoados humanos quando você era jovem" \
                                               ", para conseguir comida e talvez se vingar dos humanos.",
                                               "A casa de sua família é assombrada. Muito provavelmente porque a sua " \
                                               "casa foi o local de muitas, mas muitas mortes durante a guerra contra " \
                                               "os humanos.",
                                               "A sua família está dividida por causa de um cunhado humano que foi " \
                                               "trazido para dentro de sua casa por um irmão ou parente. Algumas " \
                                               "pessoas de sua família gostam dele e algumas o odeiam.",
                                               "A sua família foi morta por humanos que pensavam que ela era Scoia'tael." \
                                               " Eles foram chacinados ou enforcados, sem julgamento.",
                                               "A sua família descende de um traidor infame. Isso prejudica as " \
                                               "interações que sua família tem com os outros das raças ancestrais e " \
                                               "fez a vida na terra ancestral mais difícil."
                                               ]

            familia = int(random.randint(1, 2))
            if familia == 2:
                # Ao Menos Alguém de Sua Família Está Vivo
                familia_a = int(random.randint(1, 2))
                if familia_a == 2:
                    # Os Seus Pais Estão Vivos
                    familia_b = int(random.randint(1, 10))
                    if self.vida[0] == "Norte":
                        if familia_b == 1:
                            origem_d_familia = data_origem_d_familia_norte[0]
                        elif familia_b == 2:
                            origem_d_familia = data_origem_d_familia_norte[1]
                        elif familia_b == 3:
                            origem_d_familia = data_origem_d_familia_norte[2]
                        elif familia_b == 4:
                            origem_d_familia = data_origem_d_familia_norte[3]
                        elif familia_b == 5:
                            origem_d_familia = data_origem_d_familia_norte[4]
                        elif familia_b == 6 or familia_b == 7:
                            origem_d_familia = data_origem_d_familia_norte[5]
                        else:
                            origem_d_familia = data_origem_d_familia_norte[6]
                    elif self.vida[0] == "Nilfgaard":
                        if familia_b == 1:
                            origem_d_familia = data_origem_d_familia_nif[0]
                        elif familia_b == 2:
                            origem_d_familia = data_origem_d_familia_nif[1]
                        elif familia_b == 3:
                            origem_d_familia = data_origem_d_familia_nif[2]
                        elif familia_b == 4:
                            origem_d_familia = data_origem_d_familia_nif[3]
                        elif familia_b == 5:
                            origem_d_familia = data_origem_d_familia_nif[4]
                        elif familia_b == 6 or familia_b == 7:
                            origem_d_familia = data_origem_d_familia_nif[5]
                        else:
                            origem_d_familia = data_origem_d_familia_nif[6]
                    elif self.vida[0] == "Terras Ancestrais":
                        if familia_b == 1:
                            origem_d_familia = data_origem_d_familia_ances[0]
                        elif familia_b == 2:
                            origem_d_familia = data_origem_d_familia_ances[1]
                        elif familia_b == 3:
                            origem_d_familia = data_origem_d_familia_ances[2]
                        elif familia_b == 4:
                            origem_d_familia = data_origem_d_familia_ances[3]
                        elif familia_b == 5:
                            origem_d_familia = data_origem_d_familia_ances[4]
                        elif familia_b == 6 or familia_b == 7:
                            origem_d_familia = data_origem_d_familia_ances[5]
                        else:
                            origem_d_familia = data_origem_d_familia_ances[6]
                else:
                    # Alguma Coisa Aconteceu Com Os Seus Pais
                    familia_b = int(random.randint(1, 10))
                    if self.vida[0] == "Norte":
                        if familia_b == 1:
                            origem_d_familia = data_origem_d_familia_norte[7]
                        elif familia_b == 2:
                            origem_d_familia = data_origem_d_familia_norte[8]
                        elif familia_b == 3:
                            origem_d_familia = data_origem_d_familia_norte[9]
                        elif familia_b == 4:
                            origem_d_familia = data_origem_d_familia_norte[10]
                        elif familia_b == 5:
                            origem_d_familia = data_origem_d_familia_norte[11]
                        elif familia_b == 6:
                            origem_d_familia = data_origem_d_familia_norte[12]
                        elif familia_b == 7:
                            origem_d_familia = data_origem_d_familia_norte[13]
                        elif familia_b == 8:
                            origem_d_familia = data_origem_d_familia_norte[14]
                        elif familia_b == 9:
                            origem_d_familia = data_origem_d_familia_norte[15]
                        else:
                            origem_d_familia = data_origem_d_familia_norte[16]
                    elif self.vida[0] == "Nilfgaard":
                        if familia_b == 1:
                            origem_d_familia = data_origem_d_familia_nif[7]
                        elif familia_b == 2:
                            origem_d_familia = data_origem_d_familia_nif[8]
                        elif familia_b == 3:
                            origem_d_familia = data_origem_d_familia_nif[9]
                        elif familia_b == 4:
                            origem_d_familia = data_origem_d_familia_nif[10]
                        elif familia_b == 5:
                            origem_d_familia = data_origem_d_familia_nif[11]
                        elif familia_b == 6:
                            origem_d_familia = data_origem_d_familia_nif[12]
                        elif familia_b == 7:
                            origem_d_familia = data_origem_d_familia_nif[13]
                        elif familia_b == 8:
                            origem_d_familia = data_origem_d_familia_nif[14]
                        elif familia_b == 9:
                            origem_d_familia = data_origem_d_familia_nif[15]
                        else:
                            origem_d_familia = data_origem_d_familia_nif[16]
                    elif self.vida[0] == "Terras Ancestrais":
                        if familia_b == 1:
                            origem_d_familia = data_origem_d_familia_ances[7]
                        elif familia_b == 2:
                            origem_d_familia = data_origem_d_familia_ances[8]
                        elif familia_b == 3:
                            origem_d_familia = data_origem_d_familia_ances[9]
                        elif familia_b == 4:
                            origem_d_familia = data_origem_d_familia_ances[10]
                        elif familia_b == 5:
                            origem_d_familia = data_origem_d_familia_ances[11]
                        elif familia_b == 6:
                            origem_d_familia = data_origem_d_familia_ances[12]
                        elif familia_b == 7:
                            origem_d_familia = data_origem_d_familia_ances[13]
                        elif familia_b == 8:
                            origem_d_familia = data_origem_d_familia_ances[14]
                        elif familia_b == 9:
                            origem_d_familia = data_origem_d_familia_ances[15]
                        else:
                            origem_d_familia = data_origem_d_familia_ances[16]
            else:
                # Alguma Coisa Aconteceu Com a Sua Família
                familia_b = int(random.randint(1, 10))
                if self.vida[0] == "Norte":
                    if familia_b == 1:
                        origem_d_familia = data_origem_d_familia_norte[17]
                    elif familia_b == 2:
                        origem_d_familia = data_origem_d_familia_norte[18]
                    elif familia_b == 3:
                        origem_d_familia = data_origem_d_familia_norte[19]
                    elif familia_b == 4:
                        origem_d_familia = data_origem_d_familia_norte[20]
                    elif familia_b == 5:
                        origem_d_familia = data_origem_d_familia_norte[21]
                    elif familia_b == 6:
                        origem_d_familia = data_origem_d_familia_norte[22]
                    elif familia_b == 7:
                        origem_d_familia = data_origem_d_familia_norte[23]
                    elif familia_b == 8:
                        origem_d_familia = data_origem_d_familia_norte[24]
                    elif familia_b == 9:
                        origem_d_familia = data_origem_d_familia_norte[25]
                    else:
                        origem_d_familia = data_origem_d_familia_norte[26]
                elif self.vida[0] == "Nilfgaard":
                    if familia_b == 1:
                        origem_d_familia = data_origem_d_familia_nif[17]
                    elif familia_b == 2:
                        origem_d_familia = data_origem_d_familia_nif[18]
                    elif familia_b == 3:
                        origem_d_familia = data_origem_d_familia_nif[19]
                    elif familia_b == 4:
                        origem_d_familia = data_origem_d_familia_nif[20]
                    elif familia_b == 5:
                        origem_d_familia = data_origem_d_familia_nif[21]
                    elif familia_b == 6:
                        origem_d_familia = data_origem_d_familia_nif[22]
                    elif familia_b == 7:
                        origem_d_familia = data_origem_d_familia_nif[23]
                    elif familia_b == 8:
                        origem_d_familia = data_origem_d_familia_nif[24]
                    elif familia_b == 9:
                        origem_d_familia = data_origem_d_familia_nif[25]
                    else:
                        origem_d_familia = data_origem_d_familia_nif[26]
                elif self.vida[0] == "Terras Ancestrais":
                    if familia_b == 1:
                        origem_d_familia = data_origem_d_familia_ances[17]
                    elif familia_b == 2:
                        origem_d_familia = data_origem_d_familia_ances[18]
                    elif familia_b == 3:
                        origem_d_familia = data_origem_d_familia_ances[19]
                    elif familia_b == 4:
                        origem_d_familia = data_origem_d_familia_ances[20]
                    elif familia_b == 5:
                        origem_d_familia = data_origem_d_familia_ances[21]
                    elif familia_b == 6:
                        origem_d_familia = data_origem_d_familia_ances[22]
                    elif familia_b == 7:
                        origem_d_familia = data_origem_d_familia_ances[23]
                    elif familia_b == 8:
                        origem_d_familia = data_origem_d_familia_ances[24]
                    elif familia_b == 9:
                        origem_d_familia = data_origem_d_familia_ances[25]
                    else:
                        origem_d_familia = data_origem_d_familia_ances[26]
            self.vida.append(origem_d_familia)

            data_amigo = ["Uma igreja. Você cresceu sob influência da religião local e passava horas na igreja.",
                          "Um artesão. A sua maior influência foi um artesão que lhe ensinou a apreciar a arte e" \
                          " o talento.",
                          "Um conde. A sua maior influência foi um conde ou condessa que lhe ensinou a se " \
                          "comportar.",
                          "Um mago. A sua maior influência foi um mago que lhe ensinou a não temer a magia e a " \
                          "sempre questionar.",
                          "Uma bruxa. A sua maior influência foi a bruxa do vilarejo que lhe ensinou a " \
                          "importância do conhecimento.",
                          "Uma pessoa amaldiçoada. A sua maior influência foi uma pessoa amaldiçoada que lhe " \
                          "ensinou a nunca julgar os outros severamente.",
                          "Um artista. A sua maior influência foi um artista que lhe ensinou muito sobre " \
                          "apresentações.",
                          "Um mercador. A sua maior influência foi um mercador que lhe ensinou como ser astuto " \
                          "e esperto.",
                          "Um criminoso. A sua maior influência foi um criminoso que lhe ensinou a tomar conta" \
                          " de si mesmo.",
                          "Um homem de armas. A sua maior influência foi um soldado que lhe ensinou a se defender.",
                          "O culto do Grande Sol. Sua maior influência foi a igreja. Você passou muitos anos " \
                          "aprendendo cantos e rituais.",
                          "Um pária. A sua maior influência foi um pária que lhe ensinou a questionar sempre a " \
                          "sociedade.",
                          "Um conde. A sua maior influência foi um conde que lhe ensinou a liderar e manter a" \
                          " ordem.",
                          "Um mago. A sua maior influência foi um mago que lhe ensinou a importância da ordem" \
                          " e da precaução.",
                          "Um procurador. A sua maior influência foi um detetive imperial. Você passou muito " \
                          "tempo resolvendo mistérios.",
                          "Um caçador de magos. A sua maior influência foi um caçador de magos que lhe ensinou a " \
                          "ser cauteloso com magia e magos.",
                          "Um homem de armas. A sua maior influência foi um soldado que compartilhava histórias " \
                          "sobre perigo e ação.",
                          "Um artesão. A sua maior influência foi um artesão que lhe ensinou como apreciar " \
                          "perícia e precisão.",
                          "Um monstro senciente. A sua maior influência foi um monstro senciente que lhe ensinou" \
                          " que nem todos os monstros são maus.",
                          "Um artista. A sua maior influência foi um artista que lhe ensinou como se expressar.",
                          "Um humano. A sua maior influência foi um humano que lhe eninou que às vezes o " \
                          "racismo é infundado.",
                          "Um artesão. A sua maior influência foi um artesão que lhe ensinou a apreciar a " \
                          "grande arte do povo ancestral.",
                          "Um nobre guerreiro. A sua maior influência foi um Dançarino Guerreiro ou um Defensor" \
                          " de Mahakam que lhe ensinou sobre honra.",
                          "Um nobre. A sua maior influência foi um nobre que lhe ensinou sobre orgulho e como " \
                          "se comportar.",
                          "Um artista. A sua maior influência foi um artista que lhe ensinou a importância da " \
                          "felicidade e beleza.",
                          "Um saqueador. A sua maior influência foi um saqueador que lhe ensinou que você tem o" \
                          " direito de pegar o que quiser.",
                          "Um sábio. A sua maior influência foi um sábio que lhe ensinou a importância da " \
                          "história do povo ancestral.",
                          "Um criminoso. A sua maior influência foi um criminnoso que lhe ensinou a seguir as" \
                          " suas próprias regras.",
                          "Um caçador. A sua maior influência foi um caçador que lhe ensinou como sobreviver " \
                          "no ermo.",
                          "Um fazendeiro de chapada. A sua maior influência foi um fazendeiro que lhe ensinou" \
                          " a viver feliz."
                          ]
            amigo_a = int(random.randint(0, 9))
            if self.vida[0] == "Norte":
                amigo = data_amigo[amigo_a]
            elif self.vida[0] == "Nilfgaard":
                amigo = data_amigo[amigo_a + 10]
            elif self.vida[0] == "Terras Ancestrais":
                amigo = data_amigo[amigo_a + 20]
            self.vida.append(amigo)

    def info_profissao(self):
        """
        "Consciência", "Negócios", "Dedução", "Educação", "Língua", "Conhecimento sobre Monstros", "Etiqueta Social",
        "Sabedoria das Ruas", "Táticas", "Ensinar", "Sobrevivência no Ermo", "Brigar", "Esquivar/Escapar",
         "Curta Distância", "Cavalgar", "Velejar", "Lâminas Pequenas", "Cajado/Lança", "Esgrima", "Arco e Flecha",
         "Atletismo", "Besta", "Prestidigitação", "Furtividade", "Físico", "Tolerância", "Carisma", "Ludibriar",
         "Belas Artes", "Apostar", "Aparência e Estilo", "Percepção Humana", "Liderança", "Persuação", "Apresentação",
         "Sedução", "Alquimia", "Criar", "Disfarce", "Primeiros Socorros", "Falsificação", "Arrombar Fechaduras",
         "Criar Armadilhas", "Coragem", "Criar uma Hex", "Intimidação", "Lançar Feitiços", "Resistir a Magia",
          "Resistir Coerção", "Criar Ritual"

          ["0", "bardo", "artesão", "criminoso", "doutor",
                    "mago", "homem de armas", "comerciante", "sacerdote", "nobre"]
        """
        all_equip = [
            "Fluido Esterilizante x10",
            "100 Coroas em Componentes",
            "50 coroas em componentes",
            "Adaga",
            "Ampulheta",
            "Bainha de Coxa",
            "Bainha de Manga",
            "Baralho de Gwent",
            "Baú Pequeno",
            "Besta de Mão",
            "Besta e Virotes x20",
            "Bolsa",
            "Bolsa para Ritual",
            "Bolso Secreto",
            "Broquel de Ferro",
            "Cadeado",
            "Cajado",
            "Calças Blindadas",
            "Cavalo",
            "Clorofórmio",
            "Cobertor",
            "Couraça",
            "Dados Viciados",
            "Diário",
            "Diário com Cadeado",
            "Ervas Entorpecentes x10",
            "Ervas Entorpecentes x5",
            "Esboda",
            "Espada de Aço de Bruxo",
            "Espada de Prata de Bruxo",
            "Espada Longa de Ferro",
            "Espelho de Mão",
            "Estilete Nilfgaardiano",
            "Facas de Arremesso x 5",
            "Ferramenta de Criação",
            "Ferramentas de Comerciante",
            "Ferramentas de Ladrão",
            "Fluido Esterilizante",
            "Fluido Esterilizante x5",
            "Forja de Funileiro",
            "Fórmula de Elixir",
            "Fórmula de Óleo x2",
            "Fórmula de Poção x2",
            "Frasco de Destilado",
            "Jaquetão de Tecido Duplo",
            "Joias",
            "Kit de Alquimia",
            "Kit de Cirurgião",
            "Kit de Escrita",
            "Kit de Maquiagem",
            "Kit Médico",
            "Kord",
            "Lança",
            "Lanterna Sinalizadora",
            "Maça",
            "Machado de Batalha",
            "Medalhão de Bruxo",
            "Perfume / Colônia",
            "Pó de Coagulação x10",
            "Pó de Coagulação x5",
            "Pochete",
            "Roupas de Moda",
            "Símbolo Sagrado",
            "Soqueira",
            "Tabuleiro de Pôquer de Dados",
            "Tenda Grande",
            "Tinta Invisível",
            "Touca de Cota de Malha",
            "Um Diário com Cadeado",
            "Um Instrumento",
            "Velas x10",
        ]

        prof_a = self.informacoes_iniciais["Profissão"]

        if prof_a == "bardo":
            self.pericias = ["Espetáculo de Rua", "Carisma", "Ludibriar", "Apresentação", "Língua", "Percepção Humana",
                             "Persuação", "Sabedoria das Ruas", "Belas Artes", "Sedução", "Etiqueta Social"]
            self.vantagem_magica = [0, "Nenhuma"]
            self.equipamentos = []
            equip_bardo = [all_equip[64], all_equip[7], all_equip[31], all_equip[69], all_equip[43], all_equip[3],
                           all_equip[57], all_equip[60], all_equip[5], all_equip[68]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_bardo:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_bardo[escolha_1 - 1])
                del equip_bardo[escolha_1 - 1]

        elif prof_a == "artesão":
            self.pericias = ["Remendo", "Criar", "Negócios", "Atletismo", "Tolerância",
                             "Físico", "Sabedoria das Ruas", "Belas Artes", "Alquimia", "Educação",
                             "Persuação"]
            self.vantagem_magica = [0, "Nenhuma"]

            equip_artesao = [all_equip[39], all_equip[35], all_equip[30],
                             all_equip[34], all_equip[46], all_equip[4],
                             all_equip[8], all_equip[54], all_equip[2], all_equip[15]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_artesao:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_artesao[escolha_1 - 1])
                del equip_artesao[escolha_1 - 1]

        elif prof_a == "criminoso":
            self.pericias = ["Paranoia Praticada", "Prestidigitação", "Arrombar Fechaduras", "Sabedoria das Ruas",
                             "Falsificação", "Ludibriar", "Furtividade", "Intimidação", "Lâminas Pequenas",
                             "Atletismo", "Consciência"]
            self.vantagem_magica = [0, "Nenhuma"]

            equip_criminoso = [all_equip[22], all_equip[53], all_equip[13],
                               all_equip[36], all_equip[6], all_equip[32],
                               all_equip[63], all_equip[33], all_equip[19], all_equip[11]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_criminoso:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_criminoso[escolha_1 - 1])
                del equip_criminoso[escolha_1 - 1]

        elif prof_a == "doutor":
            self.pericias = ["Mãos que Curam", "Resistir Coerção", "Carisma", "Etiqueta Social", "Coragem",
                             "Percepção Humana", "Sobrevivência no Ermo", "Negócios", "Dedução", "Lâminas Pequenas",
                             "Alquimia"]
            self.vantagem_magica = [0, "Nenhuma"]

            equip_doutor = [all_equip[58], all_equip[0], all_equip[25], all_equip[50], all_equip[48], all_equip[4],
                            all_equip[70], all_equip[20], all_equip[65], all_equip[3]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_doutor:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_doutor[escolha_1 - 1])
                del equip_doutor[escolha_1 - 1]

        elif prof_a == "mago":
            self.pericias = ["Treinamento em Magia", "Percepção Humana", "Lançar Feitiços", "Criar uma Hex",
                             "Resistir a Magia", "Cajado/Lança", "Educação", "Criar Ritual", "Etiqueta Social",
                             "Sedução", "Aparência e Estilo"]
            self.vantagem_magica = [5, "5 Feitiços de Iniciante", "1 Ritual de Iniciante", "1 Hex (levemente perigoso)"]

            equip_mago = [all_equip[4], all_equip[49], all_equip[60],
                          all_equip[48], all_equip[31], all_equip[3],
                          all_equip[16], all_equip[5], all_equip[23], all_equip[1]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_mago:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_mago[escolha_1 - 1])
                del equip_mago[escolha_1 - 1]

        elif prof_a == "homem de armas":
            self.pericias = ["Firme como um Rochedo", "Sobrevivência no Ermo", "Coragem", "Físico", "Intimidação",
                             "Esquivar/Escapar"]
            pericias_homem_de_armas = ["Brigar", "Lâminas Pequenas", "Curta Distância", "Cajado/Lança", "Esgrima",
                                       "Arco e Flecha", "Besta", "Liderança", "Primeiros Socorros"]
            items_pericias = 5
            total_pericias_homem_de_armas = items_pericias
            numero_item = 1
            while items_pericias > 0:
                numero_ordem_items_lista = 1
                for item in pericias_homem_de_armas:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items_pericias -= 1
                escolha_1 = int(input(f"Escolha uma das perícias acima ({numero_item}/{total_pericias_homem_de_armas}):"
                                      f"\n---> "))
                numero_item += 1
                self.pericias.append(pericias_homem_de_armas[escolha_1 - 1])
                del pericias_homem_de_armas[escolha_1 - 1]

            self.vantagem_magica = [0, "Nenhuma"]

            equip_homem_de_armas = [all_equip[51], all_equip[52], all_equip[55], all_equip[33], all_equip[11],
                                    all_equip[67], all_equip[21], all_equip[17], all_equip[10], all_equip[14]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_homem_de_armas:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_homem_de_armas[escolha_1 - 1])
                del equip_homem_de_armas[escolha_1 - 1]

        elif prof_a == "comerciante":
            self.pericias = ["Bem Viajado", "Carisma", "Lâminas Pequenas", "Educação", "Língua x2",
                             "Sabedoria das Ruas", "Negócios", "Persuação", "Percepção Humana", "Apostar",
                             "Resistir Coerção"]
            self.vantagem_magica = [0, "Nenhuma"]

            equip_comerciante = [all_equip[48], all_equip[35], all_equip[65],
                                 all_equip[23], all_equip[10], all_equip[3]]
            self.equipamentos = ["Uma Mula", "Uma Carroça", "1000 Coroas de Itens Comuns"]

            items = 3
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_comerciante:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_comerciante[escolha_1 - 1])
                del equip_comerciante[escolha_1 - 1]

        elif prof_a == "sacerdote":
            self.pericias = ["Iniciados dos Deuses", "Criar Ritual", "Liderança", "Coragem", "Percepção Humana",
                             "Criar uma Hex", "Primeiros Socorros", "Carisma", "Sobrevivência no Ermo", "Ensinar",
                             "Lançar Feitiços"]
            self.vantagem_magica = [2, "2 Invocações de Iniciante", "2 Rituais de Iniciante",
                                    "2 Hexes (levemente perigosos)"]

            equip_sacerdote = [all_equip[62], all_equip[38], all_equip[46],
                               all_equip[47], all_equip[12], all_equip[3],
                               all_equip[16], all_equip[59], all_equip[26], all_equip[1]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_sacerdote:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_sacerdote[escolha_1 - 1])
                del equip_sacerdote[escolha_1 - 1]

        elif prof_a == "nobre":
            self.pericias = ["Notoriedade", "Consciência", "Ludibriar", "Educação", "Aparência e Estilo",
                             "Percepção Humana", "Liderança", "Persuação", "Cavalgar", "Etiqueta Social"]
            pericias_nobre = ["Brigar", "Lâminas Pequenas", "Curta Distância", "Cajado/Lança", "Esgrima",
                                       "Arco e Flecha", "Besta", "Liderança", "Primeiros Socorros"]
            items_pericias = 1
            total_pericias_homem_de_armas = items_pericias
            numero_item = 1
            while items_pericias > 0:
                numero_ordem_items_lista = 1
                for item in pericias_nobre:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items_pericias -= 1
                escolha_1 = int(input(f"Escolha uma das perícias acima ({numero_item}/{total_pericias_homem_de_armas}):"
                                      f"\n---> "))
                numero_item += 1
                self.pericias.append(pericias_nobre[escolha_1 - 1])
                del pericias_nobre[escolha_1 - 1]
            self.vantagem_magica = [0, "Nenhuma"]

            equip_nobre = [all_equip[27], all_equip[61], all_equip[18], all_equip[66], all_equip[45], all_equip[24],
                           all_equip[49], all_equip[57], all_equip[13], all_equip[48]]

            items = 5
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_nobre:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_nobre[escolha_1 - 1])
                del equip_nobre[escolha_1 - 1]

        elif prof_a == "bruxo":
            self.pericias = ["Treino de Bruxo", "Consciência", "Dedução", "Lançar Feitiços", "Alquimia",
                             "Esquivar/Escapar", "Sobrevivência no Ermo", "Esgrima", "Atletismo", "Furtividade",
                             "Cavalgar"]
            self.vantagem_magica = [2, "Todos Sinais Básicos"]

            self.equipamentos = [all_equip[56], all_equip[28], all_equip[29],
                                 all_equip[42], all_equip[41], all_equip[40]]

            equip_bruxo1 = [all_equip[46], all_equip[18], all_equip[33], all_equip[9], all_equip[44]]

            items = 2
            total_escolhas_de_items = items
            numero_item = 1
            while items > 0:
                numero_ordem_items_lista = 1
                for item in equip_bruxo1:
                    print(f" {numero_ordem_items_lista} - {item}")
                    numero_ordem_items_lista += 1
                items -= 1
                escolha_1 = int(input(f"Escolha um dos equipamentos acima ({numero_item}/{total_escolhas_de_items}):"
                                      f"\n---> "))
                numero_item += 1
                self.equipamentos.append(equip_bruxo1[escolha_1-1])
                del equip_bruxo1[escolha_1-1]

    def pericias(self):
        self.pericias = {
            "Inteligência": {"Consciência": 0, "Negócios": 0, "Dedução": 0, "Educação": 0, "Língua (2)": 0,
                             "Conhecimento sobre Monstros (2)": 0, "Etiqueta Social": 0, "Sabedoria das Ruas": 0,
                             "Táticas (2)": 0, "Ensinar": 0, "Sobrevivência no Ermo": 0},
            "Reflexo": {"Brigar": 0, "Esquivar/Escapar": 0, "Curta Distância": 0, "Cavalgar": 0, "Velejar": 0,
                        "Lâminas Pequenas": 0, "Cajado/Lança": 0, "Esgrima": 0},
            "Destreza": {"Arco e Flecha": 0, "Atletismo": 0, "Besta": 0, "Prestidigitação": 0, "Furtividade": 0},
            "Corpo": {"Físico": 0, "Tolerância": 0},
            "Empatia": {"Carisma": 0, "Ludibriar": 0, "Belas Artes": 0, "Apostar": 0, "Aparência e Estilo": 0,
                        "Percepção Humana": 0, "Liderança": 0, "Persuasão": 0, "Apresentação": 0, "Sedução": 0},
            "Criar": {"Alquimia (2)": 0, "Criar (2)": 0, "Disfarce": 0, "Primeiros Socorros": 0, "Falsificação": 0,
                      "Arrombar Fechadura": 0, "Criar Armadilhas": 0},
            "Vontade": {"Coragem": 0, "Criar uma Hex (2)": 0, "Intimidação": 0, "Lançar Feitiços (2)": 0,
                        "Resistir a Magia (2)": 0, "Resistir Coerção": 0, "Criar Ritual (2)": 0}
        }
        pontos_p_essencial = 44
        pontos_p_adquiridas = int(self.atributos["Inteligência"]) + int(self.atributos["Reflexos"])


# {'Nome do jogador': '1', 'Nome do personagem': '1', 'Sexo': 'Masculino', 'Raça': 'humano', 'Profissão': 'bardo'}
# {'Confiável': 'Em um mundo onde não-humanos não podem ser confiados, os humanos parecem mais confiáveis. Os humanos têm +1 em testes de Carisma, Sedução e Persuação contra outros humanos.', 'Ingenuidade': 'Os humanos são inteligentes e, no geral, têm soluções brilhantes para problemas difíceis. Os humanos ganham +1 em Dedução.', 'Cegamente Teimoso': 'Parte da grande força da raça humana é a sua interminável disposição de seguir em frente, mesmo em situações que verdadeiramente ameaçam a sua vida. Um humano pode invocar a sua coragem e jogar novamente uma jogada fracassada de Resistir Coerção ou Coragem por três vezes por sessão de jogo. Eles ficam com o resultado maior das duas jogadas, mas se ainda assim fracassarem, não podem usar novamente a habilidade para fazer a jogada.', 'vantagem background': '+1 Carisma'}
# {'Inteligência': 8, 'Reflexos': 4, 'Destreza': 3, 'Corpo': 9, 'Velocidade': 9, 'Empatia': 9, 'Criar': 7, 'Vontade': 10, 'Sorte': 5, 'Pontos de Vida': 45, 'Estamina': 45, 'Recuperação': 9, 'Atordoamento': 9, 'Soco': (1, 'd6', 4), 'Chute': (1, 'd6', 8), 'Fardo': 90, 'Correr': 27, 'Salto': 5}
# ['Norte', 'Teméria', 'Adotado por um mago. Você foi dado ainda criança para um mago. Viveu com conforto, mas mal via o seu guardião, que estava sempre ocupado.', 'Um conde. A sua maior influência foi um conde ou condessa que lhe ensinou a se comportar.']
# ['Espetáculo de Rua', 'Carisma', 'Ludibriar', 'Apresentação', 'Língua', 'Percepção Humana', 'Persuação', 'Sabedoria das Ruas', 'Belas Artes', 'Sedução', 'Etiqueta Social']
# [0, 'Nenhuma']
# ['Tabuleiro de Pôquer de Dados', 'Baralho de Gwent', 'Espelho de Mão', 'Um Instrumento', 'Frasco de Destilado']


