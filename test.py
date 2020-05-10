import batterytender

email = 'XXXXXXXXXXXXXXXXXXXX'
password = 'XXXXXXXXXXXXXXXXXXXX'

bt = batterytender.BatteryTender(email, password)

for monitor in bt.monitors:
    print('Monitor id: {}'.format(monitor.device_id))
    print('    Name: {}'.format(monitor.name))
    print('    Location: {}'.format(monitor.location))
    print('    Date: {}'.format(monitor.date))
    print('    Updated: {}'.format(monitor.updated))
    print('    Voltage: {}'.format(monitor.voltage))
    print('    SOC: {}'.format(monitor.soc))

