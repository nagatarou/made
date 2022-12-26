#各モジュールのimport
from abc import abstractmethod, ABC
import random
import time

#Characterクラスを生成
class Character:

    #初期化メソッドを定義
    def __init__(self, name, sex):

        self.__name = name
        self.__sex = sex

    #nameプロパティの設定
    @property
    def name(self):
        return self.__name

    #sexプロパティの設定
    @property
    def sex(self):
        return self.__sex

    #nameセッターの設定
    @name.setter
    def name(self, value):
        self.__name = value

    #sexセッターの設定
    @sex.setter
    def sex(self, value):
        self.__sex = value
    
    def show_status(self):
        print(f"種別:{self.__class__.kinds} 名前:{self.name} 性別:{self.sex}")

#FightCharacterクラスを生成(Characterクラスを継承、抽象クラスである)
class FightCharacter(Character, ABC):

    def __init__(self, name, sex, hp, atk):

        super().__init__(name, sex)
        self.__hp = hp
        self.__atk = atk
    
    def show_status(self):

        super().show_status()
        print(f"体力:{self.hp} 攻撃力:{self.atk}")

    @property
    def hp(self):

        return self.__hp
    
    @property
    def atk(self):

        return self.__atk

    @hp.setter
    def hp(self, value):

        self.__hp = value
    
    @atk.setter
    def atk(self, value):

        self.__atk = value

    #抽象メソッドを定義
    @abstractmethod
    def physicsattack(self):

        pass

    @abstractmethod
    def magicattack(self):

        pass

    @abstractmethod
    def special(self):

        pass

    @abstractmethod
    def fall(self):

        pass

    @abstractmethod
    def victory(self):

        pass

#勇者クラスの生成
class Brave(FightCharacter):
    kinds = "勇者"

    def physicsattack(self):

        #勇者の剣攻撃についてのセリフリストの生成
        b_phylist = ["は剣を振るった！", "の剣撃！", "のソードアタック！"]

        #セリフの生成
        print(self.name + random.choice(b_phylist))

    def magicattack(self):

        b_magiclist = ["のホーリーミサイル！", "のプレゲトーン！", "のレーヴァテイン"]

        print(self.name + random.choice(b_magiclist))

    def special(self):

        b_spelist = ["は特殊な盾を構えた！", "のリフレクター！", "のマジックコート！"]

        print(self.name + random.choice(b_spelist))

    def fall(self):

        b_falist = ["は力尽きた！", "は敗北した！", "は倒れた！"]

        print(self.name + random.choice(b_falist))  

    def victory(self):

        b_viclist = ["は勝利した！", "は勝利を勝ち取った！", "は勝鬨を上げた！"]

        print(self.name + random.choice(b_viclist))

#魔物クラスを生成
class Monster(FightCharacter):
    kinds = "魔物"

    def physicsattack(self):

        #魔物の物理攻撃につりてのセリフリストの生成
        m_phylist = ["のかみつく！", "の突進！", "のはりてうち！"]

        #セリフの生成
        print(self.name + random.choice(m_phylist))

    def magicattack(self):

        m_magiclist = ["の火の玉!", "のバブルブレス！", "のダークネスビーム！"]

        print(self.name + random.choice(m_magiclist))
    
    def special(self):

        m_spelist = ["のドレイン！", "の吸収！", "のパラボラチャージ！"]

        print(self.name + random.choice(m_spelist))

    def fall(self):

        m_falist = ["は蒸発した!", "は星になった！", "は地に還った!"]

        print(self.name + random.choice(m_falist))

    def victory(self):

        m_viclist = ["は雪辱を晴らした！", "は勝つ運命にあった！", "は白星を上げた！"]

        print(self.name + random.choice(m_viclist))


#physicsattack同士で攻撃力差があった場合のセリフリストの生成
p_plist = ["は押し負けた！", "は押し切られた!", "力負けした！"]


#空白を生成する関数
def create_blank(num):

    for _ in range(num):

        print("")


#対人戦    
def pvp():

    while True:

        #勇者の名前を入力する
        b_name = input("勇者の名前は？")

        #勇者の名前を未入力か判定
        if b_name:

            #入力済みの場合ループを終了
            break

        else:

            create_blank(5)
            print("※名前を入力してください")
            create_blank(2)

    create_blank(2)

    while True:
        
        #勇者の性別を入力する
        b_sex = input("勇者の性別は？")

        if b_sex:

            break

        else:

            create_blank(5)
            print("※性別を入力してください")
            create_blank(2)

    create_blank(2)

    while True:

        #勇者のHPを入力する
        b_hp = input("勇者のHPは？")

        #入力値が十進数であるかどうか判定する
        if b_hp.isdecimal():

            #入力値が十進数である場合ループを抜ける
            b_hp = int(b_hp)
            break
        
        else:

            #入力値が十進数でない場合もう一度入力を促す
            create_blank(5)
            print("※整数で入力してください")
            create_blank(2)
    
    create_blank(2)

    while True:

        #勇者の攻撃力を入力する
        b_atk = input("勇者の攻撃力は？")

        if b_atk.isdecimal():
            
            b_atk = int(b_atk)
            break

        else:
            
            create_blank(5)
            print("※整数で入力してください")
            create_blank(2)
    
    create_blank(2)

    while True:

        #魔物の名前を入力する
        m_name = input("魔物の名前は？")

        if m_name:

            #勇者の名前と違うか判定する
            if b_name != m_name:

                break

            else:

                create_blank(5)
                print("*違う名前にしてください")
                create_blank(2)
        
        else:
     
            create_blank(5)
            print("*名前を入力してください")
            create_blank(2)

    create_blank(2)

    while True:

        #魔物の性別を入力する
        m_sex = input("魔物の性別は？")

        if m_sex:

            break

        else:

            create_blank(5)
            print("※性別を入力してください")
            create_blank(2)
    
    create_blank(2)

    while True:

        #魔物のHPを入力する
        m_hp = input("魔物のHPは？")

        if m_hp.isdecimal():

            m_hp = int(m_hp)
            break

        else:

            create_blank(5)
            print("※整数で入力してください")
            create_blank(2)

    create_blank(2)

    while True:

        #魔物の攻撃力を入力する
        m_atk = input("魔物の攻撃力は？")

        if m_atk.isdecimal():

            m_atk = int(m_atk)
            break

        else:

            create_blank(5)
            print("※整数で入力してください")
            create_blank(2)

        
    #勇者のステータスを設定
    b = Brave(b_name, b_sex, b_hp, b_atk)

    #魔物のステータスを設定
    m = Monster(m_name, m_sex, m_hp, m_atk)

    #対戦を開始
    while True:

        time.sleep(2)

        create_blank(2)
        
        #勇者と魔物のステータスを表示
        print("-----------------------------------")
        b.show_status()
        print("-----------------------------------")
        m.show_status()
        print("-----------------------------------")

        create_blank(2)

        while True:

            time.sleep(2)
            
            #勇者の行動を選択
            b_act = input(f"{b.name}の行動を選択してください\n剣\n魔法\nリフレクター:")

            #正しい選択肢か判定する
            if b_act == "剣" or b_act == "魔法" or b_act == "リフレクター":

                break #正しかったらループを抜ける

            else:

                create_blank(5)
                print("※もう一度行動を選択してください")
                create_blank(2)

        create_blank(50)
    
        while True:

            #魔物の行動を選択
            m_act = input(f"{m.name}の行動を選択してください\n物理攻撃\n魔法\n吸収:")

            #正しい選択肢か判定する
            if m_act == "物理攻撃" or m_act == "魔法" or m_act == "吸収":

                #正しい選択肢であればループを抜ける
                break 

            else:

                create_blank(5)
                print("※もう一度行動を選択してください")
                create_blank(2)

        create_blank(50)

        #勇者physics vs 魔物physicsの場合
        if b_act == "剣" and m_act == "物理攻撃":

            #セリフを流す
            time.sleep(2)
            
            b.physicsattack()

            time.sleep(2)

            create_blank(2)

            m.physicsattack()

            time.sleep(2)

            create_blank(2)

            #勇者の攻撃力が魔物の攻撃力より上だった場合
            if b.atk > m.atk:

                #セリフの生成
                print(f"{m.name}{random.choice(p_plist)}")

                time.sleep(2)

                create_blank(2)

                print(f"{m.name}は{abs(b.atk - m.atk)}ダメージを受けた！")

                #魔物の体力を魔物の攻撃力と勇者の攻撃力の差分を引く
                m.hp -=  abs(b.atk - m.atk)

            #勇者の攻撃力と魔物の攻撃力が同じだった場合
            elif b.atk == m.atk:

                print("互いの力は拮抗している...")

            #魔物の攻撃力が勇者の攻撃力より上だった場合
            else:

                print(f"{b.name}{random.choice(p_plist)}")

                time.sleep(2)

                create_blank(2)

                print(f"{m.name}は{abs(b.atk - m.atk)}ダメージを受けた！")

                #勇者の体力を勇者の攻撃力と魔物の攻撃力の差分を引く
                b.hp -=  abs(b.atk - m.atk)

        #勇者physics vs 魔物magicの場合
        elif b_act == "剣" and m_act == "魔法":

            #セリフの生成
            time.sleep(2)

            b.physicsattack()

            time.sleep(2)

            create_blank(2)

            m.magicattack()

            time.sleep(2)

            create_blank(2)

            print(f"{b.name}は無謀な挑戦をした！")

            time.sleep(2)

            create_blank(2)

            print(f"{b.name}は{int(m.atk * 1.5)}ダメージを受けた！")

            #勇者の体力を魔物の攻撃力の1.5倍分引く
            b.hp -= int(m.atk * 1.5)

        #勇者physics vs 魔物specialの場合
        elif b_act == "剣" and m_act == "吸収":

            #セリフの生成
            time.sleep(2)

            b.physicsattack()

            time.sleep(2)

            create_blank(2)

            m.special()

            time.sleep(2)

            create_blank(2)

            print(f"{m.name}は吸収するものがなかった！")

            time.sleep(2)

            create_blank(2)

            print(f"{m.name}は{b.atk}ダメージを受けた！")

            #魔物の体力を魔物の攻撃力分引く
            m.hp -= b.atk

        #勇者magic vs 魔物physicsの場合
        elif b_act == "魔法" and m_act == "物理攻撃":

            #セリフの生成
            time.sleep(2)

            b.magicattack()

            time.sleep(2)

            create_blank(2)

            m.physicsattack()

            time.sleep(2)

            create_blank(2)

            print(f"{m.name}は無謀な挑戦をした！")

            time.sleep(2)

            create_blank(2)
         
            print(f"{m.name}は{int(b.atk * 1.5)}ダメージを受けた！")

            #魔物の体力を勇者の攻撃力の1.5倍分引く
            m.hp -= int(b.atk * 1.5)

        #勇者magic vs 魔物magicの場合
        elif b_act == "魔法" and m_act == "魔法":

            #セリフの生成
            time.sleep(2)

            b.magicattack()

            time.sleep(2)

            create_blank(2)

            m.magicattack()

            time.sleep(2)

            create_blank(2)

            print(f"{b.name}と{m.name}の魔法は相殺しあった！")

        #勇者magic vs 魔物specialの場合
        elif b_act == "魔法" and m_act == "吸収":

            #セリフの生成
            time.sleep(2)

            b.magicattack()

            time.sleep(2)

            create_blank(2)

            m.special()

            time.sleep(2)

            create_blank(2)

            print(f"{m.name}は魔法を吸収した！")

            time.sleep(2)

            create_blank(2)

            print(f"{m.name}は{int(b.atk * 0.5)}回復した！")

            #魔物の体力を勇者の攻撃力の0.5倍分回復する
            m.hp += int(b.atk * 0.5)

        #勇者special vs 魔物physicsの場合
        elif b_act == "リフレクター" and m_act == "物理攻撃":

            #セリフの生成
            time.sleep(2)

            b.special()

            time.sleep(2)

            create_blank(2)

            m.physicsattack()

            time.sleep(2)

            create_blank(2)

            print(f"{b.name}は反射するものがなかった！")

            time.sleep(2)

            create_blank(2)

            print(f"{b.name}は{m.atk}ダメージを受けた！")

            #勇者の体力を魔物の攻撃力分引く
            b.hp -= m.atk

        #勇者special vs 魔物magicの場合
        elif b_act == "リフレクター" and m_act == "魔法":

            #セリフの生成
            time.sleep(2)

            b.special()

            time.sleep(2)

            create_blank(2)

            m.magicattack()

            time.sleep(2)

            create_blank(2)

            print(f"{b.name}は魔法を反射した！")

            time.sleep(2)

            create_blank(2)

            print(f"{m.name}は{int(m.atk * 0.5)}ダメージを受けた！")

            #魔物の体力を魔物の攻撃力分の0.5倍分引く
            m.hp -= int(m.atk * 0.5)

        #勇者special vs 魔物specialの場合
        elif b_act == "リフレクター" and m_act == "吸収":

            #セリフの生成
            time.sleep(2)

            b.special()

            time.sleep(2)

            create_blank(2)

            m.special()

            time.sleep(2)

            create_blank(2)

            print("何も起こらなかった！")


        #勇者か魔物のどちらかの体力が0以下になったか判定
        if b.hp <= 0 or m.hp <= 0:

            time.sleep(2)

            create_blank(2)

            #勇者の体力が0以下になった場合
            if b.hp <= 0:

                #勇者敗北時のセリフの生成
                b.fall()

                time.sleep(2)

                create_blank(2)

                #魔物勝利時のセリフの生成
                m.victory()

                #ループを抜ける
                break
            
            else:

                #魔物敗北時のセリフの生成
                m.fall()

                time.sleep(2)

                create_blank(2)

                #勇者勝利時のセリフの生成
                b.victory()

                #ループを抜ける
                break


if __name__ == "__main__":

    pvp()



