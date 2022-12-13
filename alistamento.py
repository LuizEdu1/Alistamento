from datetime import date

ano = date.today().year
print(ano)
def alistamento():
    nascimento = int(input('Digite o ano de seu nascimento: '))
    if ano - nascimento == 18:
        print('Você deve se alistar esse ano')
    elif ano - nascimento > 18:
        print('Voce deveria estár alistado há {} ano(s)'.format(ano - nascimento - 18))
        print('Seu alistamento foi em {}'.format(nascimento + 18))
    else:
        print('Você ainda é muito novo, faltam {} ano(s) para o seu alistamento militar'.format(18-(ano-nascimento)))
        print('Seu alistamento será em {}'.format(nascimento + 18))
alistamento()