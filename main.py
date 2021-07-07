notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

bass = str(input('What is the bass note of the chord?\n\t'))


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



for i in range(len(notes)):
    if bass == notes[i]:
        bass_index = i
    if bass == enharmonize(notes[i]):
        bass_index = i

major = []
dominant = []
minor = []
half_diminished = []
diminished = []

MAJOR_THIRD = 4  # a major third is 4 half steps above the bass
MINOR_THIRD = 3  # a minor third is 3 half steps above the bass

MAJOR_SEVENTH = 11
MINOR_SEVENTH = 10
DIMINISHED_SEVENTH = 9


def steps_to_index(root, steps) -> int:
    root_index = int(root)
    half_steps = int(steps)
    new_pos = root_index + half_steps
    # print(new_pos)
    if new_pos > 11:
        distance = new_pos - 12
        # print(distance)
        new_pos = distance
    return int(new_pos)


def check_note(bass_note, other_note):
    for j in range(len(alphabet)):
        if str(alphabet[j]) == str(bass_note):
            bass_loc = j
        if str(alphabet[j]) == str(other_note):
            other_loc = j

    count = 0

    if other_loc < bass_loc:
        bass_loc = abs()


def raise_note(note):
    if note[1] == 'b':
        note = note[0]
    else:
        note = note + '#'


def lower_note(note):
    pass


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


# Calculate indexes for use later
minor_third_index = steps_to_index(bass_index, MINOR_THIRD)
major_third_index = steps_to_index(bass_index, MAJOR_THIRD)

diminished_fifth_index = steps_to_index(minor_third_index, MINOR_THIRD)
fifth_index = steps_to_index(major_third_index, MINOR_THIRD)

diminished_seventh_index = steps_to_index(bass_index, DIMINISHED_SEVENTH)
minor_seventh_index = steps_to_index(bass_index, MINOR_SEVENTH)
major_seventh_index = steps_to_index(bass_index, MAJOR_SEVENTH)

# major seventh chord
major.append(notes[bass_index])

major.append(notes[major_third_index])

major.append(notes[fifth_index])

major.append(notes[major_seventh_index])

print('MM7: {0}  {1}  {2}  {3}'.format(major[0], major[1], major[2], major[3]))
# end major seventh code


# dominant seventh chord
dominant.append(notes[bass_index])

# indexes are the same as the one above for the triad
dominant.append(notes[major_third_index])

dominant.append(notes[fifth_index])

# dominant sevenths have a minor seventh
dominant.append(notes[minor_seventh_index])

print('Mm7: {0}  {1}  {2}  {3}'.format(dominant[0], dominant[1], dominant[2], dominant[3]))
# end dominant seventh code


# minor seventh chord
minor.append(notes[bass_index])

minor.append(notes[minor_third_index])

minor.append(notes[fifth_index])

minor.append(notes[minor_seventh_index])

print('mm7: {0}  {1}  {2}  {3}'.format(minor[0], minor[1], minor[2], minor[3]))
# end minor seventh code


# half_diminished seventh chord
half_diminished.append(notes[bass_index])

half_diminished.append(notes[minor_third_index])

half_diminished.append(notes[diminished_fifth_index])

half_diminished.append(notes[minor_seventh_index])

print('/°7: {0}  {1}  {2}  {3}'.format(half_diminished[0], half_diminished[1], half_diminished[2], half_diminished[3]))
# end half diminished code


# diminished seventh chord
diminished.append(notes[bass_index])

diminished.append(notes[minor_third_index])

diminished.append(notes[diminished_fifth_index])

diminished.append(notes[diminished_seventh_index])

print('°7: {0}  {1}  {2}  {3}'.format(diminished[0], diminished[1], diminished[2], diminished[3]))
# end diminished seventh code
