#Function to detect tachycardia in medical history
#Katrina Barth, 02/05/2019

def is_tachycardia(text):
    if text.find('tachycardia') != -1:
        return True
    else:
        return False

def main():
    text = input("Med Entry: ")
    print(is_tachycardia(text))

if __name__ == "__main__":
    main()
