import pytest


@pytest.mark.parametrize("text, expected", [
                            ('Tachycardia', True),
                            ('tachycardia', True),
                            ('tackycardia', True),
                            ('tacHyCardia', True),
                            ('   tachycardia', True),
                            ('tachycardia   ', True),
                            ('tachycardia!', True),
                            ('tacicardia', True),
                            ('bradycardia', False),
])
def test_is_tachy(text, expected):
    from tachycardia import is_tachycardia
    answer = is_tachycardia(text)
    assert answer == expected
