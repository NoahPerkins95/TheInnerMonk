from itertools import count


INTENSITIES = ["Gentle", "Balanced", "Strong"]
SOUL_STATES = ["Distracted", "Anxious", "Tired", "Angry", "Dry", "Grateful"]
TIME_OPTIONS = ["5 minutes", "15 minutes", "30 minutes"]
SCROLL_STATES = ["Restless", "Numb", "Avoiding", "Lonely"]


_ids = count(1)


def _rule(
    intensity,
    state,
    time,
    scripture,
    father,
    prayer,
    body,
    mind,
    reflection,
):
    return {
        "id": next(_ids),
        "intensity": intensity,
        "state": state,
        "time": time,
        "scripture": scripture,
        "father": father,
        "prayer": prayer,
        "body": body,
        "mind": mind,
        "reflection": reflection,
    }


RULES = [
    _rule(
        "Gentle",
        "Distracted",
        "5 minutes",
        "Jesus said, 'Abide in me, and I in you.' (John 15:4)",
        "St. Isaac the Syrian: 'Enter eagerly into the treasure house that is within you.'",
        "Lord Jesus Christ, Son of God, have mercy on me.",
        "Drink a glass of water slowly, without doing anything else.",
        "Place your phone out of reach for five minutes of silence.",
        "Where is Christ already waiting in the place I keep avoiding within myself?",
    ),
    _rule(
        "Gentle",
        "Anxious",
        "5 minutes",
        "Jesus said, 'Peace I leave with you; my peace I give to you.' (John 14:27)",
        "St. John Climacus: 'Stillness is the mother of prayer.'",
        "Lord Jesus Christ, give me Your peace.",
        "Sit with both feet on the floor and take ten slow breaths.",
        "Name one concern, then let it rest before God without solving it.",
        "What would it mean to receive peace as communion rather than control?",
    ),
    _rule(
        "Gentle",
        "Tired",
        "5 minutes",
        "Jesus said, 'Come to me, all who labor and are heavy laden, and I will give you rest.' (Matthew 11:28)",
        "St. Macarius the Great: 'The heart itself is but a small vessel, yet there are dragons and lions there, and there also is God.'",
        "Lord Jesus Christ, receive my weariness.",
        "Rest your eyes and shoulders for five minutes.",
        "Do nothing useful. Let the silence be enough.",
        "Can I allow weakness to become a doorway into dependence on God?",
    ),
    _rule(
        "Gentle",
        "Angry",
        "5 minutes",
        "Jesus said, 'Blessed are the meek, for they shall inherit the earth.' (Matthew 5:5)",
        "St. Maximus the Confessor: 'He who loves God cannot help loving every man as himself.'",
        "Lord Jesus Christ, make my heart meek.",
        "Unclench your jaw, hands, and shoulders; breathe slowly.",
        "Do not answer the provoking thought for five minutes.",
        "What passion is asking to be healed beneath my anger?",
    ),
    _rule(
        "Gentle",
        "Dry",
        "5 minutes",
        "Jesus said, 'Whoever drinks of the water that I will give him will never be thirsty again.' (John 4:14)",
        "St. Silouan the Athonite: 'Keep thy mind in hell, and despair not.'",
        "Lord Jesus Christ, stay with me in dryness.",
        "Drink water as a small sign of desire for living water.",
        "Read one Gospel sentence twice, slowly.",
        "What if dryness is not absence, but an invitation to seek God without reward?",
    ),
    _rule(
        "Gentle",
        "Grateful",
        "5 minutes",
        "Jesus said, 'Freely you received; freely give.' (Matthew 10:8)",
        "St. Basil the Great: 'A good deed is never lost.'",
        "Lord Jesus Christ, teach me thanksgiving.",
        "Stand, bow once, and give thanks for one concrete mercy.",
        "Send no message about it. Let gratitude remain hidden before God.",
        "How can thanksgiving become union with the Giver, not attachment to the gift?",
    ),
    _rule(
        "Gentle",
        "Distracted",
        "15 minutes",
        "Jesus said, 'Seek first the kingdom of God and his righteousness.' (Matthew 6:33)",
        "St. Theophan the Recluse: 'To pray is to descend with the mind into the heart.'",
        "Lord Jesus Christ, gather my scattered mind into my heart.",
        "Take a quiet ten-minute walk without headphones.",
        "Choose one task and give it undivided attention afterward.",
        "What kingdom is my attention serving today?",
    ),
    _rule(
        "Gentle",
        "Anxious",
        "15 minutes",
        "Jesus said, 'Do not be anxious about tomorrow.' (Matthew 6:34)",
        "St. Porphyrios: 'Christ is everything. He is joy, He is life, He is light.'",
        "Lord Jesus Christ, illumine this anxious place.",
        "Stretch your neck, back, and hands with slow breathing.",
        "Write down one fear, then write: 'Christ is here.'",
        "Where is anxiety asking me to live apart from trust?",
    ),
    _rule(
        "Gentle",
        "Tired",
        "15 minutes",
        "Jesus said, 'The Sabbath was made for man.' (Mark 2:27)",
        "St. Gregory Palamas: 'The grace of the Spirit comes to those who are purified.'",
        "Lord Jesus Christ, sanctify my rest.",
        "Lie down or sit quietly for fifteen minutes.",
        "Let the next unnecessary demand remain unanswered.",
        "Do I believe rest can be obedient when it restores love?",
    ),
    _rule(
        "Gentle",
        "Angry",
        "15 minutes",
        "Jesus said, 'Love your enemies and pray for those who persecute you.' (Matthew 5:44)",
        "St. Dorotheos of Gaza: 'The more one is united to his neighbor, the more he is united to God.'",
        "Lord Jesus Christ, have mercy on me and on the one who troubles me.",
        "Walk slowly until your breathing softens.",
        "Pray once for the person involved without rehearsing the story.",
        "What would love look like if I did not need to win the inner argument?",
    ),
    _rule(
        "Gentle",
        "Dry",
        "15 minutes",
        "Jesus said, 'Ask, and it will be given to you; seek, and you will find.' (Matthew 7:7)",
        "St. Anthony the Great: 'Our life and our death is with our neighbor.'",
        "Lord Jesus Christ, teach me to seek You.",
        "Lightly tidy one small area as an offering.",
        "Sit in silence for seven minutes, asking nothing but God's presence.",
        "How might faithfulness in small things purify desire?",
    ),
    _rule(
        "Gentle",
        "Grateful",
        "15 minutes",
        "Jesus said, 'Let your light shine before others, so that they may see your good works and give glory to your Father.' (Matthew 5:16)",
        "St. John Chrysostom: 'Glory be to God for all things.'",
        "Lord Jesus Christ, let my gratitude glorify the Father.",
        "Prepare a simple drink or meal with attention and thanks.",
        "Do one hidden kindness without announcing it.",
        "Where can gratitude become self-emptying love today?",
    ),
    _rule(
        "Balanced",
        "Distracted",
        "15 minutes",
        "Jesus said, 'The eye is the lamp of the body.' (Matthew 6:22)",
        "St. Hesychios the Priest: 'Attention is the heart's stillness.'",
        "Lord Jesus Christ, guard the door of my heart.",
        "Take a brisk walk for ten minutes.",
        "Fast from scrolling until your next meal.",
        "What enters through my attention, and does it make me more like Christ?",
    ),
    _rule(
        "Balanced",
        "Anxious",
        "15 minutes",
        "Jesus said, 'Let not your hearts be troubled, neither let them be afraid.' (John 14:27)",
        "St. Seraphim of Sarov: 'Acquire the Spirit of peace, and thousands around you will be saved.'",
        "Lord Jesus Christ, establish Your peace in me.",
        "Breathe slowly while walking outside or near a window.",
        "Refuse prediction. Return to the present commandment of love.",
        "What would peace in me make possible for the people near me?",
    ),
    _rule(
        "Balanced",
        "Tired",
        "15 minutes",
        "Jesus said, 'My yoke is easy, and my burden is light.' (Matthew 11:30)",
        "St. Barsanuphius: 'Do what you can, and God will help you.'",
        "Lord Jesus Christ, carry what I cannot carry.",
        "Drink water and rest away from a screen.",
        "Reduce one obligation to its simplest faithful form.",
        "Where is God inviting me out of performance and into communion?",
    ),
    _rule(
        "Balanced",
        "Angry",
        "15 minutes",
        "Jesus said, 'First be reconciled to your brother, and then come and offer your gift.' (Matthew 5:24)",
        "St. Ephrem the Syrian: 'Blessed is the one who has become completely free of anger.'",
        "Lord Jesus Christ, cleanse my memory and my tongue.",
        "Wash your face and hands as a sign of beginning again.",
        "Keep silence about the offense for fifteen minutes.",
        "What reconciliation must begin inside me before it can become visible?",
    ),
    _rule(
        "Balanced",
        "Dry",
        "15 minutes",
        "Jesus said, 'If anyone thirsts, let him come to me and drink.' (John 7:37)",
        "St. Gregory of Nyssa: 'The one who rises never stops going from beginning to beginning.'",
        "Lord Jesus Christ, awaken holy thirst.",
        "Take a plain walk or stretch with no entertainment.",
        "Read the Beatitudes slowly and choose one to carry today.",
        "What desire in me needs purification rather than satisfaction?",
    ),
    _rule(
        "Balanced",
        "Grateful",
        "15 minutes",
        "Jesus said, 'Blessed are the pure in heart, for they shall see God.' (Matthew 5:8)",
        "St. Irenaeus: 'The glory of God is a living man.'",
        "Lord Jesus Christ, make my thanks pure.",
        "Offer fifteen minutes of careful work as thanksgiving.",
        "Do not multitask during the offering.",
        "How does gratitude make the heart simpler and more transparent to God?",
    ),
    _rule(
        "Balanced",
        "Distracted",
        "30 minutes",
        "Jesus said, 'One thing is necessary.' (Luke 10:42)",
        "St. Mary of Egypt: 'God protects all who turn to Him from every temptation.'",
        "Lord Jesus Christ, make me attentive to the one thing needful.",
        "Walk for twenty minutes without audio.",
        "Set the phone in another room and complete one humble task.",
        "What must become less important so Christ can become central?",
    ),
    _rule(
        "Balanced",
        "Anxious",
        "30 minutes",
        "Jesus said, 'Look at the birds of the air... your heavenly Father feeds them.' (Matthew 6:26)",
        "St. Paisios the Athonite: 'The more a person forgets himself, the more God remembers him.'",
        "Lord Jesus Christ, teach me childlike trust.",
        "Spend twenty minutes walking or resting in fresh air.",
        "Fast from checking news, email, or messages for thirty minutes.",
        "Which anxious responsibility can I return to the Father today?",
    ),
    _rule(
        "Balanced",
        "Tired",
        "30 minutes",
        "Jesus said, 'Remain here, and watch with me.' (Matthew 26:38)",
        "St. John Cassian: 'The goal of our life is the kingdom of God.'",
        "Lord Jesus Christ, keep me with You in weakness.",
        "Take a restorative rest, then drink water.",
        "Keep the room quiet; let no media fill the fatigue.",
        "Can tiredness become watchfulness rather than escape?",
    ),
    _rule(
        "Balanced",
        "Angry",
        "30 minutes",
        "Jesus said, 'Forgive, and you will be forgiven.' (Luke 6:37)",
        "St. Mark the Ascetic: 'Do not try to explain away your fault.'",
        "Lord Jesus Christ, give me the courage to forgive.",
        "Take a long walk and breathe before speaking.",
        "Write the truth plainly without accusation; do not send it yet.",
        "What part of my anger is defending an image of myself that needs to die?",
    ),
    _rule(
        "Balanced",
        "Dry",
        "30 minutes",
        "Jesus said, 'I am the vine; you are the branches.' (John 15:5)",
        "St. Symeon the New Theologian: 'Do not say it is impossible to receive the Spirit of God.'",
        "Lord Jesus Christ, graft me again into Your life.",
        "Do a simple chore slowly and prayerfully.",
        "Keep silence for fifteen minutes after reading a Gospel passage.",
        "Where is God pruning me so I may bear fruit?",
    ),
    _rule(
        "Balanced",
        "Grateful",
        "30 minutes",
        "Jesus said, 'As the Father has loved me, so have I loved you; abide in my love.' (John 15:9)",
        "St. Athanasius: 'God became man so that man might become god.'",
        "Lord Jesus Christ, let me abide in Your love.",
        "Prepare or clean something for another person with care.",
        "Let the act remain quiet, without seeking recognition.",
        "How is thanksgiving drawing me into participation in divine love?",
    ),
    _rule(
        "Strong",
        "Distracted",
        "30 minutes",
        "Jesus said, 'If anyone would come after me, let him deny himself and take up his cross.' (Mark 8:34)",
        "St. John Climacus: 'Obedience is the burial of the will and the resurrection of humility.'",
        "Lord Jesus Christ, make my will obedient to Yours.",
        "Fast from snacks until the next meal and take a sober walk.",
        "Turn off nonessential notifications for the rest of the day.",
        "What cross of attention is Christ asking me to carry without complaint?",
    ),
    _rule(
        "Strong",
        "Anxious",
        "30 minutes",
        "Jesus said, 'Whoever loses his life for my sake will find it.' (Matthew 16:25)",
        "St. Maximus the Confessor: 'Theology without practice is the theology of demons.'",
        "Lord Jesus Christ, free me from self-preservation.",
        "Walk for thirty minutes, breathing the Jesus Prayer with your steps.",
        "Do one concrete act of love before checking the source of anxiety.",
        "What false self am I trying to preserve, and how can I surrender it to Christ?",
    ),
    _rule(
        "Strong",
        "Tired",
        "30 minutes",
        "Jesus said, 'Watch and pray that you may not enter into temptation.' (Matthew 26:41)",
        "St. Isaac the Syrian: 'Be at peace with your own soul; then heaven and earth will be at peace with you.'",
        "Lord Jesus Christ, grant watchful rest.",
        "Rest for twenty minutes, then stand and make three slow bows.",
        "Avoid entertainment as anesthesia; choose quiet restoration.",
        "What kind of rest restores my capacity to love God and neighbor?",
    ),
    _rule(
        "Strong",
        "Angry",
        "30 minutes",
        "Jesus said, 'Father, forgive them, for they know not what they do.' (Luke 23:34)",
        "St. Silouan the Athonite: 'The soul that has known the Lord loves the whole world.'",
        "Lord Jesus Christ, crucify resentment in me.",
        "Fast from food or snacks for one small interval if health permits.",
        "Pray slowly for the salvation of the person you resent.",
        "How is Christ inviting me to share His mercy from the Cross?",
    ),
    _rule(
        "Strong",
        "Dry",
        "30 minutes",
        "Jesus said, 'Unless a grain of wheat falls into the earth and dies, it remains alone.' (John 12:24)",
        "St. Gregory Nazianzen: 'We must be buried with Christ, rise with Christ, and inherit with Christ.'",
        "Lord Jesus Christ, let what is barren die in You.",
        "Keep a simple fast from comfort eating or unnecessary pleasure.",
        "Sit in silence for twenty minutes with the Jesus Prayer.",
        "What must fall into the earth so the life of Christ may grow in me?",
    ),
    _rule(
        "Strong",
        "Grateful",
        "30 minutes",
        "Jesus said, 'You shall love the Lord your God with all your heart.' (Matthew 22:37)",
        "St. Nikolai Velimirovich: 'Love is joy, and joy is strength.'",
        "Lord Jesus Christ, receive all that I am.",
        "Give thirty minutes to service, cleaning, care, or preparation for another.",
        "Keep the work hidden and prayerful.",
        "How can gratitude become total offering, not pleasant feeling alone?",
    ),
    _rule(
        "Strong",
        "Distracted",
        "15 minutes",
        "Jesus said, 'Enter by the narrow gate.' (Matthew 7:13)",
        "St. Philotheos of Sinai: 'Watchfulness is a continual fixing of the mind at the entrance to the heart.'",
        "Lord Jesus Christ, narrow my attention into love.",
        "Stand, stretch, and then begin the hardest small task.",
        "Block one distracting app or site until evening.",
        "What narrow gate would make my soul more spacious in God?",
    ),
    _rule(
        "Strong",
        "Anxious",
        "15 minutes",
        "Jesus said, 'Take heart; it is I. Do not be afraid.' (Matthew 14:27)",
        "St. Anthony the Great: 'Expect temptation until your last breath.'",
        "Lord Jesus Christ, meet me on the waters.",
        "Take a firm walk and breathe the Jesus Prayer with each step.",
        "Do the next duty before asking for reassurance.",
        "How can courage become trust in Christ rather than confidence in myself?",
    ),
    _rule(
        "Strong",
        "Angry",
        "15 minutes",
        "Jesus said, 'Be merciful, even as your Father is merciful.' (Luke 6:36)",
        "St. John Chrysostom: 'Nothing makes us so like God as being ready to forgive.'",
        "Lord Jesus Christ, make me merciful as the Father is merciful.",
        "Hold silence while walking or standing until the body calms.",
        "Refuse the satisfying sentence you want to say.",
        "What would it cost my pride to become more like God in mercy?",
    ),
]


SCROLL_RULES = [
    _rule(
        "Strong",
        "Distracted",
        "5 minutes",
        "Jesus said, 'If your eye is healthy, your whole body will be full of light.' (Matthew 6:22)",
        "St. Hesychios the Priest: 'Watchfulness is a continual fixing of the mind at the entrance to the heart.'",
        "Lord Jesus Christ, Son of God, have mercy on me.",
        "Put the phone face down, stand up, drink water, and make one slow bow.",
        "Do not open the feed. Keep silence for five minutes.",
        "What hunger am I trying to feed with noise, and how can I bring it to Christ?",
    ),
    _rule(
        "Gentle",
        "Anxious",
        "5 minutes",
        "Jesus said, 'Take heart; it is I. Do not be afraid.' (Matthew 14:27)",
        "St. Seraphim of Sarov: 'Acquire the Spirit of peace, and thousands around you will be saved.'",
        "Lord Jesus Christ, steady my heart.",
        "Sit upright, loosen your shoulders, and breathe the Jesus Prayer ten times.",
        "Leave every app closed. Name the fear without obeying it.",
        "What would trust do in the next five minutes?",
    ),
    _rule(
        "Balanced",
        "Dry",
        "5 minutes",
        "Jesus said, 'If anyone thirsts, let him come to me and drink.' (John 7:37)",
        "St. Isaac the Syrian: 'Enter eagerly into the treasure house that is within you.'",
        "Lord Jesus Christ, meet me in this thirst.",
        "Walk to another room or window without carrying the phone.",
        "Let boredom remain empty before God instead of filling it.",
        "Can this moment of wanting become prayer instead of consumption?",
    ),
    _rule(
        "Balanced",
        "Tired",
        "5 minutes",
        "Jesus said, 'Come to me, all who labor and are heavy laden, and I will give you rest.' (Matthew 11:28)",
        "St. Barsanuphius: 'Do what you can, and God will help you.'",
        "Lord Jesus Christ, give me true rest.",
        "Rest your eyes and breathe slowly with both hands open.",
        "Choose silence over stimulation for five minutes.",
        "What kind of rest would return me to love?",
    ),
]


def _without_last(matches, avoid_id):
    if avoid_id is None or len(matches) <= 1:
        return matches

    fresh_matches = [rule for rule in matches if rule["id"] != avoid_id]
    return fresh_matches or matches


def get_rule(intensity, state, time, avoid_id=None):
    exact_matches = [
        rule
        for rule in RULES
        if rule["intensity"] == intensity and rule["state"] == state and rule["time"] == time
    ]
    if exact_matches:
        return _without_last(exact_matches, avoid_id)[0]

    close_matches = [
        rule
        for rule in RULES
        if rule["intensity"] == intensity and rule["state"] == state
    ]
    if close_matches:
        return _without_last(close_matches, avoid_id)[0]

    state_matches = [rule for rule in RULES if rule["state"] == state]
    if state_matches:
        return _without_last(state_matches, avoid_id)[0]

    return RULES[0]


def get_scroll_rule(scroll_state, avoid_id=None):
    state_map = {
        "Restless": "Distracted",
        "Numb": "Dry",
        "Avoiding": "Anxious",
        "Lonely": "Tired",
    }
    mapped_state = state_map.get(scroll_state, "Distracted")
    matches = [rule for rule in SCROLL_RULES if rule["state"] == mapped_state]
    if matches:
        return _without_last(matches, avoid_id)[0]

    return _without_last(SCROLL_RULES, avoid_id)[0]
