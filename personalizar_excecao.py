class Error(Exception):
  pass

class InputError(Error):
  def __init__(self,message):
    self.message = message


while True:
  try:
    x = int(input('Digite a nota entre 0 a 10: '))
    if x > 10 :
      raise InputError('Nota não pode ser maior que 10')
    if x < 0 :
      raise InputError('Nota não pode ser menor que 0')
    
    
    break;
  except ValueError:
    print('valor inálido. digite apenas números')
  except InputError as exception:
    print(exception)