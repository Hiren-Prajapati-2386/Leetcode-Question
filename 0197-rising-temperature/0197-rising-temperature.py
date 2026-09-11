import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by=['recordDate'],inplace=True)

    weather['prev_date'] = weather['recordDate'].shift(1)
    weather['prev_temp'] = weather['temperature'].shift(1)

    mask = (
        (weather['temperature'] > weather['prev_temp']) & 
        ((weather['recordDate'] - weather['prev_date']).dt.days == 1)
    )

    

    return weather[mask][['id']]

    