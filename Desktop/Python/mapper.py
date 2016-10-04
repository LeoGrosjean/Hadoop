#!/usr/bin/env python
#on import ces modules
import re, string
phrase = input()
#phrase = ' A ABCDEDFGG lâge de treize ans, la mere grosjean une future sorcière doit partir faire son apprentissage dans une ville inconnue durant un an. Une expérience que va vivre la jeune et espiègle Kiki aux côtés de Osono, une gentille boulangère qui lui propose un emploi de livreuse été indien où périmtre.%un deux cacahuettes trois, cruela , bachibouzouke, le mot qui suit n a rien a voir avec la chanson,gzgzefzu% trois petits chats'
#j'enlève toute la ponctuation
regex = re.compile('[%s]' % re.escape(string.punctuation))
phrase = regex.sub(' ', phrase)
#je met tout en minuscule
phrase = phrase.lower()
#je remplace les caractères avec les accents, j'ai des problemes de gestion d'encodage
phrase = phrase.replace('é','e')
phrase = phrase.replace('è','e')
phrase = phrase.replace('ê','e')
phrase = phrase.replace('ù','u')
phrase = phrase.replace('à','a')
phrase = phrase.replace('â','a')
phrase = phrase.replace('ô','o')
#j'affiche la phrase en input
print (phrase)
words = phrase.split()
words.sort()
motactuel = ''
f = open('Map.txt','w')

for word in words:
    n = words.count(word)
    if(word !=motactuel):
        ligne = str(word) +','+ str(n) + '\n'
        f.write(ligne)
        #print (ligne)
        motactuel = word
    else:
        motactuel = word
f.close()
