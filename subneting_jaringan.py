# Percobaan Subnetting Jaringan 
import ipaddress

def subnet_calculator():
    ip_address = input("Masukkan alamat IP: ")
    subnet_class = input("Masukkan kelas subnet (A/B/C): ")
    subnet_bits = int(input("Masukkan jumlah bit subnet: "))

    if subnet_class == 'A':
        subnet_mask = '255.0.0.0'
    elif subnet_class == 'B':
        subnet_mask = '255.255.0.0'
    elif subnet_class == 'C':
        subnet_mask = '255.255.255.0'
    else:
        print("Kelas subnet tidak valid.")
        return

    network = ipaddress.IPv4Network(ip_address+'/'+str(subnet_bits), strict=False)  
    print("\nInformasi Subnet:")
    print("IP Network:", network.network_address)
    print("IP Broadcast:", network.broadcast_address)
    print("IP Host Range:", network.network_address + 1, "-", network.broadcast_address - 1)
    print("Subnet Mask:", subnet_mask)
    print("Jumlah Blok Subnet:", 2**(32-subnet_bits))

subnet_calculator()