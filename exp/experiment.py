import json
import glob
import matplotlib.pyplot as plt
import pandas as pd

###########

filtered=[]
cond_list=[]

with open('battery.json', 'r') as f:
  json_data=json.load(f)

for i in json_data:
  if i['DOI'] not in filtered:
    filtered.append(i['DOI'])
  
for i in json_data:
  if i['Property']=='Conductivity':
    cond_list.append(i)

print('###### Composition ratio of relations extracted from previous studies (battery database) ######')    
print('Number of papers used to build the battery database (before deduplication): ', len(json_data))
print('Number of papers used to build the battery database (after deduplication): ', len(filtered))
print('Number of conductivity-related relationships: ', len(cond_list))

###########

name_list=[]
count_list=[0,]*len(name_list)

for i in cond_list:
  if i['Specifier'] not in name_list:
    name_list.append(i['Specifier'])
    
for i in cond_list:
  for j in range(len(name_list)):
    if i['Specifier']==name_list[j]:
      count_list[j]+=1

print('###### Specifier of relations extracted from previous studies ######')
for i in range(len(name_list)):
  print(name_list[i],':', count_list[i])
  
###########  

print('###### Visualization Material 1 ######')  
data = [4597, 1861, 177, 23, 8, 200, 3, 275, 3, 13, 7, 1] # Fill in the results from the above in the order of output you want
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
ax.set_xticklabels(['None','conductivity','conductivities','Conductivity','Conductivities','electrical conductivity','Electronic conductivity','electronic conductivity','Electrical conductivity','electrical conductivities','electronic conductivities','Electrical Conductivity'], rotation=90)
colors=['blue',]*5 +['red',]*7
plt.bar(range(len(data)), data, color=colors)
x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]

for i, v in enumerate(x):
    plt.text(v, data[i], data[i], fontsize = 10, color='black', horizontalalignment='center', verticalalignment='bottom') 
plt.ylim([0,5000])
plt.show()
plt.clf()

###########

print('###### Visualization Material 2-1 ######')  
ratio = [502, 6666] # Fill in the above result
labels = ['Electrical\nconductivity', 'Unknown']

plt.pie(ratio, labels=labels, autopct='%.1f%%', colors=['lavender', 'lightskyblue'], textprops={'fontsize': 14})
plt.show()
plt.clf()

###########

print('###### Visualization Material 2-2 ######') 
ratio = [502, 6666-4924, 4924] # Fill in the above result, 4924 is the number of papers finally extracted using our program
labels = ['Electrical\nconductivity', 'Unknown','Ionic           \nconductivity']

plt.pie(ratio, labels=labels, autopct='%.1f%%', colors=['lavender', 'lightskyblue', 'pink'], textprops={'fontsize': 14})
plt.show()
plt.clf()

###########

names=[]
database=[]
record_count=0

names = glob.glob('../batterydatabase/save/*.json')
names_length = len(names)

for name in names:
  with open(name, 'r') as f:
    lines=f.readlines()
  for i in lines:
    try:
      record_count+=1
      database.append(json.loads(i))
    except:
      continue

with open('Database.json', 'w+') as f:
  json.dump(database, f, indent=4)

print('Number of papers extracted with ionical conductivity: ', names_length, '\nNumber of relations from which ion conductivity was extracted: ', record_count)


###########

cond_names=[]
val_list=[]
not_list=[]
extra_list=[]

def is_json_key_present(json, key):
  try:
    buf=json[key]
  except KeyError:
    return False
  return True

for i in cond_list:
  if i['Name'] not in cond_names:
    cond_names.append(i['Name'])

with open('Database.json', 'r') as f:
  extracted_json=json.load(f)

for itm in extracted_json:
  if is_json_key_present(itm, 'BatteryConductivity'):
    if is_json_key_present(itm['BatteryConductivity'],'names'):
      if itm['BatteryConductivity']['names'] in cond_names:
        val_list.append(itm)
      else:
        not_list.append(itm['BatteryConductivity']['names'])
  else:
    extra_list.append(itm)

print('Number of total relations: ', len(extracted_json))
print('Number of valid relations: ', len(val_list))
print('Number of invalid relations: ', len(not_list))
print('Number of relations not related to the battery: ', len(extra_list))

with open('valid_database.json','w+') as f:
  json.dump(val_list, f, indent=4)
    
###########

print('###### Visualization Material 3 ######') 
data = [54, 22, 90, 136, 6, 15, 26, 5] # Find out the number of relationships in 8 categories and fill it out.
ax = plt.subplot()
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
ax.set_xticklabels(['LISICON-like','Argyrodite','Garnet','NASICON-like','Li-Nitride','Li-Hydride','Perovskite','Li-Halide'], rotation=45)
plt.bar(range(len(data)), data, color='blue')
x=[0, 1, 2, 3, 4, 5, 6, 7]

for i, v in enumerate(x):
    plt.text(v, data[i], data[i],             
             fontsize = 10, 
             color='black',
             horizontalalignment='center',  
             verticalalignment='bottom') 

plt.ylim([0,150])
plt.show()
plt.clf()

###########

print('###### Visualization Material 4 ######') 
xdata=[]
ydata=[]

with open('sorted/0', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(0)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/1', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(1)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/2', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(2)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/3', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(3)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/4', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(4)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/5', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(5)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/6', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(6)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))
      
with open('sorted/7', 'r') as f:
  f0=json.load(f)
  print('numbers:',len(f0))
  for itm in f0:
    xdata.append(7)
    if type(itm['BatteryConductivity']['value']) is list:
      ydata.append(float(itm['BatteryConductivity']['value'][0]))
    else:
      ydata.append(float(itm['BatteryConductivity']['value']))

ax = plt.subplot()
ax.set_xticklabels([0,'LISICON-like','Argyrodite','Garnet','NASICON-like','Li-Nitride','Li-Hydride','Perovskite','Li-Halide'],rotation=45)
plt.semilogy(base=10)
plt.scatter(xdata,ydata,color='orange')
plt.clf()


###########

list0=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]

with open('./sorted/0', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list0:
      list0.append(i['BatteryConductivity']['names'])
with open('./sorted/1', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list1:
      list1.append(i['BatteryConductivity']['names'])
with open('./sorted/2', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list2:
      list2.append(i['BatteryConductivity']['names'])
with open('./sorted/3', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list3:
      list3.append(i['BatteryConductivity']['names'])
with open('./sorted/4', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list4:
      list4.append(i['BatteryConductivity']['names'])
with open('./sorted/5', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list5:
      list5.append(i['BatteryConductivity']['names'])
with open('./sorted/6', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list6:
      list6.append(i['BatteryConductivity']['names'])
with open('./sorted/7', 'r') as f:
  f0=json.load(f)
  for i in f0:
    if i['BatteryConductivity']['names'] not in list7:
      list7.append(i['BatteryConductivity']['names'])

      
df_json=pd.read_json('battery_backup.json')

with open('battery.json', 'r') as f:
  database1=json.load(f)
  cond_list=[]
  cond_name=[]
  
  for i in database1:
    if i['Property']=='Conductivity':
      cond_list.append(i)
      if i['Name'] not in cond_name:
        cond_name.append(i['Name'])

  with open('valid_database.json', 'r') as f:
    database2=json.load(f)
    cond_name2=[]
    
    for i in database2:
      if i['BatteryConductivity']['names'] not in cond_name2:
        cond_name2.append(i['BatteryConductivity']['names'])
    
    n0,n1,n2,n3,n4,n5,n6,n7=0,0,0,0,0,0,0,0
    
    df_json=pd.read_json('battery_backup.json')
    df_json['IonConductivity']=0
    df_json['StructureType']='None'
    for i in range(len(database1)):
      if database1[i]['Property']=='Conductivity' and database1[i]['Name'] in cond_name2:
        df_json[i:i+1]['IonConductivity']=1
        if database1[i]['Name'] in list0:
          df_json[i:i+1]['StructureType']='LISICON-like'
          n0+=1
        elif database1[i]['Name'] in list1:
          df_json[i:i+1]['StructureType']='Argyrodite'
          n1+=1
        elif database1[i]['Name'] in list2:
          df_json[i:i+1]['StructureType']='Garnet'
          n2+=1
        elif database1[i]['Name'] in list3:
          df_json[i:i+1]['StructureType']='NASICON-like'
          n3+=1
        elif database1[i]['Name'] in list4:
          df_json[i:i+1]['StructureType']='Li-Nitride'
          n4+=1
        elif database1[i]['Name'] in list5:
          df_json[i:i+1]['StructureType']='Li-Hydride'
          n5+=1
        elif database1[i]['Name'] in list6:
          df_json[i:i+1]['StructureType']='Perovskite'
          n6+=1
        elif database1[i]['Name'] in list7:
          df_json[i:i+1]['StructureType']='Li-Halide'
          n7+=1

    df_json.to_excel('ion.xlsx')
