library('ggplot2')

cls = read.csv('C:/TAREAN/Galaxy55/proper_tab_new.csv', header = T, sep = ';')

# Building dotplot combined with diagonal line
# Distribution of reads from two samples in clusters
cls$AA = log10(cls$AA)
cls$BB = log10(cls$BB)
ggplot(data = cls, aes(x=AA, y=BB, group=annotation, colour=annotation)) +
       labs(y = 'Number of KK2 reads (log)', x = 'Number of KK1 reads (log)') +
  geom_point(size=2) +
  geom_abline(col='red', size=1) +
  scale_color_brewer(palette = "Paired") +
  coord_cartesian(xlim = c(0,4), ylim = c(0,4))
  
# Several classes of repetitive sequences
classes = c('Ty1/copia', 'Ty3/gypsy', 'LTR', 'satellite', 'plastid', 'rDNA', 'unknown')

# Building barplot with annotated clusters
cls$sum = rowSums(df)
w = c(cls$sum * 0.0005)
n = c(cls$cluster)
barplot(cls$sum, width = w, xlim =c(0, 120), 
        names = n,
        col = c("red","green", "blue","yellow","purple","orange","black"),
        ylab = "Number of reads", xlab = "Cluster index", legend.text=classes)
