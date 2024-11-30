import json
file=input()
try:
    with open(file,encoding='utf8') as data_file:
        data = json.load(data_file)
    print(data)
except:
    print("Ocorreu um erro!")
finally:
    print("Processo concluído!")