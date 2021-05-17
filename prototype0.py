import pandas as pb
import re
data = pb.read_csv("data.csv")

weight = int(input ("enter your weight"))
print("--------------------")
height = int(input ("enter your height"))
print("--------------------")
age = int(input ("enter your age"))
print("--------------------------------------------")
print("Entre tour activity level")
print("Enter 1 for Sedentary (little or no exercise")
print("Enter 2 for Lightly active (1-3 days/week)")
print("Enter 3 for Moderately active (3-5 days/week)")
print("Enter 4 for Very active (6-7 days/week)")
act = int(input ("Enter 5 for Super active (twice/day) "))
print("---------------------------------")
gender = int(input ("Enter 1 for male and 0 for female "))
print("---------------------------------")

if gender == 1:
        cal = int(88.362 + (13.397*float(weight)) + (4.799*float(height)) - (5.677*float(age)))
elif gender == 0:
        cal = int(447.593 + (9.247*float(weight)) + (3.098*float(height)) - (4.330*float(age)))

#requirements protiens , fats and carbo
if act == 1:
    cal = cal*1.2
    protiens_req= (cal*0.3)//4
    carb_req = (cal*0.5)//4
    fats_req = (cal*0.2)//9

elif act == 2:
    cal = cal*1.375
    protiens_req= (cal*0.3)//4
    carb_req = (cal*0.5)//4
    fats_req = (cal*0.2)//9

elif act == 3:
    cal = cal*1.55
    protiens_req= (cal*0.3)//4
    carb_req = (cal*0.5)//4
    fats_req = (cal*0.2)//9

elif act == 4:
    cal = cal*1.725
    protiens_req= (cal*0.3)//4
    carb_req = (cal*0.5)//4
    fats_req = (cal*0.2)//9

elif act == 5:
    cal = cal*1.9
    protiens_req= (cal*0.3)//4
    carb_req = (cal*0.5)//4
    fats_req = (cal*0.2)//9

#print(cal)
#print(protiens_req,carb_req,fats_req)


#spltiting all the micros for brakfast, lunch, snack, dinner

#breakfast requirement
bpr = (protiens_req*30)//100
bcr = (carb_req*30)//100
bfr = (fats_req*30)//100

#lunch requirement
lpr = (protiens_req*40)//100
lcr= (carb_req*40)//100
lfr = (fats_req*40)//100

#snacks requirement
spr = (protiens_req*10)//100
scr = (carb_req*10)//100
sfr = (fats_req*10)//100

#dinner requirement
dpr = (protiens_req*20)//100
dcr = (carb_req*20)//100
dfr= (fats_req*20)//100
#print(bpr,bcr,bfr,"::::",lpr,lcr,lfr,"::::",spr,scr,sfr,"::::",dpr,dcr,dfr)


#giving the diet

#for breakfast
b_food= {}
for index, row in data.iterrows():
    if int(row["Protein (g)"])==bpr:
        #print(row["Protein (g)"])
        b_food[row["name"]]=row["Serving Weight 1 (g)"]
        bfr -= int(row["Fat (g)"])
        bcr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Fat (g)"]) == bfr:
        b_food[row["name"]]=row["Serving Weight 1 (g)"]
        bcr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Carbohydrate (g)"])== bcr:
        b_food[row["name"]]=row["Serving Weight 1 (g)"]
        break

#for lunch
l_food= {}
for index, row in data.iterrows():
    if int(row["Protein (g)"])==lpr:
        #print(row["Protein (g)"])
        l_food[row["name"]]=row["Serving Weight 1 (g)"]
        lfr -= int(row["Fat (g)"])
        lcr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Fat (g)"]) == lfr:
        l_food[row["name"]]=row["Serving Weight 1 (g)"]
        lcr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Carbohydrate (g)"])== lcr:
        l_food[row["name"]]=row["Serving Weight 1 (g)"]
        break

#for snacks
s_food= {}
for index, row in data.iterrows():
    if int(row["Protein (g)"])==spr:
        #print(row["Protein (g)"])
        s_food[row["name"]]=row["Serving Weight 1 (g)"]
        sfr -= int(row["Fat (g)"])
        scr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Fat (g)"]) == sfr:
        s_food[row["name"]]=row["Serving Weight 1 (g)"]
        scr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Carbohydrate (g)"])== scr:
        s_food[row["name"]]=row["Serving Weight 1 (g)"]
        break

#for dinner
d_food= {}
for index, row in data.iterrows():
    if int(row["Protein (g)"])==dpr:
        #print(row["Protein (g)"])
        d_food[row["name"]]=row["Serving Weight 1 (g)"]
        dfr -= int(row["Fat (g)"])
        dcr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Fat (g)"]) == dfr:
        d_food[row["name"]]=row["Serving Weight 1 (g)"]
        dcr -= int(row["Carbohydrate (g)"])
        break
for index, row in data.iterrows():
    if int(row["Carbohydrate (g)"])== dcr:
        d_food[row["name"]]=row["Serving Weight 1 (g)"]
        break




#this prints the name and the serving quatity 
print("Diet for breakfast")
for key,val in b_food.items():
 print(f" {key} == {val} grams")
print("Diet for lunch")
for key,val in l_food.items():
 print(f" {key} == {val} grams")
print("Diet for snacks")
for key,val in s_food.items():
 print(f" {key} == {val} grams")
print("Diet for dinner")
for key,val in d_food.items():
 print(f" {key} == {val} grams")