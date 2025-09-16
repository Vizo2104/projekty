osoba = {}
osoba['jméno'] = ' Karel '
osoba['příjmeí'] = ' Tran '
osoba['věk'] = ' 21 '
osoba['město'] = ' Praha '
osoba['exy'] = ' linh ', "  minh ", " vuong "
print(osoba)
# přístup k hodnotám 
print(f"jméno: {osoba['jméno']}") # print (f"jméno: {osoba['jméné]}"")
#změna hodnoty
osoba['věk'] = 22
print(f"Nový věk: {osoba['věk']}" )
print("tento rok bude "+ str(osoba['věk']))
print(osoba)
osoba[' nový město '] = ' v kolíně '
 #odstranít klíče a hodnot
 # osoba[ ' nový město']
del osoba[ 'exy'] 
print(f"po odstraněnní: {osoba}")
osoba[ 'vzdělaní'] = ' ČZU '
print(f"aktualizovaná osoba : {osoba}")
#bezpečný pčístup k hodnotám pomocí klíčem
#zkusím klíč exy , ktrerý  neexistuje v slovníku
print(osoba.get('exy' )) # to bude naspáno je none 
# ale místo tohoto se dá psat 
print(osoba.get('exy' , ' který neexistuje ' ))   # výsledek bude vypádá takto # místo none se vypíše který neexistuje 
print(f"BEZPEČNÉ MĚSTO : {osoba['město']}")
print(f"nový město : {osoba.get(' nový město' , ' v kolíně , v ktrerém bydlím')}")
print(osoba[' nový město '])
