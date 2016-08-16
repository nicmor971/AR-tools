import scipy as sp
import pytest

import sys
sys.path.append('../')
import artools
artools = reload(artools)


def test_stoich_S_M_1():
    # 2-D system
    # A -> B -> C

    # 0-D array feed
    Cf0 = sp.array([1., 0, 0])

    stoich_mat = sp.array([[-1., 0],
                           [1, -1],
                           [0, 1]])

    Cs, Es = artools.stoich_S_M(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 0],
                       [1, 0],
                       [1, 1]])

    assert(artools.same_rows(Es, Es_ref))
    assert(artools.same_rows(Cs, Cs_ref))


def test_stoich_S_M_2():
    # 3-D van de Vusse system
    # A -> B -> C
    # 2A -> D

    # 0-D array feed
    Cf0 = sp.array([1., 0, 0, 0])

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    Cs, Es = artools.stoich_S_M(Cf0, stoich_mat)

    Cs_ref = sp.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 0.5]])

    Es_ref = sp.array([[0, 0, 0.5],
                       [1, 1, 0],
                       [0, 0, 0],
                       [1, 0, 0]])

    assert(artools.same_rows(Es, Es_ref))
    assert(artools.same_rows(Cs, Cs_ref))


def test_stoich_S_M_3():
    # 3-D van de Vusse system
    # A -> B -> C
    # 2A -> D

    # row vector feed
    Cf0 = sp.array([[1., 0, 0, 0]])

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    Cs, Es = artools.stoich_S_M(Cf0, stoich_mat)

    Cs_ref = sp.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 0.5]])

    Es_ref = sp.array([[0, 0, 0.5],
                       [1, 1, 0],
                       [0, 0, 0],
                       [1, 0, 0]])

    assert(artools.same_rows(Es, Es_ref))
    assert(artools.same_rows(Cs, Cs_ref))


def test_stoich_S_M_4():
    # 3-D van de Vusse system
    # A -> B -> C
    # 2A -> D

    # column vector feed
    Cf0 = sp.array([[1., 0, 0, 0]]).T

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    Cs, Es = artools.stoich_S_M(Cf0, stoich_mat)

    Cs_ref = sp.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 0.5]])

    Es_ref = sp.array([[0, 0, 0.5],
                       [1, 1, 0],
                       [0, 0, 0],
                       [1, 0, 0]])

    assert(artools.same_rows(Es, Es_ref))
    assert(artools.same_rows(Cs, Cs_ref))


def test_stoich_S_M_positive_1():
    # 2-D system
    # A -> B -> C

    # Test negative conentrations
    Cf0 = sp.array([-1., 0, 0])

    stoich_mat = sp.array([[-1., 0],
                           [1, -1],
                           [0, 1]])

    with pytest.raises(Exception):
        artools.stoich_S_M(Cf0, stoich_mat)


def test_stoich_S_M_positive_2():
    # 2-D system
    # A -> B -> C

    # Test negative zero
    Cf0 = sp.array([1., -0, -0])

    stoich_mat = sp.array([[-1., 0],
                           [1, -1],
                           [0, 1]])

    Cs, Es = artools.stoich_S_M(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 0, 0],
                       [0, 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 0],
                       [1, 0],
                       [1, 1]])

    assert(artools.same_rows(Es, Es_ref))
    assert(artools.same_rows(Cs, Cs_ref))


def test_stoich_S_S_1():
    # A + B -> C

    # 0-D array feed
    Cf0 = sp.array([1., 1, 0])

    # column vector stoich matrix
    stoich_mat = sp.array([[-1., -1, 1]]).T

    Cs, Es = artools.stoich_S_S(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 1]]).T

    assert(artools.same_rows(Cs, Cs_ref))
    assert(artools.same_rows(Es, Es_ref))


def test_stoich_S_S_2():
    # A + B -> C

    # 0-D array feed
    Cf0 = sp.array([1., 1, 0])

    # row vector stoich matrix
    stoich_mat = sp.array([[-1., -1, 1]])

    Cs, Es = artools.stoich_S_S(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 1]]).T

    assert(artools.same_rows(Cs, Cs_ref))
    assert(artools.same_rows(Es, Es_ref))


def test_stoich_S_S_3():
    # A + B -> C

    # 0-D array feed
    Cf0 = sp.array([1., 1, 0])

    # 0-D array stoich matrix
    stoich_mat = sp.array([-1., -1, 1])

    Cs, Es = artools.stoich_S_S(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 1]]).T

    assert(artools.same_rows(Cs, Cs_ref))
    assert(artools.same_rows(Es, Es_ref))


def test_stoich_S_S_4():
    # A + B -> C

    # column vector feed
    Cf0 = sp.array([[1., 1, 0]]).T

    # column vector stoich matrix
    stoich_mat = sp.array([[-1., -1, 1]]).T

    Cs, Es = artools.stoich_S_S(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 1]]).T

    assert(artools.same_rows(Cs, Cs_ref))
    assert(artools.same_rows(Es, Es_ref))


def test_stoich_S_S_5():
    # A + B -> C

    # row vector feed
    Cf0 = sp.array([[1., 1, 0]])

    # column vector stoich matrix
    stoich_mat = sp.array([[-1., -1, 1]]).T

    Cs, Es = artools.stoich_S_S(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 1, 0],
                       [0, 0, 1]])

    Es_ref = sp.array([[0., 1]]).T

    assert(artools.same_rows(Cs, Cs_ref))
    assert(artools.same_rows(Es, Es_ref))


def test_stoich_S_S_6():
    # A -> B

    # binary system
    Cf0 = sp.array([1., 0])

    stoich_mat = sp.array([[-1., 1]]).T

    Cs, Es = artools.stoich_S_S(Cf0, stoich_mat)

    Cs_ref = sp.array([[1., 0],
                       [0, 1]])

    Es_ref = sp.array([[0., 1]]).T

    assert (artools.same_rows(Cs, Cs_ref))
    assert (artools.same_rows(Es, Es_ref))


def test_stoich_S_S_positive_1():
    # 2-D system
    # A -> B

    # Test negative conentrations
    Cf0 = sp.array([-1., 0])

    stoich_mat = sp.array([[-1.],
                           [1]])

    with pytest.raises(Exception):
        artools.stoich_S_S(Cf0, stoich_mat)


def test_stoich_S_S_positive_2():
    # 2-D system
    # A -> B

    # Test negative zero
    Cf0 = sp.array([1., -0])

    stoich_mat = sp.array([[-1.],
                           [1]])

    assert artools.stoich_S_S(Cf0, stoich_mat)


def test_1():
    # single feed, as a 0-D array
    # NB: test is incomplete still

    # A -> B -> C
    # 2A -> D
    Cf = sp.array([1., 0, 0, 0])
    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    S = artools.stoich_subspace(Cf, stoich_mat)
    print S


def test_2():
    # multiple feeds in a list, as 0-D arrays
    # NB: test is incomplete still
    Cf1 = sp.array([1., 0, 0, 0])
    Cf2 = sp.array([1., 1., 0, 0])

    feed_list = [Cf1, Cf2]

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    S = artools.stoich_subspace(feed_list, stoich_mat)
    print S


def test_3():
    # multiple feeds in a list, as row vectors
    # NB: test is incomplete still
    Cf1 = sp.array([[1., 0, 0, 0]])
    Cf2 = sp.array([[1., 1., 0, 0]])

    feed_list = [Cf1, Cf2]

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    S = artools.stoich_subspace(feed_list, stoich_mat)
    print S


def test_4():
    # multiple feeds in a list, as column vectors
    # NB: test is incomplete still
    Cf1 = sp.array([[1., 0, 0, 0]]).T
    Cf2 = sp.array([[1., 1., 0, 0]]).T

    feed_list = [Cf1, Cf2]

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    S = artools.stoich_subspace(feed_list, stoich_mat)
    print S


def test_5():
    # multiple feeds in a 2-D array
    # NB: test is incomplete still
    Cf1 = sp.array([[1., 0, 0, 0]])
    Cf2 = sp.array([[1., 1., 0, 0]])

    feeds = sp.vstack([Cf1, Cf2])

    stoich_mat = sp.array([[-1., 0, -2],
                           [1, -1, 0],
                           [0, 1, 0],
                           [0, 0, 1]])

    S = artools.stoich_subspace(feeds, stoich_mat)
#    print S


def test_2D_1():
    # test 2-D system
    # A -> B -> C

    Cf1 = sp.array([1.0, 0, 0])
    Cf2 = sp.array([1.0, 0.5, 0])

    feeds = [Cf1, Cf2]

    stoich_mat = sp.array([[-1., 0],
                           [1, -1],
                           [0, 1]])

    S = artools.stoich_subspace(feeds, stoich_mat)

    Cs1_ref = sp.array([[1., 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])

    Cs2_ref = sp.array([[1.5, 0, 0],
                        [0, 1.5, 0],
                        [0, 0, 1.5]])

    Es1_ref = sp.array([[0., 0],
                        [1, 0],
                        [1, 1]])

    Es2_ref = sp.array([[1., 0],
                        [1, 1.5],
                        [-0.5, 0]])

    Cs_bounds_ref = sp.array([[0.0, 0.0, 0.0],
                              [1.5, 1.5, 1.5]])

    Es_bounds_ref = sp.array([[-0.5, 0.0],
                              [1.0, 1.5]])

    Cs1 = S["all_Cs"][0]
    Cs2 = S["all_Cs"][1]
    Es1 = S["all_Es"][0]
    Es2 = S["all_Es"][1]
    Es_bounds = S["bounds_Es"]
    Cs_bounds = S["bounds_Cs"]

    assert (artools.same_rows(Cs1, Cs1_ref) is True)
    assert (artools.same_rows(Cs2, Cs2_ref) is True)
    assert (artools.same_rows(Es1, Es1_ref) is True)
    assert (artools.same_rows(Es2, Es2_ref) is True)
    assert (artools.same_rows(Cs_bounds, Cs_bounds_ref) is True)
    assert (artools.same_rows(Es_bounds, Es_bounds_ref) is True)

#test_2D_1()
# test for single reaction, multiple feeds

# test for single reaction, single feed

# test incompatible size feed and stoichiometric matrix

# test reversible reactions
