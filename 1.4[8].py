# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Примеры/Тесты:
# 3 2 4 -> yes
# 3 2 1 -> no

n, m = 3, 2
crash = 2
crash_test = (n * m) // crash or (n * m) // crash or (n * m) // crash or (n * m) // crash or (n * m) // crash
print('YES' if crash_test != 6 else 'NO')
