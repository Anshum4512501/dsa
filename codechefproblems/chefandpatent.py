"""
Dr. Chef is treating COVID-19 patients. There is a queue of N patients (numbered from patient 1 at the front of the queue to patient N at the back) outside his clinic. You, his assistant, found out that for each valid i, the i-th patient has an illness level Ai.

Chef treats patients based on their health, i.e. a patient with a higher illness level is always treated before any patients with a lower illness level. Chef is also fair, so he treats patients with an equal illness level based on their position in the queue, i.e. a patient ahead in the queue is always treated before a patient with the same illness level that is further behind in the queue.

The first patient to be treated has to wait an hour for Chef to set up his equipment. Treating each patient also takes an hour, and Chef always starts treating the next patient as soon as he is done with the current one.

The patients are a bit impatient. As Chef's assistant, for each patient, find out how long (in hours) this patient needs to wait before Chef starts treating this patient.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers A1,A2,…,AN.
Output
For each test case, print a single line containing N space-separated integers. For each valid i, the i-th of these integers should be the time the i-th patient needs to wait.

Constraints
1≤T≤5
1≤N≤105
1≤Ai≤1,000 for each valid i
Example Input
4
5
2 3 5 3 4
3
2 2 2
6
2 10 3 3 2 10
4
8 9 8 9
Example Output
5 3 1 4 2
1 2 3
5 1 3 4 6 2
3 1 4 2
"""
from copy import deepcopy
import time
def _find_nextmax(arr):
    index_of_max = arr.index(max(arr))
    max_element = arr.pop(index_of_max)
    return max_element

def find_index_of_max_element(list_of_enumerated_entries,max_element):
    
    for index,entry in list_of_enumerated_entries:
        if  entry == max_element:
            # print(list_of_enumerated_entries,index,entry)
            list_of_enumerated_entries.remove((index,entry))
            return index   

def find_totaltime(int_array,n):
    another_arr = deepcopy(int_array)
    result = [None]*n
    total_time = 1
    list_of_enumerated_entries  = list(enumerate(int_array))
    while list_of_enumerated_entries:
        max_element = _find_nextmax(another_arr)
        index = find_index_of_max_element(list_of_enumerated_entries,max_element)
        result[index] = total_time
        total_time = total_time + 1 
        
    string = [str(n) for n in result]
    final_string = " ".join(string)
    print(final_string)
start =time.perf_counter()
find_totaltime([2,3,5,3,4],5)   
find_totaltime([8,9,8,9],4)
find_totaltime([2,10,3,3,2,10],6)
endtime = time.perf_counter() - start

print(endtime)


