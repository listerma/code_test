# -*-coding:utf-8-*-


f_sour = open('C:\\Users\\D\\Desktop\\report.txt', encoding='utf8')
f_list = f_sour.readlines()
single_ave = []
new_data = []
all_total = []
last_data = []
final_data =[]
i = 0
while i < 30:
    f_tem = f_list[i].replace("\n","")
    single_stu = f_tem.split(' ')
    total_s = 0
    for j in single_stu[1:]:
        total_s += int(j)
    aver_s = float(total_s/(len(single_stu)-1))
    all_total.append(total_s)
    new_data.append(f_tem + (' %d'% total_s) + (' %.2f'% aver_s))
    i += 1
all_total_rev = sorted(all_total,reverse=True)
j=0
for k in all_total_rev:
    for h in new_data:
        p = h.split(' ')
        if k == int(p[-2]):
            last_data.append(('%d '%(j+1)) + h)
            j += 1
for k in last_data:
    tem = k.split(' ')
    h = 0
    for h in range(2,len(tem)-1):
        if float(tem[h]) < 60:
            tem[h] = '不及格'
    final_data.append((' ').join(tem))
print(single_ave)
# print(all_total_rev)
# print(final_data)
f_sour.close()