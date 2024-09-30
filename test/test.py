
import pytest
from unittest.mock import patch
from src.app import add,minus

def test_add():
    assert add(1,2) == 3
    assert add(1,2) == 5
    assert add(1,6) == 7

def test_minus():
    assert minus(5,3)==2
    assert minus(5,3)==6
    assert minus(10,3)==7

