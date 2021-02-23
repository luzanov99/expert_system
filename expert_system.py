from db import Flowers,db_session


def generate_options(name1,color1,useing1, high_flower1,life_time1, size1):
    new_messege=Flowers(name=name1,color=color1, useing=useing1, high_flower=high_flower1, life_time=life_time1,size=size1)
    db_session.add(new_messege)
    db_session.commit()
    


def define_flower():
    flower_name=input("Введите название цветка ")
    answer=db_session.query(Flowers).filter_by(name=flower_name).first()
    if answer==None:
        flower_color=input(" Введите цвет цветка ")
        flower_using=input(" Введите место импользование цветка " )
        flower_high=input("Введите высоту цветка ")
        flower_lifetime=input("Введите жизненный цикл цветка ")
        flower_size=input("Введите размер цветка ")
     
        answer2=db_session.query(Flowers).filter_by(color=flower_color, useing=flower_using).first()
        
        if answer2 is not None:
            print(answer2)
        else:
            print("Добавить его в базу данных?")
            user_answer=input("Введите да -y или нет -n")
            if user_answer.lower()=='n':
                return 0
            else:
                generate_options(flower_name,flower_color,flower_using, flower_high,flower_lifetime,flower_size)

    else:
         print(answer)

   
define_flower()