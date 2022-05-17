# Problem 5 Smallest Multiple

number = 2520
passes = []

for x in range(500000000,0,-1):
	if x % 20 ==0:
		if x % 19 ==0:
			if x % 18 ==0:
				if x % 17 ==0:
					if x % 16 ==0:
						if x % 15 ==0:
							if x % 14 ==0:
								if x % 13 ==0:
									if x % 12 ==0:
										if x % 11 ==0:
											if x%10==0:
												if x%9==0:
													if x%8==0:
														if x%7==0:
															if x%6==0:
																if x%5==0:
																	if x%4==0:
																		if x%3==0:
																			if x%2==0:
																				passes.append(x)
																		
print(passes)

