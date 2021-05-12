import pretty_midi
import pandas as pd

df = pd.read_csv('note_numbers.csv', index_col=False,header=None)
note_numbers=list(df[0])

#リストの中の最高音，最低音，サイズを取得
h=max(note_numbers)
l=min(note_numbers)
length=len(note_numbers)

h0=108
l0=36

adjusted_note_numbers=[int((n-l)*(h0-l0)/(h-l)+l0) for n in note_numbers]
print(adjusted_note_numbers)
print(max(adjusted_note_numbers))
print(min(adjusted_note_numbers))

# Pretty MIDIオブジェクトを作成
melody = pretty_midi.PrettyMIDI()

# Acostic Grand Pianoに対応するプログラム番号を返す
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
#Instrument Instanceを作成
piano = pretty_midi.Instrument(program=piano_program)

#取得したnote_numberのlistを表示
#print(note_numbers)





count=0.0
for note_number in adjusted_note_numbers:

    #"C5"などのnote_nameを入れると対応するnote_numberを返す。今回は使わないけど一応残しておく。
    #note_number = pretty_midi.note_name_to_number(note_name)

    # NoteInstanceを作成。音(pitch)の開始時間と終了時間、velocityを定義
    note = pretty_midi.Note(
        velocity=100, pitch=note_number, start=count*0.1, end=(count+1)*0.1)

    # Add it to our piano instrument
    # 上記で作成したNoteInstanceをPiano Instrumentに加えます。
    piano.notes.append(note)

    count=count+1


# Piano InstrumentをPretty MIDIオブジェクトにAppend
melody.instruments.append(piano)


# Write out the MIDI data
# PrettyMIDIオブジェクトをMIDIファイルとして書き出しましょう。
melody.write('melody.mid')
