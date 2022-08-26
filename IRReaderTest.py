# Circuit Playground Express Demo Code
# Adjust the pulseio 'board.PIN' if using something else
import pulseio
import board
import adafruit_irremote
import array

pulsein = pulseio.PulseIn(board.REMOTEIN, maxlen=120, idle_state=True)
pulseout = pulseio.PulseOut(board.REMOTEOUT)
decoder = adafruit_irremote.GenericDecode()

# transmitter = adafruit_irremote.GenericTransmit()


while True:
    pulses = decoder.read_pulses(pulsein)
    print("Heard", len(pulses), "Pulses:", pulses)
    try:
        code = decoder.decode_bits(pulses)
        print("Decoded:", code)
        # on_command from https://www.youtube.com/watch?v=TIbp7DzfOBM
        # probably not neccessary, probably doing the same as decoder
        on_command = array.array('H', [pulses[x] for x in range(len(pulses))])
        print(on_command)
#        if board.BUTTON_A:
#           pulseout.send(pulses)
    except adafruit_irremote.IRNECRepeatException:  # unusual short code!
        print("NEC repeat!")
    except adafruit_irremote.IRDecodeException as e:     # failed to decode
        print("Failed to decode: ", e.args)
#    except Exception as e:
#        print("Exception: ", type(e), e.args)

    print("----------------------------")


