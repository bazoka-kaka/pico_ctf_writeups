# Shop

## Problem

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 11371.

## Solution

Here's the first display when we run the program

```
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
```

first, we enter an item we can buy with our current money. When we enter the quantity of the item as negative, our money adds up. Do this until the money is sufficient to buy our flag

```
Choose an option: 
0
How many do you want to buy?
-2
You have 60 coins
        Item            Price   Count
(0) Quiet Quiches       10      14
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
0
How many do you want to buy?
-4
You have 100 coins
```

When we buy our flag:

```
        Item            Price   Count
(0) Quiet Quiches       10      18
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 56 100 55 50 55 49 102 125]
```

we get the encoded flag, we have to decode it using python

inside flag.txt:

```
112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 56 100 55 50 55 49 102 125
```

inside sol.py:

```py
#!/usr/bin/env python3

f = open("flag.txt")

flag = "".join([chr(int(x)) for x in f.read().split(' ')])

print(flag)

f.close()
```

FLAG: `picoCTF{b4d_brogrammer_b8d7271f}`