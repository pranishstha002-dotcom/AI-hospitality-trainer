"""
A small, self-contained hospitality knowledge base for the /more/learn
section. Deliberately structured as plain data (topic -> content, tagged by
category) rather than baked into templates, so a future version can swap
this dict for a real document store / RAG retriever without touching the
route or template code that reads it.
"""

KNOWLEDGE_BASE = [
    {
        "category": "Front Office",
        "topic": "The Walk (Relocation) Standard",
        "summary": (
            "When the property is oversold, guests must be relocated to equal or "
            "better accommodations, with transport and reasonable costs covered, and "
            "never left to discover the situation on their own at a busy desk."
        ),
        "checklist": [
            "Confirm there truly is no inventory before offering a walk",
            "Choose a comparable or better property nearby",
            "Cover transport both ways, plus the night itself",
            "Document the guest's original confirmation and the resolution",
            "Follow up personally the next day",
        ],
    },
    {
        "category": "Front Office",
        "topic": "VIP & Loyalty Recognition",
        "summary": (
            "Recognizing status isn't just a greeting — it's proactively knowing "
            "preferences, honoring them without being asked twice, and following up "
            "personally when something goes sideways for a top-tier guest."
        ),
        "checklist": [
            "Check status and history before the guest reaches the desk, when possible",
            "Use their name and acknowledge their tier naturally, not performatively",
            "Have a fallback plan ready for early arrivals or unavailable preferences",
            "A manager follow-up is expected for any service failure with a VIP",
        ],
    },
    {
        "category": "Housekeeping",
        "topic": "Lost & Found Process",
        "summary": (
            "Every lost-item report needs a fast, structured response: log it "
            "immediately, involve housekeeping directly, and give the guest a real "
            "timeframe rather than an open-ended 'we'll look into it.'",
        ),
        "checklist": [
            "Log the report within 15 minutes of the guest raising it",
            "Forward directly to the housekeeping supervisor, not just a general note",
            "Give a specific follow-up window (2 hours maximum)",
            "Never speculate about theft or blame staff to the guest",
        ],
    },
    {
        "category": "Food & Beverage",
        "topic": "Allergy & Dietary Requests",
        "summary": (
            "Allergy requests are never routine small talk — they require actual "
            "verification with the kitchen, honest disclosure of any uncertainty, and "
            "a real alternative when cross-contact risk exists."
        ),
        "checklist": [
            "Never reassure a guest about an allergy without checking with the kitchen first",
            "Ask about severity, not just the allergen itself",
            "State uncertainty plainly rather than guessing",
            "Offer a genuinely safe alternative, not just an apology",
        ],
    },
    {
        "category": "Compensation",
        "topic": "Goodwill Gesture Guidelines",
        "summary": (
            "Standard goodwill gestures (a comp item, dessert, or 10-15% discount) "
            "cover most service recoveries under roughly $50 of impact. Anything "
            "larger needs manager approval — compensation should match the actual "
            "issue, not the volume of a guest's complaint.",
        ),
        "checklist": [
            "Match the gesture's size to the actual impact, not to guest pressure",
            "Never promise compensation you aren't authorized to approve",
            "A sincere apology plus a concrete gesture beats an over-apology with nothing concrete",
        ],
    },
    {
        "category": "Complaints",
        "topic": "Escalation Standards",
        "summary": (
            "Any complaint that's been raised twice without resolution should reach a "
            "duty manager within five minutes. Front-line staff should never argue "
            "with a guest in a public area — de-escalate and move the conversation "
            "aside instead.",
        ),
        "checklist": [
            "Recognize the second-ask threshold and escalate promptly",
            "Move heated conversations away from other guests",
            "Document each interaction so escalation isn't starting from zero",
        ],
    },
    {
        "category": "Sales",
        "topic": "Ethical Upselling",
        "summary": (
            "A good upsell is framed around genuine guest value, offered once clearly, "
            "and dropped immediately and gracefully on a 'no' — repeated pushing after "
            "a decline damages trust more than the extra revenue is worth.",
        ),
        "checklist": [
            "Look for genuine openings (an occasion, a stated need) rather than a script",
            "Describe value in the guest's terms, not just features and price",
            "Accept a decline immediately, without a second attempt in the same interaction",
        ],
    },
    {
        "category": "Management",
        "topic": "Giving Difficult Feedback",
        "summary": (
            "Effective feedback conversations lead with specific, observed behavior — "
            "not character judgments — stay two-way, and end with a concrete, "
            "measurable next step and a follow-up point.",
        ),
        "checklist": [
            "Use specific examples, not generalizations like 'you're always...'",
            "Separate behavior from character in your language",
            "Ask for their perspective before concluding intent",
            "Agree on a measurable next step and when you'll check back in",
        ],
    },
]

KNOWLEDGE_CATEGORIES = sorted({item["category"] for item in KNOWLEDGE_BASE})
