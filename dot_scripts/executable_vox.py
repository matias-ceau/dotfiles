#! /usr/bin/python3

#DOC#@CLI@ "List Vox amp options"

import pandas as pd
from tabulate import tabulate
import sys


df = pd.DataFrame(
{'name': {0: 'CLEAN',
  1: 'CLEAN',
  2: 'CLEAN',
  3: 'CALI CLEAN',
  4: 'CALI CLEAN',
  5: 'CALI CLEAN',
  6: 'US BLUES',
  7: 'US BLUES',
  8: 'US BLUES',
  9: 'US 2x12',
  10: 'US 2x12',
  11: 'US 2x12',
  12: 'VOX AC15',
  13: 'VOX AC15',
  14: 'VOX AC15',
  15: 'VOX AC30',
  16: 'VOX AC30',
  17: 'VOX AC30',
  18: 'UK ROCK',
  19: 'UK ROCK',
  20: 'UK ROCK',
  21: 'UK METAL',
  22: 'UK METAL',
  23: 'UK METAL',
  24: 'US HIGH GAIN',
  25: 'US HIGH GAIN',
  26: 'US HIGH GAIN',
  27: 'US METAL',
  28: 'US METAL',
  29: 'US METAL',
  30: 'BOUTIQUE METAL',
  31: 'BOUTIQUE METAL',
  32: 'BOUTIQUE METAL'},
 'mode': {0: 'STD',
  1: 'SPL',
  2: 'CST',
  3: 'STD',
  4: 'SPL',
  5: 'CST',
  6: 'STD',
  7: 'SPL',
  8: 'CST',
  9: 'STD',
  10: 'SPL',
  11: 'CST',
  12: 'STD',
  13: 'SPL',
  14: 'CST',
  15: 'STD',
  16: 'SPL',
  17: 'CST',
  18: 'STD',
  19: 'SPL',
  20: 'CST',
  21: 'STD',
  22: 'SPL',
  23: 'CST',
  24: 'STD',
  25: 'SPL',
  26: 'CST',
  27: 'STD',
  28: 'SPL',
  29: 'CST',
  30: 'STD',
  31: 'SPL',
  32: 'CST'},
 'color': {0: 'g',
  1: 'o',
  2: 'r',
  3: 'g',
  4: 'o',
  5: 'r',
  6: 'g',
  7: 'o',
  8: 'r',
  9: 'g',
  10: 'o',
  11: 'r',
  12: 'g',
  13: 'o',
  14: 'r',
  15: 'g',
  16: 'o',
  17: 'r',
  18: 'g',
  19: 'o',
  20: 'r',
  21: 'g',
  22: 'o',
  23: 'r',
  24: 'g',
  25: 'o',
  26: 'r',
  27: 'g',
  28: 'o',
  29: 'r',
  30: 'g',
  31: 'o',
  32: 'r'},
 'amp_name': {0: '',
  1: '',
  2: '',
  3: 'Fender Pro 6G5-A Brownface',
  4: 'Fender 57 Custom Twin',
  5: '',
  6: '',
  7: '',
  8: '',
  9: '',
  10: '',
  11: '',
  12: '',
  13: '',
  14: '',
  15: '',
  16: '',
  17: '',
  18: '',
  19: '',
  20: '',
  21: '',
  22: '',
  23: '',
  24: '',
  25: '',
  26: '',
  27: '',
  28: '',
  29: '',
  30: '',
  31: '',
  32: ''},
 'description': {0: 'This models the clean channel of a high-quality amp that was produced only on special order, and was known as the overdrive special. With a beautifully rounded low range, a sharp midrange attack, and a sweet treble register, this is ideal for single coil pickups.',
  1: 'This models the clean channel of a Japanese-made amp with 2 x 12" speakers that went on sale in 1975. It is known for its clean full-range sound and its built-in stereo chorus, and is used on stages and in studios around the world.',
  2: 'This models is only a three-band tone control amplifier that produces a pure, clean tone. Setting TREBLE, MIDDLE, and BASS to the center will produce flat response of the pre amp. NOTE: If the input level is too high the sound may become distorted. To prevent this from happening reduce the gain in the preamp.',
  3: 'The 6G5-A “Pro” amp was produced during the years 1960–1963, and was distinctive for its yellowish brown vinyl cover and round brown knobs. This 40W combo amp is known for its warm and clean tone.',
  4: 'This American-made tweed-covered 2x12" combo amp made in 1957 is known for its rich and clean tone that’s ideal for classic rock, blues, and country. By raising the volume you can also produce a powerful and punchy overdrive sound.',
  5: 'This models an American-made black-paneled amp that has been modified. With this modification, an already-superb amp gains even greater smoothness and additional warmth.',
  6: 'This models a 4x10" combo amp from 1959 that was originally designed for bass guitar. Its smooth and crisp overdrive sound will respond sensitively to your picking dynamics and to the volume of your guitar.',
  7: 'This models the 22W Bruno Cowtipper Pro II 22 which owes its existence to a special friend of VOX, the custom amp designer Tony Bruno. It responds with extreme sensitivity to your playing touch, and its silky-sweet clean tone becomes a crunch sound rich in overtones when you turn up the volume.',
  8: 'This models a wood-finished 30W boutique amp head that costs more than $25,000. It delivers sparkling glassy clean tones. It also produces overdrive sounds that are startlingly sweet in a musical way when the gain is raised.',
  9: 'This models a black-faced 2x12" combo amp that has become an indispensible item for country and blues players. Its tight and clean sound provides deep piano-like bass tones, and will deliver the classic Chicago blues tone particularly when used with single coil pickups.',
  10: 'This models a beautiful 30W boutique amp head renowned for its peerless quality and true point-to-point wiring. Based on a concept similar to that of the VOX AC30, this amp is known for its rich overtones, sparkling clean tone, and great-sounding overdrive.',
  11: 'Based on a crunch-distortion amp, this original amp model changes the tone control to an active circuit that is more powerful than the conventional one, allowing a wide range of tones to be created. Raise the TREBLE for sparkling chords or lower it for a tasteful blues setting, or turn up the MIDDLE for a rock backing sound.',
  12: 'This models the AC15TB, which combines the beautifully sweet tonal character of the AC15’s low output power amp with the sound-creating flexibility of the AC30’s top boost channel.',
  13: 'This models channel 2 of the VOX AC15 (1x12", 15W), which was manufactured in 1962 and was a big hit for its compact cabinet, power, and great tone – along with then-popular British bands.',
  14: 'Designed to emulate the tones of the thick channel on the VOX Night Train Amplifier this tone is a modern take on the classic VOX pairing of 12AX7 preamp tubes and EL84 power tubes. Think Classic British Crunch.',
  15: 'This models an AC30 amp with a “top boost” circuit that was included as standard beginning in 1964. It delivers a smooth and refined top end, a majestically deep overdrive, and a  rich, brilliant clean sound.',
  16: 'Designed after our VOX Hand-wired Heritage AC30H2 this model provides the sparkle that is synonymous with the pairing of a classic VOX amplifier and the famed Celestion Alnico Blue.',
  17: 'This models the AC30BM Brian May signature model which faithfully reproduces every nuance of the legendary original AC30 from the 1950’s. This setting provides the screaming sound of the amp being overdriven with the treble booster turned on.',
  18: 'This 45W amp head was originally manufactured from 1962 to 1966, and was based on a tweed-covered bass amp. Its high-gain design was the beginning of the British amp tone revolution that continues to this day.',
  19: 'This models a UK-manufactured 100W single-channel head with master volume made in 1983. Turn the GAIN control all the way up to get the thick, snarling hard rock and heavy metal sound that dominated the 80’s.',
  20: 'This models the high treble channel of a hand-wired amp head made in England during the early 60’s. Raising the volume of this 50W output amp all the way produces the crunch that will forever be the sound of rock‘n’roll.',
  21: 'This models the high-gain channel of a modern 100W amp. While individual notes are clearly defined, it delivers a monster sound that’s quite aggressive and arrogant.',
  22: 'This models an English-made 100W amp head released in 2007 and boasting a four-channel design with powerful tone. We’ve used the “Overdrive 1” channel, which produces a tight low-end and transparent high-gain metal sound.',
  23: 'Based on a UK-made 100W head, this amp was created for a famous guitarist known for his amazing tone, slash rhythms, and fondness for silk hats. If you have a desire for the ultimate metal tones, this amp is the perfect choice.',
  24: 'This models a 100W boutique amp head manufactured in North Hollywood. This amp can be switched between power tube class AB or class A modes; the class AB mode used on the VT20+/VT40+ produces rich overtones and features a highly musical response.',
  25: 'This models the overdrive channel of a snakeskin-covered 100W amp head built in 1991. With an open low-end and a compressed mid/high range, its powerful, heavy sound delivers a forceful tone that will not break down even with the most extreme gain settings.',
  26: 'Designed to model the sound behind “POWER METAL” this amp will crank.',
  27: 'This models the modern high-gain channel from a wild beast of an amp. Its deep and loose low-end, sparkling highs, and monstrous gain are ideal for guitars tuned as low as possible, or for metal acts wielding seven-string guitars.',
  28: 'This models a California-made amp head with a three-channel design and versatile gain switches that produce a wide variety of sounds. We’ve modeled the lead channel, which produces the ultimate high-gain tone.',
  29: 'This two-channel 120W head manufactured in Mississippi was designed for a legendary guitar hero known for his “brown sound.” This amp models features a high-gain sound that’s ideal for the tapping performance technique.',
  30: 'This models the overdrive channel of a 100W high-quality amp that was produced only on special order, and was known as the overdrive special. The wonderful sustain obtained by raising the GAIN control is smooth and soulful.',
  31: 'This models the crushing high-gain sound that emanated from a German-made 100W four-channel amp head. We chose the “Heavy” channel, which delivers a startling tightness when played with a dropped-D metal tuning.',
  32: 'This is an original amp model based on a recent high-gain amp, marked by a rich and hot mid-range tone and extremely powerful sustain. Since active-circuit tone controls are used on this model as well, a wide range of tonal variety can be obtained.'}}
)

def main(args):
    if len(args) == 0:
      df['description'] =  df['description'].apply(lambda x: x[:40])
      print(tabulate(df))
      return
    if args[0].isnumeric():
      num = int(args[0])
      if num in df.index:
        name = df.loc[num, 'name']
        mode = df.loc[num, 'mode']
        amp = df.loc[num, 'amp_name']
        description = df.loc[num, 'description']
        length = len(name) + len(mode) + 3
        print('*'*length)
        print(f"{name} - {mode}")
        print(amp)
        print('*'*length)
        print(description)
        return
    if args[0] in ['g', 'o', 'r']:
      df['description'] =  df['description'].apply(lambda x: x[:40])
      print(tabulate(df[df['color'] == args[0]]))
      return
    names = [i for i in df['name'] if args[0].upper() in i]
    df['description'] =  df['description'].apply(lambda x: x[:40])
    print(tabulate(df[df['name'].isin(names)]))

if __name__ == '__main__':
    main(sys.argv[1:])
