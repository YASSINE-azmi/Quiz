class quiz:
    
    def quiz1(self):
        user_input = int(input("5 + 9 = ? : "))
        
        try:
            if user_input == (5 + 9):
                print("correct ✅")
                return 1
            else:
                print(f"Faux ❌, correct reponse est {5 + 9}")
                return 0
        except ValueError:
            print("pls Entre just numbers !")
            return 0

    def quiz2(self):
        user_input = int(input("258 - 145 = ? : "))
        try:
            if user_input == (258 - 145):
                print("correct ✅")
                return 1
            else:
                print(f"Faux ❌, correct reponse est {258 - 145}")
                return 0
        except ValueError:
            print("pls Entre just numbers !")
            return 0

    def quiz3(self):
        user_input = int(input("5 * 9 = ? : "))
        try:
            if user_input == (5 * 9):
                print("correct ✅")
                return 1
            else:
                print(f"Faux ❌, correct reponse est {5 * 9}")
                return 0
        except ValueError:
            print("pls Entre just numbers !")
            return 0

    def quiz4(self):
        user_input = int(input("5 ^ 9 = ? : "))
        try:
            if user_input == (5**9):
                print("correct ✅")
                return 1
            else:
                print(f"Faux ❌, correct reponse est {5**9}")
                return 0
        except ValueError:
            print("pls Entre just numbers !")
            return 0

    def quiz5(self):
        user_input = int(input("45 / 9 = ? : "))
        try:
            if user_input == (45/9):
                print("correct ✅")
                return 1
            else:
                print(f"Faux ❌, correct reponse est {45/9}")
                return 0
        except ValueError:
            print("pls Entre just numbers !")
            return 0

    def quiz6(self):
        user_input = input("Who is the best football player : ")
        
        if user_input.lower().strip() == "messi":
            print("correct ✅")
            return 1
        elif "ronaldo" in user_input.lower():
            print("🤣🤣🤣🤣🤣🤣")
            return 0
        else:
            print("Faux ❌, correct reponse est messi")
            return 0
