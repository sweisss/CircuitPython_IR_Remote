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

# transmitter = adafruit_irremote.GenericTransmit()

while True:
    if cpx.button_a:
        print("Button A is pressed")
        time.sleep(0.5)
    if cpx.button_b:
        print("Button B is pressed")
        time.sleep(0.5)
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
