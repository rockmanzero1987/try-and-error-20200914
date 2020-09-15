for A in range(0, 10):
	for B in range(0, 10):
		for C in range(0, 10):
			for D in range(0, 10):
				if (10 * B + A) * (10 * C + C) == (1001 * B + 110 * D) and (10 * B + A) * C == 111 * B:
					list0 = [A, B, C, D]
					if list0.count(1) <= 1 and list0.count(2) <= 1 and list0.count(3) <= 1 and list0.count(4) <= 1 and list0.count(5) <= 1 and list0.count(6) <= 1 and list0.count(7) <= 1 and list0.count(8) <= 1 and list0.count(9) <= 1 and list0.count(0) <= 1:
						print('Q1 answer is: ')
						print('A: ', A, 'B: ', B, 'C: ', C, 'D: ', D)

for G in range(1, 10):
	for H in range(1, 10):
		for P in range(1, 10):
			for I in range(1, 10):
				for L in range(1, 10):
					if (10000 * G + 1000 * H + 100 * P + 10 * I + L) * 4 == 10000 * L + 1000 * I + 100 * P + 10 * H + G:
						list1 = [G, H, P, I, L]
						if list1.count(1) <= 1 and list1.count(2) <= 1 and list1.count(3) <= 1 and list1.count(4) <= 1 and list1.count(5) <= 1 and list1.count(6) <= 1 and list1.count(7) <= 1 and list1.count(8) <= 1 and list1.count(9) <= 1 and list1.count(0) <= 1:
							print('Q2 answer is: ')
							print(10000 * G + 1000 * H + 100 * P + 10 * I + L, ' * 4 = ', 10000 * L + 1000 * I + 100 * P + 10 * H + G)

for V in range(0, 10):
	for W in range(1, 10):
		for X in range(0, 10):
			for Y in range(0, 10):
				for Z in range(0, 10):
					if 111111 * V / W == 10000 * W + 1000 * X + 100 * Y + 10 * Z + V:
						print('Q3 answer is: ')
						print(111111 * V, ' / ', W, ' = ', round(111111 * V / W))

