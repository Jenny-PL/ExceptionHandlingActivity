import pytest

from activity.main import *

def test_add_to_string_exception():
    # arrange
    string = "This is a string"
    # act
    with pytest.raises(AttributeError):
        add_to_string(string)