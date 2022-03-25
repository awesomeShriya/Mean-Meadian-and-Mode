from collections import Counter
import csv
def get_mean(total_weight, total_entries):
    mean=total_weight/total_entries
    print(f"mean is {mean:2f}")

def get_median(total_entries,sorted_data):
    if total_entries % 2==0:
        median1=float(sorted_data[total_entries//2])
        median2=float(sorted_data[total_entires//2-1])
        median=(median1+median2)/2
    else:
        median=float(sorted_data[total_entries//2])
    print (f"median is {median:2f}")