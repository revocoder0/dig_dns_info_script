import dns
import dns.resolver
#dig DNS information form web...
print("\n")
print("<<<<<<<<<<<Code by Revocoder>>>>>>>>>>/n")
name=input("Enter example.com >>>> : ")

print("<<<<<<< Choose Query Type >>>>>>>")
print("1\tA Record")
print("2\tMX Record")
print("3\tNS Record")
print("4\tSOA Record")
print("5\tAll Record")

option=input("input:")

def case1():
    a = dns.resolver.query(name, 'A')
    print(a.rrset)

def case2():
        mx=dns.resolver.query(name, 'MX')
        print(mx.rrset)
def case3():
    ns=dns.resolver.query(name, 'NS')
    print(ns.rrset)
def case4():
    soa=dns.resolver.query(name, 'SOA')
    print(soa.rrset)

def case5():
    for qtype in 'A', 'MX', 'NS','SOA':
        answer=dns.resolver.query(name,qtype,raise_on_no_answer=False)
        if answer.rrset is not None:
            print(answer.rrset)
    
def default():
    print("This is the default case")


def switch_case(case):
    switcher = {
        1: case1,
        2: case2,
        3: case3,
        4: case4,
        5: case5,
    }
    func = switcher.get(case, default)
    func()
if(option=='1'):
    switch_case(1)
elif(option=='2'):
    switch_case(2)
elif(option=='2'):
    switch_case(2)
elif(option=='3'):
    switch_case(3)
elif(option=='4'):
    switch_case(4)
elif(option=='5'):
    switch_case(5)

print("/n<<<<<<<<Thanks for all>>>>>>>")