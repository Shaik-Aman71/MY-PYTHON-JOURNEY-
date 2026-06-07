sample_str=("dkjbfysyusd463&$ddsdbvh")
c_count=0
d_count=0
s_count=0
for c in sample_str:
    if c.isalpha():
        c_count+=1
    elif c.isdigit():
        d_count+=1
else:
    s_count+=1
print("charecters:",c_count,"digits count:",d_count,"symbol count:",s_count)            
        
            