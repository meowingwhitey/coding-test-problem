def solution(m, musicinfos):
    answer = ''
    m = m.replace("C#", "1")
    m = m.replace("D#", "2")
    m = m.replace("F#", "3")
    m = m.replace("G#", "4")
    m = m.replace("A#", "5")
    musiclist = list()
    temp = [];
    search = [];
    max_duration  = 0
    note_str = ''
    for i in musicinfos:
        notes = []
        temp = i.split(',')
        start_time = int(temp[0][0:2])*60+int(temp[0][3:5])
        end_time = int(temp[1][0:2])*60+int(temp[1][3:5])
        duration  = end_time - start_time
        temp[3] = temp[3].replace("C#", "1")
        temp[3] = temp[3].replace("D#", "2")
        temp[3] = temp[3].replace("F#", "3")
        temp[3] = temp[3].replace("G#", "4")
        temp[3] = temp[3].replace("A#", "5")
        for j in range(duration):
            notes.append(temp[3][j%len(temp[3])])
        title = temp[2]
        note_str = ''.join(notes)
        note_str = note_str.replace("C#", "1")
        note_str = note_str.replace("D#", "2")
        note_str = note_str.replace("F#", "3")
        note_str = note_str.replace("G#", "4")
        note_str = note_str.replace("A#", "5")
        musiclist.append([start_time, end_time ,duration, title, note_str])
        if m in note_str:
            if duration > max_duration:
                max_duration = duration
                answer = title
    if not answer:
        answer = '(None)'
        
    return answer
