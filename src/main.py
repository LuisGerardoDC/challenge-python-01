# Resolve the problem!!

PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi'
    'Oscar',
]

SYMBOLS =[' ','!','¡','.',',','\n','?','¿',':','\'','\"']
VOWELS = [
    ('á','a'),
    ('é','e'),
    ('í','i'),
    ('ó','o'),
    ('ú','u'),
]
def normalize(s):
    normalized=s.lower()
    for symbol in SYMBOLS:
        normalized = normalized.replace(symbol,'')
    for a,b in VOWELS:
        normalized = normalized.replace(a,b)
    return normalized

def is_palindrome(palindrome):
    
    palindrome_original = normalize(palindrome)
    palindrome_length = len(palindrome_original)

    for i in range(int(palindrome_length/2)):
        if(palindrome_original[i] != palindrome_original[palindrome_length - i - 1]):
            return False
    
    return True

def validate():
    for palindrome in PALINDROMES:
        if not is_palindrome(palindrome):
            return False

    for not_palindrome in NOT_PALINDROMES:
        if is_palindrome(not_palindrome):
            return False
    return True


def run():
    if validate():
        print('Completaste el test')
    else:
        print('No completaste el test')


if __name__ == '__main__':
    with open('../palindromos.txt','r',encoding='utf8') as f:
        for line in f.readlines():
            PALINDROMES.append(line)
    run()
