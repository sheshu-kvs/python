
# brute appraoch
def unionofset():
    a1=[1,1,2,3,4,5];
    a2=[2,3,4,4,5,6];
    st=set();
    # O(n1(logn))
    for i in range(len(a1)):
        st.add(a1[i]);
    # O(n2(logn))
    for j in range(len(a2)):
        st.add(a2[i]);

    # O(n1+n2)
    for se in st:
        print(se,end=" ")



unionofset()