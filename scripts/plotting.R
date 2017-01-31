library(ggplot2)
library(rCharts)
library(gridExtra)

#musisz sobie tu wpisać swój folder ddgrupa4 mój wykomentuj


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

porownaj_wagi <- function(angs=3){
  inicjalizuj(angs)
    
  for(i in 1:20){
    dane <- data.frame(aa[aa$grupa==i,2:21])
    rownames(dane) <- c("aa")
    dane["min_aa",] <- min_aa[min_aa$grupa==i,2:21]
    dane["div_aa",] <- div_aa[div_aa$grupa==i,2:21]
    dane["aaprobs",] <- t(aaprobs[aaprobs$V1==paste0("grupa",toString(1)),3])
    dane <- as.matrix(t(dane))
    #barplot(dane, beside=TRUE, col = c("blue","red","green"))
    barplot(dane[,"aa"], col="blue",main = paste0("aa grupa",toString(i)))
    barplot(dane[,"min_aa"], col="red",main = paste0("min_aa grupa",toString(i)))
    barplot(dane[,"div_aa"], col="green",main = paste0("div_aa grupa",toString(i)))
    barplot(dane[,"aaprobs"], col="yellow",main = paste0("aaprobs grupa",toString(i)))
  }
  #horiz = True?
}

porownaj_wagi()
porownaj_wagi(5)