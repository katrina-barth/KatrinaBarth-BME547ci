# Function to detect tachycardia in medical history
# Katrina Barth, 02/05/2019


def is_tachycardia(text):
    text = text.casefold()  # Makes the input lowercase
    if text.find('tachycardia') != -1:
        return True
    elif text.find('trachycardia') != -1:  # hypothesized mis-spelling
        return True
    elif text.find('tac') != -1 and text.find('cardia') != 1:
        # accounting for some mis-spellings
        return True
    else:
        return False
