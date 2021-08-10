# Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes ('-') between each two odd numbers
# in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
# Note that the number will always be non-negative (>= 0).

def insertDash(num):
    sNum = str(num)
    ans = ''
    for c in range(len(sNum)-1):
        ans += sNum[c]
        if int(sNum[c]) % 2 == 1 and int(sNum[c+1]) % 2 == 1:
            ans += '-'
        if int(sNum[c]) % 2 == 0 and int(sNum[c+1]) % 2 == 0:
            ans += '+'
    ans += sNum[-1]
    return ans


def insertDash2(num):
    sNum = str(num)
    ans = ''
    for c in range(len(sNum)-1):
        ans += sNum[c]

        cond1, cond2 = int(sNum[c]) % 2, int(sNum[c+1]) % 2

        if cond1 and cond2:
            ans += '-'
        if not(cond1 or cond2):
            ans += '+'
    ans += sNum[-1]
    return ans


while 1:
    try:
        a = int(input('inserire un intero lungo\n'))
        break
    except:
        print('Vorrei un intero')

print(insertDash(a))
