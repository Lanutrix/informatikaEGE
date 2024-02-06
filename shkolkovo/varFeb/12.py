s = '1'+'2'*11+'3'*20+'4'*29

while ('12' in s) or ('13' in s) or ('14' in s):
    s = s.replace('12', '4',1)
    s = s.replace('13', '211',1)
    s = s.replace('14', '321',1)
if s.count('2')==10 and s.count('3')==20 and s.count('4')==30:
    print(s)