# editing this thing using my ipad pro now. sweet

from ipaddress import IPv4Address, IPv4Network

ifile = open('all_networks.txt');
ifile = list(ifile) # inner and outer loop can't read the same file at same time... transform to a list

# todo - pop out of the list any items that were already discovered to avoid duplicity. 

count_check = 0
count_dup = 0
count_line = 0

def innetwork(net1_ipmask,net2_ipmask): #netmask equals net/mask in unicode
    #net1_ip = net1_ipmask[0] # necessary for rule below.
    #result = ipaddress.ip_address() in ipaddress.ip_network(net2_ipmask) # checks for hosts contained in networks. Doesn't perform network overlap per say but only if hosts are included in one of the networks on the list.
    result = IPv4Network(net1_ip).overlaps(IPv4Network(net2_ipmask)) # checks for network overlap.. both ways so output will contain 2 results per match

    return result

for line in ifile:
    line = line.split(",")
    net1_ip = str(line[0]).strip().decode('utf8')
    net1_mask = str(line[1]).strip().decode('utf8')
    net1_ipmask = net1_ip + "/" + net1_mask
    count_line = count_line + 1
    for line_parse in ifile:
        line_parse = line_parse.split(",")
        net2_ip = str(line_parse[0]).strip().decode('utf8')
        net2_mask = str(line_parse[1]).strip().decode('utf8')
        if net1_ip == net2_ip : continue # prevents the loop from catching the ip being evaluated.
        net2_ipmask = net2_ip + "/" + net2_mask
        dup = innetwork(net1_ipmask,net2_ipmask)
        count_check = count_check + 1
        if dup == True:
            print "We have a dup!", "network or address", net1_ipmask, "overlaps", net2_ipmask, "at line:", count_line
            count_dup = count_dup + 1
        else:
            continue

print "total number of records is:", count_line
print "number of records checked", count_check
print "number of duplicates found", count_dup
