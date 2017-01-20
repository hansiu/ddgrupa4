# ddgrupa4
*Drug Design university project by group nr 4 (dataset 4)*

#### Teoria
Bedziemy mieli do czynienia z hipotezą *bioizosteryzmów*, czyli taką że istnieją grupy funkcyjne w ligandach które są preferowane przez jakieś otoczenie aminokwasowe centrum aktywnego (np. jeśli w jakimś otoczeniu są hydrofobowe, to powinien tam się znajdować benzen, czy grupa metylowa). Bioizosteryzm polega na znajdowaniu takich grup i wymienianiu (np wymiana jednej grupy hydrofobowej z drugą która wiaże się z podobnym wzorem aa).
Będziemy chcieli potwierdzić lub zaprzeczyć hipotezie chemoinformatycznie.

#### Technikalia
* Są 4 zbiory.
* Baza *pdbbind*, rejestracja darmowa.
* Z bazy możemy wyciągnać struktury razem z ligandami.
* Następnie w ligandach można znalezć grupy funkcyjne zawarte w pliku ze smilesami.
* Chcemy zobaczyć jakie jest otoczenie tych grup w tych wszystkich strukturach niosących taką grupę.
* Preferowane jest zautomatyzowanie korzystając z biblioteki *pybel* ale można to wykonać łącząc ze sobą w pipeline *openbabel, chimera* i *R*.

> **Jak zdefiniujemy sobie otoczenie?**
>Otoczenie grupy funkcyjnej zdefiniujemy w prosty i zgrubny sposób : wybierzemy trzy >aminokwasy które mają jakikolwiek atom najbliżej naszej grupy funkcyjnej - np. w chimerze można wyznaczyć *zone* w okolicy grupy funkcyjnej, do outputu wypisalibyśmy listę atomów w odl. 3A.

* Następnie wybierzemy trzy atomy najbliższe należące do różnych aa.
* Mając otoczenie (czy listę otoczeń, bo duża liczba struktur - każda z tych grup funkcyjnych będzie miała ~100 struktur albo nawet 500), czy właściwie statystykę rozkładu otoczenia możemy porównywać między sobą grupy funkcyjne.

#### Cel
* Zobaczyć czy hipoteza o hydrofobowości jest prawdziwa (np czy wokół benzenu występują same te ...).
* Potwierdzić lub zaprzeczyć hipotezie że grupy o podobnych właściwościach fizykochemicznych czy wielkości lub ładunku preferują podobne otoczenia.
* Albo w ogóle coś innego - np. że grupy hydrofobowe wcale nie potrzebują otoczenia hydrofobowego bo np. elektrostatyka odgrywa główną rolę.

#### Ocenianie
* Analiza tych danych i wyciąganie z nich korelacji lub własne podejście do analizy i własne pytania badawcze są silnie promowane.
* Im ciekawsze pytania i analizy zrobione, tym wyższa ocena.
* Niezbyt nudna prezentacja.
* Odpowiedzi na pytania wynikające z poprzednich pytań i odpowiedzi.
* Ocena końcowa z przedmiotu: średnia z projektów indywidualnego i grupowego oraz subiektywna ocena pracy na zajęciach.

#### Uwaga
Należy pamiętać o tym, żeby zrobić coś w rodzaju *background probability* (statystyka jak często dane aa są w centrum aktywnym). Grupy funkcyjne z najczęstszymi powinny mieć niższy score/być mniej promowane.