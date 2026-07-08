# set is unchangeable, not allows duplicate members

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies));

# set is unchangeable
print(it_companies.add("twitter"));
print(it_companies);

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["oracle","zoho"]);

print(it_companies);

# Remove one of the companies from the set it_companies
it_companies.remove("Google");
print(it_companies)

# Join A and B
print(A.union(B));

# Find A intersection B
print(A.intersection(B));