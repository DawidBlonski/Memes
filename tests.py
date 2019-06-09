from main import calculate


def test_data_test():

    assert calculate(1, [("dolan.png", 126, 5), ("expanding_brain.jpeg", 421, 10)]) == (
        15,
        {"dolan.png", "expanding_brain.jpeg"},
    )

    assert calculate(
        1,
        [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ],
    ) == (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})


def test_no_data():
    assert calculate(0,[]) == (0,set())

def test_duplicate_data():
    assert calculate(
        1,
        [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ],
    ) == (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})


