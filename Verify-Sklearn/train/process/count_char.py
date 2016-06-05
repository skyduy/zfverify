kv_dict = {}
with open('../answer.txt') as f:
    for value in f:
        value = value.strip()
        for i in value:
            kv_dict.setdefault(i, 0)
            kv_dict[i] += 1
print kv_dict.keys()
print len(kv_dict)
# with open('C:\\Users\\skyduy\\PycharmProjects\\keras_recon\\answer.csv', 'wb') as f:
#     for k, v in kv_dict.iteritems():
#         f.write('%s,%s\n' % (k, v))

