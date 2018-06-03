import random
import time
from cart.models import Sex_Info, Customer_Info, Cart_Info, Item_Sort_Info, Items, Item_Info, Camera_Info, Pur_History, Matrix, Mv_History, Ad_Info, Coupons_Item, Coupon_Item_Info


data = Sex_Info(sex='F')
data.save()
data = Sex_Info(sex='M')
data.save()


sexf = Sex_Info.objects.get(sex='F')
sexm = Sex_Info.objects.get(sex='M')


i=0
while i < 50:
	data = Customer_Info(id='customer'+str(2*i+1), pwd='asdf', age=random.randrange(15,80), sex=sexf)
	data.save()
	data = Customer_Info(id='customer'+str(2*i+2), pwd='asdf', age=random.randrange(15,80), sex=sexm)
	data.save()
	i=i+1



i=0
while i < 100:
	if i<51:
		data = Cart_Info(num=i+1, serial_num='cart'+str(i+1)+str(random.randrange(10000, 100000)), owner=Customer_Info.objects.get(id='customer'+str(i+1)))
		i=i+1
	else:
		data = Cart_Info(num=i+1, serial_num='cart'+str(i+1)+str(random.randrange(10000, 100000)))
		i=i+1






data = Item_Sort_Info(sort='우유')
data.save()
data = Item_Sort_Info(sort='과자')
data.save()
data = Item_Sort_Info(sort='술')
data.save()
data = Item_Sort_Info(sort='음료수')
data.save()
data = Item_Sort_Info(sort='과일')
data.save()
data = Item_Sort_Info(sort='생수')
data.save()
data = Item_Sort_Info(sort='빵')
data.save()
data = Item_Sort_Info(sort='생선')
data.save()
data = Item_Sort_Info(sort='고기')
data.save()
data = Item_Sort_Info(sort='라면')
data.save()
data = Item_Sort_Info(sort='커피')
data.save()


milk = Item_Sort_Info.objects.get(sort='우유')
snack = Item_Sort_Info.objects.get(sort='과자')
wine = Item_Sort_Info.objects.get(sort='술')
drink = Item_Sort_Info.objects.get(sort='음료수')
fruit = Item_Sort_Info.objects.get(sort='과일')
water = Item_Sort_Info.objects.get(sort='생수')
bread = Item_Sort_Info.objects.get(sort='빵')
fish = Item_Sort_Info.objects.get(sort='생선')
meat = Item_Sort_Info.objects.get(sort='고기')
noodle = Item_Sort_Info.objects.get(sort='라면')
coffee = Item_Sort_Info.objects.get(sort='커피')





data = Items(name='매일우유', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=milk)
data.save()
data = Items(name='서울우유', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=milk)
data.save()
data = Items(name='아주우유', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=milk)
data.save()
data = Items(name='연세우유', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=milk)
data.save()
data = Items(name='비타우유', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=milk)
data.save()






data = Items(name='포카칩', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=snack)
data.save()
data = Items(name='바나나킥', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=snack)
data.save()
data = Items(name='몽쉘', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=snack)
data.save()
data = Items(name='초코파이', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=snack)
data.save()
data = Items(name='썬칩', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=snack)
data.save()

data = Items(name='참이슬', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=wine)
data.save()
data = Items(name='좋은데이', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=wine)
data.save()
data = Items(name='카스', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=wine)
data.save()
data = Items(name='동동주', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=wine)
data.save()
data = Items(name='막걸리', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=wine)
data.save()

data = Items(name='코카콜라', inventory=random.randrange(100, 200), price=random.randrange(1000, 2000), sort=drink)
data.save()
data = Items(name='스프라이트', inventory=random.randrange(100, 200), price=random.randrange(1000, 2000), sort=drink)
data.save()
data = Items(name='펩시', inventory=random.randrange(100, 200), price=random.randrange(1000, 2000), sort=drink)
data.save()
data = Items(name='칠성사이다', inventory=random.randrange(100, 200), price=random.randrange(1000, 2000), sort=drink)
data.save()
data = Items(name='맥콜', inventory=random.randrange(100, 200), price=random.randrange(1000, 2000), sort=drink)
data.save()

data = Items(name='오렌지', inventory=random.randrange(100, 200), price=random.randrange(4000, 5000), sort=fruit)
data.save()
data = Items(name='사과', inventory=random.randrange(100, 200), price=random.randrange(4000, 5000), sort=fruit)
data.save()
data = Items(name='배', inventory=random.randrange(100, 200), price=random.randrange(4000, 5000), sort=fruit)
data.save()
data = Items(name='딸기', inventory=random.randrange(100, 200), price=random.randrange(4000, 5000), sort=fruit)
data.save()
data = Items(name='포도', inventory=random.randrange(100, 200), price=random.randrange(4000, 5000), sort=fruit)
data.save()

data = Items(name='평창생수', inventory=random.randrange(100, 200), price=random.randrange(500, 1500), sort=water)
data.save()
data = Items(name='제주도생수', inventory=random.randrange(100, 200), price=random.randrange(500, 1500), sort=water)
data.save()
data = Items(name='북한산생수', inventory=random.randrange(100, 200), price=random.randrange(500, 1500), sort=water)
data.save()
data = Items(name='맛있어생수', inventory=random.randrange(100, 200), price=random.randrange(500, 1500), sort=water)
data.save()
data = Items(name='아주생수', inventory=random.randrange(100, 200), price=random.randrange(500, 1500), sort=water)
data.save()

data = Items(name='슈크림빵', inventory=random.randrange(100, 200), price=random.randrange(2000, 3000), sort=bread)
data.save()
data = Items(name='메론빵', inventory=random.randrange(100, 200), price=random.randrange(2000, 3000), sort=bread)
data.save()
data = Items(name='단팥빵', inventory=random.randrange(100, 200), price=random.randrange(2000, 3000), sort=bread)
data.save()
data = Items(name='앙금빵', inventory=random.randrange(100, 200), price=random.randrange(2000, 3000), sort=bread)
data.save()
data = Items(name='식빵', inventory=random.randrange(100, 200), price=random.randrange(2000, 3000), sort=bread)
data.save()

data = Items(name='연어', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=fish)
data.save()
data = Items(name='고등어', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=fish)
data.save()
data = Items(name='전어', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=fish)
data.save()
data = Items(name='삼치', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=fish)
data.save()
data = Items(name='갈치', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=fish)
data.save()

data = Items(name='소고기', inventory=random.randrange(100, 200), price=random.randrange(3000, 4000), sort=meat)
data.save()
data = Items(name='닭고기', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=meat)
data.save()
data = Items(name='돼지고기', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=meat)
data.save()
data = Items(name='오리고기', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=meat)
data.save()
data = Items(name='칠면조고기', inventory=random.randrange(100, 200), price=random.randrange(2000, 4000), sort=meat)
data.save()

data = Items(name='신라면', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=noodle)
data.save()
data = Items(name='너구리', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=noodle)
data.save()
data = Items(name='삼양라면', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=noodle)
data.save()
data = Items(name='무파마', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=noodle)
data.save()
data = Items(name='사발면', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=noodle)
data.save()

data = Items(name='카누', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=coffee)
data.save()
data = Items(name='모카골드', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=coffee)
data.save()
data = Items(name='화이트골드', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=coffee)
data.save()
data = Items(name='TOP', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=coffee)
data.save()
data = Items(name='스타벅스', inventory=random.randrange(100, 200), price=random.randrange(1000, 3000), sort=coffee)
data.save()


milk1ob = Items.objects.get(name='매일우유')
milk1num = Items.objects.get(name='매일우유').inventory

milk2ob = Items.objects.get(name='서울우유')
milk2num = Items.objects.get(name='서울우유').inventory

milk3ob = Items.objects.get(name='아주우유')
milk3num = Items.objects.get(name='아주우유').inventory

milk4ob = Items.objects.get(name='연세우유')
milk4num = Items.objects.get(name='연세우유').inventory

milk5ob = Items.objects.get(name='비타우유')
milk5num = Items.objects.get(name='비타우유').inventory



snack1ob = Items.objects.get(name='포카칩')
snack1num = Items.objects.get(name='포카칩').inventory

snack2ob = Items.objects.get(name='바나나킥')
snack2num = Items.objects.get(name='바나나킥').inventory

snack3ob = Items.objects.get(name='몽쉘')
snack3num = Items.objects.get(name='몽쉘').inventory

snack4ob = Items.objects.get(name='초코파이')
snack4num = Items.objects.get(name='초코파이').inventory

snack5ob = Items.objects.get(name='썬칩')
snack5num = Items.objects.get(name='썬칩').inventory



wine1ob = Items.objects.get(name='참이슬')
wine1num = Items.objects.get(name='참이슬').inventory

wine2ob = Items.objects.get(name='좋은데이')
wine2num = Items.objects.get(name='좋은데이').inventory

wine3ob = Items.objects.get(name='카스')
wine3num = Items.objects.get(name='카스').inventory

wine4ob = Items.objects.get(name='동동주')
wine4num = Items.objects.get(name='동동주').inventory

wine5ob = Items.objects.get(name='막걸리')
wine5num = Items.objects.get(name='막걸리').inventory



drink1ob = Items.objects.get(name='코카콜라')
drink1num = Items.objects.get(name='코카콜라').inventory

drink2ob = Items.objects.get(name='스프라이트')
drink2num = Items.objects.get(name='스프라이트').inventory

drink3ob = Items.objects.get(name='펩시')
drink3num = Items.objects.get(name='펩시').inventory

drink4ob = Items.objects.get(name='칠성사이다')
drink4num = Items.objects.get(name='칠성사이다').inventory

drink5ob = Items.objects.get(name='맥콜')
drink5num = Items.objects.get(name='맥콜').inventory



fruit1ob = Items.objects.get(name='오렌지')
fruit1num = Items.objects.get(name='오렌지').inventory

fruit2ob = Items.objects.get(name='사과')
fruit2num = Items.objects.get(name='사과').inventory

fruit3ob = Items.objects.get(name='배')
fruit3num = Items.objects.get(name='배').inventory

fruit4ob = Items.objects.get(name='딸기')
fruit4num = Items.objects.get(name='딸기').inventory

fruit5ob = Items.objects.get(name='포도')
fruit5num = Items.objects.get(name='포도').inventory



water1ob = Items.objects.get(name='평창생수')
water1num = Items.objects.get(name='평창생수').inventory

water2ob = Items.objects.get(name='제주도생수')
water2num = Items.objects.get(name='제주도생수').inventory

water3ob = Items.objects.get(name='북한산생수')
water3num = Items.objects.get(name='북한산생수').inventory

water4ob = Items.objects.get(name='맛있어생수')
water4num = Items.objects.get(name='맛있어생수').inventory

water5ob = Items.objects.get(name='아주생수')
water5num = Items.objects.get(name='아주생수').inventory



bread1ob = Items.objects.get(name='슈크림빵')
bread1num = Items.objects.get(name='슈크림빵').inventory

bread2ob = Items.objects.get(name='메론빵')
bread2num = Items.objects.get(name='메론빵').inventory

bread3ob = Items.objects.get(name='단팥빵')
bread3num = Items.objects.get(name='단팥빵').inventory

bread4ob = Items.objects.get(name='앙금빵')
bread4num = Items.objects.get(name='앙금빵').inventory

bread5ob = Items.objects.get(name='식빵')
bread5num = Items.objects.get(name='식빵').inventory



fish1ob = Items.objects.get(name='연어')
fish1num = Items.objects.get(name='연어').inventory

fish2ob = Items.objects.get(name='고등어')
fish2num = Items.objects.get(name='고등어').inventory

fish3ob = Items.objects.get(name='전어')
fish3num = Items.objects.get(name='전어').inventory

fish4ob = Items.objects.get(name='삼치')
fish4num = Items.objects.get(name='삼치').inventory

fish5ob = Items.objects.get(name='갈치')
fish5num = Items.objects.get(name='갈치').inventory



meat1ob = Items.objects.get(name='소고기')
meat1num = Items.objects.get(name='소고기').inventory

meat2ob = Items.objects.get(name='닭고기')
meat2num = Items.objects.get(name='닭고기').inventory

meat3ob = Items.objects.get(name='돼지고기')
meat3num = Items.objects.get(name='돼지고기').inventory

meat4ob = Items.objects.get(name='오리고기')
meat4num = Items.objects.get(name='오리고기').inventory

meat5ob = Items.objects.get(name='칠면조고기')
meat5num = Items.objects.get(name='칠면조고기').inventory



noodle1ob = Items.objects.get(name='신라면')
noodle1num = Items.objects.get(name='신라면').inventory

noodle2ob = Items.objects.get(name='너구리')
noodle2num = Items.objects.get(name='너구리').inventory

noodle3ob = Items.objects.get(name='삼양라면')
noodle3num = Items.objects.get(name='삼양라면').inventory

noodle4ob = Items.objects.get(name='무파마')
noodle4num = Items.objects.get(name='무파마').inventory

noodle5ob = Items.objects.get(name='사발면')
noodle5num = Items.objects.get(name='사발면').inventory



coffee1ob = Items.objects.get(name='카누')
coffee1num = Items.objects.get(name='카누').inventory

coffee2ob = Items.objects.get(name='모카골드')
coffee2num = Items.objects.get(name='모카골드').inventory

coffee3ob = Items.objects.get(name='화이트골드')
coffee3num = Items.objects.get(name='화이트골드').inventory

coffee4ob = Items.objects.get(name='TOP')
coffee4num = Items.objects.get(name='TOP').inventory

coffee5ob = Items.objects.get(name='스타벅스')
coffee5num = Items.objects.get(name='스타벅스').inventory









from faker import Faker
fake = Faker()


from pytz import timezone
tz=timezone('Asia/Seoul')


i=0
while i < milk1num:
	serial=milk1ob.name+str(milk1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=milk1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < milk2num:
	serial=milk2ob.name+str(milk2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=milk2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < milk3num:
	serial=milk3ob.name+str(milk3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=milk3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < milk4num:
	serial=milk4ob.name+str(milk4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=milk4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < milk5num:
	serial=milk5ob.name+str(milk5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=milk5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < snack1num:
	serial=snack1ob.name+str(snack1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=snack1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < snack2num:
	serial=snack2ob.name+str(snack2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=snack2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < snack3num:
	serial=snack3ob.name+str(snack3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=snack3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < snack4num:
	serial=snack4ob.name+str(snack4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=snack4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < snack5num:
	serial=snack5ob.name+str(snack5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=snack5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < wine1num:
	serial=wine1ob.name+str(wine1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=wine1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < wine2num:
	serial=wine2ob.name+str(wine2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=wine2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < wine3num:
	serial=wine3ob.name+str(wine3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=wine3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < wine4num:
	serial=wine4ob.name+str(wine4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=wine4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < wine5num:
	serial=wine5ob.name+str(wine5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=wine5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < drink1num:
	serial=drink1ob.name+str(drink1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=drink1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < drink2num:
	serial=drink2ob.name+str(drink2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=drink2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < drink3num:
	serial=drink3ob.name+str(drink3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=drink3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < drink4num:
	serial=drink4ob.name+str(drink4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=drink4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1



i=0
while i < drink5num:
	serial=drink5ob.name+str(drink5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=drink5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < fruit1num:
	serial=fruit1ob.name+str(fruit1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fruit1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < fruit2num:
	serial=fruit2ob.name+str(fruit2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fruit2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < fruit3num:
	serial=fruit3ob.name+str(fruit3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fruit3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < fruit4num:
	serial=fruit4ob.name+str(fruit4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fruit4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < fruit5num:
	serial=fruit5ob.name+str(fruit5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fruit5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < water1num:
	serial=water1ob.name+str(water1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=water1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < water2num:
	serial=water2ob.name+str(water2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=water2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < water3num:
	serial=water3ob.name+str(water3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=water3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < water4num:
	serial=water4ob.name+str(water4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=water4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < water5num:
	serial=water5ob.name+str(water5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=water5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < bread1num:
	serial=bread1ob.name+str(bread1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=bread1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < bread2num:
	serial=bread2ob.name+str(bread2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=bread2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < bread3num:
	serial=bread3ob.name+str(bread3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=bread3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < bread4num:
	serial=bread4ob.name+str(bread4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=bread4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < bread5num:
	serial=bread5ob.name+str(bread5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=bread5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < fish1num:
	serial=fish1ob.name+str(fish1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fish1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < fish2num:
	serial=fish2ob.name+str(fish2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fish2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < fish3num:
	serial=fish3ob.name+str(fish3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fish3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < fish4num:
	serial=fish4ob.name+str(fish4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fish4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < fish5num:
	serial=fish5ob.name+str(fish5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=fish5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < meat1num:
	serial=meat1ob.name+str(meat1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=meat1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < meat2num:
	serial=meat2ob.name+str(meat2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=meat2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < meat3num:
	serial=meat3ob.name+str(meat3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=meat3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < meat4num:
	serial=meat4ob.name+str(meat4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=meat4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < meat5num:
	serial=meat5ob.name+str(meat5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=meat5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1






i=0
while i < noodle1num:
	serial=noodle1ob.name+str(noodle1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=noodle1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < noodle2num:
	serial=noodle2ob.name+str(noodle2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=noodle2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < noodle3num:
	serial=noodle3ob.name+str(noodle3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=noodle3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < noodle4num:
	serial=noodle4ob.name+str(noodle4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=noodle4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < noodle5num:
	serial=noodle5ob.name+str(noodle5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=noodle5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1






i=0
while i < coffee1num:
	serial=coffee1ob.name+str(coffee1num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=coffee1ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < coffee2num:
	serial=coffee2ob.name+str(coffee2num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=coffee2ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1




i=0
while i < coffee3num:
	serial=coffee3ob.name+str(coffee3num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=coffee3ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < coffee4num:
	serial=coffee4ob.name+str(coffee4num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=coffee4ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1





i=0
while i < coffee5num:
	serial=coffee5ob.name+str(coffee5num+i+1)+str(random.randrange(10000, 100000))
	inbound=fake.date_time_between(start_date="-45d", end_date="-1d", tzinfo=tz)
	expire=fake.date_time_between(start_date="+46d", end_date="+90d", tzinfo=tz)
	data = Item_Info(serial_num=serial, item=coffee5ob, inbound_date=inbound, expire_date=expire)
	data.save()
	i=i+1






i = 1
while i <= 100:
	j = 0
	cus = Customer_Info.objects.get(id='customer'+str(i))
	i = i + 1
	while j < 20:
		date = fake.date_time_between(start_date="now", end_date ="+45d", tzinfo = tz)
		aitem = Item_Info.objects.order_by('?').first()
		if aitem.pur_use == True:
			continue
		data = Pur_History(time=date, customer=cus, item=aitem)
		data.save()
		Item_Info.objects.filter(serial_num=aitem.serial_num).update(pur_use=True)
		j = j + 1
