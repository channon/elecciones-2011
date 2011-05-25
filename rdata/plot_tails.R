d <- data.frame(read.csv('2011.csv'))
d7 <- data.frame(read.csv('2007.csv'))

png(filename="tails.png", height=450, width=600, bg="white")

plot(d$rank + 1, d$conc, log="xy", ylim=c(1,27000), xlim=c(1,1200), col="orange", xlab="", ylab="")
par(new=TRUE)
plot(d7$rank + 1, d7$conc, log="xy", ylim=c(1,27000), xlim=c(1,1200), col="black", xlab="orden de los partidos", ylab="numero de concejales", main="#nolesvotamos")

tick.seq <- c(1:10, seq(20,100,by=10), seq(200,1000,by=100), seq(2000,10000, by=1000))
axis(1, at=tick.seq, labels=F, tck=-0.01)
axis(2, at=tick.seq, labels=F, tck=-0.01)

dev.off()
