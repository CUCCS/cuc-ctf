txt = open('flag.txt','r',encoding='utf-8').read()

def count_char1():
    count ={}
    for i in txt:
        if i not in count:
            count[i]=1
        else:
            count[i]=count[i]+1
    
    count=sorted(count.items(),key=lambda d:d[1],reverse=True)
    print("直接计算每个字符出现的次数：",count)

if __name__ =='__main__':
    count_char1()
  