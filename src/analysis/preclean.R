library(data.table)

dt <- fread('../../gen/data-preparation/output/dataset.csv')
dt2 <- fread('../../gen/data-preparation/output/dataset2.csv')


dir.create('../../gen/analysis/temp/', recursive = TRUE)
dir.create('../../gen/analysis/output/', recursive = TRUE)
fwrite(dt, '../../gen/analysis/temp/preclean.csv')
fwrite(dt2, '../../gen/analysis/temp/preclean2.csv')
