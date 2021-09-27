flat=int(input("Введите номер квартиры "))

if flat<=144 and flat>0:
    ent=int(flat/36-0.01)+1
    floor=int(flat/4-0.01)+1-(ent-1)*9
    print(f"Квартира находится в {ent} подъезде, на {floor} этаже")
else:
    print("Квартиры с таким номером не существует в доме")
