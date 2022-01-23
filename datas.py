#datas

from datetime import date,time, datetime, timedelta

def trabalhandoComDate():
  dataAtual = date.today()
  print(dataAtual.strftime('%d/%m/%Y'))

def trabalhandoComTime():
  horario = time(hour=14,minute=31,second=25)
  horario = (horario.strftime('%H:%M:%S'))
  print(type(horario))
  
def trabalhandoComDateTime():
  dataAtual = datetime.now()
  #print(dataAtual.strftime('%Y-%m-%d'))
  print(dataAtual.strftime('%H:%M:%S'))
  print(dataAtual.strftime('%c'))
  print(dataAtual.day)
  print(dataAtual.month)
  
  dataString = '01/01/2022'
  dataConvertida = datetime.strptime(dataString, '%d/%m/%Y')
  print(dataConvertida)
  
  novaData = dataConvertida - timedelta(days=365,seconds=10)
  print(novaData)
  
if __name__ == '__main__':
  #trabalhandoComDate()  
  #trabalhandoComTime()
  trabalhandoComDateTime()