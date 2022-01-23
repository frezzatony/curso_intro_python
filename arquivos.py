#arquivos
import shutil
  
def escrever_arquivo(texto):
  arquivo = open('teste.txt','w')
  arquivo.write(texto)
  arquivo.close()

def atualizar_arquivo(arquivo,texto):
  arquivo = open(arquivo,'a')
  arquivo.write(texto)
  arquivo.close()
  
def ler_arquivo(arquivo):
  arquivo = open('teste.txt','a')
  texto = arquivo.write(texto)
  print(texto)
  arquivo.close()

def media_notas(nome_aquivo):
  arquivo = open(nome_aquivo,'r')
  bancoNotas = arquivo.read()
  bancoNotas = bancoNotas.split('\n')
  
  for x in bancoNotas:
    listaNotas = x.split(',')
    nomeAluno = listaNotas[0]
    listaNotas.pop(0)
    media = lambda notas: sum([int(i) for i in notas])/len(notas)
    #print('Média de {}: {}'.format(nomeAluno, media(listaNotas)))
    #print(media(listaNotas))
    listaMedias = {nomeAluno:media(listaNotas)}
    
    print(listaMedias)
  
def copiaArquivo(nomeArquivo):
  shutil.copy(nomeArquivo,'notas_copiado.txt')
  
def moveArquivo(nomeArquivo):
  shutil.move(nomeArquivo,'notas2Renomeado.txt')
  
if __name__ == '__main__':
  #alunos = 'Leo,7,9,3,8\n'
  #atualizar_arquivo('notas.txt',alunos)
 #media_notas('notas.txt')
 #copiaArquivo('notas.txt')
 moveArquivo('notas2.txt')