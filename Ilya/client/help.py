def to_data(message):
    return bytes(str(message), encoding = 'utf-8')

def get_data(message):
    return message.decode('utf-8')
