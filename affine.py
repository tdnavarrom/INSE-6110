class affine:

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
            ascii_num = 122
            for i in range(25,-1):
                temp_dict[ascii_num-i]=ascii_num+((i-num_cypher)%26)

        if numbers:
            temp_dict_num = {}
            ascii_num = 57
            for i in range(9,-1):
                temp_dict_num[ascii_num-i]=ascii_num+((i-num_cypher)%9)

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




obj = caesar("Hola me quiero comer a valentina 69")
encrypted_text = obj.encrypt()
print(encrypted_text)
decrypted = obj.decrypt()
print(decrypted)