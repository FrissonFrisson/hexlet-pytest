import pytest
from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''


def test_stack():
    stack = []
    assert not stack
    stack.append('1x')
    stack.append('2x')
    assert bool(stack)
    assert stack.pop() == '2x'
    assert stack.pop() == '1x'
    assert not stack
    with pytest.raises(IndexError):
        stack.pop()

