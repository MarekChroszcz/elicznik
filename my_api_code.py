import datetime
import elicznik

with elicznik.ELicznik("chroszcz.marek@gmail.com", "sf3^^@2SDcyd") as m:
    # date range
    #print("July 2021")

    readings = m.get_readings(datetime.date(2024, 6, 1), datetime.date(2024, 6, 17))

    for timestamp, consumed, produced, consumed_net, produced_net in readings:
        print(timestamp, consumed, produced, consumed_net, produced_net)

    # single day
    #print("Yesterday")

    #yesterday = datetime.date.today() - datetime.timedelta(days=1)
   # readings = m.get_readings(yesterday)

    #for timestamp, consumed, produced, consumed_net, produced_net in readings:
      #  print(timestamp, consumed, produced, consumed_net, produced_net)