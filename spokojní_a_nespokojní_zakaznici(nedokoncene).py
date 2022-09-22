spokojní = [0] * 24
nespokojní = [0] * 24

subo= open ('subory/spokojnost_2.txt',  'r')
for riadok in subor:
    riadok = riadok.strip ()
    info = riadok.split()
    spokojnost = info[1]
    cas = info[0].split(':')
    hodina = int(cas[0])
    minuta = int (cas[1])
    if spokojnost == 'ano':
        spokojní [hodina] +=1
    else:
        nespokojní[hodina] +=1

pocet_spokojnych = sum(spokojní)
pocet_nespokojnych = sum(nespokoni)
spolu = pocet_spokonych + pocet_nespokojnych
print('Vyjadrilo sa { } zákazníkov.'.format(spolu))
pocet_ok = max(spokojni)
hodina = spokojni.index(pocet_ok)
print('Najviac spokojných zak. ({ }) je cez hodinu: {}'.format (pocet_ok,hodina))
nespokojni2 = [ ]
for pocet in nespokojní:
    if pocet >0:
        nespokojná2.append(pocet)
pocet_zle = min(nespokojni2)
hodina = nespokojní.index(pocet_zle)
print('Najmenej spokojných zak. ({ }) je cez hodinu :{}.'.format(pocet_zle, hodina)

percenta_spokojni = [0] *24
for i in range(24):
      pocet = spokojni[1]+nespokojni[1]
      if pocet >0:
          percenta_
      
