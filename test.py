from dotenv import load_dotenv


load_dotenv()


a = 'Кондрат $ Правитель соседнего государства заявляет, что вы должны спасти его дочь'


arr = a.split(' $ ')

print('|' + arr[1] + '|')


from utils.image_gen import get_id


print(get_id(
    person='Командир Родион',
    replica='ПРивт миер',
    values=[50, 50, 50, 50],
    changes=[-1, 0, 1, 0]
))
