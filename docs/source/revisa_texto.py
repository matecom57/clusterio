import sys

filin = sys.argv[1]

file = filin + '.dat'

#file = 'Home.rst'

fil = open(file, 'r')

datos = fil.readlines()
fil.close()

fileN = filin + '.rst'

filo = open(fileN, 'w')

ray = '====================\n\n'

dd = datos[0]

sal = ''

if dd[0] == '#':
  sal=sal + dd[2:]
  sal=sal + ray

nl = len(datos)

i=1
while i < nl:
  dd = datos[i]
  if dd[0] == '#':  
    sal=sal + dd[2:]
    sal=sal + '--------------------\n\n'
  elif '`' in dd:
    nc3 = len(dd)
    ddn = ''
    m=1
    while m < nc3:
      if dd[m] == '`':
        ddn = ddn + '``'
      else:
        ddn = ddn + dd[m]
      m = m+1
    print(dd)
  elif '](' in dd:
#    print(dd)
    k2 = dd.find('](')
    k1 = dd.find('[',0,k2-1)
    s1 = dd[k1+1:k2]
    k3 = dd.find(')',k2+1,len(dd))
#    print(s1)
    s2 = dd[k2+2:k3]
#    print(s2)
    if 'http' in s2:
      sal = sal +dd[0:k1-1] + ' `' + s1 + ' <' + s2 + '>`_' + dd[k3+1:]
    elif './' in s2:
      s2 = s2[2:]
      s2 = s2.replace('ú', 'u')
      s2 = s2.replace(':-', '-')
      s2 = s2.replace(':', '-')
      sal = sal +dd[0:k1-1] + ' :doc:`' + s1 + ' <' + s2 + '>`' + dd[k3+1:] + '\n'
    else:
      sal = sal +dd[0:k1-1] + ' `' + s1 + 'xxxx' + s2 + 'xxx' + dd[k3+1:]
  else:
    sal = sal + dd 
  i = i+1

filo.write(sal)
filo.close()

