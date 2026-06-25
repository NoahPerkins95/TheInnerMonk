LITURGICAL_MOMENTS = [
    "Morning",
    "Midday",
    "Evening",
    "Before sleep",
]

WORLD_PULLS = [
    "The feed",
    "Status",
    "Comfort",
    "Distraction",
    "Approval",
    "Control",
    "Lust / Flesh",
]

MONASTIC_LONGINGS = [
    "Silence",
    "Purity of heart",
    "Repentance",
    "Unceasing prayer",
    "Simplicity",
    "Union with Christ",
]

LITURGICAL_SEASONS = [
    "Daily",
    "Repentance / Lent",
    "Cross-bearing / Holy Week",
    "Resurrection / Pascha",
    "Preparation / Nativity Fast",
]

SEASONAL_THREADS = {
    "Daily": {
        "tone": "Keep the ordinary day as a hidden offering.",
        "cross": "Let one ordinary self-will die quietly.",
        "resurrection": "Let ordinary obedience become a small participation in risen life.",
        "fast": "Keep the table simple and thankful.",
        "departure": "Return to the day without noise. Let ordinary work become prayer.",
    },
    "Repentance / Lent": {
        "tone": "Enter with repentance, sobriety, and hope.",
        "cross": "Let appetite, excuse, and self-defense be nailed to the Cross.",
        "resurrection": "Let compunction become the first light of healing.",
        "fast": "Prefer plain food, restraint, water, and hidden mercy. Do not display the fast.",
        "departure": "Carry repentance gently. Repair one thing without dramatizing yourself.",
    },
    "Cross-bearing / Holy Week": {
        "tone": "Stand near the Passion of Christ with silence and reverence.",
        "cross": "Do not flee the Cross given today: patience, forgiveness, restraint, or truth.",
        "resurrection": "Hope is hidden in the tomb before it is visible in the garden.",
        "fast": "Eat soberly and avoid comfort-seeking. Let hunger remember Christ.",
        "departure": "Carry the Cross without complaint. Answer one wound with mercy.",
    },
    "Resurrection / Pascha": {
        "tone": "Enter with bright sobriety. Christ is risen, and death is being trampled down.",
        "cross": "Let the old sadness, cynicism, and slavery to the feed remain in the tomb.",
        "resurrection": "Practice joy as obedience, thanksgiving, and mercy.",
        "fast": "Receive food with gratitude, not excess. Let feasting become thanksgiving and generosity.",
        "departure": "Carry Paschal joy into one hidden act of love.",
    },
    "Preparation / Nativity Fast": {
        "tone": "Prepare room for Christ to be born in the heart.",
        "cross": "Let clutter, noise, and consumption be laid down.",
        "resurrection": "Let simplicity make space for the humility of Christ.",
        "fast": "Choose simple food and fewer purchases. Let restraint become generosity.",
        "departure": "Make room for Christ by removing one unnecessary thing from the day.",
    },
}


CHAMBER_MAP = [
    {
        "name": "Mouth",
        "purpose": "Leave the noise outside the cave.",
    },
    {
        "name": "Witness",
        "purpose": "Remember a saint, martyr, or holy witness who chose Christ over the world.",
    },
    {
        "name": "Scripture",
        "purpose": "Receive the word of Christ from the Gospels.",
    },
    {
        "name": "Cross",
        "purpose": "Let the old life die and receive the risen life of Christ.",
    },
    {
        "name": "Creed",
        "purpose": "Stand inside the faith of the Church before acting.",
    },
    {
        "name": "Body",
        "purpose": "Train the body as a temple and servant of prayer, not vanity.",
    },
    {
        "name": "Purity",
        "purpose": "Break contact with lust, recover watchfulness, and turn the whole man toward Christ.",
    },
    {
        "name": "Return",
        "purpose": "Gather the mind from the world's false pattern and return to Christ.",
    },
    {
        "name": "Departure",
        "purpose": "Carry one obedience back into the world.",
    },
]

CHAMBER_STAGES = [
    {
        "stage": "Entrance",
        "purpose": "Leave the world at the mouth of the cave.",
        "chambers": [
            {
                "name": "Mouth",
                "purpose": "Renounce the noise and name what you are leaving behind.",
            },
            {
                "name": "Daily Order",
                "purpose": "Receive a small order for the day.",
            },
        ],
    },
    {
        "stage": "Illumination",
        "purpose": "Let the faith of the Church give light to the heart.",
        "chambers": [
            {
                "name": "Witness",
                "purpose": "Remember a saint, martyr, or holy witness.",
            },
            {
                "name": "Scripture",
                "purpose": "Receive the word of Christ from the Gospels.",
            },
            {
                "name": "Creed",
                "purpose": "Stand inside the confession of the Church.",
            },
        ],
    },
    {
        "stage": "Struggle",
        "purpose": "Bring the passions, body, and attention under the lordship of Christ.",
        "chambers": [
            {
                "name": "Passion",
                "purpose": "Name the passion and the Christward virtue.",
            },
            {
                "name": "Cross",
                "purpose": "Let the old life die and receive risen life.",
            },
            {
                "name": "Body",
                "purpose": "Train the body as a temple and servant of prayer.",
            },
            {
                "name": "Purity",
                "purpose": "Break contact with unreality and guard the eyes, imagination, and body for Christ.",
            },
            {
                "name": "Prayer",
                "purpose": "Return the mind to the name of Jesus.",
            },
        ],
    },
    {
        "stage": "Return",
        "purpose": "Return to Christ, receive the daily oath of service, and depart under the Cross.",
        "chambers": [
            {
                "name": "Return",
                "purpose": "Gather the mind, receive mercy, and keep the next clean obedience.",
            },
            {
                "name": "Vigil and Oath",
                "purpose": "Receive Christ's love, give Him today's allegiance, and take up the next obedience.",
            },
            {
                "name": "Departure",
                "purpose": "Carry one obedience back into the world.",
            },
        ],
    },
]


SAINT_WITNESSES = [
    {
        "name": "St. Polycarp of Smyrna",
        "title": "Bishop and martyr",
        "story": "An old bishop, formed by the apostolic age, refused to curse Christ when threatened with death. His witness teaches the soul not to trade faithfulness for safety.",
        "martyrdom": "According to the ancient account, Polycarp was condemned at Smyrna. When the fire did not consume him as expected, he was killed by the sword and his body was burned.",
        "paschal_thread": "His death is remembered as participation in Christ's victory: the Cross received without denial, and the Resurrection hoped for beyond the flames.",
        "depth": "Polycarp's witness is not only about a dramatic death. It is about a long obedience that had already trained the heart before the moment of trial arrived.",
        "world_resisted": "Fear, self-preservation, and the demand to treat Christ as negotiable.",
        "lesson": "Do not negotiate with the world when it asks you to deny Christ in small ways.",
        "virtue": "Faithfulness",
        "theosis": "Faithfulness heals the divided heart until confession and life become one.",
        "imitation": "Keep one clear confession of Christ today, especially where silence would be cowardice.",
        "small_act": "Refuse one compromise that makes prayer colder.",
        "reflection": "Where am I tempted to make peace with something that weakens my love for Christ?",
    },
    {
        "name": "St. Ignatius of Antioch",
        "title": "Bishop and martyr",
        "story": "On the road to martyrdom, he wrote to the churches with burning love for Christ, the Eucharist, and unity. He saw suffering not as performance, but as being joined to the Lord.",
        "martyrdom": "Ignatius was taken to Rome under guard and, according to tradition, was killed by wild beasts in the arena.",
        "paschal_thread": "He saw martyrdom through the Cross and Resurrection: not self-destruction, but being offered to Christ in hope of life with Him.",
        "depth": "Ignatius shows that holiness is not private intensity. His longing for Christ made him more ecclesial, more Eucharistic, and more bound to the body of believers.",
        "world_resisted": "Individualism, spiritual noise, and zeal detached from love.",
        "lesson": "Let zeal become communion, not noise.",
        "virtue": "Holy zeal",
        "theosis": "Zeal becomes Christlike when it is purified into love, unity, and self-offering.",
        "imitation": "Let your desire for holiness become love for the Church, not private intensity.",
        "small_act": "Pray once for your parish, priest, bishop, and those you find difficult.",
        "reflection": "Does my desire for holiness make me more loving, patient, and united to the Church?",
    },
    {
        "name": "St. Mary of Egypt",
        "title": "Desert penitent",
        "story": "After a life ruled by passion, she entered the desert in repentance and became a sign of radical mercy. Her life says no one is too lost for transformation.",
        "martyrdom": "Mary was not killed as a martyr. Her witness is a bloodless martyrdom of repentance: the old life was put to death in the desert so a new life could rise in Christ.",
        "paschal_thread": "Her story is Paschal: the Cross of repentance becomes the doorway to resurrection of the soul.",
        "depth": "Mary's life refuses despair. The desert did not erase her story; it became the place where Christ transfigured it into repentance, humility, and freedom.",
        "world_resisted": "Despair, lust, shame, and the false belief that a person is only their past.",
        "lesson": "Repentance is not self-hatred; it is coming home to God.",
        "virtue": "Repentance",
        "theosis": "Repentance opens the whole person to healing, so even wounds can become places of grace.",
        "imitation": "Stop arguing with the past. Turn toward Christ with one honest movement.",
        "small_act": "Name one passion plainly before God without despair or excuse.",
        "reflection": "What false identity must I stop defending so Christ can heal me?",
    },
    {
        "name": "St. Anthony the Great",
        "title": "Father of monasticism",
        "story": "He heard the Gospel command to forsake all and followed Christ into the desert. There he learned that the real battle is the purification of the heart.",
        "martyrdom": "Anthony was not killed as a martyr. His witness is ascetic martyrdom: dying daily to comfort, illusion, and demonic temptation in order to live to Christ.",
        "paschal_thread": "His desert life shows the Cross as voluntary self-denial and the Resurrection as freedom from slavery to the passions.",
        "depth": "Anthony did not go into the desert because the world was merely annoying. He went because Christ was worth everything, and silence exposed what comfort concealed.",
        "world_resisted": "Comfort, distraction, possessions, and the illusion that exterior quiet alone heals the soul.",
        "lesson": "The cave is not escape; it is the place where illusions are exposed before God.",
        "virtue": "Detachment",
        "theosis": "Detachment frees the heart from slavery to created things so it can receive creation as gift.",
        "imitation": "Choose one voluntary simplicity today so the heart can become free.",
        "small_act": "Put away one unnecessary comfort for the length of this rule.",
        "reflection": "What comfort keeps me from the freedom of obedience?",
    },
    {
        "name": "St. Athanasius the Great",
        "title": "Defender of the faith",
        "story": "He suffered exile for confessing the true divinity of Christ. His witness protects the heart from reducing Jesus to an idea, teacher, or mood.",
        "martyrdom": "Athanasius was not killed as a martyr, but he endured repeated exile for the confession of Christ.",
        "paschal_thread": "His witness guards the meaning of the Cross and Resurrection: only the true God-man can heal humanity and raise it into communion with God.",
        "depth": "Athanasius defended doctrine because salvation was at stake. If Christ is not truly God, He cannot unite us to God; if He is not truly man, He has not healed our humanity.",
        "world_resisted": "Reducing Christ to a symbol, moral teacher, or private inspiration.",
        "lesson": "Theosis depends on who Christ truly is: God became man so man might be united to God by grace.",
        "virtue": "Right confession",
        "theosis": "True confession guards true communion: the heart is healed by the living Christ, not by an idea of Christ.",
        "imitation": "Speak to Christ as Lord and God, not as a distant religious idea.",
        "small_act": "Pray the Jesus Prayer slowly, emphasizing 'Son of God.'",
        "reflection": "Do I relate to Christ as living Lord, or only as inspiration?",
    },
    {
        "name": "St. Perpetua and St. Felicity",
        "title": "Martyrs",
        "story": "These young women faced death with courage, refusing to let empire, fear, or family pressure steal their confession of Christ.",
        "martyrdom": "Perpetua and Felicity were martyred in Carthage, exposed to beasts and finally killed by the sword in the arena.",
        "paschal_thread": "Their death witnesses that the Cross is stronger than empire and the Resurrection stronger than fear.",
        "depth": "Their courage was not numbness. It was love trained to stand when every visible pressure demanded surrender.",
        "world_resisted": "Fear, social pressure, empire, and the demand to make safety the highest good.",
        "lesson": "Holy courage is love stronger than fear.",
        "virtue": "Courage",
        "theosis": "Courage is fear purified by love until the soul can obey Christ without needing permission from the world.",
        "imitation": "Let love for Christ be stronger than the pressure to please.",
        "small_act": "Do one faithful thing today without asking whether it will be understood.",
        "reflection": "Where is fear training me to obey something other than Christ?",
    },
    {
        "name": "St. John Chrysostom",
        "title": "Teacher and pastor",
        "story": "He preached repentance, mercy, almsgiving, and the danger of luxury with fearless clarity. His life reminds the soul that worship and justice cannot be separated.",
        "martyrdom": "Chrysostom was not executed, but he died in exile after suffering for pastoral truth and refusal to flatter power.",
        "paschal_thread": "His exile reflects the Cross of truthful love; his hope rests in the risen Christ who vindicates mercy over worldly power.",
        "depth": "Chrysostom would not let worship become aesthetic comfort. The altar and the neighbor belonged together; prayer had to become mercy.",
        "world_resisted": "Luxury, indifference, religious performance, and contempt for the poor.",
        "lesson": "The poor, the wounded, and the difficult neighbor reveal whether prayer has become love.",
        "virtue": "Mercy",
        "theosis": "Mercy makes the soul resemble Christ, who receives, forgives, feeds, and heals.",
        "imitation": "Let prayer become concrete mercy toward another person.",
        "small_act": "Give, encourage, forgive, or serve someone quietly today.",
        "reflection": "What hidden act of mercy should accompany my prayer today?",
    },
    {
        "name": "St. Stephen the Protomartyr",
        "title": "Deacon and first martyr",
        "story": "Stephen served at the tables of the needy and bore witness to Christ with a face full of grace. When accused, he confessed the risen Lord and forgave his killers.",
        "martyrdom": "Stephen was dragged outside the city and stoned. As he died, he prayed that the sin would not be held against those killing him.",
        "paschal_thread": "His martyrdom shows the Cross as forgiveness under violence and the Resurrection as vision of Christ standing at the right hand of God.",
        "depth": "Stephen joins service and witness. He does not choose between mercy for the poor and confession of Christ; both are one life.",
        "world_resisted": "Hatred, accusation, fear of death, and the desire to curse one's enemies.",
        "lesson": "A heart filled with Christ can forgive even while suffering injustice.",
        "virtue": "Forgiving courage",
        "theosis": "Forgiveness makes the soul resemble the crucified Lord.",
        "imitation": "Pray once for someone you are tempted to accuse.",
        "small_act": "Refuse one resentful rehearsal and replace it with the Jesus Prayer.",
        "reflection": "Who needs to be released from my inner court?",
    },
    {
        "name": "St. Moses the Black",
        "title": "Desert father and penitent",
        "story": "Once violent and feared, Moses entered repentance and became a monk known for humility, hospitality, and mercy toward the weak.",
        "martyrdom": "According to tradition, he accepted death without violence when raiders came, refusing to return to the old life of bloodshed.",
        "paschal_thread": "His life is Paschal: the violent man dies, and a merciful father rises in Christ.",
        "depth": "Moses shows that repentance is not cosmetic. Grace can remake the instincts of a person.",
        "world_resisted": "Violence, domination, despair, and identity built on the past.",
        "lesson": "No passion is stronger than the mercy of Christ when repentance becomes obedience.",
        "virtue": "Merciful humility",
        "theosis": "Humility lets divine mercy reshape even old wounds and habits.",
        "imitation": "Answer one provocation with gentleness instead of force.",
        "small_act": "Keep silence when you want to prove you are strong.",
        "reflection": "What old self do I keep protecting instead of burying with Christ?",
    },
    {
        "name": "St. Maximus the Confessor",
        "title": "Confessor of Christ",
        "story": "Maximus defended the truth that Christ has a fully human will healed and united to the divine will. He suffered for refusing a false peace.",
        "martyrdom": "He was not killed immediately, but his tongue and hand were mutilated and he was exiled for his confession.",
        "paschal_thread": "His suffering witnesses that the Cross heals the human will and the Resurrection restores true obedience.",
        "depth": "Maximus matters because salvation reaches the will. Christ heals not only thoughts and feelings, but the deep choosing center of the person.",
        "world_resisted": "False compromise, theological laziness, and peace without truth.",
        "lesson": "The human will is healed by surrender to Christ, not by self-assertion.",
        "virtue": "Confession with endurance",
        "theosis": "Theosis means the human will becoming free enough to say yes to God.",
        "imitation": "Choose one obedience you have been delaying.",
        "small_act": "Say plainly: Not my will, but Thine be done.",
        "reflection": "Where is my will resisting healing?",
    },
    {
        "name": "St. Maria of Paris",
        "title": "Martyr of mercy",
        "story": "Mother Maria served the poor, refugees, and persecuted Jews in Paris, seeing Christ in the suffering neighbor.",
        "martyrdom": "She died in Ravensbruck concentration camp, remembered for self-giving love in a place built to destroy the image of God.",
        "paschal_thread": "Her witness shows the Cross as love entering hellish places and the Resurrection as mercy stronger than dehumanization.",
        "depth": "She refused a spirituality detached from the suffering human person. Mercy was not an idea; it had an address, a face, and a cost.",
        "world_resisted": "Indifference, hatred, nationalism without Christ, and religious escape from mercy.",
        "lesson": "The neighbor in danger is not an interruption to prayer, but a place where Christ waits.",
        "virtue": "Costly mercy",
        "theosis": "Mercy makes room for Christ's own love to act through the person.",
        "imitation": "Notice one person who is easy to ignore.",
        "small_act": "Give practical help, encouragement, or protection without seeking credit.",
        "reflection": "Where is Christ hidden in the person I avoid?",
    },
    {
        "name": "St. Silouan the Athonite",
        "title": "Monk of prayer and humility",
        "story": "Silouan learned the terrible battle against pride and despair, and received the word to keep the mind in hell and despair not.",
        "martyrdom": "He was not killed as a martyr. His witness is the hidden martyrdom of humility, prayer, and love for enemies.",
        "paschal_thread": "His life shows the Cross as descent without despair and the Resurrection as love that prays for the whole world.",
        "depth": "Silouan teaches that humility is not self-loathing. It is truth held inside the mercy of Christ.",
        "world_resisted": "Pride, despair, spiritual comparison, and hatred of enemies.",
        "lesson": "The soul can tell the truth about its darkness without losing hope in Christ.",
        "virtue": "Humility with hope",
        "theosis": "Humility opens the heart to divine love for every person.",
        "imitation": "Pray for one person you dislike or fear.",
        "small_act": "Do not justify yourself for one moment; stand before Christ instead.",
        "reflection": "Can I see my poverty without despairing of mercy?",
    },
]


NICENE_CREED_REFLECTION = {
    "title": "Nicene Creed",
    "note": "The Nicene-Constantinopolitan Creed is the central creed of Orthodox worship and faith.",
    "practice": [
        "Stand or sit still before reading.",
        "Read one line slowly, not as information but as confession.",
        "Pause at the line that resists you, comforts you, or awakens desire.",
        "Answer with: Lord, I believe; help my unbelief.",
    ],
    "lines": [
        "I believe in one God, the Father Almighty, Maker of heaven and earth, and of all things visible and invisible.",
        "And in one Lord Jesus Christ, the Son of God, the Only-begotten, begotten of the Father before all ages.",
        "Light of Light, true God of true God, begotten, not made, of one essence with the Father, by whom all things were made.",
        "Who for us men and for our salvation came down from heaven, and was incarnate of the Holy Spirit and the Virgin Mary, and became man.",
        "And He was crucified for us under Pontius Pilate, and suffered, and was buried.",
        "And the third day He rose again, according to the Scriptures.",
        "And ascended into heaven, and sits at the right hand of the Father.",
        "And He shall come again with glory to judge the living and the dead, whose kingdom shall have no end.",
        "And in the Holy Spirit, the Lord, the Giver of life, who proceeds from the Father.",
        "Who with the Father and the Son together is worshiped and glorified, who spoke by the prophets.",
        "In one, holy, catholic, and apostolic Church.",
        "I acknowledge one baptism for the remission of sins.",
        "I look for the resurrection of the dead, and the life of the age to come. Amen.",
    ],
    "reflection": "Which line of the Creed do I live as theory, but not yet as trust?",
}


APOSTLES_CREED_REFLECTION = {
    "title": "Apostles' Creed",
    "note": "A short ancient Western baptismal creed. Use it here as historical reflection, while keeping the Nicene Creed central for Orthodox practice.",
    "prompt": "What does it mean today to say, with the whole Church, that Christ is Lord of my body, my attention, and my desires?",
}


EARLY_CHURCH_PRAYERS = {
    "Trisagion": "Holy God, Holy Mighty, Holy Immortal, have mercy on us.",
    "Glory": "Glory to the Father, and to the Son, and to the Holy Spirit, now and ever and unto ages of ages. Amen.",
    "Lord's Prayer": "Our Father, who art in heaven, hallowed be Thy name. Thy kingdom come. Thy will be done on earth as it is in heaven.",
    "Jesus Prayer": "Lord Jesus Christ, Son of God, have mercy on me, a sinner.",
}


BEATITUDES = [
    "Blessed are the poor in spirit, for theirs is the kingdom of heaven.",
    "Blessed are those who mourn, for they shall be comforted.",
    "Blessed are the meek, for they shall inherit the earth.",
    "Blessed are those who hunger and thirst for righteousness, for they shall be filled.",
    "Blessed are the merciful, for they shall obtain mercy.",
    "Blessed are the pure in heart, for they shall see God.",
    "Blessed are the peacemakers, for they shall be called sons of God.",
    "Blessed are those who are persecuted for righteousness' sake, for theirs is the kingdom of heaven.",
]


GOSPEL_READINGS = [
    {
        "title": "Abide in Christ",
        "reference": "John 15:4-5",
        "text": "Abide in me, and I in you. As the branch cannot bear fruit of itself, except it abide in the vine; no more can ye, except ye abide in me.",
        "practice": "Read slowly once. Then sit with the word 'abide' before beginning the rule.",
        "carry": "Abide.",
        "question": "Where is Christ asking me to remain instead of escaping?",
    },
    {
        "title": "Come Unto Me",
        "reference": "Matthew 11:28-30",
        "text": "Come unto me, all ye that labour and are heavy laden, and I will give you rest.",
        "practice": "Read as Christ speaking directly to your weariness, not as an idea to analyze.",
        "carry": "Come unto Me.",
        "question": "What burden am I carrying as if Christ has not invited me to Him?",
    },
    {
        "title": "Seek First the Kingdom",
        "reference": "Matthew 6:33-34",
        "text": "Seek ye first the kingdom of God, and his righteousness; and all these things shall be added unto you.",
        "practice": "Name one lesser kingdom you are tempted to serve today.",
        "carry": "Seek first the Kingdom.",
        "question": "Which lesser kingdom is asking for my obedience today?",
    },
    {
        "title": "Take Up the Cross",
        "reference": "Mark 8:34-35",
        "text": "Whosoever will come after me, let him deny himself, and take up his cross, and follow me.",
        "practice": "Ask what small denial of self is being given to you in this rule.",
        "carry": "Take up the cross.",
        "question": "What small self-denial would make room for love?",
    },
    {
        "title": "Blessed Are the Pure in Heart",
        "reference": "Matthew 5:8",
        "text": "Blessed are the pure in heart: for they shall see God.",
        "practice": "Let this reading become a prayer for simplicity and purity of attention.",
        "carry": "Pure in heart.",
        "question": "What divided desire needs to become simple before Christ?",
    },
    {
        "title": "Peace I Leave With You",
        "reference": "John 14:27",
        "text": "Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you.",
        "practice": "Receive peace as communion with Christ, not as control of circumstances.",
        "carry": "My peace I give.",
        "question": "Where am I seeking worldly peace instead of the peace of Christ?",
    },
    {
        "title": "Lose Your Life",
        "reference": "Matthew 16:25",
        "text": "For whosoever will save his life shall lose it: and whosoever will lose his life for my sake shall find it.",
        "practice": "Read this as the pattern of the Cross and Resurrection in daily obedience.",
        "carry": "Lose and find.",
        "question": "What false life am I trying to save?",
    },
    {
        "title": "Watch and Pray",
        "reference": "Matthew 26:41",
        "text": "Watch and pray, that ye enter not into temptation: the spirit indeed is willing, but the flesh is weak.",
        "practice": "Name the temptation without panic. Keep watch with Christ for one small interval.",
        "carry": "Watch and pray.",
        "question": "Where is my weakness asking for watchfulness instead of shame?",
    },
    {
        "title": "Forgive From the Heart",
        "reference": "Matthew 18:21-22",
        "text": "I say not unto thee, Until seven times: but, Until seventy times seven.",
        "practice": "Do not force a feeling. Refuse revenge and ask Christ for mercy.",
        "carry": "Seventy times seven.",
        "question": "Whom am I still holding in debt before my own judgment?",
    },
    {
        "title": "The Narrow Way",
        "reference": "Matthew 7:13-14",
        "text": "Enter ye in at the strait gate... because strait is the gate, and narrow is the way, which leadeth unto life.",
        "practice": "Let today's small rule be the narrow way, not a dramatic display.",
        "carry": "The narrow way.",
        "question": "What broad and easy escape is asking for my soul?",
    },
    {
        "title": "The Hidden Father",
        "reference": "Matthew 6:6",
        "text": "When thou prayest, enter into thy closet, and when thou hast shut thy door, pray to thy Father which is in secret.",
        "practice": "Let the cave become the secret place: no performance, no audience, no spiritual image management.",
        "carry": "Pray in secret.",
        "question": "What part of my spiritual life still wants to be seen?",
    },
    {
        "title": "The Good Shepherd",
        "reference": "John 10:11",
        "text": "I am the good shepherd: the good shepherd giveth his life for the sheep.",
        "practice": "Receive Christ as the One who gives Himself before asking you to give yourself.",
        "carry": "The Shepherd gives His life.",
        "question": "Where do I still live as if I am abandoned?",
    },
    {
        "title": "Deny Yourself",
        "reference": "Luke 9:23",
        "text": "If any man will come after me, let him deny himself, and take up his cross daily, and follow me.",
        "practice": "Ask for the daily cross, not an imagined heroic one.",
        "carry": "Daily cross.",
        "question": "What is today's actual cross, not the one I would have chosen?",
    },
    {
        "title": "Remain in My Love",
        "reference": "John 15:9",
        "text": "As the Father hath loved me, so have I loved you: continue ye in my love.",
        "practice": "Before discipline, receive love. Then let obedience become remaining.",
        "carry": "Continue in My love.",
        "question": "Do I practice discipline as fear, or as remaining in Christ's love?",
    },
    {
        "title": "Not My Will",
        "reference": "Luke 22:42",
        "text": "Nevertheless not my will, but thine, be done.",
        "practice": "Pray this slowly over one place of resistance.",
        "carry": "Thy will be done.",
        "question": "Where is my will asking to be healed by surrender?",
    },
    {
        "title": "It Is Finished",
        "reference": "John 19:30",
        "text": "It is finished.",
        "practice": "Stand before the completed work of Christ. You are not saving yourself by intensity.",
        "carry": "It is finished.",
        "question": "Where am I trying to earn what Christ gives by mercy?",
    },
    {
        "title": "Peace Be Unto You",
        "reference": "John 20:19-21",
        "text": "Peace be unto you: as my Father hath sent me, even so send I you.",
        "practice": "Receive peace from the risen Christ and let it become mission.",
        "carry": "So I send you.",
        "question": "Where is the risen Christ sending me after this rule?",
    },
]


HOLY_DIET_PLANS = {
    "Gentle": {
        "title": "Created Food",
        "plan": "Eat what is simple and close to creation: water, fruit, vegetables, eggs, fish, beans, grains, potatoes, olive oil, nuts, or plain meat if appropriate.",
        "fast": "Turn away from ultra-processed food, excess sugar, and eating for stimulation. Receive enough food to serve with peace.",
        "prayer": "Lord Jesus Christ, teach me to receive food as gift, not entertainment.",
    },
    "Balanced": {
        "title": "Biblical Table",
        "plan": "Keep a plain table: water, bread or grains, legumes, vegetables, fruit, fish, eggs, olive oil, herbs, and simple protein as your rule and health allow.",
        "fast": "Avoid the modern false feast: seed-oil snacks, candy, soda, fast food, constant grazing, and food engineered to inflame appetite.",
        "prayer": "Christ our God, bless this food and make my body ready for prayer, labor, and mercy.",
    },
    "Strong": {
        "title": "Ascetic Table",
        "plan": "Choose a sober plate: water, vegetables, legumes, grains or potatoes, fruit, olive oil, fish, eggs, or simple protein as appropriate.",
        "fast": "Keep a deliberate fast from snacks, sweets, alcohol, fast food, and appetite-driven eating. Do not display the fast.",
        "prayer": "Lord Jesus Christ, free me from appetite as master and make my body a servant of prayer.",
    },
}


BODY_TEMPLE_WORKOUTS = {
    "5 minutes": {
        "title": "Hardstyle Swing Practice",
        "workout": [
            "5 sets of 10 two-hand hardstyle swings",
            "Hike the bell, snap the hips, stand tall, and let the bell float",
            "After each set, park the bell and pray the Jesus Prayer once with attention",
            "Rest until your breathing is calm and your next set can be crisp",
            "If swings are not safe yet, practice 5 sets of 5 kettlebell deadlifts",
        ],
        "kettlebell": "Strength is a skill. Stop every set before form degrades.",
    },
    "15 minutes": {
        "title": "Swings and Get-Ups",
        "workout": [
            "10 sets of 10 hardstyle swings",
            "After every set, pray: Lord Jesus Christ, Son of God, have mercy on me",
            "Rest as needed so every set is powerful, clean, and sober",
            "Then practice 1 Turkish get-up per side, slow and controlled",
            "If get-ups are new, practice only the floor roll-to-elbow and tall sit",
        ],
        "kettlebell": "Use a bell you can master. Do fewer reps before you do ugly reps.",
    },
    "30 minutes": {
        "title": "Simple Strength Rule",
        "workout": [
            "10 sets of 10 hardstyle swings with generous rest",
            "After every set, pray the Jesus Prayer once with attention",
            "Practice 5 Turkish get-ups per side, one rep at a time",
            "Rest between get-ups. Treat each rep as a quiet act of attention",
            "Finish with one minute of standing silence and thanksgiving",
        ],
        "kettlebell": "This is Pavel-inspired hardstyle practice, not exhaustion training. Never go to failure.",
    },
}


REST_OBEDIENCE_BY_TIME = {
    "5 minutes": {
        "title": "Small Restoration",
        "actions": [
            "Drink water slowly and give thanks.",
            "Stand outside or near a window for one minute without the phone.",
            "Stretch the neck, hips, and back gently while praying the Jesus Prayer.",
        ],
        "warning": "Do not call scrolling rest. Let the nervous system become quiet without stimulation.",
    },
    "15 minutes": {
        "title": "Quiet Recovery",
        "actions": [
            "Take a ten-minute walk without headphones if possible.",
            "Drink water and eat only if the body truly needs food.",
            "Sit for two minutes in silence before returning to work or family.",
        ],
        "warning": "Rest is obedience when it restores love, attention, and patience.",
    },
    "30 minutes": {
        "title": "Sabbath in Miniature",
        "actions": [
            "Walk, stretch, or lie down without a screen for twenty minutes.",
            "Prepare simple food or water with thanksgiving.",
            "End with three Jesus Prayers and one act of practical service.",
        ],
        "warning": "Do not punish the body. Discipline and rest both serve communion with Christ.",
    },
}


def get_body_rule(intensity, time, seasonal_thread):
    diet = get_holy_diet(intensity)
    workout = get_body_temple_workout(time)
    rest = REST_OBEDIENCE_BY_TIME.get(time, REST_OBEDIENCE_BY_TIME["5 minutes"])
    return {
        "food": {
            "title": "Food as Thanksgiving, Not Entertainment",
            "rule": diet["plan"],
            "fast": diet["fast"],
            "season": seasonal_thread["fast"],
            "prayer": diet["prayer"],
        },
        "strength": {
            "title": "Strength as Service",
            "name": workout["title"],
            "workout": workout["workout"],
            "kettlebell": workout["kettlebell"],
            "fallback": "If kettlebells are not safe today, do slow squats, wall push-ups, hip hinges, walking, or gentle mobility. Keep the Jesus Prayer between efforts.",
        },
        "rest": rest,
    }


FATHER_TEACHINGS = {
    "Distracted": {
        "father": "St. Theophan the Recluse",
        "teaching": "Bring the mind down into the heart and stand there before the Lord.",
        "practice": "When you notice distraction, do not chase it. Return to the name of Jesus.",
    },
    "Anxious": {
        "father": "St. Seraphim of Sarov",
        "teaching": "Acquire the Spirit of peace, and thousands around you will be saved.",
        "practice": "Seek peace as a gift of the Holy Spirit, not as control over the future.",
    },
    "Tired": {
        "father": "St. Barsanuphius",
        "teaching": "Do what you can, and God will help you.",
        "practice": "Let humility choose a small faithful obedience instead of collapse or display.",
    },
    "Angry": {
        "father": "St. John Chrysostom",
        "teaching": "Nothing makes us so like God as being ready to forgive.",
        "practice": "Refuse the pleasure of accusation. Ask Christ to teach mercy before speech.",
    },
    "Dry": {
        "father": "St. Isaac the Syrian",
        "teaching": "Enter eagerly into the treasure house that is within you.",
        "practice": "Stay before God without demanding felt consolation. Hidden faith is still faith.",
    },
    "Grateful": {
        "father": "St. John Chrysostom",
        "teaching": "Glory be to God for all things.",
        "practice": "Let thanksgiving become hidden service rather than a feeling you possess.",
    },
}


PASSION_VIRTUE_BY_STATE = {
    "Distracted": {
        "passion": "Acedia",
        "description": "Acedia is the restless refusal of the present obedience: boredom, avoidance, scrolling, and flight from prayer.",
        "virtue": "Watchfulness",
        "virtue_description": "Watchfulness gathers the mind into the heart and keeps the soul awake before Christ.",
        "obedience": "Do one necessary task slowly, without checking the phone, and pray the Jesus Prayer when the urge to flee appears.",
    },
    "Anxious": {
        "passion": "Fearful control",
        "description": "Fearful control tries to secure the future without surrendering it to the Father.",
        "virtue": "Trust",
        "virtue_description": "Trust receives enough light for one obedient step and leaves tomorrow with God.",
        "obedience": "Name the fear once, pray once, and do the next concrete act of love before seeking reassurance.",
    },
    "Tired": {
        "passion": "Despondency",
        "description": "Despondency turns weariness into despair, escape, or neglect of the small good at hand.",
        "virtue": "Perseverance",
        "virtue_description": "Perseverance keeps a small flame of obedience without pretending to be strong.",
        "obedience": "Choose the smallest faithful version of the rule, then rest without numbing yourself.",
    },
    "Angry": {
        "passion": "Anger",
        "description": "Anger seeks judgment, victory, and the pleasure of being right more than the healing of communion.",
        "virtue": "Meekness",
        "virtue_description": "Meekness is strength under Christ: truth without cruelty, silence without resentment.",
        "obedience": "Keep silence for one interval, pray for the person involved, and refuse the sentence that would wound.",
    },
    "Dry": {
        "passion": "Unbelief of the heart",
        "description": "Dryness tempts the soul to believe God is absent because felt consolation is absent.",
        "virtue": "Faithfulness",
        "virtue_description": "Faithfulness remains before God without demanding consolation as proof.",
        "obedience": "Keep the prayer briefly and plainly. Offer the dryness itself to Christ.",
    },
    "Grateful": {
        "passion": "Possessiveness",
        "description": "Even gratitude can turn inward when the soul clings to the gift more than the Giver.",
        "virtue": "Thanksgiving",
        "virtue_description": "Thanksgiving returns every gift to God and becomes hidden love for neighbor.",
        "obedience": "Turn one gratitude into one hidden act of service today.",
    },
}


PASSION_VIRTUE_BY_WORLD_PULL = {
    "The feed": {
        "passion": "Acedia",
        "description": "The feed trains the soul to flee silence, prayer, and the present commandment.",
        "virtue": "Watchfulness",
        "virtue_description": "Watchfulness refuses to be dragged by every image and impulse.",
        "obedience": "Keep the phone away until the rule is complete.",
    },
    "Status": {
        "passion": "Vainglory",
        "description": "Vainglory hungers to be seen, praised, noticed, and measured highly.",
        "virtue": "Humility",
        "virtue_description": "Humility is freedom from performing the self before others.",
        "obedience": "Do one good thing today that no one sees.",
    },
    "Comfort": {
        "passion": "Gluttony",
        "description": "Gluttony is not only excess food; it is the rule of comfort over obedience.",
        "virtue": "Temperance",
        "virtue_description": "Temperance receives created things with thanksgiving and restraint.",
        "obedience": "Refuse one unnecessary comfort and receive enough with gratitude.",
    },
    "Distraction": {
        "passion": "Acedia",
        "description": "Distraction scatters the mind so the heart cannot stand before God.",
        "virtue": "Attention",
        "virtue_description": "Attention offers the whole person to Christ in the present moment.",
        "obedience": "Single-task for the length of this rule.",
    },
    "Approval": {
        "passion": "People-pleasing",
        "description": "People-pleasing asks human approval to give the soul what only Christ can give.",
        "virtue": "Holy freedom",
        "virtue_description": "Holy freedom seeks mercy from Christ rather than identity from reaction.",
        "obedience": "Do not check for a reaction, reply, like, or affirmation during the fast.",
    },
    "Control": {
        "passion": "Pride",
        "description": "Pride grasps at mastery and resists receiving life as gift.",
        "virtue": "Surrender",
        "virtue_description": "Surrender entrusts the uncontrollable to the Father without abandoning obedience.",
        "obedience": "Write down one thing you cannot control and pray: Thy will be done.",
    },
    "Lust / Flesh": {
        "passion": "Lust",
        "description": "Lust trains the body and imagination to consume persons instead of receiving them as icons of God.",
        "virtue": "Chastity",
        "virtue_description": "Chastity is not hatred of the body; it is desire healed by Christ so the whole person can love truthfully.",
        "obedience": "Turn the eyes away immediately, stand up, pray the Jesus Prayer, and do one concrete task with the body.",
    },
}


WORLD_RENUNCIATIONS = {
    "The feed": "I turn from the endless feed and return to the living Christ.",
    "Status": "I turn from being seen and return to being known by God.",
    "Comfort": "I turn from comfort as master and receive Christ as life.",
    "Distraction": "I turn from scattered attention and return to the prayer of the heart.",
    "Approval": "I turn from the need for approval and return to the mercy of Jesus.",
    "Control": "I turn from control and entrust myself to the Father.",
    "Lust / Flesh": "I turn from lust and the misuse of the body, and return to Christ who makes the whole man pure.",
}


MONASTIC_DESIRE_WORDS = {
    "Silence": "This longing is a call to make room for the still, small obedience of love.",
    "Purity of heart": "This longing is a call to let the heart become simple before God.",
    "Repentance": "This longing is a call to come home without disguise.",
    "Unceasing prayer": "This longing is a call to let the name of Jesus descend from the lips into the heart.",
    "Simplicity": "This longing is a call to need less so you may love more freely.",
    "Union with Christ": "This longing is a call to theosis: life healed, illumined, and joined to God by grace.",
}


ORTHODOX_POSTURE_BY_MOMENT = {
    "Morning": {
        "invocation": "In the name of the Father, and of the Son, and of the Holy Spirit. Amen.",
        "posture": "Stand if you are able. Face a quiet corner, an icon, or a simple still place.",
        "remembrance": "Begin the day by remembering that your life is hidden with Christ in God.",
        "closing": "Go into the day as one sent to love without display.",
    },
    "Midday": {
        "invocation": "O Heavenly King, Comforter, Spirit of Truth, come and abide in us.",
        "posture": "Pause before continuing your work. Let the body become still before the mind asks to move.",
        "remembrance": "Return the scattered hours to Christ before they become your master.",
        "closing": "Return to your work with a guarded mind and a softened heart.",
    },
    "Evening": {
        "invocation": "Lord Jesus Christ, Light of the world, illumine the darkness of my heart.",
        "posture": "Lower the lights if you can. Sit or stand quietly and let the day become visible before God.",
        "remembrance": "Offer the day back to God without defending, editing, or performing it.",
        "closing": "Let the evening become repentance, thanksgiving, and peace.",
    },
    "Before sleep": {
        "invocation": "Into Your hands, O Lord Jesus Christ, I commend my soul and body.",
        "posture": "Put the phone away from the bed. Sit at the edge of the bed or stand in stillness.",
        "remembrance": "Sleep is a small surrender. Practice entrusting yourself to God.",
        "closing": "Keep silence after this rule if you can. Let the last word be prayer.",
    },
}


THEOSIS_THREADS = {
    "Distracted": "Theosis is not escape from the world, but the healing of attention until the heart can perceive Christ everywhere.",
    "Anxious": "Theosis heals fear by drawing the soul from self-protection into filial trust in the Father.",
    "Tired": "Theosis includes the body: rest can become obedience when it restores the capacity for love.",
    "Angry": "Theosis makes mercy possible where the passions demand judgment, victory, and self-defense.",
    "Dry": "Theosis often grows without felt consolation; hidden faithfulness purifies love from the need for reward.",
    "Grateful": "Theosis turns gratitude into participation, so that every gift becomes communion with the Giver.",
}


CROSS_RESURRECTION_THREADS = {
    "Distracted": {
        "cross": "The Cross interrupts scattered desire: not every impulse gets to rule you.",
        "resurrection": "The Resurrection gathers the mind into living attention before Christ.",
        "practice": "Let one distraction die without obeying it; return once to the Jesus Prayer.",
    },
    "Anxious": {
        "cross": "The Cross is surrender of control into the hands of the Father.",
        "resurrection": "The Resurrection is the promise that fear does not have the final word.",
        "practice": "Name one fear, release it to Christ, and do the next act of love.",
    },
    "Tired": {
        "cross": "The Cross receives weakness without shame or escape.",
        "resurrection": "The Resurrection restores the person for love, not performance.",
        "practice": "Choose sober rest instead of numbing stimulation.",
    },
    "Angry": {
        "cross": "The Cross refuses revenge and bears the wound without becoming hatred.",
        "resurrection": "The Resurrection opens the possibility of mercy where judgment felt final.",
        "practice": "Let one accusation die before it becomes speech.",
    },
    "Dry": {
        "cross": "The Cross remains faithful when consolation is absent.",
        "resurrection": "The Resurrection is hidden life rising beneath dry obedience.",
        "practice": "Keep the prayer without demanding felt consolation.",
    },
    "Grateful": {
        "cross": "The Cross gives the gift back to God instead of possessing it.",
        "resurrection": "The Resurrection turns gratitude into generous life.",
        "practice": "Make one thanksgiving into hidden service.",
    },
}


WATCHFULNESS_BY_STATE = {
    "Distracted": "When the mind wanders, do not scold it. Bring it back gently with the Jesus Prayer.",
    "Anxious": "When fear predicts the future, answer only with the present commandment of love.",
    "Tired": "When exhaustion asks for stimulation, choose quiet restoration before entertainment.",
    "Angry": "When the wound begins to argue, keep silence until mercy can speak truthfully.",
    "Dry": "When prayer feels empty, remain before God without bargaining for feeling.",
    "Grateful": "When gratitude becomes excitement, let it become hidden service.",
}


SENSE_GUARD_BY_RENUNCIATION = {
    "Noise": "Guard the ear: refuse background sound for the length of the rule.",
    "Comparison": "Guard the eye: do not look at another person's life as a measure of your own soul.",
    "Outrage": "Guard the tongue: do not rehearse accusation, even inwardly, during the rule.",
    "Vanity": "Guard the face: do not seek to be seen, praised, noticed, or affirmed.",
    "Escape": "Guard the feet: remain with the next faithful action instead of fleeing into novelty.",
    "Lust": "Guard the eyes and imagination: turn away before the image becomes consent.",
}


PURITY_RULES = {
    "Gentle": {
        "title": "Return Without Despair",
        "watch": "Do not argue with the image, fantasy, or urge. Turn away at once and say the Jesus Prayer once.",
        "body": "Stand up, drink water, and move to a public or well-lit place if possible.",
        "mind": "Do not study or narrate the temptation. Refuse it attention and turn the mind to the name of Jesus.",
        "repair": "If you fell, do not spiral or rehearse it. Get up, restore a clean boundary, and seek spiritual guidance when the pattern persists. Despair is not repentance.",
    },
    "Balanced": {
        "title": "Custody of the Eyes",
        "watch": "Guard the first look. The second look is where consent begins to bargain.",
        "body": "Take a brisk walk, do ten slow squats, or complete one necessary task immediately.",
        "mind": "Refuse secrecy and negotiation. Turn the mind to Christ before the image becomes a private world.",
        "repair": "Remove one near occasion: app, search, account, habit, or private setting that repeatedly opens the door.",
    },
    "Strong": {
        "title": "Cut Off the Occasion",
        "watch": "Do not make peace with the trigger. Cut off access quickly and without drama.",
        "body": "Cold water on the face, hard walk, kettlebell deadlifts, or physical labor until the body is obedient and calm.",
        "mind": "Remember the Cross: desire is not killed by shame, but crucified and raised as chastity.",
        "repair": "Make a concrete boundary today. Tell a trusted Christian man, priest, or mentor if this has become a pattern. Do not keep a private kingdom of unreality.",
    },
}


def get_purity_rule(intensity):
    return PURITY_RULES.get(intensity, PURITY_RULES["Gentle"])


SENSE_GUARD_BY_STATE = {
    "Distracted": "Guard the eye: let one thing be enough.",
    "Anxious": "Guard the imagination: do not obey imagined futures.",
    "Tired": "Guard the body: do not confuse stimulation with rest.",
    "Angry": "Guard the tongue: let no sharp word become your prayer.",
    "Dry": "Guard the will: remain faithful without demanding consolation.",
    "Grateful": "Guard the gift: give thanks without possessing the moment.",
}


EXAMEN_BY_STATE = {
    "Distracted": [
        "Where did my attention become divided?",
        "Where did I remember Christ, even briefly?",
        "What must be simplified before tomorrow so obedience can become possible?",
    ],
    "Anxious": [
        "What fear did I treat as lord?",
        "Where did God offer enough light for one step?",
        "What can I entrust back to the Father tonight?",
    ],
    "Tired": [
        "What did my body reveal truthfully today?",
        "Where did I confuse usefulness with faithfulness?",
        "What form of rest would make love possible again?",
    ],
    "Angry": [
        "What wound did I defend today?",
        "Where did mercy try to interrupt me?",
        "Whom must I release from the court of my own judgment?",
    ],
    "Dry": [
        "What small faithfulness remained when feeling was absent?",
        "Where did I seek consolation apart from God?",
        "What can I offer without felt consolation?",
    ],
    "Grateful": [
        "Which gift did I receive today?",
        "Did gratitude turn me outward in love?",
        "How can thanksgiving become offering tomorrow?",
    ],
}


def get_posture(moment):
    return ORTHODOX_POSTURE_BY_MOMENT[moment]


def get_world_renunciation(world_pull):
    return WORLD_RENUNCIATIONS.get(world_pull, "I turn from the world and return to Christ.")


def get_monastic_desire_word(longing):
    return MONASTIC_DESIRE_WORDS.get(
        longing,
        "This longing is a call to seek Christ with the whole heart.",
    )


def get_theosis_thread(state):
    return THEOSIS_THREADS.get(state, "Theosis is the healing of the whole person by communion with God.")


def get_cross_resurrection_thread(state):
    return CROSS_RESURRECTION_THREADS.get(
        state,
        {
            "cross": "The Cross is the death of the old life that cannot inherit the Kingdom.",
            "resurrection": "The Resurrection is new life in Christ, already beginning in the heart.",
            "practice": "Let one old impulse die and do one act of risen obedience.",
        },
    )


def get_watchfulness(state):
    return WATCHFULNESS_BY_STATE.get(state, "Return to Christ with attention and peace.")


def get_sense_guard(state, renunciation=None):
    if renunciation:
        return SENSE_GUARD_BY_RENUNCIATION.get(renunciation, SENSE_GUARD_BY_STATE.get(state))

    return SENSE_GUARD_BY_STATE.get(state, "Guard the senses and return to prayer.")


def get_examen(state):
    return EXAMEN_BY_STATE.get(
        state,
        [
            "Where did I turn toward Christ?",
            "Where did I turn away?",
            "What is the next small obedience?",
        ],
    )


def get_daily_beatitude(rule_id):
    return BEATITUDES[(rule_id - 1) % len(BEATITUDES)]


def get_chamber_map():
    return CHAMBER_MAP


def get_chamber_stages():
    return CHAMBER_STAGES


def get_seasonal_thread(season):
    return SEASONAL_THREADS.get(season, SEASONAL_THREADS["Daily"])


def get_daily_witness(day_number):
    return SAINT_WITNESSES[(day_number - 1) % len(SAINT_WITNESSES)]


def get_creed_reflections():
    return {
        "nicene": NICENE_CREED_REFLECTION,
        "apostles": APOSTLES_CREED_REFLECTION,
    }


def get_scripture_reading(rule_id):
    return GOSPEL_READINGS[(rule_id - 1) % len(GOSPEL_READINGS)]


def get_ancient_prayer(moment):
    if moment == "Morning":
        return ("Trisagion", EARLY_CHURCH_PRAYERS["Trisagion"])
    if moment == "Midday":
        return ("Lord's Prayer", EARLY_CHURCH_PRAYERS["Lord's Prayer"])
    if moment == "Evening":
        return ("Glory", EARLY_CHURCH_PRAYERS["Glory"])
    return ("Jesus Prayer", EARLY_CHURCH_PRAYERS["Jesus Prayer"])


def get_father_teaching(state):
    return FATHER_TEACHINGS.get(
        state,
        {
            "father": "The Fathers",
            "teaching": "Return to Christ with humility, attention, and love.",
            "practice": "Keep the next small obedience.",
        },
    )


def get_passion_virtue(state, world_pull=None):
    if world_pull in PASSION_VIRTUE_BY_WORLD_PULL:
        return PASSION_VIRTUE_BY_WORLD_PULL[world_pull]

    return PASSION_VIRTUE_BY_STATE.get(
        state,
        {
            "passion": "Disorder of the heart",
            "description": "The passions pull the heart away from communion with God.",
            "virtue": "Repentance",
            "virtue_description": "Repentance turns the whole person back toward Christ.",
            "obedience": "Keep the next small commandment with humility.",
        },
    )


def get_little_typikon(moment, rule, passion_virtue):
    return [
        {
            "hour": "Morning",
            "rule": "Begin with the sign of the Cross, the Trisagion or Jesus Prayer, and the Gospel reading.",
        },
        {
            "hour": "Labor",
            "rule": f"Work with attention. Fight {passion_virtue['passion'].lower()} by keeping one task before God.",
        },
        {
            "hour": "Body",
            "rule": f"Keep the {rule['time']} body rule, eat simply, and let strength serve prayer.",
        },
        {
            "hour": "Mercy",
            "rule": "Do one hidden act of love without announcing it or seeking return.",
        },
        {
            "hour": "Evening",
            "rule": "Make a short examen: where did I turn toward Christ, and where did I turn away?",
        },
        {
            "hour": "Sleep",
            "rule": "Put the phone away from the bed. Let the last words be the Jesus Prayer.",
        },
    ]


def get_holy_diet(intensity):
    return HOLY_DIET_PLANS.get(intensity, HOLY_DIET_PLANS["Gentle"])


def get_body_temple_workout(time):
    return BODY_TEMPLE_WORKOUTS.get(time, BODY_TEMPLE_WORKOUTS["5 minutes"])
