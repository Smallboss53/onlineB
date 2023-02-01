import datetime
from projects.models import Hotel, Booking

def check_availability(hotel, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(hotel=hotel)
    for booking in booking_list:
        if booking.check_in > check_out or check_out< check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)