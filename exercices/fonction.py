
def table(base, debut, fin, inc):
    """Affiche la table des <base>, de <debut> a <fin>, de <inc> en <inc>."""
    n = debut
    while n <= fin:
        print(n, 'x', base, '=', n*base)
        n = n + inc
table (5 ,5 ,9 ,4)