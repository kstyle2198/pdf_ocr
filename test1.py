# #importing re model
# import re

# #define input string
# # sample_string = "2022년 1/4분기 노사협의회 협의 @#결과"
# sample_string = "The Problem Seeker@10"

# #print input sample string 
# print("Original String:", sample_string)

# # using regex expression
# final_string = re.sub('[^A-Za-z0-9]+', '', sample_string)
 
# # print final sample string    
# print("Final String:",sample_string)


import time



t1 = time.strftime('%Y%m%d_%I%M%S%p', time.localtime())
print(t1)
print(type(t1))