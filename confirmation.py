"""
Generates a plausible reservation or order confirmation record for a
scenario, so trainees have concrete details to reference (confirmation
number, dates, rate, itemized charges) instead of having to invent them.

Deterministic per scenario (seeded by scenario id) so the same scenario
always shows the same confirmation within a given day — it isn't meant to
perfectly narrate every scenario's specific plot detail, just to give the
trainee something real-looking to check, the way an actual reservation
system or POS receipt would.
"""

import datetime
import random
import re

ORDER_DEPARTMENTS = {"Room Service", "Food & Beverage", "Kitchen"}

_ROOM_TYPES = [
    "Standard King", "Standard Queen", "Deluxe City View",
    "Deluxe Ocean View", "Junior Suite", "Executive Suite",
]
_RATES = [139, 159, 189, 219, 259, 299, 349]
_BOOKING_SOURCES = ["Direct / Hotel Website", "Online Travel Agency", "Corporate Rate Program", "Phone Reservation"]

_MENU_ITEMS = [
    ("Grilled Chicken Caesar Salad", 18.00),
    ("Classic Beef Burger", 16.00),
    ("Sparkling Water", 4.00),
    ("Still Water", 3.00),
    ("Club Sandwich", 15.00),
    ("Margherita Pizza", 17.00),
    ("House Red Wine (glass)", 12.00),
    ("Chocolate Lava Cake", 9.00),
    ("Caprese Salad", 13.00),
    ("Espresso", 5.00),
]


def _guest_name(scenario: dict) -> str:
    match = re.match(r"You are ([^,]+),", scenario.get("persona", ""))
    return match.group(1) if match else "Guest"


def build_confirmation(scenario: dict) -> dict:
    rnd = random.Random(scenario["id"])  # deterministic per scenario
    guest_name = _guest_name(scenario)
    confirmation_number = f"HTL-{rnd.randint(100000, 999999)}"

    if scenario["department"] in ORDER_DEPARTMENTS:
        n_items = rnd.randint(2, 4)
        chosen = rnd.sample(_MENU_ITEMS, n_items)
        items = []
        for name, price in chosen:
            qty = rnd.choice([1, 1, 1, 2])
            items.append({"name": name, "qty": qty, "price": price, "line_total": round(qty * price, 2)})
        subtotal = round(sum(i["line_total"] for i in items), 2)
        tax = round(subtotal * 0.08, 2)
        total = round(subtotal + tax, 2)
        hour = rnd.randint(6, 11)
        minute = rnd.choice(["00", "15", "30", "45"])
        ampm = rnd.choice(["AM", "PM"])
        return {
            "kind": "order",
            "confirmation_number": confirmation_number,
            "guest_name": guest_name,
            "location": f"Room {rnd.randint(200, 999)}",
            "order_time": f"{hour}:{minute} {ampm}",
            "line_items": items,
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
        }

    nights = rnd.randint(1, 4)
    room_type = rnd.choice(_ROOM_TYPES)
    rate = rnd.choice(_RATES)
    subtotal = rate * nights
    taxes_fees = round(subtotal * 0.14, 2)
    total = round(subtotal + taxes_fees, 2)
    today = datetime.date.today()
    checkin = today - datetime.timedelta(days=rnd.randint(0, 2))
    checkout = checkin + datetime.timedelta(days=nights)
    return {
        "kind": "reservation",
        "confirmation_number": confirmation_number,
        "guest_name": guest_name,
        "room_type": room_type,
        "rate_per_night": rate,
        "nights": nights,
        "checkin": checkin.strftime("%b %d, %Y"),
        "checkout": checkout.strftime("%b %d, %Y"),
        "subtotal": subtotal,
        "taxes_fees": taxes_fees,
        "total": total,
        "booking_source": rnd.choice(_BOOKING_SOURCES),
        "payment_method": f"Visa ending in {rnd.randint(1000, 9999)}",
    }
