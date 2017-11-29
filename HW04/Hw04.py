
# coding: utf-8

# # 九九乘法表
# 

# In[17]:


def multiplication_table(m, n):
    print ('\n'.join(['\t'.join(['{}*{}={}'.format(i,j,i*j) for i in range(m,n+1)]) for j in range(1,10)]))
    
multiplication_table(1, 3)
print()
multiplication_table(4, 6)
print()
multiplication_table(7, 9)


# # 金字塔

# In[12]:


def pyramid(n):
    for i in range(1,n+1):
        s=" "*(n-i)+"*"*(2*i-1)
        print(s)
pyramid(10)


# # . 將 Q1 跟 Q2 的函式寫入一個模組，並呼叫模組裡面的函式來使用。
