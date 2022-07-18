def isfloat(xstr):
    try:  float(xstr);  return True;
    except ValueError:  return False;

float_filter = lambda xlist: list(filter(lambda x: isfloat(x), xlist));
qexit_filter = lambda xlist: list(filter(lambda x: x.upper() == 'Q', xlist));

def nums_sum(xlist, s = 0.):
    xarray = list(map(float, float_filter(xlist)));
    xsum = 0.;
    for x in xarray:  xsum += x;
    print(f'{s + xsum} ({xsum})');
    return s + xsum;

print('Enter numbers to calculate their sum, or type "Q" to finish:')
s = 0.;
while True:
    ylist = list(input().split());
    if ylist[0].upper() == 'Q':  break;
    qsymbols = qexit_filter(ylist);
    if qsymbols == []:
        s = nums_sum(ylist, s);
    else:
        qindex = list(map(lambda y: y.upper(), ylist)).index('Q');
        s = nums_sum(ylist[:qindex], s);
        break;