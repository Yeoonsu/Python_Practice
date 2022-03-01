class family:
    # 클래스의 생성자
    def __init__(self, father, mother, child):
        self.father = father
        self.mother = mother
        self.child = child
        
    #클래스의 메소드
    def show_info(self):
        print("아빠:", self.father, "/ 엄마:", self.mother, "/ 나:", self.child)
         
#인스턴스
family1 = family("멋쨍이", "이뿌니", "귀요미")
family1.show_info()

family2 = family("아부징", "어무니", "딸래미")
family2.show_info()
