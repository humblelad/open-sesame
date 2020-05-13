def refresh():

    import requests
    import csv
    from bs4 import BeautifulSoup



    no=0
    convert=[]
    for i in range(0,10):

        print("Collecting page "+str(i+1))
        URL = 'http://h1.nobbd.de/index.php?start='+str(no)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')
        results=soup.find(id='reports-all')
        test=results.find_all(class_='title')


        for o in test:
            s=o['href']
            #print(s)


            convert.append(s)



        no+=20




    body= convert
    #print (body)

    with open('final.txt') as f:
        first_line = f.readline().strip()



    for x in range(len(body)):

        if body[x]!=first_line:
            f=open('filter.txt', 'a')
            f.write(body[x]+'\n')
            f.close()
            find = open("final.txt", "r")
            data2 = find.read()
            find.close()
            fin = open("filter.txt", "r")
            data3 = fin.read()
            fin.close()
            fout = open("temp.txt", "w")
            fout.write(data3)
            fout.write(data2)
            fout.close()
            print("Added "+body[x])

        else:
            # print(first_line)
            print("No more data can be added!")
            break





    find = open("temp.txt", "r")
    cp = find.read()
    find.close()

    find = open("final.txt", "w")
    find.write(cp)
    find.close()

if __name__ == "__main__":
        refresh()