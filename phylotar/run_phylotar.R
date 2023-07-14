library(phylotaR)
library(tidyverse)

ncbi_ids = read_csv('updated_cuticle_papers_taxa.csv') %>%
  pull(`NCBI ID`) %>%
  na.exclude() %>%
  as.numeric()

workdir = './phylotar/'

dir.create(workdir, showWarnings = F)
blast_path ='/home/bdemedeiros/software/miniconda3/envs/r_env/bin/'
#setup(wd = workdir,
#      txid = ncbi_ids,
#      ncbi_dr = blast_path,
#      v = T,
#      ncps = 16
#      )

restart(workdir)
