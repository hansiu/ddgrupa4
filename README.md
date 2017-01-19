# ddgrupa4
drug design university project by group nr 4
bedziemy mieli do czynienia z hipoteza bioizosteryzmów, czyli taką że istnieją grupy funkcyjne w ligandach które są preferowane przez jakieś otoczenie aminokwasowe centrum aktywnego (np. jesli w jakims otoczeniu sa hydrofobowe, to powinien tam sie znajdowac benzen, czy grupa metylowa.) bioizosteryzm polega na znajdowaniu takich grup i wymienianiu (np wymiana jednej grupy hydrofobowej z druga ktora wiaze sie z podobnym wzorem aa)
bedziemy chcieli potwierdzic lub zaprzeczyc chemoinformatycznie

sa 4 zbiory.

baza pdbbind, rejestracja darmowa.

w bazie mozemy wyciagnac struktury razem z ligandami.
nastepnie w ligandach znalezc grupy funkcyjne w pliku ze smilesami zawarte
zobaczyc jakie jest otoczenie tych grup w tych wszystkich strukturach niosących taką grupę.

preferowane jest zautomatyzowanie korzystając z biblioteki pybel ale można to wykonać łącząc ze sobą w pipeline openbabel, chimera i R.

jak zdefiniujemy sobie otoczenie?
otoczenie grupy funkcyjnej my zdefiniujemy w prosty i zgrubny sposob : wybierzemy trzy aminokwasy ktore maja jaki kolwiek atom najbliżej naszej grupy funkcyjnej. np. w chimerze można wyznaczyć zone w okolicy grupy funkcyjnej i wypisalibyśmy do outputu listę atomów w odl. 3A.

następnie wybierzemy trzy atomy najbliższe należące do różnych aa.



mając otoczenie (czy listę otoczeń, bo duża liczba struktur) (kazda z tych grup funkcyjnych będzie miała ~100 struktur albo nawet 500)
czy właściwie statystyke rozkłądu otoczenia możemy porównywać między sobą grupy funkcyjne i zobaczyć czy hipoteza o hydrofobowości jest prawdziwa (np czy wokół benzenu występują same te).

druga rzecz potwierdzić lub zaprzeczyć hipotezie że grupy o podobnych właściwościach fizykochemicznych czy wielkości czy ładunku preferują podobne otoczenia. albo w ogóle coś innego że grupy hydrofobowe wcale nie potrzebują otoczenia hydrofobowego bo np. elektrostatyka odgrywa główną rolę.

analiza tych danych i wyciąganie z nich korelacji czy własne podejście do analizy/własnego pytania jest silnie promowanie.
im ciekawsze pytania i rzeczy zrobione tym wyższa ocena.

pamiętać o tym, żeby zrobić coś w rodzaju background probability. (statystyka jak często dane aa są w centrum aktywnym). grupy funkcyjne z najczęstszymi powinny mieć niższy score być mniej promowane.

prezentacja nie będąca strasznie nudna, tok jak odpowiedzi na pytanie wynikają z poprzednich pytań i odpowiedzi

grupa 4 dane 4

ocena końcowa średnia z indywidualnego i grupowego oraz subiektywna ocena pracy na zajęciach
