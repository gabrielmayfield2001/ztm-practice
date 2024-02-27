class SuperList(list):
    
    def __len__(self):
        return 1000
    
superlist1 = SuperList()

print(len(superlist1))

superlist1.append(5)

print(superlist1[0])

print(issubclass(SuperList, list))