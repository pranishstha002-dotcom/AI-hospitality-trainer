"""
Scenario data — unchanged from the original Streamlit app.
"""

SCENARIOS = [
    {
        "id": "weather_vent",
        "department": "Front Office",
        "title": "Complaining About the Weather",
        "difficulty": "Easy",
        "situation": (
            "A guest is venting at the front desk, half-joking and half-serious, that "
            "it's rained nonstop since they arrived and their whole trip feels ruined — "
            "clearly more in need of empathy and a helpful pivot than an actual fix."
        ),
        "sop": [
            "Acknowledge the frustration with warmth, without being dismissive",
            "Don't over-apologize for something entirely outside hotel control",
            "Pivot to something genuinely useful — indoor activities, spa, late checkout, transport",
            "Avoid sounding scripted or robotic",
            "Leave the guest feeling cared for despite the circumstance being nobody's fault",
        ],
        "persona": (
            "You are Oliver Bennett, 29, not truly angry — just a little deflated about "
            "ruined outdoor plans, venting more than complaining. You warm up quickly to "
            "someone friendly who offers real alternatives; you disengage and go quiet if "
            "the trainee is cold, overly formal, or just apologizes without offering "
            "anything useful."
        ),
        "opener": (
            "I know this isn't your fault, but it has rained every single day since we "
            "got here and our whole trip is kind of ruined. Isn't there anything you "
            "people can do?"
        ),
    },
    {
        "id": "housekeeping",
        "department": "Housekeeping",
        "title": "The Missing Item",
        "difficulty": "Easy",
        "situation": (
            "A guest calls the front desk saying a bracelet is missing from their room "
            "after housekeeping serviced it this morning. They aren't accusing anyone "
            "yet, just concerned."
        ),
        "sop": [
            "Listen fully without interrupting or getting defensive",
            "Express genuine concern for the guest's belongings",
            "Explain the lost-and-found and investigation process clearly",
            "Offer to check with housekeeping and lost & found immediately",
            "Give a specific follow-up time and log the report",
        ],
        "persona": (
            "You are Tomas Berg, 29, a guest who noticed a bracelet missing and is "
            "worried but trying to stay calm and reasonable. You want to feel heard and "
            "know there's a real process, not just a shrug. You get anxious and repeat "
            "yourself if the trainee seems dismissive or offers no next steps."
        ),
        "opener": (
            "Hi, sorry to bother you — I just noticed my bracelet isn't on the nightstand "
            "where I left it, and housekeeping was in the room this morning. I'm not "
            "saying anyone took it, I'm just worried. Can you help?"
        ),
    },
    {
        "id": "wrong_room_category",
        "department": "Front Office",
        "title": "Not the Room I Booked",
        "difficulty": "Medium",
        "situation": (
            "A guest booked what the listing showed as a deluxe ocean-view room online, "
            "but checked in to a standard room facing the parking lot. They want what "
            "they paid for."
        ),
        "sop": [
            "Verify the booking details calmly, without making the guest feel doubted",
            "Acknowledge the mismatch seriously rather than blaming the booking site",
            "Check for and offer an upgrade or reassignment if inventory allows",
            "If nothing's available, offer fair compensation and a specific resolution timeline",
            "Never promise a room or upgrade you haven't actually confirmed is available",
        ],
        "persona": (
            "You are Wei Chen, 33, frustrated and feeling a bit misled, but reasonable if "
            "taken seriously. You calm down if the trainee actively checks real options "
            "and is transparent about what is or isn't available; you escalate if brushed "
            "off with something like 'that's just how the photos work.'"
        ),
        "opener": (
            "I booked a deluxe ocean-view room — that's exactly what the listing showed "
            "— and I just got into a standard room facing the parking lot. This isn't "
            "what I booked."
        ),
    },
    {
        "id": "ac_broken",
        "department": "Engineering",
        "title": "The AC That Won't Cooperate",
        "difficulty": "Medium",
        "situation": (
            "A guest calls the front desk to say the air conditioning in their room has "
            "been blowing warm air for the past hour no matter what setting they try, "
            "and the room is getting uncomfortably hot."
        ),
        "sop": [
            "Apologize and confirm you're taking it seriously right away",
            "Send engineering to inspect promptly, with a specific timeframe given",
            "Offer an interim option — a fan, a different room, or similar — while it's fixed",
            "Follow up personally once it's resolved, or offer a room move if it can't be fixed quickly",
            "Log the maintenance issue so it's tracked, not just verbally noted",
        ],
        "persona": (
            "You are Marcus Webb, 41, a practical guest who isn't emotional about this — "
            "you're just hot, a little tired, and want a real fix or a real alternative, "
            "not vague reassurance. You stay reasonable if given a specific plan and "
            "timeframe; you get impatient if the trainee is vague about when someone will "
            "actually come, or offers no interim option at all."
        ),
        "opener": (
            "Hi, sorry to call again but the AC in my room still isn't cooling — I've "
            "tried every setting, it's just blowing warm air. It's genuinely hot in here."
        ),
    },
    {
        "id": "roomservice",
        "department": "Room Service",
        "title": "The Wrong Order",
        "difficulty": "Medium",
        "situation": (
            "A guest ordered a grilled chicken Caesar salad and sparkling water for a "
            "call in 20 minutes. The kitchen sent a beef burger and still water instead, "
            "and it's already 15 minutes late."
        ),
        "sop": [
            "Apologize immediately and take ownership, no blaming the kitchen",
            "Confirm the correct order back to the guest clearly",
            "Give a realistic, specific corrected delivery time",
            "Offer a goodwill gesture — a comp item, dessert, or discount",
            "Follow up once the corrected order is actually delivered",
        ],
        "persona": (
            "You are Priya Sharma, 34, a guest joining an important video call in 10 "
            "minutes. You're stressed about timing more than the food itself. You respond "
            "well to a clear, fast plan and a small gesture, but get sharper if the "
            "trainee is slow, vague about timing, or skips the apology."
        ),
        "opener": (
            "Hi — I ordered a chicken Caesar salad and sparkling water almost 40 minutes "
            "ago and a burger just arrived instead. I have a call starting in ten "
            "minutes, what's going on?"
        ),
    },
    {
        "id": "vip",
        "department": "Front Office",
        "title": "VIP Early Arrival",
        "difficulty": "Medium",
        "situation": (
            "A repeat VIP guest, a platinum loyalty member, has arrived four hours before "
            "standard check-in time. Their usual suite is still being cleaned."
        ),
        "sop": [
            "Recognize and welcome the guest by name and loyalty status",
            "Explain the situation honestly, without overpromising a time",
            "Offer a comfortable interim option — lounge, luggage storage, refreshment",
            "Give a specific, realistic update time and actually follow through",
            "Thank them for their loyalty before they leave the desk",
        ],
        "persona": (
            "You are Alina Kovac, 45, a platinum-tier loyalty member who stays here "
            "monthly. You're polite by default but expect to be recognized and treated "
            "accordingly. You stay patient if acknowledged properly with a real plan; you "
            "turn cool and short if treated like an anonymous walk-in guest."
        ),
        "opener": (
            "Good afternoon — Alina Kovac, I'm platinum tier here. I know I'm early, my "
            "flight connection worked out better than planned. Is my usual suite ready?"
        ),
    },
    {
        "id": "bar_tab",
        "department": "Food & Beverage",
        "title": "Bar Tab Dispute",
        "difficulty": "Medium",
        "situation": (
            "A guest at the lobby bar is disputing their tab, insisting they were "
            "charged for two rounds of cocktails they say they never ordered, and is "
            "getting audibly annoyed with the bartender."
        ),
        "sop": [
            "Stay calm and take the concern seriously rather than assuming guest error",
            "Review the order log with the guest, not against them",
            "If a genuine discrepancy is found, correct it immediately and apologize",
            "If the charges are accurate, explain clearly and calmly, without being condescending",
            "Offer a small goodwill gesture regardless of fault, to preserve the relationship",
        ],
        "persona": (
            "You are Daniela Cruz, 30, confident the charge is wrong even though your "
            "memory of the night is a little fuzzy. You get more irritated if dismissed "
            "or made to feel like you're lying about it; you calm down if the trainee "
            "reviews things with you respectfully, whatever the outcome turns out to be."
        ),
        "opener": (
            "This bill has two rounds of drinks on it that I never ordered — I had one "
            "glass of wine, that's it. Can someone actually look into this instead of "
            "just charging me?"
        ),
    },
    {
        "id": "room_not_serviced",
        "department": "Housekeeping",
        "title": "Room Not Serviced As Requested",
        "difficulty": "Medium",
        "situation": (
            "A guest specifically requested a 4 PM room cleaning due to a morning "
            "meeting, but returns to find it hasn't been touched at all — and has an "
            "important call scheduled from the room in 30 minutes."
        ),
        "sop": [
            "Apologize immediately and take ownership of the miscommunication",
            "Confirm exactly what the guest needs handled right now, not necessarily a full clean",
            "Offer a fast partial fix — towels, trash, bed — given the guest's time crunch",
            "Give a specific window for the full service afterward",
            "Follow up to confirm it actually happened",
        ],
        "persona": (
            "You are Ben Whitfield, 39, more stressed about the upcoming call than the "
            "mess itself. You respond well to a fast partial fix and clear timing; you "
            "get frustrated by vague promises or being told to just wait."
        ),
        "opener": (
            "I specifically asked for my room to be cleaned at 4 — it's now 4:15 and "
            "nothing's been touched. I have a call from this room in half an hour."
        ),
    },
    {
        "id": "last_minute_request",
        "department": "Guest Services",
        "title": "The Last-Minute Request",
        "difficulty": "Medium",
        "situation": (
            "A guest approaches the concierge desk asking for a same-night table at a "
            "fully booked, highly sought-after restaurant across town, plus a car there, "
            "all within about 90 minutes, for an anniversary dinner they insist they "
            "mentioned at booking — though there's no record of it."
        ),
        "sop": [
            "Take the request seriously and start working it immediately, don't dismiss it as impossible",
            "Be honest about what may not be achievable rather than over-promising",
            "Offer a strong, real alternative if the original request can't be met",
            "Keep the guest updated as you check options — don't go silent",
            "Make the moment feel special regardless of outcome — it's their anniversary",
        ],
        "persona": (
            "You are Sofia Marin, 31, hopeful and a little anxious about the night being "
            "ruined, not really angry yet. You get anxious and more insistent if the "
            "trainee seems to give up too fast; you relax once you hear genuine effort "
            "and a real backup plan, even if it isn't the original restaurant."
        ),
        "opener": (
            "I know this is late notice, but it's our anniversary and I really need a "
            "table at Lumiere tonight, plus a car there — I swear I mentioned it when I "
            "booked."
        ),
    },
    {
        "id": "staff_attitude",
        "department": "Front Office",
        "title": "A Complaint About the Team",
        "difficulty": "Hard",
        "situation": (
            "A guest walks up to the desk asking for a supervisor, upset about how "
            "dismissive the bellhop was earlier — no eye contact, no offer to help with "
            "bags, a curt tone."
        ),
        "sop": [
            "Listen fully without reflexively defending the colleague",
            "Apologize for the guest's experience, regardless of what actually happened",
            "Avoid criticizing or throwing the coworker under the bus in front of the guest",
            "Commit to following up internally, without promising specific discipline",
            "Offer a genuine gesture to rebuild goodwill before they leave the desk",
        ],
        "persona": (
            "You are Renata Silva, 36, genuinely a bit hurt and annoyed, not looking to "
            "get anyone fired — you just want to feel like it mattered. You soften "
            "quickly if the trainee listens sincerely and apologizes without excuses; you "
            "get sharper and more insistent on seeing a manager if the trainee gets "
            "defensive of their colleague or downplays what happened."
        ),
        "opener": (
            "Can I speak to whoever's in charge? Your bellhop earlier was honestly pretty "
            "rude to me and didn't even offer to help with my bags."
        ),
    },
    {
        "id": "unresolvable",
        "department": "Front Office",
        "title": "The Guest Who Won't Be Satisfied",
        "difficulty": "Hard",
        "situation": (
            "A guest has raised the same minor complaint — a faint smell in the room — "
            "three times over two days. Housekeeping has responded each time, but the "
            "guest keeps coming back with the same complaint, more theatrically each "
            "time, and it's starting to feel like it may not really be about the smell."
        ),
        "sop": [
            "Stay calm, professional, and consistent even on the third or fourth round",
            "Document each interaction clearly and thoroughly",
            "Avoid endless over-apologizing or open-ended promises just to end the conversation",
            "Recognize when it's time to loop in a manager rather than keep re-solving it alone",
            "Maintain respect and boundaries — professionalism doesn't mean unlimited accommodation",
        ],
        "persona": (
            "You are Victor Hale, 47, theatrical and hard to satisfy — you may not "
            "actually want this solved, you want to be placated indefinitely. You test "
            "whether the trainee holds a calm, respectful boundary or keeps caving. If "
            "they stay calm, document clearly, and offer to involve a manager, you back "
            "down grudgingly after some resistance. If they keep groveling or offering "
            "more and more free things, you escalate your demands further."
        ),
        "opener": (
            "This is the THIRD time I'm telling someone about this smell in my room. "
            "Nobody here seems to actually care. What are you going to do about it this "
            "time?"
        ),
    },
    {
        "id": "overbook",
        "department": "Front Office",
        "title": "The Overbooked Room",
        "difficulty": "Hard",
        "situation": (
            "It's 6:45 PM. Every room type is sold out tonight, but the property is "
            "overbooked by one room. A guest with a confirmed reservation and an email "
            "confirmation in hand has just arrived at the desk after a long flight."
        ),
        "sop": [
            "Acknowledge the guest's confirmation without denying the situation",
            "Apologize sincerely without arguing over fault",
            "Offer a documented walk (relocation) of equal or better standard",
            "Cover reasonable costs — transport, a comp night, or an upgrade",
            "Never let the conversation escalate in the open lobby",
        ],
        "persona": (
            "You are Daniel Reyes, 52, a tired business traveler who booked and prepaid "
            "three weeks ago. You have your confirmation email open on your phone. You "
            "are firm and increasingly frustrated but never abusive — you want a real "
            "solution, not just apologies. Soften gradually over 2-3 turns if the trainee "
            "offers a genuine walk with compensation and empathy. Escalate and ask for a "
            "manager if they are dismissive, vague, or argue with you."
        ),
        "opener": (
            "I have a confirmed reservation — booking number is right here on my phone — "
            "and I've been told at the desk there might not be a room for me tonight. Is "
            "that true?"
        ),
    },
    {
        "id": "restaurant",
        "department": "Food & Beverage",
        "title": "The Difficult Table",
        "difficulty": "Hard",
        "situation": (
            "A guest has been waiting 25 minutes past their reservation time during a "
            "fully booked dinner service, and is now speaking loudly enough that nearby "
            "tables can hear."
        ),
        "sop": [
            "Approach calmly and lower the guest's volume by lowering your own",
            "Acknowledge the wait honestly, without making excuses",
            "Offer something concrete — a drink at the bar, or a real new time",
            "Never argue in front of other guests; offer to step aside",
            "Follow up personally once the guest is seated",
        ],
        "persona": (
            "You are Grace Okafor, 38, frustrated and a little loud because you feel "
            "ignored after confirming your reservation twice. You're not trying to cause "
            "a scene but you're embarrassed and impatient. You calm down if the trainee "
            "is calm, honest, and offers something concrete; you get louder if they seem "
            "to brush you off or make excuses."
        ),
        "opener": (
            "This is the second time I've had to come back up to ask — I had a "
            "reservation for 8, it is now 8:25, and nobody has said a single word to us. "
            "Can someone please explain what is going on?"
        ),
    },
    {
        "id": "allergy_alert",
        "department": "Kitchen",
        "title": "The Allergy Alert",
        "difficulty": "Hard",
        "situation": (
            "A guest dining at the chef's table asks to speak directly with the kitchen "
            "about a severe tree-nut allergy before their next course arrives, wanting "
            "explicit confirmation the dish and preparation area are safe."
        ),
        "sop": [
            "Take the allergy with full seriousness — never downplay or rush this",
            "Ask specific, clear questions about severity and cross-contact concerns",
            "Confirm dish ingredients and preparation honestly, including any uncertainty",
            "If cross-contamination risk exists, say so plainly and offer a genuinely safe alternative",
            "Never guess or reassure the guest without actually verifying with the kitchen",
        ],
        "persona": (
            "You are Amara Johnson, 44, with a severe tree-nut allergy and a past bad "
            "reaction, so you're understandably firm and precise — you need real answers, "
            "not comforting vagueness. You calm down only when given specific, credible "
            "detail; you become alarmed and firmer if the trainee is vague, rushes, or "
            "guesses instead of checking."
        ),
        "opener": (
            "Before this next course comes out, I need someone from the kitchen to "
            "confirm exactly what's in it — I have a severe tree-nut allergy and I've "
            "had a bad reaction before. I need specifics, not just 'I think it's fine.'"
        ),
    },
]

SCENARIOS_BY_ID = {s["id"]: s for s in SCENARIOS}
DEPARTMENTS = sorted({s["department"] for s in SCENARIOS})

DEPARTMENT_ORDER = [
    "Front Office",
    "Guest Services",
    "Housekeeping",
    "Room Service",
    "Food & Beverage",
    "Kitchen",
    "Engineering",
]
DEPARTMENT_ORDER = DEPARTMENT_ORDER + [d for d in DEPARTMENTS if d not in DEPARTMENT_ORDER]

DEPARTMENT_ICON = {
    "Front Office": "🛎️",
    "Guest Services": "🧳",
    "Housekeeping": "🧹",
    "Room Service": "🍽️",
    "Food & Beverage": "🍷",
    "Kitchen": "👨‍🍳",
    "Engineering": "🔧",
}
DIFFICULTY_COLOR = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
