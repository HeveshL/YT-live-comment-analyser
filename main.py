from pytchat import LiveChat
from collections import Counter 
  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0]

chat = LiveChat(video_id = "HXLpCVBO2lY")
bufferlength = 100
chats = []

while chat.is_alive():
  try:
    try:
        print('------------------------------------')
        temp = most_frequent(chats)
        print(temp,chats.count(temp))
        print('------------------------------------')
    except:
        pass
    data = chat.get()
    items = data.items
    for c in items:
        print(f"{c.datetime} [{c.author.name}]- {c.message}")
        if len(chats)>bufferlength:
            chats.pop(0)
        chats.append(str(c.message).lower())
        data.tick()
  except KeyboardInterrupt:
    chat.terminate()
    break