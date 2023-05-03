from datetime import date, timedelta, datetime

def gen_dates_times(week_offset=0, times_matrix=None):
    if times_matrix is None:
        print("Please provide times_matrix argument")
        return
    
    today = date.today()

    # First figure out the week_offset's "Monday" information
    current_monday = today - timedelta(days=today.weekday())
    target_monday = current_monday + timedelta(days=(week_offset * 7))
    
    # Now we have the target Monday date, format the strings
    result = ""
    if times_matrix['Monday'][0] != "":
        result += "Monday\t"
        result += target_monday.strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Monday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Monday'][1], "%H:%M").strftime("%I:%M %p")

        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Monday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Tuesday\t"
            result += (target_monday+timedelta(days=1)).strftime("%d %b")
            result += ")"

        result += "\n"

    if times_matrix['Tuesday'][0] != "":
        result += "Tuesday\t"
        result += (target_monday+timedelta(days=1)).strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Tuesday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Tuesday'][1], "%H:%M").strftime("%I:%M %p")

        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Tuesday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Wednesday\t"
            result += (target_monday+timedelta(days=2)).strftime("%d %b")
            result += ")"

        result += "\n"

    if times_matrix['Wednesday'][0] != "":
        result += "Wednesday\t"
        result += (target_monday+timedelta(days=2)).strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Wednesday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Wednesday'][1], "%H:%M").strftime("%I:%M %p")

        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Wednesday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Thursday\t"
            result += (target_monday+timedelta(days=3)).strftime("%d %b")
            result += ")"

        result += "\n"

    if times_matrix['Thursday'][0] != "":
        result += "Thursday\t"
        result += (target_monday+timedelta(days=3)).strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Thursday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Thursday'][1], "%H:%M").strftime("%I:%M %p")

        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Thursday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Friday\t"
            result += (target_monday+timedelta(days=4)).strftime("%d %b")
            result += ")"

        result += "\n"

    if times_matrix['Friday'][0] != "":
        result += "Friday\t"
        result += (target_monday+timedelta(days=4)).strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Friday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Friday'][1], "%H:%M").strftime("%I:%M %p")
        
        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Friday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Saturday\t"
            result += (target_monday+timedelta(days=5)).strftime("%d %b")
            result += ")"

        result += "\n"

    if times_matrix['Saturday'][0] != "":
        result += "Saturday\t"
        result += (target_monday+timedelta(days=5)).strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Saturday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Saturday'][1], "%H:%M").strftime("%I:%M %p")

        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Saturday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Sunday\t"
            result += (target_monday+timedelta(days=6)).strftime("%d %b")
            result += ")"
        
        result += "\n"

    if times_matrix['Sunday'][0] != "":
        result += "Sunday\t"
        result += (target_monday+timedelta(days=6)).strftime("%d %b")
        result += " | "
        result += datetime.strptime(times_matrix['Sunday'][0], "%H:%M").strftime("%I:%M %p")
        result += " - "
        result += datetime.strptime(times_matrix['Sunday'][1], "%H:%M").strftime("%I:%M %p")

        # Check if the finish time is on the following day
        finish_time_meridiem = datetime.strptime(times_matrix['Sunday'][1], "%H:%M").strftime("%p").lower()

        if finish_time_meridiem == "am":
            result += " ("
            result += "Monday\t"
            result += (target_monday+timedelta(days=7)).strftime("%d %b")
            result += ")"

        result += "\n"

    result = result.rstrip("\n")
    return result

def format_result(result):
    if len(result) == 0 or result == None:
        print('Result should not be None or empty string')
        return None

    lines = result.split("\n")

    # Find position of "|" character
    ref_char_index = lines[0].index("|")
    for l in lines:
        if l.index("|") > ref_char_index:
            ref_char_index = l.index("|")

    # Add the spaces to the lines
    f_result = ""
    for l in lines:
        f_result += ' '.join(l.split()[:3])
        f_result += ' ' * (ref_char_index - len(' '.join(l.split()[:3])))
        f_result += ' '.join(l.split()[3:])
        f_result += '\n'

    f_result = f_result.rstrip("\n")
    return f_result
