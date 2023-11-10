class caesar:

    def __init__(self, text:str) -> None:
        self.text = text
        print(self.text)

    def encrypt_algorithm(self, lower_case_only:bool = True, numbers:bool = True, num_cypher:int=3) -> dict[str]:
        temp_dict = {}

        if lower_case_only:
            ascii_num = 97
            for i in range(0,26):
                temp_dict[ascii_num+i]=ascii_num+((i+num_cypher)%26)

        if numbers:
            temp_dict_num = {}
            ascii_num = 48
            for i in range(0,10):
                temp_dict_num[ascii_num+i]=ascii_num+((i+num_cypher)%9)

            temp_dict.update(temp_dict_num)

        return temp_dict
    
    def decrypt_algorithm(self, lower_case_only:bool = True, numbers:bool = True, num_cypher:int=3) -> dict[str]:
        temp_dict = {}

        if lower_case_only:
            ascii_num = 97
            for i in range(0,26):
                temp_dict[ascii_num+i]=ascii_num+((i-num_cypher)%26)

        if numbers:
            temp_dict_num = {}
            ascii_num = 57
            for i in range(0,10):
                temp_dict_num[ascii_num+i]=ascii_num+((i-num_cypher)%9)

            temp_dict.update(temp_dict_num)

        return temp_dict

    def encrypt(self) -> str:
        if self.text.isascii():
            self.text = self.text.lower()
            dict_cypher = self.encrypt_algorithm()
            cypher = self.text.translate(dict_cypher)
            
            return cypher
        else:
            return "Sorry, only ascii letters are supported"

    def decrypt(self):
        if self.text.isascii():
            self.text = self.text.lower()
            dict_cypher = self.decrypt_algorithm()
            cypher = self.text.translate(dict_cypher)
            return cypher
        else:
            return "Sorry, only ascii letters are supported"



text = input("Ingrese cualquier maricada: ")
opcion = input("Ingrese 1 para encriptar, ingrese 2 para desencriptar:")
obj = caesar(text)


if opcion == "1":
    encrypted_text = obj.encrypt()
    print(encrypted_text)
elif opcion == "2":
    decrypted = obj.decrypt()
    print(decrypted)
else:
    print("que putas pusiste ?")