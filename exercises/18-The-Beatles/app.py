# ✅↓ Write your code here ↓✅
def sing():
    song="let it be,\n"
    for i in range(10):
        if i==3:
            song=song+"there will be an answer,\n"
        elif i==9:
            song=song+"whisper words of wisdom, let it be"
        else:
            song=song+"let it be,\n"
    return song

print(sing())
