for A in range(1, 10):
	for B in range(1, 10):
		for C in range(1, 10):
			for D in range(1, 10):
				if (10 * B + A) * (10 * C + C) == (1001 * B + 110 * D) and (10 * B + A) * C == 111 * B:
					print('Q1 answer is: ')
					print('A: ', A, 'B: ', B, 'C: ', C, 'D: ', D)

for G in range(1, 10):
	for H in range(1, 10):
		for P in range(1, 10):
			for I in range(1, 10):
				for L in range(1, 10):
					if (10000 * G + 1000 * H + 100 * P + 10 * I + L) * 4 == 10000 * L + 1000 * I + 100 * P + 10 * H + G:
						#list0 = [G, H, P, I, L]
						#if list0.count(1) <= 1 and list0.count(2) <= 1 and list0.count(3) <= 1 and list0.count(4) <= 1 and list0.count(5) <= 1 and list0.count(6) <= 1 and list0.count(7) <= 1 and list0.count(8) <= 1 and list0.count(9) <= 1 and list0.count(0) <= 1:
						print('Q2 answer is: ')
						print('G: ', G, 'H: ', H, 'P: ', P, 'I: ', I, 'L: ', L)

for A in range(1, 10):
	for B in range(1, 10):
		for C in range(1, 10):
			for D in range(1, 10):
				for E in range(1, 10):
					if 111111 * A / B == 10000 * B + 1000 * C + 100 * D + 10 * E + A:
						print('Q3 answer is: ')
						print(111111 * A, ' / ', B, ' = ', round(111111 * A / B))