def place_student(liste):
        sira_sayisi=liste[0]
        liste.remove(sira_sayisi)
        sol=[]
        sag=[]
        tam_liste=[]
        cnt = 0
        for i in range(1,sira_sayisi+1):
                if (liste.count(i)==0):
                        tam_liste.append('1')
                
                else:
                        tam_liste.append('0')
                        
        for i in range(1,sira_sayisi+1):
                if (liste.count(i)==0):
                        if(i%2==0):
                                sag.append('1')
                        else:
                                sol.append('1')
                else:
                        if(i%2==0):
                                sag.append('0')
                        else:
                                sol.append('0')



        for i in range(1,len(sol)):
                if(sol[i-1]  =='1' and sol [i]=='1'):
                        cnt+=1

        for i in range(1,len(sag)):
               
                if(sag[i-1]  == '1'and sag[i] =='1'):
                        cnt+=1

        for i in range(1,len(tam_liste),2):
                if( tam_liste[i-1]== '1' and tam_liste[i]=='1'):
                        cnt+=1
        print(cnt)


siralar=input()
sira_listesi=siralar.split(",")
sira_listesi=list(map(int,sira_listesi))

place_student(sira_listesi)
