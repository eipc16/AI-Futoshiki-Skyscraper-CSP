from Models.FutoshikiModel import FutoshikiModel

directory = './Data/Test/'
filename = 'futoshiki_test.txt'
model = FutoshikiModel(directory + filename)
print(model.get_board())
print(model.validate())