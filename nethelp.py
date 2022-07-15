#!/usr/bin/env python3

import sys
from utility import *

mode = sys.argv[1]


if mode == "net":
    inp = sys.argv[2].split("/")
    ip = ip_to_array(inp[0])
    mask = mask_to_ip(int(inp[1]))
    find_net_ip(ip, mask)

if mode == "htype":
    inp = sys.argv[2].split("/")
    ip = ip_to_array(inp[0])
    mask = mask_to_ip(int(inp[1]))
    find_hosttype(ip, mask)

if mode == "subnet":
    inp = sys.argv[2].split("/")
    ip = ip_to_array(inp[0])
    mask = mask_to_ip(int(inp[1]))
    subnet(ip, mask, "non c'è")

if mode == "valid":
    inp = sys.argv[2].split("/")
    ip = ip_to_array(inp[0])
    mask = mask_to_ip(int(inp[1]))
    valid(ip, mask)