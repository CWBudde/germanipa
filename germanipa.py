import sys
from text import Text

if __name__ == "__main__":
    if len(sys.argv) == 2:
        text_input = sys.argv[1]
        b = Text(text_input)
        b.print_ipa()
        sys.exit(1)

    while True:
        sentinel = '/'  # ends when this string is seen
        print('Enter a German text below.\nThen type "/" and hit enter.\n')
        a = '\n'.join(iter(input, sentinel))
        if a == "":
            break
        b = Text(a)
        b.print_ipa()