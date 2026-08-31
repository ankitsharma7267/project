
print('=============PARKING SLOTS ISSUE=============')


parking_slots = [0, 0, 1, 0, 1, 0, 0, 0, 1, 0]

for i in range(len(parking_slots)):
  
  if parking_slots[i] == 0:
    print('Empty slots', i )

  else:
    print('occupied slot', i )


slot = int(input('Enter the slot no.:'))

if parking_slots[slot] == 0:
  parking_slots[slot] = 1
  print('Car has been parked in parking area')


slot = int(input('Enter the slot no.:'))

if parking_slots[slot] == 1:
  parking_slots[slot] = 0
  print('Car has been Removed from the parking slot')



first_hour = 50
Extra_charge = 20

if first_hour <= 1:
  print('parking fee for 1 hour is:', first_hour)

else:
  total_charge = first_hour + Extra_charge
  print('Total parking charge is:', total_charge)


print('Parking Slots :', parking_slots)