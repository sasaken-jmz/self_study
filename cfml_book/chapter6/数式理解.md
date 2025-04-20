# 数式理解

ある1年間$t$~$t+11$に観測される報酬$r_{u, t:t+11}$の同時分布に関する分解を考える  
$
p(r_{u,t:t+11} \mid x_u, a_{u,t-h:t+11})
=
p(r_{u,t} \mid x_u, a_{u,t-h:t}) \,
p(r_{u,t+1:t+11} \mid x_u, a_{u,t-h+1:t+11}, r_{u,t})
$ - (6.9)

$
\textcolor{red}{
p(r_{u,t:t+11} \mid x_u, a_{u,t-h:t+11})
}
=
p(r_{u,t} \mid x_u, a_{u,t-h:t}) \,
p(r_{u,t+1:t+11} \mid x_u, a_{u,t-h+1:t+11}, r_{u,t})
$  
左辺:  
ユーザの状態$x_u$と$t-h$から$t+11$までに取った行動$a_{u,t-h:t+11}$に基づく、  
ユーザ$u$が時刻$t$から$t+11$までに得る報酬$r_{u, t:t+11}$の確率分布

$
p(r_{u,t:t+11} \mid x_u, a_{u,t-h:t+11})
=
\textcolor{red}{
p(r_{u,t} \mid x_u, a_{u,t-h:t}) \,
}
p(r_{u,t+1:t+11} \mid x_u, a_{u,t-h+1:t+11}, r_{u,t})
$  
右辺①:  
ユーザの状態$x_u$と$t-h$から$t$までに取った行動$a_{u,t-h:t}$に基づく、  
ユーザ$u$が時刻$t$に得る報酬$r_{u, t}$の確率分布

$
p(r_{u,t:t+11} \mid x_u, a_{u,t-h:t+11})
=
p(r_{u,t} \mid x_u, a_{u,t-h:t}) \,
\textcolor{red}{
p(r_{u,t+1:t+11} \mid x_u, a_{u,t-h+1:t+11}, r_{u,t})
}
$  
右辺②:  
ユーザの状態$x_u$と$t-h+1$から$t+11$までに取った行動$a_{u,t-h:t}$と時刻$t$における報酬$r_{u,t}$に基づく、  
ユーザ$u$が時刻$t$に得る報酬$r_{u, t:t+11}$の確率分布