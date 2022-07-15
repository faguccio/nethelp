# Nethelp

This is a tool to solve easy networking exercise. It has just 4 modes, but it's very easy to adapt to your own need.

## Use

```
./nethelp mode [arguments]
```

### Modes

- `./nethelp net 112.25.98.56/32`
    - Return the network ip of the subnet
    - shows ip in binary, mask ip in binary and result both in binary and int

- `./nethelp htype 112.25.98.56/32`
    - Return first, last router and broadcast of net

- `./nethelp subnet 112.25.98.56/32`
    - does the subnet

- `./nethelp valid 112.25.98.56/32`
    - same as htype, but also tells the number of this host (it may not be an host)

### Why chose this over `networking_kit`

This project is very similiar to [this other project](https://github.com/giammirove/networking_kit.git), so why you should choose me over him :sad: ???

1. It shows the whole process
    - converts the ip in binary
    - does the bitwise or
2. It's written in python :snake:
    - why should you use javascript? It's ugly and difficult to read. Use python instead!

I have to admit that [network_kit](https://github.com/giammirove/networking_kit.git) has many more functionality, it's better calibrated to solve the exercise of the esams [of this course](https://github.com/csunibo/reti-di-calcolatori). 

**chose wisely**