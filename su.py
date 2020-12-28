#!/usr/bin/env python

debug=1

def clean():
   foreach bR (0,1,2):
      foreach bC (0,1,2)
      :
         foreach lR (0,1,2)
         :
            foreach lC (0,1,2)
            :
               if (sudoku[bR][bC][lR][lC]{is  not = 0)
               :
                  foreach i (1,2,3,4,5,6,7,8,9)
                  :
                     sudoku[bR][bC][lR][lC]{couldbe{i = 0
                  

                  value = sudoku[bR][bC][lR][lC]{is

                  # eliminate couldbe' bR/lilrow
                  foreach i (0,1,2)
                  :
                     foreach j (0,1,2)
                     :
                        # eliminate couldbe' bR/lR
                        sudoku[bR][i][lR][j]{couldbe{value = 0

                        # eliminate couldbe' bC/lC
                        sudoku[i][bC][j][lC]{couldbe{value = 0

                        # eliminate couldbe' bR/bC
                        sudoku[bR][bC][i][j]{couldbe{value = 0
                     
                  
               
            
         
      
   


   if (debug)
   :
      print "done cleaning+++\n"
      printMatrix()
   


def markOnlyOneAnswer():
   foreach bR (0,1,2)
   :
      foreach bC (0,1,2)
      :
         foreach lR (0,1,2)
         :
            foreach lC (0,1,2)
            :
               if (sudoku[bR][bC][lR][lC]{is == 0)
               :
                  #=============================================================
                  # evaluate couldbe to see if there is only 1 answer
                  answer = 0
                  foreach i (1,2,3,4,5,6,7,8,9)
                  :
                     if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                     :
                        answer += 1
                        value = i
                     
                  

                  if (answer == 1)
                  :
                     sudoku[bR][bC][lR][lC]{is = value
                     changes++

                     if (debug)
                     :
                        print "found answer: "
                        print "bR+bC+lR+lC = value\n"
                        printMatrix()
                     
                  
                  elsif (answer == 0)
                  :
                     print "ERROR bR+bC+lR+lC = value not  not \n"; exit
                  


                  #=============================================================
                  # evaluate 
               
            
         
      
   


def clearNumbersOnlyInXCells():
   #  This analysis has to do with the X numbers only appearing in X cells in a row
   #  or a column+   Say for instance you have 1,2,3 as possible choices in 3 cells
   #  in a row+  Then you can safely eliminate 4,5,6,7,8,9 as possible choices in
   #  those cells+


   foreach first (1,2,3,4,5,6,7,8,9)
   :
      foreach second (1,2,3,4,5,6,7,8,9)
      :
         if (second > first)
         :
         ### foreach third (1,2,3,4,5,6,7,8,9)
         ### :
            ### foreach fourth (1,2,3,4,5,6,7,8,9)
            ### :
               ### foreach fifth (1,2,3,4,5,6,7,8,9)
               ### :



                  ### Check Rows
                  foreach bR (0,1,2)
                  :
                     foreach lR (0,1,2)
                     :
                        rowCount=0
                        rowFails=0
                        foreach bC (0,1,2)
                        :
                           foreach lC (0,1,2)
                           :
                              value = ""
                     
                              if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  && 
                                  sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                              :
                                 rowCount++
                              
                              elsif (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  ||
                                  sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                              :
                                 rowFails++
                                
                           
                        
                        if ( not rowFails && rowCount == 2)
                        :
                           if (debug) { print "found a hidden pair first,second in br=bR,lr=lR\n"; 
                           foreach bC (0,1,2)
                           :
                              foreach lC (0,1,2)
                              :
                                 if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  &&
                                     sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                                 :
                                    foreach i (1,2,3,4,5,6,7,8,9)
                                    :
                                       if (i  not = first && i  not = second)
                                       :
                                          sudoku[bR][bC][lR][lC]{couldbe{i = 0
                                       
                                    
                                 
                              
                           
                        
                     
                  

                  ### Check Columns
                  foreach bC (0,1,2)
                  :
                     foreach lC (0,1,2)
                     :
                        colCount=0
                        colFails=0
                        foreach bR (0,1,2)
                        :
                           foreach lR (0,1,2)
                           :
                              value = ""
                     
                              if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  && 
                                  sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                              :
                                 colCount++
                              
                              elsif (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  ||
                                  sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                              :
                                 colFails++
                                
                           
                        
                        if ( not colFails && colCount == 2)
                        :
                           if (debug) { print "found a hidden pair first,second in bc=bC,lc=lC\n"; 
                           foreach bR (0,1,2)
                           :
                              foreach lR (0,1,2)
                              :
                                 if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  &&
                                     sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                                 :
                                    foreach i (1,2,3,4,5,6,7,8,9)
                                    :
                                       if (i  not = first && i  not = second)
                                       :
                                          sudoku[bR][bC][lR][lC]{couldbe{i = 0
                                       
                                    
                                 
                              
                           
                        
                     
                  


               ### 
            ### 
         ### 
         
      
   


def xwinganlysis_rows():
   foreach first (1,2,3,4,5,6,7,8,9)
   :
       vecs
       ### Check Rows
       foreach bR (0,1,2)
       :
          foreach lR (0,1,2)
          :
             rownum=bR*3+lR

             # create vectors for each first, see if there are 2 solutions and compare
             vecs[rownum]=sudoku[bR][*][lR][*]{couldbe{first
          
       

       #find vecs that have exactly 2 solutions
       foreach vec @vecs
       :
           @{vec
       


                if ( not rowFails && rowCount == 2)
                :
                   if (debug) { print "found a hidden pair first,second in br=bR,lr=lR\n"; 
                   foreach bC (0,1,2)
                   :
                      foreach lC (0,1,2)
                      :
                         if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  &&
                             sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                         :
                            foreach i (1,2,3,4,5,6,7,8,9)
                            :
                               if (i  not = first && i  not = second)
                               :
                                  sudoku[bR][bC][lR][lC]{couldbe{i = 0
                               
                            
                         
                      
                   
                

          ### Check Columns
          foreach bC (0,1,2)
          :
             foreach lC (0,1,2)
             :
                colCount=0
                colFails=0
                foreach bR (0,1,2)
                :
                   foreach lR (0,1,2)
                   :
                      value = ""
             
                      if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  && 
                          sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                      :
                         colCount++
                      
                      elsif (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  ||
                          sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                      :
                         colFails++
                        
                   
                
                if ( not colFails && colCount == 2)
                :
                   if (debug) { print "found a hidden pair first,second in bc=bC,lc=lC\n"; 
                   foreach bR (0,1,2)
                   :
                      foreach lR (0,1,2)
                      :
                         if (sudoku[bR][bC][lR][lC]{couldbe{first  == 1  &&
                             sudoku[bR][bC][lR][lC]{couldbe{second == 1)
                         :
                            foreach i (1,2,3,4,5,6,7,8,9)
                            :
                               if (i  not = first && i  not = second)
                               :
                                  sudoku[bR][bC][lR][lC]{couldbe{i = 0
                               
                            
                         
                      
                   
                
             
          
   


def clearPairROW():
   my (clearValue,bR,lR) = @_

   if (debug)
   :
      print "clearing pair row, clearValue, from bigRow, bR, lilRow, lR\n"
   

   foreach bC (0,1,2)
   :
      foreach lC (0,1,2)
      :
         value = ""

         foreach i (1,2,3,4,5,6,7,8,9)
         :
            if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
            :
               value = value+i
            
         


         if (value ne clearValue)
         :
            for (i=0; i < length(clearValue); i++)
            :
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]{couldbe{foo = 0
            
         
      
   


def clearPairCOL():
   my (clearValue,bC,lC) = @_

   if (debug)
   :
      print "clearing pair col, clearValue, from bigCol, bC, lilCol, lC\n"
   

   foreach bR (0,1,2)
   :
      foreach lR (0,1,2)
      :
         value = ""

         foreach i (1,2,3,4,5,6,7,8,9)
         :
            if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
            :
               value = value+i
            
         


         if (value ne clearValue)
         :
            for (i=0; i < length(clearValue); i++)
            :
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]{couldbe{foo = 0
            
         
      
   


def clearBlockExceptROW():
   my (clearValue,bR,bC,excludelR) = @_

   if (debug)
   :
      print "clearing block exept row, clearValue, from bigRow, bR, bigCol, "
      print "bC, lilRow, excludelR\n"
   

   foreach lR (0,1,2)
   :
      if (lR  not = excludelR)
      :
         foreach lC (0,1,2)
         :
            for (i =0; i < length(clearValue); i++)
            :
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]{couldbe{foo = 0
            
         
      
   


def clearBlockExceptCOL():
   my (clearValue,bR,bC,excludelC) = @_

   if (debug)
   :
      print "clearing block exept col, clearValue, from bigRow, bR, bigCol, "
      print "bC, lilCol, excludelC\n"
   

   foreach lR (0,1,2)
   :
      foreach lC (0,1,2)
      :
         if (lC  not = excludelC)
         :
            for (i =0; i < length(clearValue); i++)
            :
               foo = substr(clearValue,i,1)
               sudoku[bR][bC][lR][lC]{couldbe{foo = 0
            
         
      
   



def printMatrix():
   my %numbersLeft
   
   if (debug)
   :
      foreach bR (0,1,2)
      :
         foreach lR (0,1,2)
         :
            for(i =0; i<3; i++)
            :
               foreach bC (0,1,2)
               :
                  foreach lC (0,1,2)
                  :
                     if (sudoku[bR][bC][lR][lC]{is  not = 0)
                     :
                        ### if (i == 0 || i == 2)
                        ### :
                           ### print "***"
                        ### 
                        ### elsif (i == 1)
                        ### :
                           ### print "*"+sudoku[bR][bC][lR][lC]{is+"*"
                        ### 
                        print sudoku[bR][bC][lR][lC]{is+sudoku[bR][bC][lR][lC]{is+sudoku[bR][bC][lR][lC]{is
                     
                     else
                     :
                        my @subset

                        if (i == 0)
                        :
                           @subset = (1,2,3)
                        
                        elsif (i == 1)
                        :
                           @subset = (4,5,6)
                        
                        elsif (i == 2)
                        :
                           @subset = (7,8,9)
                        

                        foreach i (@subset)
                        :
                           if(sudoku[bR][bC][lR][lC]{couldbe{i)
                           :
                              print "i"
                              numbersLeft{i++
                           
                           else
                           :
                             print "_"
                           
                        
                     
                     print " "
                  
   
                  print "  "
               
               print "\n"
            
            print "\n"
         
         print "\n"
      

      foreach i (1,2,3,4,5,6,7,8,9)
      :
         print "i: numbersLeft{i\n"
      
   
   else
   :
      foreach bR (0,1,2)
      :
         foreach lR (0,1,2)
         :
            foreach bC (0,1,2)
            :
               foreach lC (0,1,2)
               :
                  if (sudoku[bR][bC][lR][lC]{is  not = 0)
                  :
                     print "sudoku[bR][bC][lR][lC]{is"
                  
                  else
                  :
                     print "?"
                  
   
                  print " "
               
               print "  "
            
            print "\n"
         
         print "\n"
      
   


def puzzleSolved():
   # calculate whether the puzzle is solved or not
   if (debug)
   :
      print "checking if puzzle solved+++"
   

   foreach bR (0,1,2)
   :
      foreach bC (0,1,2)
      :
         foreach lR (0,1,2)
         :
            foreach lC (0,1,2)
            :
               foreach i (1,2,3,4,5,6,7,8,9)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i  not = 0)
                  :
                     if (debug)
                     :
                        print " nope\n"
                     
                     return 0
                  
               
            
         
      
   

   if (debug)
   :
      print " YES not \n"
   
   return 1



#=======================
#        START
#=======================

@input

foreach bR (0,1,2)
:
   foreach lR (0,1,2)
   :
      foreach bC (0,1,2)
      :
         foreach lC (0,1,2)
         :
            while (#input == -1 | 0)
            :
               chomp(entry = <>)
               @input = split(/ /,entry)
            

            sudoku[bR][bC][lR][lC]{is = shift(@input)
         
      
   




#=======================
#      Initialize
#=======================
foreach bR (0,1,2)
:
   foreach bC (0,1,2)
   :
      foreach lR (0,1,2)
      :
         foreach lC (0,1,2)
         :
            if (sudoku[bR][bC][lR][lC]{is  not = 0)
            :
               foreach i (1,2,3,4,5,6,7,8,9)
               :
                  sudoku[bR][bC][lR][lC]{couldbe{i = 0
               
            
            else
            :
               foreach i (1,2,3,4,5,6,7,8,9)
               :
                  sudoku[bR][bC][lR][lC]{couldbe{i = 1
               
            
         
      
   




while ( not puzzleSolved)
:
   iterations++
   changes = 0

   clean()

   # check each ROW for single values
   if (debug) { print "check each ROW for single values\n"; 
   foreach bR (0,1,2)
   :
      foreach lR (0,1,2)
      :
         foreach i (1,2,3,4,5,6,7,8,9)
         :
            answer = 0
            foreach bC (0,1,2)
            :
               foreach lC (0,1,2)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     answer += 1
                     value = i
                     valueBC = bC
                     valueLC = lC
                  
               
            
            if (answer == 1)
            :
               sudoku[bR][valueBC][lR][valueLC]{is = value
               changes++

               if (debug)
               {  
                  print "found ROW answer: "
                  print "bR+valueBC+lR+valueLC = value\n"
                  printMatrix()
               

               clean()
            
         
      
   

   clean()

   # check each COL for single values
   if (debug) { print "check each COL for single values\n"; 
   foreach bC (0,1,2)
   :
      foreach lC (0,1,2)
      :
         foreach i (1,2,3,4,5,6,7,8,9)
         :
            answer = 0
            foreach bR (0,1,2)
            :
               foreach lR (0,1,2)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     answer += 1
                     value = i
                     valueBR = bR
                     valueLR = lR
                  
               
            
            if (answer == 1)
            :
               sudoku[valueBR][bC][valueLR][lC]{is = value
               changes++

               if (debug)
               {  
                  print "found COL answer: "
                  print "valueBR+bC+valueLR+lC = value\n"
                  printMatrix()
               

               clean()
            
         
      
   

   # check each COL for BLOCK only values
   if (debug) { print "check each COL for BLOCK only values\n"; 
   foreach bC (0,1,2)
   :
      foreach lC (0,1,2)
      :
         foreach i (1,2,3,4,5,6,7,8,9)
         :
            my %colBlockOnly
            answer = 0
            foreach bR (0,1,2)
            :
               foreach lR (0,1,2)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     colBlockOnly{bR = 1
                  
               
            
            my @foo = keys %colBlockOnly
            if (#foo == 0)
            :
               print "found COL for BLOCK only, i,foo[0],bC,lC\n"
               clearBlockExceptCOL(i,foo[0],bC,lC)
               clean()
            
            undef %colBlockOnly
         
      
   


   # check each ROW for BLOCK only values
   if (debug) { print "check each ROW for BLOCK only values\n"; 
   foreach bR (0,1,2)
   :
      foreach lR (0,1,2)
      :
         foreach i (1,2,3,4,5,6,7,8,9)
         :
            my %rowBlockOnly
            answer = 0
            foreach bC (0,1,2)
            :
               foreach lC (0,1,2)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     rowBlockOnly{bC = 1
                  
               
            
            my @foo = keys %rowBlockOnly
            if (#foo == 0)
            :
               print "found ROW for BLOCK only, i,bR,foo[0],lR\n"
               clearBlockExceptROW(i,bR,foo[0],lR)
               clean()
            
            undef %rowBlockOnly
         
      
   



   # check each BLOCK for single values
   if (debug) { print "check each BLOCK for single values\n"; 
   foreach bR (0,1,2)
   :
      foreach bC (0,1,2)
      :
         foreach i (1,2,3,4,5,6,7,8,9)
         :
            answer = 0
            foreach lR (0,1,2)
            :
               foreach lC (0,1,2)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     answer += 1
                     value = i
                     valueLC = lC
                     valueLR = lR
                  
               
            
            if (answer == 1)
            :
               sudoku[bR][bC][valueLR][valueLC]{is = value
               changes++

               if (debug)
               {  
                  print "found BLOCK answer: "
                  print "bR+bC+valueLR+valueLC = value\n"
                  printMatrix()
               

               clean()
            
         
      
   

   clean()
   markOnlyOneAnswer()

   if (debug) { print "check each ROW for pairs\n"; 
   foreach bR (0,1,2)
   :
      foreach lR (0,1,2)
      :
         my @savedValue
         count = 0
         foreach bC (0,1,2)
         :
            foreach lC (0,1,2)
            :
               answer = 0
               value = ""

               foreach i (1,2,3,4,5,6,7,8,9)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     answer += 1
                     value = value+i
                  
               

               if (answer == 2)
               :
                  found = 0
                  for (i=0; i <= #savedValue; i++)
                  :
                     if (value eq savedValue[i])
                     :
print "FOUND: #savedValue savedValue[i] value\n"
                        found = 1
                     
                  

                  if (found == 0)
                  :
                     savedValue[count] = value
print "FOUND0: #savedValue savedValue[i] value\n"
                     count++
                  
                  else
                  :
                     # we have found a "pair"
                     if (debug) { print "ROW pair found: bR+bC+lR+lC = value\n";  printMatrix(); 
                     clearPairROW(value,bR,lR)
                  
               
            
         
         undef @savedValue
      
   

   clean()
   markOnlyOneAnswer()

   if (debug) { print "check each ROW for cell pairs\n"; 
   foreach bR (0,1,2)
   :
      foreach lR (0,1,2)
      :
         my @value
         foreach bC (0,1,2)
         :
            foreach lC (0,1,2)
            :
               answer = 0

               foreach i (1,2,3,4,5,6,7,8,9)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     value[i]++
                  
               
            
         

         foreach i (1,2,3,4,5,6,7,8,9)
         :
            #### TODO ####
         
      
   

   if (debug) { print "check each COL for pairs\n"; 
   foreach bC (0,1,2)
   :
      foreach lC (0,1,2)
      :
         my @savedValueCOL
         count = 0
         foreach bR (0,1,2)
         :
            foreach lR (0,1,2)
            :
               answer = 0
               value = ""

               foreach i (1,2,3,4,5,6,7,8,9)
               :
                  if (sudoku[bR][bC][lR][lC]{couldbe{i == 1)
                  :
                     answer += 1
                     value = value+i
                  
               

               if (answer == 2)
               :
                  found = 0
                  for (i=0; i <= #savedValueCOL; i++)
                  :
                     if (value eq savedValueCOL[i])
                     :
                        found = 1
                     
                  

                  if (found == 0)
                  :
                     savedValueCOL[count] = value
                     count++
                  
                  else
                  :
                     # we have found a "pair"
                     if (debug) { print "COL pair found: bR+bC+lR+lC = value\n";  printMatrix(); 
                     clearPairCOL(value,bC,lC)
                  
               
            
         
         undef @savedValueCOL
      
   

   clearNumbersOnlyInXCells()

   if (debug)
   :
      printMatrix()
      print "================================================================================\n"
   

   if (changes == 0)
   :
      if (changeIterations++ == 40)
      :
         print "something's hosed+++\n"; exit
      
   
   else
   :
      changeIterations = 0
   




print "Solved in iterations Iterations \n"
printMatrix()
