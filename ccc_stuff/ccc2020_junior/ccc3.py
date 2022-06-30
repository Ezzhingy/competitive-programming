
def smolrect(fill_lst):
    x_val = []
    y_val = []
    for item in fill_lst:
        item = item.replace(",","                    ")
        
        x = item[:5]
        x = x.replace(" ","")
        x_val.append(int(x))
        y = item[-5:]
        y = y.replace(" ","")
        y_val.append(int(y))

    xmins = min(x_val)
    ymins = min(y_val)

    xmax = max(x_val)
    ymax = max(y_val)
    
    return f'{xmins-1},{ymins-1}\n{xmax+1},{ymax+1}'
    

  
            
            
        


lst = []
a = int(input())
for i in range(0,a):
    b = input()
    lst.append(b)

print(smolrect(lst))
