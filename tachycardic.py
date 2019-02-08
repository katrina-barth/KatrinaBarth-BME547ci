# Function to detect tachycardia in medical history
# Katrina Barth, 02/05/2019


def is_tachycardic(text):
    text = text.casefold()  # Makes the input lowercase
    if text.find('tachycardic') != -1:
        return True
    elif text.find('trachycardic') != -1:  # hypothesized mis-spelling
        return True
    elif text.find('tachycardia') != -1:
        return True
    elif text.find('tac') != -1 and text.find('cardic') != 1:
        # accounting for some mis-spellings
        return True
    else:
        return False
