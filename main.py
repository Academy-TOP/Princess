castle = [1, ["ц"], 543, "П", ["н", ["р"]], "и", [[["с"]]]]
castle[0] = 'е'
castle[2] = 'а'
print(castle)
castle[1] = castle[1][0]
print(castle)
castle.insert(5, castle[4][1][0])
castle[4] = castle[4][0]
print(castle)
castle[7] = castle[7][0][0][0]
print(castle)

princess = castle[3] +  castle[5] + castle[6] + castle[4] + castle[1] + castle[0] + castle[7] + castle[2]
print(princess)

castle = [1, ["ц"], 543, "П", ["н", ["р"]], "и", [[["с"]]]]
castle[0] = 'е'
castle[2] = 'а'

princess  = castle[3] + castle[4][1][0] + castle[5] + castle[4][0] + castle[1][0] + castle[0] + castle[6][0][0][0]*2 + castle[2]
print(princess)
