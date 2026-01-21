nums = [3, 10, 7, 14, 9, 20]

for n in nums:
    if n % 2 == 0:
        print(n)


nums = [5, 12, 3, 25, 8, 30]
count = 0

for n in nums:
    if n > 10:
        count += 1

print("Count:", count)


text = "machine"
rev = ""

for ch in text:
    rev = ch + rev

print(rev)


arr = [9, 2, 15, 4]
min_val = arr[0]

for n in arr:
    if n < min_val:
        min_val = n

print("Min:", min_val)
