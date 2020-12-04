#!/bin/python3

# %%
import re


filename = 'input'

with open(filename) as f:
    content = f.readlines()

content.append('\n')


# %%

class Passport:
    def __init__(self, str):
        for a in str.split():
            [e, val] = a.strip().split(':')

            if hasattr(self, e):
                print("VLAURD alreday set")

            setattr(self, e, val)

    def print(self):
        #print( dir(self))
        #print(len(self.__dict__),  self.__dict__)
        #print(self.pid)
        s = f"{len(self.__dict__)}"
        for key in sorted(self.__dict__.keys()):
            if key != 'cid':
                s = "%s, %s:%s" % (s, key, self.__dict__[key])
        print(s)



    def isValidS1(self):
        if hasattr(self, 'byr') and hasattr(self, 'iyr') and hasattr(self, 'eyr') and hasattr(self, 'hgt') and hasattr(self, 'hcl') and hasattr(self, 'ecl') and hasattr(self, 'pid') and hasattr(self, 'cid'):
            return True

        # with missing cid
        if hasattr(self, 'byr') and hasattr(self, 'iyr') and hasattr(self, 'eyr') and hasattr(self, 'hgt') and hasattr(self, 'hcl') and hasattr(self, 'ecl') and hasattr(self, 'pid'):
            return True

        return False


    def isValid(self):

        if not hasattr(self, 'byr') or int(self.byr) < 1920 or int(self.byr) > 2002:
            return False

        if not hasattr(self, 'iyr') or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False

        if not hasattr(self, 'eyr') or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False

        if not hasattr(self, 'hgt'):
            return False
        else:
            matchObj = re.match( r'^(\d+)(in|cm)$', self.hgt, re.I)
            if matchObj:
                hgt_val = int(matchObj.group(1))
                hgt_unit = matchObj.group(2)
                if hgt_unit == 'cm':
                    if (hgt_val < 150 or hgt_val > 193):
                        return False

                elif hgt_unit == 'in':
                    if (hgt_val < 59 or hgt_val > 76):
                        return False

                else:
                    return False

            else:
                return False
    
        if not hasattr(self, 'hcl'):
            return False
        else:
            matchObj = re.match( r'^#([0-9a-f]{6})$', self.hcl, re.I)
            if matchObj:
                hcl_val = matchObj.group(1)
            else:
                return False

        if not hasattr(self, 'ecl') or self.ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False

        if not hasattr(self, 'pid'):
            return False
        else:
            matchObj = re.match( r'^(\d{9})$', self.pid, re.I)
            if not matchObj:
                return False

        return True



N_valid_S1 = 0
N_valid = 0
passport = ''
for l in content:
    passport = passport+l
    if l == '\n':
        #print("Precess passport", passport.split())
        p = Passport(passport)

        if p.isValidS1():
            N_valid_S1 = N_valid_S1 + 1

        if p.isValid():
            N_valid = N_valid + 1
            #p.print()

        passport = ''


print("Solution 1: ", N_valid_S1)

# 102 is too high
print("Solution 2: ", N_valid)
#area = []

#for l in content:
#    area.append(([x for x in l.strip()]))

# %%