

def compute_ema(closes, periods):

    avarages = []
    emas = []
    smoothfactor = 2 / (periods + 1)
    counter = 0

    for price in closes():

        if len(avarages) < periods:

            avarages.append(price)
            emas.append(None)

        elif len(avarages) >= periods:

            if counter < 1:

                ema = price * smoothfactor + (sum(avarages) / periods) * (1 - smoothfactor)
                emas.append(ema)
                counter += 1

            elif counter >= 1:

                real_ema = price * smoothfactor + emas[-1] * (1 - smoothfactor)
                emas.append(real_ema)

    return emas


