
#!/bin/bash

<<comment 
#lab1

#if statement 
echo "enter the n1"

read n1


if [ $n1 -gt 0 ]
then 
echo "we have positive number"
exit
fi

echo "we have negative number"



# Lab 2acode to return the abslute number
echo "enter the n1"

read n1


if [ $n1 -gt 0 ]
then 
echo "we have Entered "$n1
exit
fi

echo "u have entered "  $(($n1*-1))


# operations on positive numbers

echo "enter the n1"

read n1
echo "enter the n1"

read n2


if [ $n1 -gt 0 ]
then 
if [ $n1 -gt 0 ]
then 
echo $n1 + $n2 = $((n1+n2))
echo $n1 / $n2 = $((n1/n2))
echo $n1 \* $n2 = $((n1 * n2))
echo $n1 - $n2 = $((n1-n2))
exit
fi
fi

echo "we have negative negative number"





#lab 4 using the same code with logical and 
echo "enter the n1"

read n1
echo "enter the n1"

read n2


if [ $n1 -gt 0 -a $n2 -gt 0 ]

then 

echo $n1 + $n2 = $((n1+n2))
echo $n1 / $n2 = $((n1/n2))
echo $n1 \* $n2 = $((n1 * n2))
echo $n1 - $n2 = $((n1-n2))
exit

fi

echo "we have negative negative number"



#lab 5 using if else and elif

echo enter n1
read n1
echo enter n2
read n2 

if [ $n1 -gt 0 -a $n2 -gt 0 ]
then
echo u have entered two positive numbers $n1 and $n2 
elif [ $n1 -lt 0 -a $n2 -gt 0 ]
then
echo "num1 > num2"
else 
echo u have entered two negative numbers
fi





#gedit $1  #to open the file which entered by the user 



if [ $# -lt 2 ]
then
echo "............no file entered................."
else 
mv $1 /home/elnagar/$2
echo "....process end successfully ...."
fi




#lab6 case esac statement 

echo "please enter your number "

read var


case $var in 

	1) echo "alaa elnagar"
	;;
	2)echo "number two"
	
	esac








echo  "please enter your command and help "

if [ $2 = "help" ]
then
$1 --$2

else 
echo "wrong help please write help "
fi



#lab8 code to print 1:10 with while





n=20
while [ $n -gt 0 ]
do
echo $n
n=$(($n-1))
done



# for loop
for i in *
do 
echo $i

done 



# lab 8 to search for file in the directory and print it using cat

for i in * 
do 
if [ $i = $1 ]
then 
cat $1

fi
done 



#code to inform u about type of files which directory or files

for i in * 
do 
if [ -f $i ]
then 
echo "-->file"
elif [ -d $i ]
then 
echo "-->dir"
fi
done 



#this code concerned with writting to another file 
echo "/*PROJECT NAME : AVR PIN CONFIGRATION */">DIOConfig.c 
echo "/*NAME : ALAA ELNAGAR */">>DIOConfig.c 

echo "void DIO_PORTA_DIR(void)">>DIOConfig.c    #this instruction to overwrite to a file note >> append 

echo "{">>DIOConfig.c

echo "DDRA=Ob"$1";">>DIOConfig.c
echo "DDRB=Ob"$2";">>DIOConfig.c
echo "DDRC=Ob"$3";">>DIOConfig.c
echo "DDRD=Ob"$4";">>DIOConfig.c

echo "}">>DIOConfig.c






#array with  linux 

names=('ahmed' 'alaa' 'ebrahim')

echo ${names[3]}


#dfeh 3ak gameeed henaaaaaaaa
Files=('ahmed' 'alaa' 'ebrahim')
Directory=('ahmed' 'alaa' 'ebrahim')
x=0
y=0
for i in * 
do 
if [ -f $i ]
then 
Files[x]=$i
x=$(($x+1))
echo "-->file"
elif [ -d $i ]
then 
${Directory[$y]}
x=$(($y+1))
echo "-->dir"
fi
done 

echo ${Files[0]}
echo ${Directory[0]}




for i in *


do 
if [ -f i ]
then 


elif [ -d i ]
then
folders[foldercount]=$i
foldercount=`expr $foldercount+1`
if


done 


#functions with bash script 

PrintMyName()
{
echo "Elnagar"
}


PrintMyName





PrintMyName()
{
echo $1
echo $2
}

PrintMyName "ALAA" "ELNAGAR"


comment

#change the file name 

ChangeFileName()
{
mv $1 $2

}

ChangeFileName $1 $2
































































































































































































































































































