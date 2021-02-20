import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_1 import Case1, Case2, Case3, Case4


if __name__ == '__main__':
    Case1.make_dateset()
    Case2.make_dateset()
    Case3.make_dateset()
    Case4.make_dateset()

    data = Case1.objects.filter(c="c-1").explain()
    with open('data_1.json', 'w') as fp:
        json.dump(data, fp, indent=4)
    
    data = Case2.objects.filter(c="c-1").explain()
    with open('data_2.json', 'w') as fp:
        json.dump(data, fp, indent=4)
    
    data = Case3.objects.filter(c="c-1").explain()
    with open('data_3.json', 'w') as fp:
        json.dump(data, fp, indent=4)
    
    data = Case4.objects.filter(c="c-1").explain()
    with open('data_4.json', 'w') as fp:
        json.dump(data, fp, indent=4)
