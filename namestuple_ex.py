'''tuples can be used as records and we name the column data as well
  in this example employee data would be name and retrived with the name '''

from collections import namedtuple as nt

Emp=nt('Emp','id name dept address')
    """This is emp object"""

siva=Emp(1,'Siva kumar','Information technology',('Nellore','bangalore','Tirupati'))


print(siva.name)

print(siva.address) #('Nellore', 'bangalore', 'Tirupati')

print(siva.__doc__) #Emp(id, name, dept, address)

#print(dir(siva))

print(siva._asdict())

for i,v in siva._asdict().items():
    print(i+' --> ',v)
        # id -->  1
        # name -->  Siva kumar
        # dept -->  Information technology
        # address -->  ('Nellore', 'bangalore', 'Tirupati')
