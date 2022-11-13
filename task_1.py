from pprint import pprint

# result = []
#
# for i in range(16):
#     temp_dict = dict()
#     temp_dict['dec'] = i
#     temp_dict['bin'] = bin(i)
#     temp_dict['oct'] = oct(i)
#     temp_dict['hex'] = hex(i)
#     if temp_dict not in result:
#         result.append(temp_dict)
#
# pprint(result)

# -----------------------------------
result = [{'dec': i, 'bin': bin(i), 'oct': oct(i), 'hex': hex(i)} for i in range(16)]
pprint(result)