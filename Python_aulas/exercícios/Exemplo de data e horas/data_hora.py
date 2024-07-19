# formatação de data e hora

from datetime import datetime

# data e hora atual usando o método now()

agora = datetime.now()
data_hora = agora.strftime('%d/%m/%Y %H:%M:%S')
print(data_hora)

# obiter apenas a data atual usando o método today()

hoje = datetime.today()
data = hoje.strftime('%d/%m/%Y %H:%M:%S')
print(data)

# solicitar ao usuário uma data e hora

data_hora = input('Digite uma data (dd/mm/aaaa): ')
data_hora = input('Digite uma hora (hh:mm:ss): ')