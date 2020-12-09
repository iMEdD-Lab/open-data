rm(list = ls())
library(proxy)
library(missForest)
library(KRLS)
similarity =TRUE

setwd("/Users/angelos/Documents/Tennis_Report_and_Data/Rcode_18032020/")
years = as.character(2000:2020)

myrankings = read.csv("ultimate_tennis_rankings_historical.csv")
myplayers_org = read.csv("ultimate_tennis_players_profiles.csv",dec=".")
myplayers_org$age[967] = 40 #correct mistake in ages -was appearing as newborn!!
names_org = as.character(myplayers_org$name)

tsitsi_inds=which(!is.na(myplayers_org[which(names_org=="Stefanos Tsitsipas"),]))
myplayers = myplayers_org[,tsitsi_inds]

names = as.character(myplayers$name)
names_factor = myplayers$name

names_on_rankings = as.character(myrankings$name)
#########################player_specific_stats################################################## 
ages = myplayers$age
years_pro= 2020-myplayers$turned_pro
age_turned_pro =myplayers$turned_pro-(2020-ages) 
number_of_seasons = myplayers$seasons
prize_money= round(as.numeric(myplayers$prize_money)/number_of_seasons,2)
titles = round(myplayers$titles/number_of_seasons,2)
best_rank= myplayers$best_rank
dd = as.character(myplayers$best_rank_date)
yy_best_rank = substring(dd,7,10)
age_best_rank =as.numeric(yy_best_rank) -(2020-ages)
years_best_rank_after_turned_pro =as.numeric(yy_best_rank)-myplayers$turned_pro
dd_elo = as.character(myplayers$best_elo_rank_date)
yy_best_rank_elo = substring(dd_elo,7,10)
age_best_rank_elo =as.numeric(yy_best_rank_elo) -(2020-ages)
year_appeared = (2020-ages) + age_turned_pro
years_best_rank_elo_after_turned_pro =as.numeric(yy_best_rank_elo)-myplayers$turned_pro
overall_sur_pct= round(as.numeric(as.character(myplayers$overall_surfaces_pct)))
hard_sur_pct= round(as.numeric(as.character(myplayers$hard_surfaces_pct)))
clay_sur_pct=round(as.numeric(as.character(myplayers$clay_surfaces_pct)))
grass_sur_pct=round(as.numeric(as.character(myplayers$grass_surfaces_pct)))
h2h=round(as.numeric(as.character(myplayers$h2h)))
favorite_surface = as.character(myplayers$favorite_surface)
backhand = as.character(myplayers$backhand)
plays = as.character(myplayers$plays)
ranks4=matrix(NA,length(names),4)
ranksDiff = matrix(NA,length(names),3)
for(i in 1:length(names)){
  
  inds = which(names_on_rankings ==names[i])
  ranks4[i,]= myrankings[inds,1][1:4]
  ranksDiff[i,] =abs(diff(ranks4[i,],na.rm=T))
}


continuous_stats = cbind(years_pro,age_turned_pro,prize_money,best_rank,age_best_rank,years_best_rank_after_turned_pro,
                         age_best_rank_elo,years_best_rank_elo_after_turned_pro,overall_sur_pct,
                         hard_sur_pct,clay_sur_pct,grass_sur_pct,h2h,ranksDiff[,1],ranksDiff[,2],ranksDiff[,3],ranks4[,1],ranks4[,2],ranks4[,3],ranks4[,4])
colnames(continuous_stats) = c('years_pro','age_turned_pro','prize_money',
                               'best_rank','age_best_rank','years_best_rank_after_turned_pro',
                               'age_best_rank_elo','years_best_rank_elo_after_turned_pro','overall_sur_pct',
                               'hard_sur_pct','clay_sur_pct','grass_sur_pct','h2h','ranksDiff1','ranksDiff2','ranksDiff3',
                               'rank1','rank2','rank3','rank4')


####################################################################################################

#########################checking missing values################################################## 

nas_columns = colnames(continuous_stats)[colSums(is.na(continuous_stats)) > 0]
nas_rows = rownames(continuous_stats)[rowSums(is.na(continuous_stats)) > 0]
na_col_prop = colSums(is.na(continuous_stats))/dim(continuous_stats)[1]
na_row_prop = rowSums(is.na(continuous_stats))/dim(continuous_stats)[2]

continuous_stats = continuous_stats[-which(na_row_prop>0.5),]  
nas_columns = colnames(continuous_stats)[colSums(is.na(continuous_stats)) > 0]
na_col_prop = colSums(is.na(continuous_stats))/dim(continuous_stats)[1]

continuous_stats = continuous_stats[,-which(na_col_prop>0.5)]  
names = names[-which(na_row_prop>0.5)]


