from random import randint
#-------------------------------------------------------------
from operator import add
from functools import reduce
#-------------------------------------------------------------
from random import random

#-------------------------------------------------------------
def individual(length,min,max):
	return[randint(min,max) for x in range(length)]

def populasi(count,length,min,max):
	return[individual(length,min,max) for x in range(count)]
#-------------------------------------------------------------
def fitness(individual,target):
	sum=reduce(add,individual,0)
	return abs(target-sum)
def grade(pop,target):
	summed=reduce(add,(fitness(x,target) for x in pop))
	return summed/(len(pop)*1.0)
#-------------------------------------------------------------
def mutatex(ga):
	chance_to_mutate=0.6
	print(ga)
	n=0
	for i in ga:
		r=random()
		if chance_to_mutate > r:
			print(i)
			place_to_modify = randint(0,len(i)-1)
			i[place_to_modify] = randint(min(i),max(i))
			print(i)
		ga[n]=i
		n=n+1
	return ga
#-------------------------------------------------------------
def evolve(pop,target,retain=0.2,mutate=0.01,random_select=0.05):
	gradeda=[(fitness(x,target),x) for x in pop]
	graded = [x[1] for x in sorted(gradeda)]
	retain_length=int(len(graded)*retain)
	parents = graded[:retain_length]
	for individu in graded[retain_length:]:
		if random_select > random():
			parents.append(individu)
	for individu in parents:
		if mutate > random():
			mutate_pos = randint(0,len(individu)-1)
			individu[mutate_pos] = randint(min(individu),max(individu))
	len_par = len(parents)
	len_desired = len(pop) - len_par
	children = []
	while len(children) < len_desired:
		malenumber=randint(0,len_par-1)
		femalenumber=randint(0,len_par-1)
		if malenumber!=femalenumber:
			male = parents[malenumber]
			female = parents[femalenumber]
			half = round(len(male)/2)
			child = male[:half] + female[half:]
			children.append(child)
	parents.extend(children)
	return parents

target = 371
pop_count = 100
i_len = 5
i_min = 0
i_max = 100
pp = populasi(pop_count,i_len,i_min,i_max)
fitness_history=[grade(pp,target)]
for i in range(100):
	pp = evolve(pp,target)
	fitness_history.append(grade(pp,target))
for datum in fitness_history:
	print(datum)
print(pp[0])
