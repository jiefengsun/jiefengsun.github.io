Title: Debug the TCA modeling
Date: 2020-05-18 08:00
Modified: 2020-06-01 08:00
password: jiefeng

## Bugs
- The matplotlib don't have a equal axis view

I solved this problem by adding some code to the `utils` file. However, I expect that they fix this problem in the future. 

-  cannot convert float NaN to integer, caused by `expm` when its inut is zero. 


## Modifications
1. To adapt the original code to the 

## Tried

1 The static will not work even for a Conventional Explicit Euler Method. 

2. The Dynamic one did not work. I am not sure what is the problem. 