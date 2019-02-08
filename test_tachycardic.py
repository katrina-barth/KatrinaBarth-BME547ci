import pytest


@pytest.mark.parametrize("text, expected", [
                            ('Tachycardic', True),
                            ('tachycardic', True),
                            ('tackycardic', True),
                            ('tacHyCardic', True),
                            ('   tachycardic', True),
                            ('tachycardic   ', True),
                            ('tachycardia!', True),
                            ('tacicardic', True),
                            ('tachycardia', True),
                            ('bradycardia', False),
])
def test_is_tachy(text, expected):
    from tachycardic import is_tachycardic
    answer = is_tachycardic(text)
    assert answer == expected
