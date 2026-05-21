import numpy as np

a = np.arange(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)

print(np.sort(a))
print(np.sort(b))

np.append(a,200)
np.append(b,np.ones((b.shape[0],1)))

print(np.where(a>50))

print(np.where(a>50,0,a))

print(np.argmax(a))
print(np.argmin(a))
print(a[0],a[6])
print(np.cumsum(a))
print(np.cumprod(a))

print(np.percentile(a,100))
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70]))
salary = np.array([20000,40000,10000])
experience = np.array([1,2,3])
print(np.corrcoef(salary,experience))