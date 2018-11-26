def my_product_two_dim_with_threshold(a,b): #dimension(2 boyut)
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2] #[2]'deki değerler eşik değerleri
    
def get_my_data():
    my_data_x=[]
    my_data_x.append([1,0,0]) #threshold degeri her zaman için 1 aldım
    my_data_x.append([1,0,1])
    my_data_x.append([1,1,0])
    my_data_x.append([1,1,1])
    my_data_x
    
    my_data_y=[]
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(0)
    my_data_y.append(1)
    my_data_y
    
    return my_data_x, my_data_y


x,y = get_my_data()
for a,b in zip(x,y): #4 tane samples'ım var 3 tanesi a'dan 1 tanesi b'den
    print(a,b)
    
    
def get_parameters():
    w=[]
    w.append(300)
    w.append(200)             #random olarak oluşturduk(randomly)
    w.append(100)
    w
    learning_rate=1
    epoch=100              #randomly
    
    return w,learning_rate,epoch
get_parameters()



w,learning_rate,epoch=get_parameters()
samples,output=get_my_data() #sample -> x değerleri


output


for i in range(100): #(epoch):
    error="hata_yok"
    s=-1
    print("******************************************************************")
    for each_sample, d in zip(samples, output):
        s=s+1
        print("ağırlık:", w)
        print("örnek:", each_sample)
        print("Gerçek output:", d)
        #print(my_product_two_dim_with_threshold(w,each_sample))
        
        u=my_product_two_dim_with_threshold(each_sample,w)
        #print(u)
        if(u>0):
            y=1
        else:
            y=0
            
        print("tahmin çıktı:",y)
        print("")
        
        if(y!=d): #error var
            for s in range(3):
                w[s]=w[s]-learning_rate*(y-d)*each_sample[s]# d gerçek output, y benim bulduğum output
                #w[s]=w[s]+learning_rate*(d-y)*each_sample[s] #her iki ifade de aynıdır
                error="hata_var"
    if(error=="hata_yok"):
        print("hata_yok", i)
        break #return 0
print(w)




