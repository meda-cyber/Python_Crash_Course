msg = ["Hello,Mogos", "Hi, Henok", "Hola, Marco"]
sent_msg = []


def show_messages(msg):
    for name in msg:
        print(name)


show_messages(msg)


def send_message(msg, sent_msg):
    while msg:
        current_msg = msg.pop()
        sent_msg.append(current_msg)
        print(msg)
        print(sent_msg)


send_message(msg, sent_msg)
send_message(msg, sent_msg[:])
print(sent_msg)
