weight = 22
cost = 0
total_cost = 0
cost_ground_premium  = 125

#print("Ground Shipping Premium $", cost_ground_premium)

#Ground Shipping
if weight <= 2:
  flat_charge = 20
  cost = 1.5
  total_cost = cost * weight + flat_charge
elif weight > 2 and weight <= 6:
  flat_charge = 20
  cost = 3.0
  total_cost = cost * weight + flat_charge
elif weight > 6 and weight <= 10:
  flat_charge = 20
  cost = 4.0
  total_cost = cost * weight + flat_charge
elif weight > 10:
  flat_charge = 20
  cost = 4.75
  total_cost = cost * weight + flat_charge
else:
  print("Set up the weight")

#drone shipping
if weight <= 2:
  cost = 4.5
  total_cost_drone = cost * weight
elif weight > 2 and weight <= 6:
  cost = 9.0
  total_cost_drone = cost * weight
elif weight > 6 and weight <= 10:
  cost = 12.0
  total_cost_drone = cost * weight
elif weight > 10:
  cost = 14.25
  total_cost_drone = cost * weight
else:
  print("Set up the weight")

if (total_cost < total_cost_drone) and (total_cost < cost_ground_premium):
  print("Shipping: Ground")
  print(total_cost)
elif (total_cost_drone < total_cost) and (total_cost_drone < cost_ground_premium):
  print("Shipping: Drone")
  print(total_cost_drone)
else:
  print("Shipping: Premium")
  print(cost_ground_premium)



