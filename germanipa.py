from text import Text

if __name__ == "__main__":
    while True:
        sentinel = '/'  # ends when this string is seen
        print('Enter a German text below.\nThen type "/" and hit enter.\n')
        a = '\n'.join(iter(input, sentinel))
        if a == "":
            break
        b = Text(a)
        b.print_ipa()