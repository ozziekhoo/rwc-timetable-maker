from roster_generator import gen_dates_times, format_result, gen_dates_times_helper

t = { "Monday" : ["06:00", "14:30"],
      "Tuesday" : ["06:00", "14:30"],
      "Wednesday" : ["19:00", "00:00"],
      "Thursday" : ["", ""],
      "Friday" : ["", ""],
      "Saturday" : ["06:00", "16:00"],
      "Sunday" : ["", ""],
}

t = { "Monday" : ["19:00", "00:00"],
      "Tuesday" : ["19:00", "00:00"],
      "Wednesday" : ["19:00", "00:00"],
      "Thursday" : ["19:00", "00:00"],
      "Friday" : ["19:00", "00:00"],
      "Saturday" : ["19:00", "00:00"],
      "Sunday" : ["19:00", "00:00"],
}

print(format_result(gen_dates_times(1, t)))
