import src.game.rules as rules


def test_a_live_cell_with_less_than_two_live_neighbours():
    # should die
    assert rules.infer_new_state(True, [False, False, False]) == False


def test_a_live_cell_with_two_or_three_live_neighbours():
    # should stay alive
    assert rules.infer_new_state(True, [True, True, False, False]) == True
    assert rules.infer_new_state(True, [True, True, True, False]) == True


def test_a_live_cell_with_more_than_three_live_neighbours():
    # should die
    assert rules.infer_new_state(False, [True, True, True, True]) == False


def test_a_dead_cell_with_three_exactly_live_neighbours():
    # should come to life
    assert rules.infer_new_state(False, [True, True, True, False]) == True


def test_a_dead_cell_that_does_not_have_exaclty_three_live_neighbours():
    # any dead cell that does not have exactly 3 live neigbours should stay dead
    assert rules.infer_new_state(False, [False, False, False, False]) == False
    assert rules.infer_new_state(False, [True, False, False, False]) == False
    assert rules.infer_new_state(False, [True, True, False, False]) == False
    assert rules.infer_new_state(False, [True, True, True, True]) == False
