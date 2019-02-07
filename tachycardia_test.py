import pytest

@pytest.mark.parameterize("text, expected", [
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

def is_tachy_test(text, expected):
    from tachycardia.py import is_tachycardia
    answer = is_tachycardia(text)
    assert answer == expected
