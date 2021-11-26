## Capitais do Brasil

print('''
      .  .-+  ._/V\\
     / \/   \/    /__
    )                "-+._
   ."                     \\
  (       B R A S I L      )
   \                      /
     \__                 (
        >_               )
          \_.           /
             < S.Paulo /
              \   *  _/
               >    /
              /    /
             <    /
              "^./
''')

acerto=0
capitais = {"Acre" : "Rio Branco",
            "Alagoas" : "Maceió",
            "Amapa" : "Macapa",
            "Amazonas" : "Manaus",
            "Bahia" : "Salvador",
            "Ceará" : "Fortaleza",
            "Ditrito Federal" : "Brasília",
            "Espírito Santo" : "Vitória",
            "Goias" : "Goiânia",
            "Maranhão" : "São Luís",
            "Mato Grosso" : "Cuiabá",
            "Mato Grosso do Sul" : "Campo Grande",
            "Minas Gerais" : "Belo Horizonte",
            "Pará" : "Belém",
            "Paraíba" : "João Pessoa",
            "Paraná" : "Curitiba",
            "Pernambuco" : "Recife",
            "Piauí" : "Teresina",
            "Rio de Janeiro" : "Rio de Janeiro",
            "Rio Grande do Norte " : "Natal",
            "Rio Grande do Sul" : "Porto Alegre",
            "Rondônia" : "Porto Velho",
            "Roraima" : "Boa Vista",
            "Santa Catarina" : "Florianópolis",
            "São Paulo" : "São Paulo",
            "Sergipe" : "Aracaju",
            "Tocantins" : "Palmas"
} 

print("Voce consegue conhece todas as capitais do Brasil ? Quer testar seus conhecimentos? \n")

print("Vamos Começar ? \n")

for estado in capitais:
    resposta=input(f"Qual a capital do estado de {estado} ? :").lower()
    if resposta == capitais[estado].lower():
        acerto += 1
        print(f"Certa Resposta! {capitais[estado]} \n" )
    else:
        print(f"Errou . . . A capital do {estado} é {capitais[estado]} \n")
        
score = round((acerto / 27) * 100)
print(f"Voce acertou : {score} %\n")