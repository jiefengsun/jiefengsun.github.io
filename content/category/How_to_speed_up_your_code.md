Title: How to speed up your code
Date: 2020-08-24 08:00
Modified: 2020-08-25 10:50
Category: Research

1. Preallocate the memory. The prepared memory will save time on finding a new address. 

2. Vectorization. The program can deal with blocks instead of individual values. 

3. Precalculation. You don't want to calculate repeat things, and it's better to calculate it before using it in a loop. 

4. Use functions from standard libraries. These functions may run faster than yours. 

5. Use more hardware. GPUs, multiple cores, and parallel your code. 


Of course, using `C++` rather than `Python` or `Malab` will also speed up your code a lot.
