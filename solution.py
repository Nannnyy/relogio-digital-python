def seven_segmentify(time_: str) -> str:

    digitos = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"],
        ':': ["   ", " . ", " . "],
        ' ': ["   ", "   ", "   "]
    }

    if time_[0] == "0":
        time_ = " " + time_[1:]

    horas, minutos = time_.split(':')
    print(horas[0])
    print(horas[1])
    

    linha1 = []
    linha2 = []
    linha3 = []

    for char in horas + ':' + minutos:
        linha1.append(digitos[char][0])
        linha2.append(digitos[char][1])
        linha3.append(digitos[char][2])

    return '\n'.join([''.join(linha1), ''.join(linha2), ''.join(linha3)])