import pytest
from main import uniqueString

def test_uniqueString():
    assert uniqueString("leetcode") == 0
    assert uniqueString("loveleetcode") == 2
    assert uniqueString("aabb") == -1
    assert uniqueString("") == -1

test_uniqueString()