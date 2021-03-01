b=t=e=m=0
file = ['/Users/skr/Desktop/100/06/test.txt','/Users/skr/Desktop/100/06/train.txt','/Users/skr/Desktop/100/06/valid.txt']
for i in file:
    with open(i, 'r') as f:
        for line in f:
            data = line.split('\t')
            if data[0] == 'b':
                b = b + 1
            if data[0] == 't':
                t = t + 1
            if data[0] == 'e':
                e = e + 1
            if data[0] == 'm':
                m = m + 1
    i = i.split('/')
    print('{} : {} {} {} {} = {}'.format(i[6], b, t, e, m ,b+t+e+m))
    b=t=e=m=0
