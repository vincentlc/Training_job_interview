import pytest 
from two_anagram import is_anagram, Solution
@pytest.mark.parametrize(
    "text, anagram, expected",
    [
        ("anagram", "nagaram", True),
        ("car", "rat", False),
        ("Barco", "arcob", True),
        ("","test", False),
        ("","", True),
        ("dormitory", "dirtyroom", True),
        ("a!b", "b@a", False),
    ],
)

def test_twoAnagram(text: str, anagram:str, expected: bool):
    assert is_anagram(text, anagram) == expected

def test_solution_class():
    
    solution = Solution()
    assert solution.is_anagram("anagram", "nagaram") == True
    assert solution.is_anagram("car", "rat") == False
