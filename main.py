from Puzzles.Futoshiki.FutoshikiModel import FutoshikiModel

directory = './Data/Test/'
filename = 'futoshiki_test.txt'
model = FutoshikiModel(directory + filename)
model.print_info()
model.check_unique()