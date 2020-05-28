import pandas as pd

arr1 = ["udp","arp","tcp","igmp","ospf","sctp","gre","ggp","ip","9n9","st2","argus","chaos","egp","emcon","nvp","pup","xnet","mux","dcn","hmp","prm","trunk-1","trunk-2","xns-idp","leaf-1","leaf-2","irtp","rdp","netblt","mfe-nsp","merit-inp","3pc","idpr","ddp","34-cmtp","tp++","9v6","sdrp","38-frag","38-route","idrp","tcf","eigrp","il","dgp","nsfnet-igp","vines","xtp","ttp","secure-vmtp","sep","vmtp","wb-expak","wb-mon","iso-tp4","sun-nd","br-sat-mon","pvp","wsn","cphb","9cv","cpnx","visa","sat-mon","any","kryptolan","igp","9pc","cftp","38-opts","38-no","bbn-rcc","sw9e","n2","cbt","i-nlsp","bna","mhrp","scps","qnx","pnni","ifmp","gmtp","pri-enc","encap","micp","aes-sp3-d","ax.25","mtp","l2sprite-rpc","sat-expak","tlsp","sk9","mob45e","rvd","rsvp","unas","fc","iso-9","ether9","pim","aris","a/n","9comp","snp","compaq-peer","9x-n-9","pgm","vrrp","91tp","zero","ddx","iatp","stp","srp","uti","sm","119p","isis","ptp","fire","crtp","cr1","sccopmce","9lt","p9e","sps","ib"]
arr2 = ["INT","FIN","REQ","ACC","CON","RST","CLO"]
arr3 = ["Normal","Recnaissance","Backdoor","DoS","Exploits","Analysis","Fuzzers","Worms","Shellcode","Generic"]

dic1 = {}
dic2 = {}
dic3 = {}

for i in range(len(arr1)):
    dic1[arr1[i]] = (i+1)

for i in range(len(arr2)):
    dic2[arr2[i]] = (i+1)

for i in range(len(arr3)):
    dic3[arr3[i]] = (i+1)


#print(dic1)
#print(dic2)
#print(dic3)
df = pd.read_csv('Copy.csv')

for j in df:
    print(j)
    for i in range(len(df)):
        for n in arr1:
            print("i",n)
            if df.at[i,j] == n :
                df.at[i,j] = dic1[n]
                print("found")
        for m in arr2:
            if df.at[i,j] == m :
                df.at[i,j] = dic2[m]
                print("found")
        for l in arr3:
            if df.at[i,j] == l :
                df.at[i,j] = dic3[l]
                print("found")

df.to_csv('Copy1.csv') 
