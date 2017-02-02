library(ggplot2)
library(rCharts)
library(gridExtra)
library(scales)
library(tidyr)

inicjalizuj <- function(angs=3){
  #tu ustawiam folder w którym pracuję
  #musisz sobie tu wpisać swój folder ddgrupa4 mój wykomentuj
  #setwd("Asiowe")
  setwd("/home/hania/ProjLek/ddgrupa4")
  
  if(angs==3){
    setwd("results")
  } else
  {
    setwd("results_5A")
  }
  
  #wiem że brzydko globalne, ale robie tu bo a) wygodnie, b) to nie na zaliczenie u Bieceła przeca.
  aa <<- read.csv('normalWynikiaa.csv',sep=';')
  div_aa <<- read.csv('weightedWynikiaa.csv',sep=';')
  min_aa <<- read.csv('weightedminusWynikiaa.csv',sep=';')
  aaprobs <<- read.csv('all_groups.csv',sep=',',header=FALSE)
  
  ion <<- read.csv('normalWynikiion.csv',sep=';')
  div_ion <<- read.csv('weightedWynikiion.csv',sep=';')
  min_ion <<- read.csv('weightedminusWynikiion.csv',sep=';')
  ionprobs <<- read.csv('ions_all_group.csv',sep=',',header=FALSE)
  
  #pytanie czy chcemy też dla grup zrobić wykresy dla ilu plików były
  #znalezione jakiekolwiek otoczenia/dla ilu nie?
}

przygotuj_i_zrob_ladniusi_wykres <- function(angs=3){
  divaa <- data.frame(div_aa)
  divion <- data.frame(div_ion)
  for(i in 1:20){
    danea <- data.frame(div_aa[div_aa$grupa==i,2:21])
    divaa[i,2:21] <- rescale(as.matrix(danea))
    danei <- data.frame(div_ion[div_ion$grupa==i,2:24])
    divion[i,2:24] <- rescale(as.matrix(danei))
    
  
  }
  divaa <- gather(divaa, 'aminokwas','wartosc', -grupa)
  wszystkieaa <- nPlot(wartosc ~ aminokwas, group = 'grupa', data = divaa, type = 'multiBarChart')
  wszystkieaa$save(paste0(toString(angs),'_wszystkieaa.html'))
  
  divion <- gather(divion, 'heteroatom','wartosc', -grupa)
  wszystkieion <- nPlot(wartosc ~ heteroatom, group = 'grupa', data = divion, type = 'multiBarChart')
  wszystkieion$save(paste0(toString(angs),'_wszystkieion.html'))
  
  #prwdp trzebaby dla osobnych grup
  #prawdopodobienstwa <- nPlot(V3 ~ V2, group = 'grupa', data = aaprobs, type = 'pieChart')
  
}





inicjalizuj()
przygotuj_i_zrob_ladniusi_wykres()
inicjalizuj(5)
przygotuj_i_zrob_ladniusi_wykres(5)
#porownaj_wagi()
#porownaj_wagi(5)