# import collections

# count = collections.Counter()
# count1 = collections.Counter()

# with open("app.log") as f:
#     for line in f:
#         parts = line.split()
#         ip = parts[4]
#         count[ip] += 1
#         if "ERROR" in line:
#             er=parts[5:]
#             error= " ".join(er)
#             count1[error] +=1

# print(count)
# print(count1.most_common(1))

# import collections
# import re
# count = collections.Counter()
# count1 = collections.Counter()
# pattern=(r"(?P<date>\S+)\s+" r"(?P<time>\S+)\s+" r"(?P<type>\S+)\s+" r"(?P<name>\S+)\s+" r"(?P<ip>\d+\.\d+\.\d+\.\d+)\s" r"(?P<message>.*)")
# with open("app.log") as f:
#     for row in f:
#         r=re.search(pattern,row)
#         ip=r.group('ip')
#         count[ip]+=1
#         if "ERROR" in row:
#             error=r.group('message')
#             count1[error]+=1
# print(count)
# print(count1.most_common(1))
