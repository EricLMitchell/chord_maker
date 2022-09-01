notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
normal_keys = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
flat_keys = ['F', 'Bb', 'Eb', 'Ab']
special_sharp_keys = ['G#', 'D#', 'A#']
special_flat_keys = ['Cb', 'Gb', 'Db']

# use alphabet instead of notes for building the chords

use_enharmonics = False
lower_notes = False
raise_notes = False

bass = str(input('What is the bass note of the chord?\n\t')).strip()


def enharmonize(note):
    if note == notes[1]:
        note = 'Bb'
    elif note == notes[2]:
        note = 'Cb'
    elif note == notes[3]:
        note = 'B#'
    elif note == notes[4]:
        note = 'Db'
    elif note == notes[6]:
        note == 'Eb'
    elif note == notes[7]:
        note == 'Fb'
    elif note == notes[8]:
        note == 'E#'
    elif note == notes[9]:
        note == 'Gb'
    elif note == notes[11]:
        note == 'Ab'
    return note


if bass in normal_keys:
    pass
elif bass in flat_keys:
    bass = enharmonize(bass)
    use_enharmonics = True
elif bass in special_flat_keys:
    use_harmonics = True
    lower_notes = True
    bass = bass[0]
elif bass in special_sharp_keys:
    raise_notes = True
    bass = bass[0]

for i in range(len(notes)):
    if bass == notes[i] or bass == enharmonize(notes[i]):
        bass_index = i
        # print(bass_index)
        break

major = []
dominant = []
minor = []
half_diminished = []
diminished = []

MAJOR_THIRD = 4  # a major third is 4 half steps above the bass

MAJOR_SEVENTH = 11
MINOR_SEVENTH = 10
DIMINISHED_SEVENTH = 9


def steps_to_index(root, steps) -> int:
    root_index = int(root)
    half_steps = int(steps)
    new_pos = root_index + half_steps
    if new_pos > 11:
        distance = new_pos - 12
        new_pos = distance
    return int(new_pos)


def raise_note(note):
    if note[-1] == 'b':
        note = note[0]
    elif note[-1] == '#':
        note = note[0] + 'x'
    else:
        note = note + '#'
    return note


def lower_note(note):
    if note[-1] == '#':
        note = note[0]
    else:
        note = note + 'b'
    return note


major_third_index = steps_to_index(bass_index, MAJOR_THIRD)

fifth_index = steps_to_index(bass_index, FIFTH)

major_seventh_index = steps_to_index(bass_index, MAJOR_SEVENTH)

major.append(bass)
major.append(notes[major_third_index])
major.append(notes[fifth_index])
major.append(notes[major_seventh_index])

if use_enharmonics:
    for i in range(len(major)):
        major[i] = enharmonize(major[i])

if raise_notes:
    print(len(major))
    for i in range(len(major)):
        major[i] = raise_note(major[i])
elif lower_notes:
    for i in range(len(major)):
        major[i] = lower_note(major[i])

print('MM7: {0}  {1}  {2}  {3}'.format(major[0], major[1], major[2], major[3]))
