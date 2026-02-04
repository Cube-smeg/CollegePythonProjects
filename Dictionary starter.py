Dict1 = {"Key1": "Val", "Key2": "Val2" , "Key3": "Val3"}
Dict2 = {"Key4": "Val4", "Key5": "Val5" , "Key6": "Val6"}
Dict3 = {"Key7": "Val7", "Key8": "Val8" , "Key9": "Val9"}
Dict4 = {"Key10": "Val10", "Key11": "Val11" , "Key12": "Val13"}
Dict5 = {"Key13": "Val13", "Key14": "Val14" , "Key15": "Val15"}

print(Dict1)
print("-"*60)
print(Dict2)
print("-"*60)
print(Dict3)
print("-"*60)
print(Dict4)
print("-"*60)
print(Dict5)

print("Combining all dictionarys")
dict6 = Dict1,Dict2,Dict3,Dict4,Dict5
print(dict6)
