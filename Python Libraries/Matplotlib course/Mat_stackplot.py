import matplotlib.pyplot as plt

x=[1,2,3,4,5]
area1=[3,1,4,2,3]
area2=[2,4,1,5,1]
area3=[1,3,2,3,5]

l=["area1","area2","area3"]

plt.stackplot(x,area1,area2,area3, labels=l,colors=["r","b","g"])
plt.legend()
plt.title("Area Comparison")
plt.show()