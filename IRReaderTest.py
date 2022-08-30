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
orb_on = array.array('H', [8930, 4442, 566, 530, 589, 534, 616, 506, 570, 525, 593, 529, 620, 502, 564, 531, 597, 526, 615, 1603, 593, 1651, 564, 1654, 615, 1603, 593, 530, 620, 1598, 598, 1647, 570, 1648, 620, 1597, 588, 1656, 570, 526, 594, 528, 620, 502, 564, 532, 597, 526, 614, 508, 568, 528, 592, 531, 617, 1600, 595, 1650, 567, 1652, 585, 1632, 595, 1650, 567, 1651, 586])
orb_off = array.array('H', [8926, 4444, 564, 559, 570, 552, 565, 557, 540, 556, 562, 561, 568, 554, 543, 554, 565, 558, 560, 1631, 596, 1650, 566, 1651, 586, 1632, 595, 528, 590, 1628, 588, 1656, 571, 1647, 590, 533, 565, 1653, 594, 528, 569, 554, 564, 559, 560, 564, 544, 552, 567, 556, 562, 1629, 598, 524, 594, 1624, 592, 1653, 564, 1655, 594, 1625, 592, 1653, 572, 1646, 591])


while True:
    if cpx.button_a:
        print("Button A is pressed")
        pulseout.send(orb_off)
        time.sleep(0.5)
    if cpx.button_b:
        print("Button B is pressed")
        pulseout.send(orb_on)
        time.sleep(0.5)
    
    """
    ###### The Listen and Decode Section.#######
    ###### Comment out when trying to send.#####
    
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

