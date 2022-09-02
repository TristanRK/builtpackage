from mypackage import mymodule

def testtopn():
    """
    make sure topn works correctly
    """
    
    assert mymodule.topn([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert mymodule.topn([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert mymodule.topn([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'