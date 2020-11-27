#!/bin/bash


<<comment 



# This is a comment!
echo Hello World	
echo "im here "
printf "heloiaaa  who number is %d\n" 20


printf "halioiaa my name is %s and my age is %d\n" alaa 25




#  alaa as comment 


#readonly name="alaa elnagar"   #  cant change its value 
age=20

echo $name $age 
name="luka"
	
echo $name $age 

printf "my name is %s and my age is %d " alaa 20


echo name = $name and my age = $age 



unset name 

echo my name is $name 

comment


<<comment
#SPECIAL VARIABLES 


echo $$  	#return bash script process number 


echo $?		#return 0 incase of no error 

echo here we go $1 and $2 

echo $#  #define number of variables entered with user 


 echo $0  #return name of bash 
 name="alaa"
 echo $2  #n return number or var enterd by user
 
 
echo plz enter first name

read f_name

echo plz enter second name 

read second_name 


echo you have ntered $f_name $second_name


comment


#operations 

ex=$((5+10))

echo $ex

echo enter first num 

read f1

echo enter the second num 

read f2

#the folwing instruction is more trustd 

echo $f1 + $f2 =`echo $f1 + $f2 | bc`




































































