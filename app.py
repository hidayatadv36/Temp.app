normal_temp=99
high_temp=100
very_high_temp=103

temp=106

if temp<=normal_temp:
    print("temp is normal")
elif temp>=very_high_temp:
    print("temp is extremely high")
elif temp>=high_temp:
    print("temp is high")
else:
    print("warning")
