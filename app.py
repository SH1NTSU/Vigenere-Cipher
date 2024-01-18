from flask import Flask, render_template, request

app = Flask(__name__)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_i = dict(zip(alphabet, range(1, 27)))
index_l = dict(zip(range(1, 27), alphabet))


@app.route('/', methods=['GET', 'POST'])
def encryption():
    if request.method == 'POST':
        open_text = request.form.get('user_input')
        key = request.form.get('key')
        split_text = [open_text[i:i + len(key)] for i in range(0, len(open_text), len(key))]

        encrypted_text = ''

        for split in split_text:
            i = 0
            for letter in split:
                num = (letter_i[letter] + letter_i[key[i]]) % 26
                encrypted_text += index_l[num]
                i += 1

        return encrypted_text

    return render_template('encryption.html')
@app.route('/decrypt', methods=['GET', 'POST'])
def decryption():
    if request.method == 'POST':
        encrypted_text = request.form.get('user_input')
        key = request.form.get('key')
        split_enctypted_text = [encrypted_text[i:i + len(key)] for i in range(0, len(encrypted_text), len(key))]
        decrypted_text = ''

        for split in split_enctypted_text:
            i = 0
            for letter in split:
                num = (letter_i[letter] - letter_i[key[i]]) % 26
                decrypted_text += index_l[num]
                i += 1
        return decrypted_text
    return render_template('decryption.html')


if __name__ == '__main__':
    app.run(debug=True)
