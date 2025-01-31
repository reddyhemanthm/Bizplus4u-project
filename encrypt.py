from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()

# Load the key (from a secure environment variable or configuration)
key = b'your-generated-key-here'
cipher_suite = Fernet(key)

def encrypt_data(plain_text):
    return cipher_suite.encrypt(plain_text.encode())

def decrypt_data(encrypted_text):
    return cipher_suite.decrypt(encrypted_text).decode()
  import sqlite3

# Connect to the database
conn = sqlite3.connect('encrypted_data.db')
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS secure_data (
        id INTEGER PRIMARY KEY,
        encrypted_text BLOB NOT NULL
    )
''')
conn.commit()

# Function to store encrypted data
def store_data(plain_text):
    encrypted_text = encrypt_data(plain_text)
    cursor.execute('INSERT INTO secure_data (encrypted_text) VALUES (?)', (encrypted_text,))
    conn.commit()

# Example usage
store_data('Sensitive Data to Encrypt')
# Function to retrieve and decrypt data
def retrieve_data(data_id):
    cursor.execute('SELECT encrypted_text FROM secure_data WHERE id = ?', (data_id,))
    encrypted_text = cursor.fetchone()[0]
    return decrypt_data(encrypted_text)

# Example usage
data_id = 1  # Replace with the actual ID
decrypted_data = retrieve_data(data_id)
print(f'Decrypted Data: {decrypted_data}')
