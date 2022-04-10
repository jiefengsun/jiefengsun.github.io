Title: Numerical Conventions in Python and Matlab
Date: 2020-08-3 08:00
Modified: 2020-08-03 08:00
Category: Research Tricks & Tools

### Python mesh conventions

Usually, we will need to loop through the discretized time or spatial ponits in numerical computation. 

I just come up with some conventions to facilite nice codes. 


##### Name and loop conventions
N_t: Number of time steps;
N_s: Nummber of spatial points;


First we can generate a series of points
```python
t = linspace(0, N_t*dt, N_t+1)
```

When loop through the steps
```python
for n in range(0, N_t):
	u[n+1] = u[n] + dt*F[n] # F = u', Jacobian. 
```


##### Save conventions

```python
filestem = 'growth1_%dsteps' % N_t # format string with modulo operator
plt.savefig('%s.png' % filestem); plt.savefig('%s.pdf' % filestem)
```


##### Note

1. Remember to return an array. If it is an list, remember to convert it to an array. 



