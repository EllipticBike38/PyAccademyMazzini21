# 30 -> True: sum( fattori_primi ** -1 ) == 1 / 30

# 70k limite max

#i numeri di Giuga noti sono:
#30
#858
#1.722
#66.198
#2.214.408.306
#24.423.128.562
#432.749.205.173.838
#14.737.133.470.010.574
#550.843.391.309.130.318
#244.197.000.982.499.715.087.866.346
#554.079.914.617.070.801.288.578.559.178
#1.910.667.181.420.507.984.555.759.916.338.506
#4.200.017.949.707.747.062.038.711.509.670.656.632.404.195.753.751.630.609.228.764.416.142.557.211.582.098.432.545.190.323.474.818

#abbandonato: funzionava ma è troppo lento, non potevo aspettarmi diversamente visto che ne sono noti 13 e l'ultimo è esageratamente lungo

#per gentile concessione, mi serviva che fosse veloce
def numeri_primid(n: int) -> dict:

    out = {}
    registro = [True]*(n+1)  # [True for x in range(n+1)]

    for p in range(2, n+1):
        if registro[p]:
            out[p] = None
            for i in range(p, n+1, p):
                registro[i] = False
    return out

def fattori_primi_invertiti(n):
        return [1/x for x in numeri_primid(int(n**0.5)+1) if not n%x]
    
def giuga(n):
        ss=sum(el for el in fattori_primi_invertiti(n))
        if 0.99999999999<ss-1/n<1.000000000001:
            print(ss-1/n, ss, 1/n, n)
            return True
        return False
for i in range(2,3000000000, 2):
    if not giuga(i):pass
