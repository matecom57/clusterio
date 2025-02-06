xx = '''
[Tensor de Estructura (Structure Tensor)](./TensorEstructura) es una herramienta que se utiliza para procesar y analizar la 
información direccional y de coherencia local de una imagen. Es un método análogo al tensor de difusión de la resonancia magnética sensible a 
difusión, pero aplicado en imágenes histológicas. En el link encontraras mas información y un tutorial de como aplicarlo.'''


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
  sal = dd[0:k1-1] + ' :doc:`' + s2 + '`' + dd[k3+1:]
  return sal

def parentesis_corchete(dd=''):
    k2 = dd.find('](')
    k1 = dd.rfind('[',0,k2-1)
    s1 = dd[k1+1:k2]
    k3 = dd.find(')',k2+1)
    s2 = dd[k2+2:k3]

    if 'http' in s2:
      ss = http(dd, k1, k2, k3, s1, s2)
    elif './' in s2:
      ss = punto_raya(dd, k1, k2, k3, s2)

    return ss



yy = parentesis_corchete(xx)

print('----------------------------------------------')
print(yy)





