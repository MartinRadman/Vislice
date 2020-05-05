def gen_prastevil():
    prastevila = []
    kandidat = 2
    while True:
        status = True
        for prastevilo in prastevila:
            if kandidat % prastevilo == 0:
                status = False
        if status:
            prastevila.append(kandidat)
            yield kandidat
        kandidat += 1