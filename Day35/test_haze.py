import pytest





# sort this thing by the 1st element in each inner list and return a list that contains the 2nd elements from each inner list (sorted by 1st)



def test_new_list():
    expected_result = ["zebra", "apple", "banana", "candy"]
    subject = [ [2,'apple'], [4,'banana'], [5,'candy'], [1,'zebra'] ]

    result = [ a[1] for a in sorted(subject) ]
    assert result == expected_result

    result = [ a[1] for a in sorted(subject, key=lambda x: x[0]) ]
    assert result == expected_result

    # result = list(zip(*sorted(subject, key=lambda x:x[1])))[1]
    result = list(list(zip(*sorted(subject, key=lambda x:x[0])))[1])
    assert result == expected_result


def test_list_of_lists():
    list_of_lists = [ [1,2], [1,3], [1,4], [1,5] ]
    expected_results = [2,3,4,5]

    # Reason: avoiding using a named variable in the loop that you only need temporarily
    result = [ a for a in map( (lambda a: a[1]), list_of_lists) ]
    assert result == expected_results

    result = [ a[1] for a in list_of_lists ]
    assert result == expected_results
