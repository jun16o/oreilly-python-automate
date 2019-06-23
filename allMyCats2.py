cats_names = []
while True:
    print('猫' + str(len(cats_names) + 1) + 'の名前を入力してください' + '（終了するにはEnterキーだけ押してください）')
    name = input()
    if name == '':
        break
    cats_names = cats_names + [name]
print('猫の名前は次の通り：')
for name in cats_names:
    print('　' + name)  