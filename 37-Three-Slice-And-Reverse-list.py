sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = []
chunk2 = []
chunk3 = []

for i in range(len(sample_list)):
    if i >= 0 and i <= 2:
        chunk1.append(sample_list[i])
    elif i >= 3 and i <= 5:
        chunk2.append(sample_list[i])
    else:
        chunk3.append(sample_list[i])

print("Chunk 1", chunk1)
chunk1.reverse()
print("After Reverse ", chunk1)

print("Chunk 2", chunk2)
chunk2.reverse()
print("After Reverse ", chunk2)

print("Chunk 3", chunk3)
chunk3.reverse()
print("After Reverse ", chunk3)
