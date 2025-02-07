import sys

var = sys.argv[2]

def http(dd='', k1=0, k2=0, k3=0, s1='', s2=''):
  sal = dd[0:k1-1] + ' `' + s1 + ' <' + s2 + '>`_' + dd[k3+1:]
  return sal

def punto_raya(dd='', k1=0, k2=0, k3=0, s2=''):
  s2 = s2[2:]
  s2 = s2.replace('á', 'a')
  s2 = s2.replace('é', 'e')
  s2 = s2.replace('í', 'i')
  s2 = s2.replace('ú', 'u')
  s2 = s2.replace('ó', 'o')
  s2 = s2.replace(':-', '-')
  s2 = s2.replace(':', '-')
  s2 = s2.replace('_-', '-')
  if k1 > 0:
    sal = dd[0:k1-1] + ' :doc:`' + s2 + '`' + dd[k3+1:]
  else:
    sal = ' :doc:`' + s2 + '`' + dd[k3+1:]
  return sal

def es_gato(dd=''):
    k=1
    while dd[k] == '#':
      k = k+1
    while dd[k] == ' ':
      k = k+1
    sal= dd[k:]
    sal= sal + '--------------------\n\n'
    return sal

def parentesis_corchete(dd=''):
    print('parentesis_corchete --- ' +dd)
    k2 = dd.find('](')
    k1 = dd.rfind('[',0,k2-1)
    s1 = dd[k1+1:k2]
    k3 = dd.find(')',k2+1)
    s2 = dd[k2+2:k3]
    print([k1, k2, k3]) 
    print(s1)
    print(s2)
    if 'http' in s2:
      ss = http(dd, k1, k2, k3, s1, s2)
    elif './' in s2:
      ss = punto_raya(dd, k1, k2, k3, s2)
    print('salida ---- '+ss)
    return ss

filin = sys.argv[1]

file = filin + '.md'

#file = 'Home.rst'

fil = open(file, 'r')

datos = fil.readlines()
fil.close()

fileN = filin + '.rst'

filo = open(fileN, 'w')

ray = '====================\n\n'

dd = datos[0]

sal = ''

# encabezado ===========================================

palabra = dd.replace('\n','')
print(palabra)

sal=sal + palabra[2:] + ' ' + var + '\n' +  ray

filo.write(sal)

nl = len(datos)

i=1
while i < nl:
  print(i)
  dd = datos[i]
  if len(dd) == 0:
    filo.write(dd)
  else:
    dd = dd.replace('`','``')
    if dd[0] == '#':
      ss = es_gato(dd)
      filo.write(ss)
    elif '](' in dd:
      sal = parentesis_corchete(dd)
      filo.write(sal)
    else:
      sal = dd
      filo.write(sal)
  i = i+1

filo.close()

'''
    elif '](' in dd:
      sal = parentesis_corchete(dd)
      filo.write(ss)
    elif '[[images' in dd:
      k1 = dd.find('/')
      k2 = dd.find(']')
      x2 = dd[k1+1:k2]
      sal = '.. image:: '+ x2 + '\n'
      filo.write(sal)
    elif '```' in dd:
      sal = '.. code-block:: Bash \n\n'
      i = i+1
      dd = datos[i]
      while '```' not in dd:
        sal = sal + '   ' + dd
        i = i+1
        dd = datos[i]
      i=i+1
      filo.write(sal)
'''

