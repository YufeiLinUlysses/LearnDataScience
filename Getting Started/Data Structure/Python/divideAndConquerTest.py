import divideAndConquer as d

def test_recMC():
    test1 = 63
    assert d.recMC([1, 5, 10, 25], test1, [0]*(test1+1)) == 6
    assert d.dpMakeChange([1, 5, 10, 25], test1, [0]*(test1+1)) == 6
    assert d.dpMakeChange([1, 5, 10, 21, 25], test1, [0]*(test1+1)) == 3
