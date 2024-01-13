import random as r 
sonlar=r.sample(range(100),15)
toq_sonlar=list(filter(lambda son:son%2==1,sonlar))
print(sonlar)
print(toq_sonlar)