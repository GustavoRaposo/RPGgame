# RPGgame
Introdução:
  Este é um jogo de RPG por turno. As mecânicas são básicas e baseadas nos RPG's clássicos, onde quem ataca primeiro é quem tem o maior
  atributo de velocidade e vence quem levar os pontos de vida (HP) do oponente a 0 por primeiro.
  Inicialmente existe dois tipos de ataque:
    - ataque básico:
      Este ataque por definição é uma magia, mas este ataque não consome pontos de mana (MP) e recupera sua pontos de mana (MP),
      porém causa um dano menor comparado aos demais ataques.
    - magias:
      Este ataque necessita que o jogador tenha pontos de mana (MP) maior ou igual ao custo desta magia, se atender essa condição o custo
      da magia é subtraido aos pontos mana (MP) total do jogador, estes ataques causam um dano maior
  Todo ataque possui chances de falhar ou causar um acerto crítico, estes dois eventos tem 5% de chance acontecer, caso o ataque falhe
  seu dano ao oponente será nulo, caso aconteça um acerto crícito o dano é multiplicado pelo atributo de dano crítico do personagem.
  Cada personagem possui atributos como:
    - pontos de vida (HP)
    - pontos de mana (MP)
    - ataque
    - defesa
    - velocidade
    - dano crítico
  Além destes atributos cada personagem possui um conjunto de  quatro (4) magias, sendo um (1) ataque básico e três (3) magias.

Como rodar o jogo:
  Primeiramente é necessário que a máquina possua Python instalado.
  Em seguiga abra algum terminal de sua preferência.
  Dentro no terminal acesse a pasta do jogo e digite "python main.py"

Codigo Fonte:
  O codigo fonte apresenta quatro (4) arquivos principais:
    - main.py
    - game.py
    - player.py
    - spell.py
    
  arquivo main:
    Este aqruivo tem a única função de executar o jogo atraves do metodo "run" que está contida no arquivo game.py
    
  arquivo game:
    Aqui estão todas as mecâncias do jogo e as instanciações das classes Player e Spell
    
  arquivo player:
    Aqui é definido a classe Player com seus atributos e metodos conrrespondente a ele.
    
  arquivo spell:
    Assim como o arquivo player, aqui é definido a classe Spell com seus atributos
