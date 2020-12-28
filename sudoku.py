#!/usr/bin/env python3





def readInput(lines):
    """
    lines = 9x9 matrix in text form, 0's represent blanks
    """
    # create 9x9x9 puzzle matrix from text
    puzzle =  [ ]
    return puzzle


def checkRow():
   pass 


def clean():
   for bR in (0,1,2):
      for bC in (0,1,2):
         for lR in (0,1,2):
            for lC in (0,1,2):
               if (sudoku[bR][bC][lR][lC]['is'] != 0):
                  for i in (1,2,3,4,5,6,7,8,9):
                     sudoku[bR][bC][lR][lC]['couldbe'][i] = 0

                  value = sudoku[bR][bC][lR][lC]['is']

                  # eliminate couldbe' bR/lilrow
                  for i in (0,1,2):
                     for j in (0,1,2):
                        # eliminate couldbe' bR/lR
                        sudoku[bR][i][lR][j]['couldbe'][value] = 0

                        # eliminate couldbe' bC/lC
                        sudoku[i][bC][j][lC]['couldbe'][value] = 0

                        # eliminate couldbe' bR/bC
                        sudoku[bR][bC][i][j]['couldbe'][value] = 0

   if (debug):
      print "done cleaning...\n"
      printMatrix()

def markOnlyOneAnswer():
   for bR in (0,1,2):
      for bC in (0,1,2):
         for lR in (0,1,2):
            for lC in (0,1,2):
               if (sudoku[bR][bC][lR][lC]['is'] == 0):
                  #=============================================================
                  # evaluate couldbe to see if there 'is' only 1 answer
                  answer = 0
                  for i in (1,2,3,4,5,6,7,8,9):
                     if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                        answer += 1
                        value = i

                  if (answer == 1):
                     sudoku[bR][bC][lR][lC]['is'] = value
                     changes+=1

                     if (debug):
                        print "found answer: "
                        print "bR.bC.lR.lC = value\n"
                        printMatrix()
                  elif answer == 0:
                     print "ERROR bR.bC.lR.lC = value!!\n"; exit


def clearNumbersOnlyInXCells():
   #  This analysis has to do with the X numbers only appearing in X cells in a row
   #  or a column.   Say for instance you have 1,2,3 as possible choices in 3 cells
   #  in a row.  Then you can safely eliminate 4,5,6,7,8,9 as possible choices in
   #  those cells.


   for first in (1,2,3,4,5,6,7,8,9):
      for second in (1,2,3,4,5,6,7,8,9):
         if (second > first):
                  ### Check Rows
                  for bR in (0,1,2):
                     for lR in (0,1,2):
                        rowCount=0
                        rowFails=0
                        for bC in (0,1,2):
                           for lC in (0,1,2):
                              value = ""
                     
                              if (sudoku[bR][bC][lR][lC]['couldbe'][first]  == 1  and 
                                 sudoku[bR][bC][lR][lC]['couldbe'][second] == 1):
                                 rowCount+=1
                              elif (sudoku[bR][bC][lR][lC]['couldbe'][first]  == 1  or
                                 sudoku[bR][bC][lR][lC]['couldbe'][second] == 1):
                                 rowFails+=1
                        if (!rowFails and rowCount == 2):
                           if (debug) [ print "found a hidden pair first,second in br=bR,lr=lR\n"; ]:
                           for bC in (0,1,2):
                              for lC in (0,1,2):
                                 if (sudoku[bR][bC][lR][lC]['couldbe'][first]  == 1  and
                                     sudoku[bR][bC][lR][lC]['couldbe'][second] == 1):
                                    for i in (1,2,3,4,5,6,7,8,9):
                                       if (i != first and i != second):
                                          sudoku[bR][bC][lR][lC]['couldbe'][i] = 0

                  ### Check Columns
                  for bC in (0,1,2):
                     for lC in (0,1,2):
                        colCount=0
                        colFails=0
                        for bR in (0,1,2):
                           for lR in (0,1,2):
                              value = ""
                     
                              if (sudoku[bR][bC][lR][lC]['couldbe'][first]  == 1  and 
                                  sudoku[bR][bC][lR][lC]['couldbe'][second] == 1):
                                 colCount+=1
                              elsif (sudoku[bR][bC][lR][lC]['couldbe'][first]  == 1  or
                                  sudoku[bR][bC][lR][lC]['couldbe'][second] == 1):
                                 colFails+=1
                        if (!colFails and colCount == 2):
                           if (debug):
                              print "found a hidden pair first,second in bc=bC,lc=lC\n"
                           for bR in (0,1,2):
                              for lR in (0,1,2):
                                 if (sudoku[bR][bC][lR][lC]['couldbe'][first]  == 1  and
                                     sudoku[bR][bC][lR][lC]['couldbe'][second] == 1):
                                    for i in (1,2,3,4,5,6,7,8,9):
                                       if (i != first and i != second):
                                          sudoku[bR][bC][lR][lC]['couldbe'][i] = 0


def clearPairROW(clearValue,bR,lR):

   if (debug):
      print("clearing pair row, clearValue, from bigRow, bR, lilRow, lR\n")

   for bC in (0,1,2):
      for lC in (0,1,2):
         value = ""

         for i in (1,2,3,4,5,6,7,8,9):
            if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
               value = value.i

         if (value ne clearValue):
            for (i=0; i < length(clearValue); i+=1):
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]['couldbe'][foo] = 0


def clearPairCOL(clearValue,bC,lC):

   if (debug):
      print "clearing pair col, clearValue, from bigCol, bC, lilCol, lC\n"

   for bR in (0,1,2):
      for lR in (0,1,2):
         value = ""

         for i in (1,2,3,4,5,6,7,8,9):
            if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
               value = value.i

         if (value ne clearValue):
            for (i=0; i < length(clearValue); i+=1):
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]['couldbe'][foo] = 0


def clearBlockExceptROW(clearValue,bR,bC,excludelR):
   if (debug):
      print "clearing block exept row, clearValue, from bigRow, bR, bigCol, "
      print "bC, lilRow, excludelR\n"

   for lR in (0,1,2):
      if (lR != excludelR):
         for lC in (0,1,2):
            for (i=0; i < length(clearValue); i+=1):
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]['couldbe'][foo] = 0

def clearBlockExceptCOL(clearValue,bR,bC,excludelC):

   if (debug):
      print "clearing block exept col, clearValue, from bigRow, bR, bigCol, "
      print "bC, lilCol, excludelC\n"

   for lR in (0,1,2):
      for lC in (0,1,2):
         if (lC != excludelC):
            for (i=0; i < length(clearValue); i+=1):
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]['couldbe'][foo] = 0


def printMatrix():
   if (debug):
      for bR in (0,1,2):
         for lR in (0,1,2):
            for(i=0; i<3; i+=1):
               for bC in (0,1,2):
                  for lC in (0,1,2):
                     if (sudoku[bR][bC][lR][lC]['is'] != 0):
                        print sudoku[bR][bC][lR][lC]['is'].sudoku[bR][bC][lR][lC]['is'].sudoku[bR][bC][lR][lC]['is']
                     else
                        subset=[]

                        if (i == 0):
                           subset = (1,2,3)
                        elsif (i == 1):
                           subset = (4,5,6)
                        elsif (i == 2):
                           subset = (7,8,9)

                        for i in (@subset):
                           if(sudoku[bR][bC][lR][lC]['couldbe'][i]):
                              print "i"
                              numbersLeft[i]+=1
                           else
                             print "_"
                     print " "
                  print "  "
               print "\n"
            print "\n"
         print "\n"

      for i in (1,2,3,4,5,6,7,8,9):
         print "i: numbersLeft[i]\n"
   else:
      for bR in (0,1,2):
         for lR in (0,1,2):
            for bC in (0,1,2):
               for lC in (0,1,2):
                  if (sudoku[bR][bC][lR][lC]['is'] != 0):
                     print "sudoku[bR][bC][lR][lC]['is']"
                  else:
                     print "?"
                  print " "
               print "  "
            print "\n"
         print "\n"

def puzzleSolved():
   # calculate whether the puzzle is solved or not
   if (debug):
      print "checking if puzzle solved..."

   for bR in (0,1,2):
      for bC in (0,1,2):
         for lR in (0,1,2):
            for lC in (0,1,2):
               for i in (1,2,3,4,5,6,7,8,9):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] != 0):
                     if (debug):
                        print " nope\n"
                     return 0

   if (debug):
      print " YES!\n"
   return 1


#=======================
#        START
#=======================

@input

for bR in (0,1,2):
   for lR in (0,1,2):
      for bC in (0,1,2):
         for lC in (0,1,2):
            while (#input == -1 | 0):
               chomp(entry = <>)
               @input = split(/ /,entry)

            sudoku[bR][bC][lR][lC]['is'] = shift(@input):



#=======================
#      Initialize
#=======================
for bR in (0,1,2):
   for bC in (0,1,2):
      for lR in (0,1,2):
         for lC in (0,1,2):
            if (sudoku[bR][bC][lR][lC]['is'] != 0)
               for i in (1,2,3,4,5,6,7,8,9):
                  sudoku[bR][bC][lR][lC]['couldbe'][i] = 0
            else
               for i in (1,2,3,4,5,6,7,8,9):
                  sudoku[bR][bC][lR][lC]['couldbe'][i] = 1

while (!puzzleSolved)
   iterations+=1
   changes = 0

   clean()

   # check each ROW for single values:
   if (debug) [ print "check each ROW for single values\n"; ]:
   for bR in (0,1,2):
      for lR in (0,1,2):
         for i in (1,2,3,4,5,6,7,8,9):
            answer = 0
            for bC in (0,1,2):
               for lC in (0,1,2):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     answer += 1
                     value = i
                     valueBC = bC
                     valueLC = lC
            if (answer == 1):
               sudoku[bR][valueBC][lR][valueLC]['is'] = value
               changes+=1

               if (debug):
                  print "found ROW answer: "
                  print "bR.valueBC.lR.valueLC = value\n"
                  printMatrix()

               clean()

   clean()

   # check each COL for single values:
   if (debug) [ print "check each COL for single values\n"; ]:
   for bC in (0,1,2):
      for lC in (0,1,2):
         for i in (1,2,3,4,5,6,7,8,9):
            answer = 0
            for bR in (0,1,2):
               for lR in (0,1,2):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     answer += 1
                     value = i
                     valueBR = bR
                     valueLR = lR
            if (answer == 1):
               sudoku[valueBR][bC][valueLR][lC]['is'] = value
               changes+=1

               if (debug):
                  print "found COL answer: "
                  print "valueBR.bC.valueLR.lC = value\n"
                  printMatrix()

               clean()

   # check each COL for BLOCK only values
   if (debug):
      print "check each COL for BLOCK only values\n"
   for bC in (0,1,2):
      for lC in (0,1,2):
         for i in (1,2,3,4,5,6,7,8,9):
            answer = 0
            for bR in (0,1,2):
               for lR in (0,1,2):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     colBlockOnly[bR] = 1
            foo = keys %colBlockOnly
            if (#foo == 0):
               print "found COL for BLOCK only, i,foo[0],bC,lC\n"
               clearBlockExceptCOL(i,foo[0],bC,lC)
               clean()
            undef %colBlockOnly


   # check each ROW for BLOCK only values
   if (debug): 
      print "check each ROW for BLOCK only values\n"
   for bR in (0,1,2):
      for lR in (0,1,2):
         for i in (1,2,3,4,5,6,7,8,9):
            rowBlockOnly
            answer = 0
            for bC in (0,1,2):
               for lC in (0,1,2):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     rowBlockOnly[bC] = 1
            foo = keys %rowBlockOnly
            if (#foo == 0):
               print "found ROW for BLOCK only, i,bR,foo[0],lR\n"
               clearBlockExceptROW(i,bR,foo[0],lR)
               clean()
            undef %rowBlockOnly


   # check each BLOCK for single values
   if (debug): print "check each BLOCK for single values\n"
   for bR in (0,1,2):
      for bC in (0,1,2):
         for i in (1,2,3,4,5,6,7,8,9):
            answer = 0
            for lR in (0,1,2):
               for lC in (0,1,2):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     answer += 1
                     value = i
                     valueLC = lC
                     valueLR = lR
            if (answer == 1):
               sudoku[bR][bC][valueLR][valueLC]['is'] = value
               changes+=1

               if (debug):
                  print "found BLOCK answer: "
                  print "bR.bC.valueLR.valueLC = value\n"
                  printMatrix()

               clean()

   clean()
   markOnlyOneAnswer()

   if (debug): print "check each ROW for pairs\n"
   for bR in (0,1,2):
      for lR in (0,1,2):
         savedValue
         count = 0
         for bC in (0,1,2):
            for lC in (0,1,2):
               answer = 0
               value = ""

               for i in (1,2,3,4,5,6,7,8,9):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     answer += 1
                     value = value.i

               if (answer == 2):
                  found = 0
                  for (i=0; i <= #savedValue; i+=1):
                     if (value eq savedValue[i]):
print "FOUND: #savedValue savedValue[i] value\n"
                        found = 1
                  if (found == 0):
                     savedValue[count] = value
print "FOUND0: #savedValue savedValue[i] value\n"
                     count+=1
                  else
                     # we have found a "pair"
                     if (debug): [ print "ROW pair found: bR.bC.lR.lC = value\n";  printMatrix(); ]
                     clearPairROW(value,bR,lR)
         undef @savedValue

   clean()
   markOnlyOneAnswer()

   if (debug): 
      print "check each ROW for cell pairs\n"
   for bR in (0,1,2):
      for lR in (0,1,2):
         for bC in (0,1,2):
            for lC in (0,1,2):
               answer = 0

               for i in (1,2,3,4,5,6,7,8,9):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     value[i]+=1

         for i in (1,2,3,4,5,6,7,8,9):
            #### TODO ####

   if (debug):
      print "check each COL for pairs\n"
   for bC in (0,1,2):
      for lC in (0,1,2):
         savedValueCOL=[]
         count = 0
         for bR in (0,1,2):
            for lR in (0,1,2):
               answer = 0
               value = ""

               for i in (1,2,3,4,5,6,7,8,9):
                  if (sudoku[bR][bC][lR][lC]['couldbe'][i] == 1):
                     answer += 1
                     value = value.i

               if (answer == 2):
                  found = 0
                  for (i=0; i <= #savedValueCOL; i+=1):
                     if (value eq savedValueCOL[i]):
                        found = 1

                  if (found == 0):
                     savedValueCOL[count] = value
                     count+=1
                  else
                     # we have found a "pair"
                     if (debug): 
                        print "COL pair found: bR.bC.lR.lC = value\n"
                        printMatrix()
                     clearPairCOL(value,bC,lC)
         undef @savedValueCOL

   clearNumbersOnlyInXCells()

   if (debug):
      printMatrix()
      print "================================================================================\n"

   if (changes == 0):
      if (changeIterations+=1 == 40):
         print "something's hosed...\n"; exit
   else
      changeIterations = 0



print "Solved in iterations Iterations \n"
printMatrix()
