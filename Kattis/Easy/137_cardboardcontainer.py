# find the factor of n
def find_factors(n):
    factors = []
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            factors.append(i)
            if i != n//i:
                factors.append(n//i)
    return sorted(factors)
    
# find the combination regarding of factors
def find_combination(n):
    factors = find_factors(n)
    combination=[]
    
    for p in factors:
        for l in factors:
            if n%(p*l)==0:
                t = n//(p*l)
                combination.append((p,l,t))
    return combination

# find the surface area
def surface_area(p,l,t):
    surface = 2*((p*l)+(p*t)+(l*t))
    return surface
    
# find the minimum of the surface
def surface_minimum(n):
    combination = find_combination(n)
    min_area = float('inf')
    for p,l,t in combination:
        area = surface_area(p,l,t)
        if area < min_area:
            min_area=area
        
    return min_area


def main():
    n = int(input())
    a = surface_minimum(n)
    print(a)

main()