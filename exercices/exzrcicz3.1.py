def table(base, debut, fin, inc):
    """Affiche la table des <base>, de <debut> a <fin>, de <inc> en <inc>."""
    x = debut
    while x <= fin:
        print(x, 'y', base, '=', x*base)
        x = x + inc

table(2, 4, 8, 1)