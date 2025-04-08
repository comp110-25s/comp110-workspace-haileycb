"""Unit tests for dictionary functions"""

__author__: str = "730562399"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert1() -> None:
    """Test if invert function runs as expected"""
    assert invert({"bob": "john"}) == {
        "john": "bob"
    }  # test a use case of expected input


def test_invert2() -> None:
    """Test if invert function runs as expected"""
    assert invert({"q": "z", "f": "s"}) == {"z": "q", "s": "f"}


def test_invert3() -> None:
    """Test if invert function runs as expected"""
    assert invert({"4": "7", "f": ""}) == {
        "7": "4",
        "": "f",
    }  # edge case test with different strings and empty input


def test_count1() -> None:
    """Test if count function runs as expected"""
    assert count(["cat", "dog", "cat"]) == {
        "cat": 2,
        "dog": 1,
    }  # use case tests with typical expected inputs


def test_count2() -> None:
    """Test if count function runs as expected"""
    assert count(["a", "a", "a"]) == {"a": 3}


def test_count3() -> None:
    """Test if count function runs as expected"""
    assert count(["", "7", "7"]) == {
        "": 1,
        "7": 2,
    }  # edge case test with empty input and different style of input str


def test_favorite_color1() -> None:
    """Test if favorite color function runs as expected"""
    assert favorite_color({"bob": "blue", "jenny": "green", "sara": "blue"}) == (
        "blue"
    )  # use case typical expected inputs and results


def test_favorite_color2() -> None:
    """Test if favorite color function runs as expected"""
    assert favorite_color({"jamie": "blue", "sue": "yellow", "johnie": "yellow"}) == (
        "yellow"
    )


def test_favorite_color3() -> None:
    """Test if favorite color function runs as expected"""
    assert favorite_color({"lilly": "blue", "cole": "green", "sam": ""}) == (
        "blue"
    )  # edge case test with a tie and empty input


def test_bin_len1() -> None:
    """Test if bin length function runs as expected"""
    assert bin_len(["tree", "boy", "girl"]) == {
        4: {"girl", "tree"},
        3: {"boy"},
    }  # expected use case typical outputs


def test_bin_len2() -> None:
    """Test if bin length function runs as expected"""
    assert bin_len(["a", "aa", "aaa", "aaa"]) == {1: {"a"}, 2: {"aa"}, 3: {"aaa"}}


def test_bin_len3() -> None:
    """Test if bin length function runs as expected"""
    assert bin_len([""]) == {0: {""}}  # edge case with only one empty input
