# a python pip(Prefferd installer programme)
# Numpy is the an powerfull n-dimensional array object

import numpy as np
lst=[1,2,3,4];
np_arr=np.array(lst);
print(np_arr*2)



import webbrowser
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]


# for url in url_lists:
#     webbrowser.open_new_tab(url);



import requests;
url = 'https://api.thecatapi.com/v1/breeds';
resp=requests.get(url);
print(resp)
print(resp.status_code)
print(resp.headers)
print(resp.id)
