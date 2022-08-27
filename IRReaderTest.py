# Circuit Playground Express Demo Code
# Adjust the pulseio 'board.PIN' if using something else
import pulseio
import board
import adafruit_irremote
import array
from adafruit_circuitplayground.express import cpx
import time

pulsein = pulseio.PulseIn(board.REMOTEIN, maxlen=120, idle_state=True)
pulseout = pulseio.PulseOut(board.REMOTEOUT, frequency=38000, duty_cycle=2**15)
decoder = adafruit_irremote.GenericDecode()

vol_up = array.array('H', [4523, 4483, 573, 1664, 571, 1666, 569, 1668, 567, 551, 566, 552, 565, 554, 564, 556, 573, 545, 572, 1666, 570, 1667, 568, 1669, 566, 552, 565, 554, 563, 554, 573, 545, 572, 546, 572, 1665, 569, 1668, 568, 1670, 566, 553, 596, 522, 595, 524, 594, 525, 593, 526, 571, 548, 569, 549, 569, 550, 598, 1639, 628, 1608, 595, 1643, 592, 1645, 601, 1636, 599])
vol_down = array.array('H', [4513, 4489, 568, 1668, 567, 1669, 567, 1669, 567, 577, 540, 578, 539, 579, 540, 578, 538, 581, 536, 1673, 563, 1673, 573, 1663, 571, 573, 546, 573, 544, 574, 544, 574, 543, 576, 542, 1668, 569, 1668, 567, 577, 541, 1670, 565, 554, 563, 580, 538, 580, 537, 581, 548, 571, 546, 572, 545, 1665, 571, 573, 544, 1667, 569, 1668, 568, 1669, 568, 1669, 566])

while True:
    if cpx.button_a:
        print("Button A is pressed")
        pulseout.send(vol_up)
        time.sleep(0.5)
    if cpx.button_b:
        print("Button B is pressed")
        pulseout.send(vol_down)
        time.sleep(0.5)
    
    
    ###### The Listen and Decode Section.#######
    ###### Comment out when trying to send.#####
    """
    pulses = decoder.read_pulses(pulsein)
    if len(pulses) == 67:
        print("Heard", len(pulses), "Pulses:", pulses)
        try:
            code = decoder.decode_bits(pulses)
            print("Decoded:", code)
            # on_command from https://www.youtube.com/watch?v=TIbp7DzfOBM
            # probably not neccessary, probably doing the same as decoder
            on_command = array.array('H', [pulses[x] for x in range(len(pulses))])
            print(on_command)
            #if cpx.button_a:
                #print("Button A is pressed")
                #pulseout.send(on_command)
        except adafruit_irremote.IRNECRepeatException:  # unusual short code!
            print("NEC repeat!")
        except adafruit_irremote.IRDecodeException as e:     # failed to decode
            print("Failed to decode: ", e.args)
        #except Exception as e:
            #if e.args[0][1] != 'Too short':
                #print("Exception: ", type(e), e.args)
            # print("Reason:", e.args[0][1])
        print("----------------------------")

"""