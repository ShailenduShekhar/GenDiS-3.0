import pickle as pkl
input = input("Enter the name of the file you want to open: ")
pkl_file = open(input, 'rb')
data = pkl.load(pkl_file)
print(data)