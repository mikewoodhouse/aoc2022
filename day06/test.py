import aoc
import pytest

DAY = "06"


@pytest.fixture
def example():
    return "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


@pytest.mark.parametrize(
    "stream,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part1_example1(stream: str, expected: int):
    pkt = aoc.Packet(stream)
    assert pkt.complete_index() == expected


@pytest.mark.parametrize(
    "stream,expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_part2_example2(stream: str, expected: int):
    pkt = aoc.Packet(stream)
    assert pkt.start_of_message() == expected
