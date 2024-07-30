# compound interest rate calculation
f = open('codepractice1.txt','r') # r = read
lines = f.readlines()
[principal, rate, time_period] = [x.strip('\n') for x in lines]
f.close()
#You now have three variables: principal = 1000; rate = 0.145; time_period = 3
