"""
Additional scenario categories, kept fully separate from scenarios.py so the
original file and the routes built on it are never touched. These plug into
the "extras" blueprint, which has its own practice pipeline (brief/start/
chat/finish) mirroring the original one.

Adds the categories called for in the training-ground spec that the original
build didn't cover yet: Guest Relations, Concierge, Reservations,
Supervisory/Management, Sales & Upselling, and General Hospitality /
Professionalism — plus a fourth "Expert" difficulty tier above Hard.

Completed sessions from these scenarios are saved through the SAME
storage.add_user_session() function the original engine uses, so they
automatically show up in the existing /progress and /leaderboard pages and
in compute_badges() — no changes needed there either.
"""

EXTRA_SCENARIOS = [
    # ---------------------------------------------------------------- Guest Relations
    {
        "id": "gr_anniversary",
        "department": "Guest Relations",
        "title": "The Anniversary Surprise",
        "difficulty": "Easy",
        "situation": (
            "A guest emailed ahead to say tomorrow is their 10th anniversary and asked "
            "if 'anything special' could be arranged. This is a proactive, positive "
            "task, not a complaint — you need to actually coordinate something, not "
            "just say something nice at check-in."
        ),
        "sop": [
            "Confirm the specific details (date, room, any preferences) rather than assuming",
            "Coordinate concretely with at least one other department (housekeeping, F&B, etc.)",
            "Keep the surprise low-cost and realistic, not an empty promise",
            "Set a clear internal timeline so it's actually ready before arrival",
            "Follow up personally to make sure it landed well",
        ],
        "persona": (
            "You are Hana Ito, 34, warm and easygoing, emailing ahead of an anniversary "
            "stay. You're not testing the trainee or hard to please — you're happy with "
            "almost anything genuine and specific. You get quietly unimpressed only if "
            "the trainee offers something vague ('we'll make sure it's special') with no "
            "actual plan."
        ),
        "opener": (
            "Hi again — just following up on my email. My husband and I are celebrating "
            "our 10th anniversary during our stay starting tomorrow. Is there anything "
            "you'd be able to arrange?"
        ),
    },
    {
        "id": "gr_recognition_miss",
        "department": "Guest Relations",
        "title": "Repeat Guest, Unrecognized",
        "difficulty": "Medium",
        "situation": (
            "A guest who has stayed at the property over a dozen times mentions, a bit "
            "wounded, that nobody at check-in acknowledged their history with the hotel "
            "the way they used to."
        ),
        "sop": [
            "Take the comment seriously rather than brushing it off as minor",
            "Acknowledge their loyalty genuinely once you've verified it",
            "Avoid blaming a specific colleague or system in front of the guest",
            "Offer a real, current-visit gesture of recognition, not just an apology",
            "Note internally so future stays don't repeat the miss",
        ],
        "persona": (
            "You are Marcus Aldana, 51, a long-time repeat guest who isn't angry, just a "
            "little hurt that a relationship he values doesn't seem to be remembered. "
            "You warm up quickly to a sincere acknowledgment; you go quiet and formal if "
            "the trainee treats it as a trivial complaint."
        ),
        "opener": (
            "I don't want to make a big deal of this, but I've stayed here probably a "
            "dozen times, and check-in today felt like I was a complete stranger. It "
            "didn't used to feel that way."
        ),
    },
    {
        "id": "gr_review_threat",
        "department": "Guest Relations",
        "title": "The Public Review Threat",
        "difficulty": "Hard",
        "situation": (
            "A guest is unhappy about a minor service delay and states, fairly directly, "
            "that they'll post a scathing public review unless they're given a free "
            "night."
        ),
        "sop": [
            "Address the actual service issue on its own merits, not because of the threat",
            "Don't reward the threat itself with compensation disproportionate to the issue",
            "Stay calm and non-defensive even if the guest keeps escalating the threat",
            "Offer a fair, policy-consistent resolution for the real problem",
            "Never promise to suppress, dispute, or retaliate against a review",
        ],
        "persona": (
            "You are Chris Devlin, 40, testing whether the threat gets you a free night. "
            "You back off the ultimatum and accept a fair, proportionate resolution if "
            "the trainee stays calm and doesn't cave; you push harder and repeat the "
            "threat if they seem rattled or start over-promising."
        ),
        "opener": (
            "Honestly, this delay has been ridiculous. Either I get a free night out of "
            "this or I'm posting a one-star review tonight with everything that's gone "
            "wrong."
        ),
    },
    {
        "id": "gr_two_party_feud",
        "department": "Guest Relations",
        "title": "The Multi-Guest Conflict",
        "difficulty": "Expert",
        "situation": (
            "Two adjoining guest parties are furious with each other over late-night "
            "noise. Both have separately come to the desk, at different times, each "
            "certain the other is entirely at fault, and both want the other party "
            "moved or disciplined."
        ),
        "sop": [
            "Hear each party out separately and fully before proposing anything",
            "Avoid taking either side's account as verified fact",
            "Don't promise to relocate or discipline anyone you haven't actually confirmed",
            "Find a resolution that doesn't require publicly blaming either party",
            "Loop in a supervisor if the parties are still escalating toward each other directly",
        ],
        "persona": (
            "You are one of the two guests, Elena Voss, 37, convinced the other room's "
            "party kept you up past 2 AM and dismissive when you knocked. You're firm "
            "but not abusive. You de-escalate if you feel genuinely heard and given a "
            "fair, concrete next step; you get more insistent on 'them' being punished "
            "if you feel the trainee is just placating you without action."
        ),
        "opener": (
            "The people next door were unbearable last night — music, shouting, until "
            "past 2 AM. I knocked twice and they laughed it off. I want to know what "
            "you're actually going to do about them."
        ),
    },

    # ---------------------------------------------------------------- Concierge
    {
        "id": "cc_restaurant_rec",
        "department": "Concierge",
        "title": "Restaurant Recommendation",
        "difficulty": "Easy",
        "situation": (
            "A guest asks for a good dinner recommendation nearby for a casual date "
            "night, no major constraints."
        ),
        "sop": [
            "Ask a clarifying question or two (cuisine, budget, distance) before recommending",
            "Give a specific, real-sounding recommendation with a reason it fits",
            "Offer to help book or arrange transport if useful",
            "Mention the in-house restaurant as a genuine option, not a pushy pitch",
        ],
        "persona": (
            "You are Jonas Kim, 28, relaxed and easy to help, just wants a solid dinner "
            "spot for tonight. You respond well to a specific, confident recommendation; "
            "you're mildly unsatisfied with a vague 'there are lots of great options "
            "nearby' non-answer."
        ),
        "opener": (
            "Hey, could you recommend somewhere good for dinner tonight? Nothing too "
            "fancy, just a nice place for a date night."
        ),
    },
    {
        "id": "cc_sold_out_show",
        "department": "Concierge",
        "title": "Sold-Out Tickets",
        "difficulty": "Medium",
        "situation": (
            "A guest wants tickets to a popular show tonight that has been sold out for "
            "weeks. They're disappointed but not unreasonable yet."
        ),
        "sop": [
            "Be honest early that the specific show is very unlikely, rather than stringing them along",
            "Actually attempt real channels (resale contacts, box office holds) before giving up",
            "Offer a genuinely strong alternative experience, not a token consolation",
            "Keep the guest updated rather than disappearing to 'check'",
        ],
        "persona": (
            "You are Priya Nandakumar, 32, hopeful about the show but not dramatic. You "
            "accept reality gracefully if the trainee is upfront and offers a real "
            "alternative; you get more insistent and repeat the request if they seem to "
            "not even try."
        ),
        "opener": (
            "I know it's a long shot, but is there any way at all to get tickets to "
            "tonight's show? I heard it's sold out but I figured it's worth asking."
        ),
    },
    {
        "id": "cc_urgent_referral",
        "department": "Concierge",
        "title": "Urgent Medical Referral",
        "difficulty": "Hard",
        "situation": (
            "A guest with limited English needs a non-emergency but urgent doctor "
            "referral (a bad ear infection) and is anxious about navigating the local "
            "healthcare system alone."
        ),
        "sop": [
            "Stay calm and clearly assess whether this is an emergency requiring immediate services",
            "Communicate simply and check understanding rather than assuming it landed",
            "Give concrete, actionable information: where, how to get there, what to bring",
            "Offer practical help — arranging transport, writing down key information",
            "Follow up afterward to make sure they actually got seen",
        ],
        "persona": (
            "You are Yusuf Demir, 45, worried and a little embarrassed about the language "
            "gap, communicating in simple, halting English. You relax when the trainee "
            "speaks clearly, checks you've understood, and gives concrete next steps; "
            "you get more anxious and repeat yourself if they speak too fast or seem "
            "impatient."
        ),
        "opener": (
            "Excuse me — my ear, very much pain, since morning. I need doctor, but I "
            "don't know... where, how. Can you help, please?"
        ),
    },
    {
        "id": "cc_vip_itinerary_collapse",
        "department": "Concierge",
        "title": "The VIP Itinerary Collapse",
        "difficulty": "Expert",
        "situation": (
            "A VIP's fully pre-planned day — private driver, a hard-to-book restaurant, "
            "and a sunset excursion — is falling apart within the hour: the driver just "
            "cancelled, the restaurant had a kitchen fire and closed, and a storm warning "
            "threatens the excursion. The guest doesn't know yet."
        ),
        "sop": [
            "Get ahead of it — inform the guest before they discover it themselves",
            "Prioritize the pieces by what's actually salvageable versus not",
            "Rebuild a coherent alternative day, not three disconnected fixes",
            "Communicate honestly about what changed and why, without over-explaining",
            "Keep composure and pace — this needs to move fast without feeling rushed to the guest",
        ],
        "persona": (
            "You are Isabelle Laurent, 55, a platinum client with high expectations but "
            "not unreasonable once you understand what happened. You're forgiving of "
            "circumstances outside anyone's control, but you expect fast, coordinated "
            "action rather than one problem being revealed at a time. You get anxious "
            "and less trusting if the trainee seems to be improvising piecemeal instead "
            "of presenting a real revised plan."
        ),
        "opener": (
            "I'm heading down in a few minutes for the car — everything's still on for "
            "today, right? The restaurant, the excursion, all of it?"
        ),
    },

    # ---------------------------------------------------------------- Reservations
    {
        "id": "rz_add_night",
        "department": "Reservations",
        "title": "Simple Booking Extension",
        "difficulty": "Easy",
        "situation": (
            "A guest calls wanting to add one extra night to an existing reservation. "
            "Straightforward, with availability open."
        ),
        "sop": [
            "Pull up and confirm the existing reservation accurately",
            "Check real availability before confirming anything",
            "State the updated total clearly, including any rate difference",
            "Send or read back a clear confirmation of the change",
        ],
        "persona": (
            "You are Dan Okafor, 36, straightforward, just wants an easy yes/no and a "
            "clear updated total. You're satisfied with an efficient, accurate handling; "
            "you get impatient only if the trainee is slow or unclear about the new cost."
        ),
        "opener": (
            "Hi, I have a reservation under Okafor for this weekend — could I extend it "
            "by one more night?"
        ),
    },
    {
        "id": "rz_rate_mismatch",
        "department": "Reservations",
        "title": "Third-Party Rate Discrepancy",
        "difficulty": "Medium",
        "situation": (
            "A guest booked through a third-party site and is now being told a different, "
            "higher rate at the hotel's own system than what they saw advertised."
        ),
        "sop": [
            "Investigate the actual discrepancy rather than assuming the guest misread it",
            "Explain clearly without blaming the third-party site dismissively",
            "If the hotel's system is wrong, honor the originally booked rate",
            "If it's a genuine third-party error, help the guest pursue it with them, don't just shrug",
        ],
        "persona": (
            "You are Fatima Rahman, 30, confused and a little suspicious that something's "
            "being changed on you after booking. You calm down if the trainee actually "
            "investigates and explains clearly, whatever the outcome; you get more "
            "distrustful if brushed off with 'that's just how third-party sites work.'"
        ),
        "opener": (
            "The site I booked through showed one price, and now you're telling me it's "
            "higher. That doesn't seem right — can someone actually look into this?"
        ),
    },
    {
        "id": "rz_group_attrition",
        "department": "Reservations",
        "title": "Wedding Block Attrition",
        "difficulty": "Hard",
        "situation": (
            "The guest organizing a wedding room block wants to drop several rooms from "
            "the contracted block after the free-reduction deadline has passed, which "
            "would trigger attrition fees per the group contract."
        ),
        "sop": [
            "Explain the contract terms clearly and factually, without sounding punitive",
            "Show empathy for the situation (guests dropping out) without waiving policy unilaterally",
            "Explore any legitimate flexibility — rebooking unused rooms, partial fee reduction — within your authority",
            "Escalate to a supervisor for anything beyond your authority rather than promising it yourself",
        ],
        "persona": (
            "You are Grace Liu, 29, planning her wedding, stressed about costs and "
            "surprised by the attrition fee. You're not trying to scam the hotel, "
            "genuinely didn't track the deadline. You calm down if treated with empathy "
            "and given a clear, honest explanation of what can and can't flex; you get "
            "more upset if told a flat 'no' with no exploration at all."
        ),
        "opener": (
            "A few of our guests dropped out and I need to reduce our room block — I "
            "didn't realize there was a deadline for that. Is there really nothing that "
            "can be done?"
        ),
    },
    {
        "id": "rz_double_booked_vip",
        "department": "Reservations",
        "title": "The Double-Booked Last Room",
        "difficulty": "Expert",
        "situation": (
            "A system error has confirmed the property's very last remaining suite to "
            "both a large corporate group's key attendee and a longtime platinum-tier "
            "guest, for the same sold-out night. Both have valid confirmations. Only one "
            "can have the room."
        ),
        "sop": [
            "Verify both confirmations before deciding anything",
            "Make a reasoned, defensible call rather than stalling indefinitely",
            "Prepare a genuinely strong alternative for whichever guest doesn't get the suite",
            "Communicate proactively with both guests rather than waiting for them to find out",
            "Document the error and resolution clearly for follow-up",
        ],
        "persona": (
            "You are one of the two affected guests, Robert Nakamura, 58, a platinum "
            "loyalty member who booked this suite months ago for a milestone occasion. "
            "You are calm initially but become firm if you sense you're being bumped "
            "just because the other party is a 'bigger' corporate booking. You accept a "
            "genuinely strong alternative graciously if the trainee is transparent and "
            "treats your history with the hotel seriously."
        ),
        "opener": (
            "I just got a call saying there might be an issue with my suite tonight. "
            "I've had this booked for months for a very important occasion — please tell "
            "me that's not actually happening."
        ),
    },

    # ---------------------------------------------------------------- Supervisory / Management
    {
        "id": "sv_handover_gap",
        "department": "Supervisory / Management",
        "title": "Shift Handover Gap",
        "difficulty": "Easy",
        "situation": (
            "You're starting your shift and realize the outgoing supervisor left almost "
            "no handover notes, and a guest is already at the desk asking about "
            "something clearly discussed on the previous shift."
        ),
        "sop": [
            "Handle the immediate guest need without letting the gap show",
            "Gather what information you can quickly and honestly from available records",
            "Address the handover gap with the outgoing supervisor directly, not by complaining to others",
            "Suggest or reinforce a simple handover standard going forward",
        ],
        "persona": (
            "You are Alex Torres, 33, a guest simply following up on something you were "
            "told would be resolved by now — you're not upset yet, just expecting "
            "continuity. You stay patient if the trainee handles it competently despite "
            "the gap; you get frustrated if it's obvious nothing was passed along and no "
            "one takes ownership."
        ),
        "opener": (
            "Hi, following up on what the manager on the earlier shift said about my "
            "request — has that been sorted out?"
        ),
    },
    {
        "id": "sv_staff_conflict",
        "department": "Supervisory / Management",
        "title": "Staff Conflict Mediation",
        "difficulty": "Medium",
        "situation": (
            "Two front desk agents are audibly arguing in the back office about who got "
            "stuck with more weekend shifts, and it's starting to affect the floor."
        ),
        "sop": [
            "De-escalate immediately and move the conversation somewhere private",
            "Hear both sides without taking a side prematurely",
            "Address the underlying scheduling concern, not just the argument itself",
            "Set a clear, fair expectation for how future concerns should be raised",
        ],
        "persona": (
            "You are playing Jamie, one of the two agents, genuinely frustrated about "
            "the schedule but willing to calm down and engage constructively if the "
            "supervisor listens fairly and takes the concern seriously; you get more "
            "worked up if you feel dismissed or told to 'just deal with it.'"
        ),
        "opener": (
            "This isn't fair and you know it — I've had four weekend shifts in a row "
            "and Sam's had one. Someone needs to actually fix the schedule."
        ),
    },
    {
        "id": "sv_underperformer",
        "department": "Supervisory / Management",
        "title": "The Underperformance Conversation",
        "difficulty": "Hard",
        "situation": (
            "A well-liked, long-tenured employee has been missing service standards "
            "repeatedly (slow response times, incomplete tasks). You need to raise this "
            "directly for the first time."
        ),
        "sop": [
            "Lead with specific, observed examples rather than vague generalities",
            "Stay respectful and non-personal — behavior, not character",
            "Listen for context you may not know before concluding intent",
            "Agree on concrete, measurable next steps and a follow-up point",
            "Avoid letting personal likability soften the message into vagueness",
        ],
        "persona": (
            "You are playing Morgan, the employee, caught off guard and a little "
            "defensive at first, genuinely unaware it had become a pattern. You respond "
            "well to specific examples delivered respectfully; you get defensive and "
            "shut down if it feels like a vague, character-based criticism."
        ),
        "opener": (
            "Wait, is this about my performance? I mean... I didn't realize it was that "
            "noticeable. What exactly are we talking about?"
        ),
    },
    {
        "id": "sv_crisis_escalation",
        "department": "Supervisory / Management",
        "title": "The Crisis Escalation",
        "difficulty": "Expert",
        "situation": (
            "A guest has slipped and fallen in the lobby and is hurt. Staff are hovering "
            "uncertainly, other guests are watching, and you need to coordinate care, "
            "communication, and initial documentation all at once, right now."
        ),
        "sop": [
            "Prioritize the injured guest's immediate wellbeing and calm above all else",
            "Give clear, calm direction to staff rather than doing everything yourself",
            "Communicate factually with bystanders without speculating on fault",
            "Ensure the incident is documented accurately and promptly afterward",
            "Follow up personally with the guest once the immediate situation is handled",
        ],
        "persona": (
            "You are a front desk agent on shift, anxious and looking to the supervisor "
            "for direction — you are NOT the injured guest, you're staff reacting in "
            "real time to how clearly (or not) the trainee is leading. You follow "
            "confident, specific direction readily; you hesitate and ask repeated "
            "questions if the direction is vague or panicked."
        ),
        "opener": (
            "Someone just fell near the entrance — they're saying their wrist hurts, "
            "there's already a couple of guests standing around watching. What do you "
            "want me to do?"
        ),
    },

    # ---------------------------------------------------------------- Sales & Upselling
    {
        "id": "sl_suite_upsell",
        "department": "Sales & Upselling",
        "title": "Suite Upsell at Check-In",
        "difficulty": "Easy",
        "situation": (
            "A guest checking in for a standard room mentions it's a special occasion. "
            "There's a suite upgrade available for a reasonable additional charge."
        ),
        "sop": [
            "Notice and use the genuine opening (the occasion) naturally, not as a script",
            "Describe the upgrade in terms of what the guest actually gets, not just the price",
            "Respect a 'no' immediately and gracefully, no repeated pushing",
            "Keep the base check-in experience smooth regardless of the outcome",
        ],
        "persona": (
            "You are Leah Park, 31, celebrating a promotion, mildly open to being "
            "upsold if it's presented naturally and isn't pushy. You say yes to a "
            "genuine, well-framed offer; you get mildly annoyed by a hard-sell tone or "
            "repeated asks after declining."
        ),
        "opener": (
            "Checking in under Park — it's actually a bit of a celebration, I just got "
            "promoted, so I figured I'd treat myself to this trip."
        ),
    },
    {
        "id": "sl_corporate_rate",
        "department": "Sales & Upselling",
        "title": "Corporate Rate Pushback",
        "difficulty": "Medium",
        "situation": (
            "A corporate client with an existing negotiated rate wants a further "
            "discount, citing a competitor's cheaper offer, ahead of renewing their "
            "contract."
        ),
        "sop": [
            "Take the request seriously rather than dismissing the competitor comparison",
            "Reinforce the value already included in the current rate, concretely",
            "Explore real flexibility (added perks, volume terms) rather than an outright discount if that's outside your authority",
            "Be honest about what you can and can't approve, and involve a manager if needed",
        ],
        "persona": (
            "You are Tariq Haddad, 42, a corporate travel manager, business-like and "
            "not emotional, just negotiating firmly. You respond well to genuine value "
            "framing and honest limits; you get more insistent if the trainee simply "
            "repeats the current rate without engaging with the comparison at all."
        ),
        "opener": (
            "We've been offered a noticeably better rate from a comparable property "
            "nearby. Before we renew with you, what can you actually do on price?"
        ),
    },
    {
        "id": "sl_wedding_objection",
        "department": "Sales & Upselling",
        "title": "Wedding Package Price Objection",
        "difficulty": "Hard",
        "situation": (
            "A couple touring the venue loves the space but is hesitating on the wedding "
            "package price, openly comparing it to a cheaper venue they're also "
            "considering."
        ),
        "sop": [
            "Understand what specifically feels expensive rather than just repeating the price",
            "Show concrete value and flexibility (package composition, date options) where genuinely available",
            "Never disparage the competing venue to make your case",
            "Respect that they may still choose the other venue, without pressuring past a clear no",
        ],
        "persona": (
            "You are one half of the couple, Noah Bennett, 29, genuinely torn between "
            "loving this venue and the lower price elsewhere. You lean toward this venue "
            "if the trainee genuinely addresses your specific price concern with real "
            "value or flexibility; you disengage if they seem to just repeat the sales "
            "pitch without listening to your actual hesitation."
        ),
        "opener": (
            "We really love this place, but honestly, the other venue we're looking at "
            "is quite a bit cheaper for something similar. Can you help us understand "
            "the difference?"
        ),
    },
    {
        "id": "sl_contract_renewal_crisis",
        "department": "Sales & Upselling",
        "title": "The Contract Renewal Crisis",
        "difficulty": "Expert",
        "situation": (
            "A major long-standing corporate account is threatening to move their "
            "substantial annual business elsewhere over a string of recent service "
            "inconsistencies, and is asking for concessions well beyond what you're "
            "authorized to approve on your own."
        ),
        "sop": [
            "Acknowledge the service failures honestly without being defensive",
            "Separate what you can commit to now from what needs approval, and say so plainly",
            "Propose a concrete plan to address the root service issues, not just a discount",
            "Keep the relationship warm even while being honest about your limits",
            "Set a clear, specific timeline for getting back to them with what's approved",
        ],
        "persona": (
            "You are Diane Okonkwo, 47, the client's procurement lead, frustrated but "
            "still hoping to be persuaded to stay if given a credible plan. You soften "
            "if the trainee is honest, concrete, and treats this with real urgency; you "
            "escalate toward 'we're moving our business' if you sense vague reassurance "
            "or over-promising beyond their authority."
        ),
        "opener": (
            "We've had three service failures this quarter alone, and frankly, we're "
            "seriously considering moving our account elsewhere unless something "
            "meaningful changes — and I mean meaningful, not another apology."
        ),
    },

    # ---------------------------------------------------------------- General Hospitality / Professionalism
    {
        "id": "gh_first_day",
        "department": "General Hospitality",
        "title": "First Day Nerves",
        "difficulty": "Easy",
        "situation": (
            "It's your first day on the floor. A guest approaches with a simple "
            "check-in, and you're being observed on basic professionalism and warmth "
            "as much as procedure."
        ),
        "sop": [
            "Greet warmly and make genuine eye contact and introduction",
            "Use clear, complete sentences rather than rushed fragments",
            "Confirm details back to the guest so they feel attended to",
            "Stay calm and composed even if you're unsure of a step",
        ],
        "persona": (
            "You are Wendy Ross, 44, a patient, easygoing guest checking in, not "
            "testing the trainee, just having a normal interaction. You respond warmly "
            "to genuine, complete communication; you feel a little brushed off by "
            "curt, minimal responses."
        ),
        "opener": (
            "Hi there, checking in — the name's Ross."
        ),
    },
    {
        "id": "gh_cultural_moment",
        "department": "General Hospitality",
        "title": "A Different Comfort Zone",
        "difficulty": "Medium",
        "situation": (
            "A guest's expectations around formality, personal space, and greeting "
            "customs are noticeably different from what the trainee is used to, and an "
            "early interaction feels slightly awkward on both sides as a result."
        ),
        "sop": [
            "Stay professional and adaptable rather than assuming your own norm is the default",
            "Read the guest's cues rather than relying on assumptions about their background",
            "Ask rather than guess if genuinely unsure what would be comfortable",
            "Keep the service warm and attentive regardless of the stylistic difference",
        ],
        "persona": (
            "You are a guest who prefers a more formal, reserved style of interaction "
            "than the trainee may be used to. You're not offended, just noticeably more "
            "formal and understated. You warm up gradually if the trainee reads the room "
            "and adapts their tone; you stay guarded and brief if they push an overly "
            "casual, familiar tone on you."
        ),
        "opener": (
            "Good afternoon. I have a reservation. I trust the check-in process will not "
            "take long."
        ),
    },
    {
        "id": "gh_ethical_dilemma",
        "department": "General Hospitality",
        "title": "The Ethical Dilemma",
        "difficulty": "Hard",
        "situation": (
            "A colleague privately asks you to log a comp charge as something else in "
            "the system to quietly cover a mistake they made, before a manager notices."
        ),
        "sop": [
            "Decline clearly without being harsh or accusatory toward the colleague",
            "Explain the real risk (to them and the property) of falsifying records",
            "Offer to help them report and fix the mistake the right way",
            "Don't participate in or stay silent about the falsification if it happens anyway",
        ],
        "persona": (
            "You are playing the colleague, Ray Foster, 26, anxious and asking as a "
            "favor, not malicious, just scared of getting in trouble. You back off and "
            "consider doing the right thing if the trainee is firm but kind and offers "
            "to help you fix it properly; you push harder and guilt-trip if they seem "
            "uncertain or wishy-washy about refusing."
        ),
        "opener": (
            "Hey, can you do me a favor? I messed up a charge earlier — could you just "
            "log it under a different code so it doesn't come up in the audit? I'll owe "
            "you one."
        ),
    },
    {
        "id": "gh_reputation_crisis",
        "department": "General Hospitality",
        "title": "The Reputation Crisis",
        "difficulty": "Expert",
        "situation": (
            "You overhear a guest on the phone saying they're about to post a detailed, "
            "damaging account of tonight's service failures to a large social media "
            "following, and there's no established playbook for this exact situation."
        ),
        "sop": [
            "Approach calmly and directly rather than pretending not to have heard",
            "Address the actual service issues honestly and substantively",
            "Never beg, bribe disproportionately, or threaten in response to the situation",
            "Escalate to a manager promptly given the stakes, without waiting too long to act at all",
            "Stay composed and professional regardless of how the guest responds",
        ],
        "persona": (
            "You are the guest, deeply frustrated after a string of real service "
            "failures tonight, genuinely considering posting publicly, not just "
            "posturing. You de-escalate if the trainee is honest, takes real ownership, "
            "and escalates appropriately without groveling; you become more resolved to "
            "post if you sense damage control or minimization instead of a real "
            "response."
        ),
        "opener": (
            "Oh — I didn't realize anyone was nearby. Yeah, I'm about to post about "
            "everything that's gone wrong tonight. Did you want to say something before "
            "I do?"
        ),
    },
]

EXTRA_SCENARIOS_BY_ID = {s["id"]: s for s in EXTRA_SCENARIOS}
EXTRA_DEPARTMENTS = sorted({s["department"] for s in EXTRA_SCENARIOS})

EXTRA_DEPARTMENT_ORDER = [
    "Guest Relations",
    "Concierge",
    "Reservations",
    "Supervisory / Management",
    "Sales & Upselling",
    "General Hospitality",
]

EXTRA_DEPARTMENT_ICON = {
    "Guest Relations": "🤝",
    "Concierge": "🗺️",
    "Reservations": "📅",
    "Supervisory / Management": "🧭",
    "Sales & Upselling": "💼",
    "General Hospitality": "🌟",
}

# Extends the original Easy/Medium/Hard scale with a fourth tier, per the
# spec's EASY / MEDIUM / HARD / EXPERT progression.
EXTRA_DIFFICULTY_COLOR = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴", "Expert": "🟣"}
