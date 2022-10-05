alpha = []
for i in range(97,123):
    alpha.append(chr(i))
alpha_full = alpha+ alpha
def encrypt(text, sweep):
    en_word  = ""
    for j in text:
        initial_pos = alpha_full.index(j)
        final_pos = initial_pos+sweep
        en_word += alpha_full[final_pos]
    print('The encrypted word is ' , en_word)
    
def decrypt(text , sweep):
    de_word = ""
    for k in text:
        ini_pos = alpha.index_full(k)
        fi_pos = ini_pos-sweep
        de_word += alpha_full[fi_pos]
    print('The decrypted text is ' , de_word)

while True:
    text = input('Enter the word: ')
    sweep = int(input('Enter the sweep number: '))
    sel = input('do you want to encrypt or decrypt the text(encode/decode): ')
    if sel == 'encode':
        encrypt(text, sweep)
    elif sel == 'decode':
        decrypt(text, sweep)
    else:
        print('pls enter valid option')
