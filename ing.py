st=input("enter any string:")
if len(st)>=3: 
    if st.endswith('ing'):
        print(st+'ly')
    else:
        print(st+'ing')
else:
    print(st)