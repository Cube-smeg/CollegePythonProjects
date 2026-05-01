#Get inputs for each layer:
application_input = input("Enter the application data: ")
transport_input = input("Enter the Source aswell as the port number for destination: ")
internet_input = input("Enter source aswell as destination IP")
network_input = input("Enter the destination MAC address: ")

#Create final packet:
final_packet = application_input + internet_input + network_input + transport_input
print(final_packet)