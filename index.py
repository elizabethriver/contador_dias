from datetime import date, timedelta


def contador():
    today = date.today()
    mg_8_start = today - timedelta(56)
    mg_6_start = today - timedelta(42)
    mg_6_end = mg_6_start - timedelta(14)
    mg_4_start = today - timedelta(28)
    mg_4_end = mg_4_start - timedelta(14)
    mg_2_end = today - timedelta(14)

    print(f"""
            messages generale 8, initial: {mg_8_start} - final: {today.year},
            messages generale 6, initial: {mg_6_start} - final: {mg_6_end},
            messages generale 4, initial: {mg_4_start} - final: {mg_4_end},
            messages generale 2, initial: {today} - final: {mg_2_end}, """
        )

contador()
