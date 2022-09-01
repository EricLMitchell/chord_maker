running = True
while running:
    notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    order_of_sharps = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
    sharp_keys = ['G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#']
    sharps_dict = {'G': 1, 'D': 2, 'A': 3, 'E': 4, 'B': 5, 'F#': 6, 'C#': 7, 'G#': 8, 'D#': 9, 'A#': 10}
    is_sharp = False

    order_of_flats = ['B', 'E', 'A', 'D', 'G', 'C', 'F']
    flat_keys = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
    flats_dict = {'F': 1, 'Bb': 2, 'Eb': 3, 'Ab': 4, 'Db': 5, 'Gb': 6, 'Cb': 7}
    is_flat = False

    bass = str(input('Please enter the bass note of the chord: \n\t\t'))

    if bass == 'C':
        num_of_acc = 0
    if bass in sharp_keys:
        is_sharp = True
        num_of_acc = sharps_dict.get(bass)
    if bass in flat_keys:
        is_flat = True
        num_of_acc = flats_dict.get(bass)


    def raise_note(note):
        if note[-1] == '#':
            note = note[0] + 'x'
        else:
            note = note + '#'
        return note


    def lower_note(note):
        if note[-1] == 'x':
            note = note[0] + '#'
        elif note[-1] == '#':
            note = note[0]
        else:
            note = note + 'b'
        return note


    def change_notes(num, is_sharp):
        new_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        sharp_order = ['F', 'C', 'G', 'D', 'A', 'E', 'B']
        flat_order = ['B', 'E', 'A', 'D', 'G', 'C', 'F']

        if is_sharp:
            order = sharp_order
        else:
            order = flat_order

        for i in range(0, num):
            if i > 6:
                i = i - 7
            if is_sharp:
                order[i] = raise_note(order[i])
            else:
                order[i] = lower_note(order[i])

        for i in range(len(new_notes)):
            for j in range(len(order)):
                if str(new_notes[i])[0] == str(order[j])[0]:
                    new_notes[i] = order[j]

        return new_notes


    if num_of_acc > 0:
        notes = change_notes(num_of_acc, is_sharp)


    def make_major_seventh(bass_note):
        for i in range(len(notes)):
            if notes[i] == bass_note:
                bass_loc = i

        third_loc = bass_loc + 2
        if third_loc > 6:
            third_loc = third_loc - 7

        fifth_loc = bass_loc + 4
        if fifth_loc > 6:
            fifth_loc = fifth_loc - 7

        seventh_loc = bass_loc + 6
        if seventh_loc > 6:
            seventh_loc = seventh_loc - 7

        m_seventh = [notes[bass_loc], notes[third_loc], notes[fifth_loc], notes[seventh_loc]]
        return m_seventh


    major_seventh_chord = make_major_seventh(bass)
    root = major_seventh_chord[0]
    major_third = major_seventh_chord[1]
    perfect_fifth = major_seventh_chord[2]
    major_seventh = major_seventh_chord[3]

    print(f'MM7: {root} {major_third} {perfect_fifth} {major_seventh}')

    minor_seventh = lower_note(major_seventh)
    print(f'dom: {root} {major_third} {perfect_fifth} {minor_seventh}')

    minor_third = lower_note(major_third)
    print(f'mm7: {root} {minor_third} {perfect_fifth} {minor_seventh}')

    diminished_fifth = lower_note(perfect_fifth)
    print(f'ø7: {root} {minor_third} {diminished_fifth} {minor_seventh}')

    diminished_seventh = lower_note(minor_seventh)
    print(f'º7: {root} {minor_third} {diminished_fifth} {diminished_seventh}')

    print()

