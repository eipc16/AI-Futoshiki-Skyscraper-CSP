from Models.FutoshikiModel import FutoshikiModel

directory = './Data/Test/'
filename = 'futoshiki_4_0.txt'
model = FutoshikiModel(directory + filename)
print(model.get_board(True))
print(model.validate())
print(model.validate_non_zero())