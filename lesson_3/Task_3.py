import pymorphy2
def file_cabinet(name,sekond_name,year_of_birth,city,E_mail_address,telephone):

    morph = pymorphy2.MorphAnalyzer()
    city = morph.parse(city)[0].inflect({'loct'}).word

    print(name.title(),sekond_name.title(),year_of_birth,"года рождения, проживает в городе",city.title())
    print(f"email:",E_mail_address,"телефон:",telephone)


name = input("Введите Имя: ")
sekond_name = input("Атчество: ")
year_of_birth = int(input("Введите года рождения: "))
city = input("Ведите город проживания: ")
E_mail_address = input("введите свой имейл: ")
telephone = input("ВВедите телефон: ")


file_cabinet(name,sekond_name,year_of_birth,city,E_mail_address,telephone)