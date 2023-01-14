def printTable(tabledata):
    L=len(tableData)
    colWidths = [0] * len(tableData)
    C=len(colWidths)

    max=0
    for i in range(L):
        for j in range(L+1):
            a=tableData[i][j]
            if len(a)>max:
                max=len(a)
        colWidths[i]=max
        max=0
    
    for i in range(L+1):
        for j in range(L):
            print(tableData[j][i].rjust(colWidths[j]), end=" ")
        print()
        
        

tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)