# a programme to decypher encrptyted messages written in emoji

# emcoded message
encoded_example = '🌴🏠🍦🐍 🍦🐍 🍎 🥞🦄⚡⚡🦁🦅'

# cipher
emoji_cipher = {
    'a': '🍎', 'b': '🐝', 'c': '🌊', 'd': '🐬', 'e': '🦅',
    'f': '🍟', 'g': '🦒', 'h': '🏠', 'i': '🍦', 'j': '🕹️',
    'k': '🎋', 'l': '🦁', 'm': '🌝', 'n': '🥜', 'o': '🐙',
    'p': '🥞', 'q': '👑', 'r': '🚀', 's': '🐍', 't': '🌴',
    'u': '🦄', 'v': '🎻', 'w': '🌊', 'x': '❌', 'y': '🛳️', 'z': '⚡'
}

def main():
    decrypted_message = decrypt_message(encoded_example, emoji_cipher)
    print(decrypted_message)

def decrypt_message(encoded, cipher):

    # step 1 reverse the cipher

    reversed_cipher = {v: k for k, v in cipher.items()}

    # step 2: split the message into words

    words = encoded.split(" ")

    # step 3 decode each word

    decoded_words = []
    for word in words:
        decoded_word = ''.join(reversed_cipher.get(emoji, '?') for emoji in word)
        decoded_words.append(decoded_word)

    # step 4 join words back into a sentence
    return " ".join(decoded_words)

if __name__ == "__main__":
    main()