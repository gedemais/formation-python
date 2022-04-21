
def table(base, debut, fin, inc) : 
    """affiche la table des <base>, de <debut>, a <fin>, de <inc> en <inc>"""
    n = debut
    while n <= fin:
        print (n, 'y', base, '=', n*base)
        n = n + inc
        
table(2, 4, 8, 1)