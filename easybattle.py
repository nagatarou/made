from abc import abstractmethod, ABC
import time

class Character:
    def __init__(self, name, sex):
        self.__name = name
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @name.setter
    def name(self, value):
        self.__name = value

    @sex.setter
    def sex(self, value):
        self.__sex = value
    
    def show_status(self):
        print(f"種別:{self.__class__.kinds} 名前:{self.name} 性別:{self.sex}")


class FightCharacter(Character, ABC):
    def __init__(self, name, sex, hp, atk, mp, speed):
        super().__init__(name, sex)
        self.__hp = hp
        self.__atk = atk
        self.__mp = mp
        self.__speed = speed
    
    def show_status(self):
        super().show_status()
        print(f"体力:{self.hp} 攻撃力:{self.atk} 魔力{self.mp} 素早さ{self.speed}")

    @property
    def hp(self):
        return self.__hp
    
    @property
    def atk(self):
        return self.__atk

    @property
    def mp(self):
        return self.__mp

    @property
    def speed(self):
        return self.__speed

    @hp.setter
    def hp(self, value):
        self.__hp = value
    
    @atk.setter
    def atk(self, value):
        self.__atk = value

    @mp.setter
    def mp(self, value):
        self.__mp = value

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defence(self):
        pass

    @abstractmethod
    def away(self):
        pass

    @abstractmethod
    def fall(self):
        pass

class Brave(FightCharacter):
    kinds = "勇者"

    def attack(self):
        print(f"{self.name}の攻撃!")
    
    def defence(self):
        print(f"{self.name}の防御!")
    
    def away(self):
        print(f"{self.name}は逃げ出した...")

    def fall(self):
        print(f"{self.name}は敗北した！")   

class Monster(FightCharacter):
    kinds = "魔物"

    def attack(self):
        print(f"{self.name}の攻撃!")
    
    def defence(self):
        print(f"{self.name}の防御!")
    
    def away(self):
        print(f"{self.name}は逃げ出した...")

    def fall(self):
        print(f"{self.name}をたおした！")



class Villager(Character):
    kinds = "村人"

def versus(a, b):
    print(f"{b.name}が現れた！")
    while True:
        print("-----------------------------------")
        a.show_status()
        print("-----------------------------------")
        b.show_status()
        print("-----------------------------------")
        act1 = input("たたかう\n  にげる:")
        if act1 == "たたかう":
            print("-------------------")
            act2 = input("こうげき\n  ぼうぎょ:")
            print("-------------------")
            if act2 == "こうげき":
                if a.speed >= b.speed:
                    a.attack()
                    b.hp -= a.atk
                    time.sleep(1)
                    print(f"{b.name}に{a.atk}ポイントのダメージをあたえた！")
                    if b.hp <= 0:
                        time.sleep(1)
                        b.fall()
                        break
                    time.sleep(1)
                    b.attack()
                    a.hp -= b.atk
                    time.sleep(1)
                    print(f"{a.name}は{b.atk}ポイントのダメージをうけた！")
                    if a.hp <= 0:
                        time.sleep(1)
                        a.fall()
                        break
                else:
                    b.attack()
                    a.hp -= b.atk
                    print(f"{a.name}は{b.atk}ポイントのダメージをうけた！")
                    if a.hp <= 0:
                        time.sleep(1)
                        b.fall()
                        break
                    time.sleep(1)
                    a.attack()
                    b.hp -= a.atk
                    time.sleep(1)
                    print(f"{b.name}に{a.atk}ポイントのダメージをあたえた！")
                    if b.hp <= 0:
                        time.sleep(1)
                        b.fall()
                        break
            else:
                b.attack()
                a.hp -= b.atk // 2
                time.sleep(1)
                print(f"{a.name}は{b.atk // 2}ポイントのダメージをうけた！")
                if a.hp <= 0:
                    time.sleep(1)
                    b.fall()
                    break
            time.sleep(1)
        else:
            time.sleep(1)
            print("-------------------")
            a.away()
            break


        
if __name__ == "__main__":

    b = Brave("エ二クス", "M", 100, 45, 50, 20)
    m = Monster("スライムベス", "F", 150, 40, 0, 5)
    versus(b, m)


