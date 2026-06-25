import json
import base64
import time
from datetime import datetime
from pathlib import Path

import streamlit as st

from fathers import (
    get_father_by_name,
    get_father_trails,
    get_readings_for_father,
    get_source_collections,
    get_trail_by_name,
)
from orthodox import (
    LITURGICAL_MOMENTS,
    LITURGICAL_SEASONS,
    MONASTIC_LONGINGS,
    WORLD_PULLS,
    get_ancient_prayer,
    get_body_rule,
    get_chamber_stages,
    get_creed_reflections,
    get_cross_resurrection_thread,
    get_daily_beatitude,
    get_daily_witness,
    get_examen,
    get_father_teaching,
    get_little_typikon,
    get_monastic_desire_word,
    get_passion_virtue,
    get_posture,
    get_purity_rule,
    get_sense_guard,
    get_seasonal_thread,
    get_scripture_reading,
    get_theosis_thread,
    get_watchfulness,
    get_world_renunciation,
)
from rules import INTENSITIES, SCROLL_STATES, SOUL_STATES, TIME_OPTIONS, get_rule, get_scroll_rule
from theme import apply_theme


STILLNESS_SECONDS = 10
ASSETS_DIR = Path("assets")
COVER_IMAGE_PATH = ASSETS_DIR / "the-inner-monk-cover.png"
COVER_IMAGE_FALLBACK_PATH = ASSETS_DIR / "the-inner-monk-cover.png.png"
REFLECTIONS_PATH = Path("data") / "reflections.jsonl"
EXAMEN_PATH = Path("data") / "examen.jsonl"
FATHERS_PROGRESS_PATH = Path("data") / "fathers_progress.json"
RENUNCIATIONS = ["Noise", "Comparison", "Outrage", "Vanity", "Escape", "Lust"]
DIGITAL_FAST_OPTIONS = [
    "15 minutes",
    "1 hour",
    "Until evening",
    "Until tomorrow morning",
]
PRAYER_ROPE_OPTIONS = [12, 33, 50]


def silence_seconds_for_rule(rule):
    return minutes_from_label(rule["time"]) * 60


def format_silence_time(seconds):
    minutes = seconds // 60
    remainder = seconds % 60
    return f"{minutes:02d}:{remainder:02d}"


def get_cover_image_path():
    if COVER_IMAGE_PATH.exists():
        return COVER_IMAGE_PATH
    if COVER_IMAGE_FALLBACK_PATH.exists():
        return COVER_IMAGE_FALLBACK_PATH
    return None


def get_cover_image_data_uri():
    cover_path = get_cover_image_path()
    if not cover_path:
        return ""
    image_bytes = cover_path.read_bytes()
    encoded = base64.b64encode(image_bytes).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def default_fathers_progress():
    return {
        "current_trail": None,
        "current_father_by_trail": {},
        "read_fathers": [],
        "notes": {},
    }


def read_fathers_progress():
    if not FATHERS_PROGRESS_PATH.exists():
        return default_fathers_progress()
    try:
        with FATHERS_PROGRESS_PATH.open("r", encoding="utf-8") as file:
            loaded = json.load(file)
    except (json.JSONDecodeError, OSError):
        return default_fathers_progress()

    progress = default_fathers_progress()
    progress.update(loaded)
    progress["read_fathers"] = list(dict.fromkeys(progress.get("read_fathers", [])))
    progress["current_father_by_trail"] = progress.get("current_father_by_trail", {})
    progress["notes"] = progress.get("notes", {})
    return progress


def save_fathers_progress(progress):
    FATHERS_PROGRESS_PATH.parent.mkdir(exist_ok=True)
    with FATHERS_PROGRESS_PATH.open("w", encoding="utf-8") as file:
        json.dump(progress, file, ensure_ascii=True, indent=2)


def render_fathers_library():
    father_trails = get_father_trails()
    source_collections = get_source_collections()
    progress = read_fathers_progress()

    st.markdown(
        """
        <div class="cell-note chamber-note">
            <p class="kicker">Church history path</p>
            <p>
                A quiet library for self-exploration outside the daily chamber.
                Walk with the Fathers, martyrs, confessors, and teachers who guarded
                the faith of Christ through blood, exile, prayer, and doctrine.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    trail_names = [trail["name"] for trail in father_trails]
    saved_trail = progress.get("current_trail")
    default_trail_index = trail_names.index(saved_trail) if saved_trail in trail_names else 0
    selected_path = st.selectbox(
        "Choose a historical trail",
        trail_names,
        index=default_trail_index,
    )
    trail = get_trail_by_name(selected_path)
    path_names = trail["fathers"]
    path_fathers = [get_father_by_name(name) for name in path_names]
    read_fathers = set(progress.get("read_fathers", []))
    trail_read_count = sum(1 for name in path_names if name in read_fathers)

    if progress.get("current_trail") != selected_path:
        progress["current_trail"] = selected_path
        progress["current_father_by_trail"].setdefault(selected_path, path_names[0])
        save_fathers_progress(progress)

    saved_father = progress["current_father_by_trail"].get(selected_path, path_names[0])
    if saved_father not in path_names:
        saved_father = path_names[0]
    current_index = path_names.index(saved_father)

    st.markdown(
        f"""
        <div class="fathers-path-card">
            <p class="kicker">{selected_path}</p>
            <h3>{trail['subtitle']}</h3>
            <p>{trail['description']}</p>
            <p class="trail-progress">{trail_read_count} of {len(path_names)} read in this trail.</p>
            <div class="trail-steps">
                {''.join(f'<span class="{"read" if name in read_fathers else ""} {"active" if name == saved_father else ""}">{name}</span>' for name in path_names)}
            </div>
            <p>Read slowly. This is not trivia. Let the Church's memory judge the modern mind and call the heart back to Christ.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nav_col_1, nav_col_2, nav_col_3 = st.columns(3)
    if nav_col_1.button("Previous Father", use_container_width=True, disabled=current_index == 0):
        previous_name = path_names[current_index - 1]
        progress["current_father_by_trail"][selected_path] = previous_name
        save_fathers_progress(progress)
        st.rerun()
    if nav_col_2.button("Continue Trail", use_container_width=True):
        progress["current_father_by_trail"][selected_path] = saved_father
        save_fathers_progress(progress)
        st.rerun()
    if nav_col_3.button("Next Father", use_container_width=True, disabled=current_index == len(path_names) - 1):
        next_name = path_names[current_index + 1]
        progress["current_father_by_trail"][selected_path] = next_name
        save_fathers_progress(progress)
        st.rerun()

    selected_father_name = st.selectbox(
        "Choose a Father in this trail",
        path_names,
        index=path_names.index(saved_father),
    )
    if selected_father_name != saved_father:
        progress["current_father_by_trail"][selected_path] = selected_father_name
        save_fathers_progress(progress)
        saved_father = selected_father_name
    father = get_father_by_name(selected_father_name)
    readings = get_readings_for_father(father["name"])
    father_note = progress.get("notes", {}).get(father["name"], "")
    is_read = father["name"] in read_fathers

    st.markdown(
        f"""
        <div class="father-profile">
            <p class="kicker">{father['period']} / {father['dates']}</p>
            <h3>{father['name']}</h3>
            <p class="father-theme">{father['theme']}</p>
            <section>
                <span>Story</span>
                <p>{father['story']}</p>
            </section>
            <section>
                <span>Witness</span>
                <p>{father['witness']}</p>
            </section>
            <section>
                <span>Cross and Resurrection</span>
                <p>{father['cross_resurrection']}</p>
            </section>
            <section>
                <span>Why it matters</span>
                <p>{father['why_it_matters']}</p>
            </section>
            <section>
                <span>Read for</span>
                <p>{father['read_for']}</p>
            </section>
            <section>
                <span>Suggested readings</span>
                <div class="reading-list">
                    {''.join(
                        f'<article><strong>{reading["title"]}</strong>'
                        f'<p>{reading["context"]}</p><em>{reading["why"]}</em>'
                        + (
                            f'<a href="{reading["source_url"]}" target="_blank" rel="noopener noreferrer">{reading["source_label"]}</a>'
                            if reading["source_url"]
                            else '<small>Use the bibliography below to locate a reliable edition.</small>'
                        )
                        + '</article>'
                        for reading in readings
                    )}
                </div>
            </section>
            <section>
                <span>Reflection</span>
                <p>{father['reflection']}</p>
            </section>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Sources and bibliography"):
        st.write(
            "The stories are concise formation summaries. For study, check the primary text, "
            "an Orthodox saint life, and a reputable published translation."
        )
        for source in source_collections:
            st.markdown(
                f"**[{source['name']}]({source['url']})**  \n{source['description']}"
            )

    mark_col, note_col = st.columns([1, 2])
    if mark_col.button(
        "Mark as Read" if not is_read else "Read",
        use_container_width=True,
        disabled=is_read,
    ):
        progress["read_fathers"] = list(dict.fromkeys(progress.get("read_fathers", []) + [father["name"]]))
        progress["current_father_by_trail"][selected_path] = father["name"]
        save_fathers_progress(progress)
        st.rerun()

    with note_col:
        with st.form(f"father_note_{father['name']}"):
            note = st.text_area(
                "Private note for this Father",
                value=father_note,
                placeholder="What did this witness expose, strengthen, or call forth?",
            )
            note_saved = st.form_submit_button("Save Note", use_container_width=True)
        if note_saved:
            progress["notes"][father["name"]] = note.strip()
            progress["current_father_by_trail"][selected_path] = father["name"]
            save_fathers_progress(progress)
            st.success("Saved privately.")

    st.caption("These summaries are a study doorway, not a substitute for primary texts, parish life, confession, or guidance from a priest/spiritual father.")

COUNSEL_BY_INTENSITY = {
    "Gentle": "Receive this rule as mercy. Let Christ heal what cannot be forced.",
    "Balanced": "Keep the rule soberly. Let attention become obedience under the Cross.",
    "Strong": "Carry the rule plainly. Let the old escape die and keep the commandment before you.",
}

RESPONSE_BY_STATE = {
    "Distracted": "Gather the mind into the heart.",
    "Anxious": "Return fear to the Father.",
    "Tired": "Choose true rest over stimulation.",
    "Angry": "Let mercy interrupt the wound.",
    "Dry": "Stay faithful without felt consolation.",
    "Grateful": "Turn thanks into offering.",
}

ASCETIC_AIM_BY_STATE = {
    "Distracted": {
        "healing": "scattered attention",
        "virtue": "watchfulness",
    },
    "Anxious": {
        "healing": "fearful control",
        "virtue": "trust",
    },
    "Tired": {
        "healing": "restless exhaustion",
        "virtue": "sober rest",
    },
    "Angry": {
        "healing": "resentment",
        "virtue": "meekness",
    },
    "Dry": {
        "healing": "spiritual dullness",
        "virtue": "faithfulness",
    },
    "Grateful": {
        "healing": "possessiveness",
        "virtue": "thanksgiving",
    },
}

RENUNCIATION_AIMS = {
    "Noise": "the need to fill silence",
    "Comparison": "measuring the soul against others",
    "Outrage": "the pleasure of judgment",
    "Vanity": "the hunger to be seen",
    "Escape": "flight from the present commandment",
    "Lust": "desire detached from love, covenant, and communion",
}


def minutes_from_label(time_label):
    return int(time_label.split()[0])


def exit_instruction(rule):
    minutes = minutes_from_label(rule["time"])
    return (
        f"Leave this screen now. Keep the rule for {minutes} minutes before returning "
        "to any feed, inbox, stream, or noise."
    )


def digital_fast_vow(duration):
    return (
        f"By God's mercy, I will keep away from the feed for {duration.lower()}. "
        "I will not trade prayer for scrolling."
    )


def daily_oath_of_service(rule, passion_virtue, watchword):
    return {
        "love": (
            "Jesus Christ has loved me first, sought me in my wandering, borne the Cross, "
            "and opened the way of risen life. I do not stand to earn His love. I stand because I have received it."
        ),
        "allegiance": (
            "Today I give my attention, body, strength, speech, work, and desire to Jesus Christ, "
            "my Lord and King."
        ),
        "renunciation": (
            f"I refuse the rule of {passion_virtue['passion'].lower()}, the false promises of the world, "
            "and every habit that makes me less able to love."
        ),
        "service": (
            f"I will practice {passion_virtue['virtue'].lower()} through prayer, chastity, courage, mercy, "
            "truth, useful labor, and protection of what God has entrusted to me."
        ),
        "watchword": watchword,
        "seal": "The Cross before me. The risen Christ within me. The next obedience beneath my feet.",
    }


KNIGHTLY_RULE = [
    ("Allegiance", "Christ alone is Lord. No appetite, feed, fear, status, or approval may take His place."),
    ("Watchfulness", "Guard the eyes, imagination, tongue, and attention as gates entrusted by the King."),
    ("Courage", "Do the difficult good without display, self-pity, cruelty, or escape."),
    ("Mercy", "Strength is given to protect, forgive, serve, and lift burdens, never to despise another person."),
    ("Faithfulness", "Keep the next commandment in the ordinary place where Christ has stationed you."),
]


def cell_path():
    return [
        "Opening",
        "Cave Map",
        "Daily Order",
        "Witness",
        "Prayer Corner",
        "Renunciation",
        "Passion",
        "Cross and Resurrection",
        "Scripture",
        "Creed",
        "Prayer",
        "Prayer Rope",
        "Body Temple",
        "Purity",
        "Practice",
        "Return",
        "Vigil and Oath",
        "Depart",
    ]


def primary_cell_path():
    return [
        "Opening",
        "Prayer",
        "Scripture",
        "Body Temple",
        "Purity",
        "Return",
        "Vigil and Oath",
        "Depart",
    ]


def visible_path_steps(active_step):
    primary_steps = primary_cell_path()
    if active_step in primary_steps:
        return primary_steps

    if active_step in ["Cave Map", "Daily Order", "Witness", "Prayer Corner", "Renunciation", "Passion", "Cross and Resurrection", "Creed", "Prayer Rope", "Practice"]:
        return ["Opening", active_step, "Prayer", "Scripture", "Body Temple", "Purity", "Return", "Vigil and Oath", "Depart"]

    return primary_steps


def current_cell_step():
    step = st.session_state.cell_step
    return max(0, min(step, len(cell_path()) - 1))


def chamber_step_index(chamber_name):
    chamber_to_step = {
        "Mouth": "Renunciation",
        "Daily Order": "Daily Order",
        "Witness": "Witness",
        "Scripture": "Scripture",
        "Cross": "Cross and Resurrection",
        "Creed": "Creed",
        "Body": "Body Temple",
        "Purity": "Purity",
        "Passion": "Passion",
        "Prayer": "Prayer",
        "Seal": "Vigil and Oath",
        "Vigil and Oath": "Vigil and Oath",
        "Return": "Return",
        "Examen": "Return",
        "Departure": "Depart",
    }
    step_name = chamber_to_step.get(chamber_name)
    if step_name in cell_path():
        return cell_path().index(step_name)
    return 0


def next_path_step_index(active_step):
    primary_steps = primary_cell_path()
    if active_step in primary_steps:
        active_index = primary_steps.index(active_step)
        if active_index < len(primary_steps) - 1:
            return cell_path().index(primary_steps[active_index + 1])
        return cell_path().index(active_step)

    full_steps = cell_path()
    active_index = full_steps.index(active_step)
    return min(len(full_steps) - 1, active_index + 1)


def previous_path_step_index(active_step):
    primary_steps = primary_cell_path()
    if active_step in primary_steps:
        active_index = primary_steps.index(active_step)
        if active_index > 0:
            return cell_path().index(primary_steps[active_index - 1])
        return cell_path().index(active_step)

    full_steps = cell_path()
    active_index = full_steps.index(active_step)
    return max(0, active_index - 1)


def rule_seal(rule):
    response = RESPONSE_BY_STATE.get(rule["state"], "Return to Christ.")
    return f"Today I will {response.lower()} through the Cross and Resurrection of Jesus Christ. Lord, have mercy."


def daily_watchword(rule, passion_virtue, cross_thread):
    passion = passion_virtue["passion"].lower()
    virtue = passion_virtue["virtue"].lower()

    if st.session_state.world_pull == "The feed":
        return "Do not negotiate with the feed; return to Christ before the impulse becomes consent."
    if st.session_state.world_pull == "Lust / Flesh":
        return "Turn the eyes away, let lust die under the Cross, and carry desire back to Christ."
    if rule["state"] == "Anxious":
        return "Release control to the Father and do the next act of love."
    if rule["state"] == "Angry":
        return "Let accusation die before it becomes speech; answer the wound with mercy."
    if rule["state"] == "Tired":
        return "Choose sober rest, not stimulation, so the body can rise again for love."
    if rule["state"] == "Dry":
        return "Keep the prayer without demanding consolation; hidden faith is still faith."

    return f"Let {passion} be crucified, and practice {virtue} as risen obedience."


def departure_rule(rule, cross_thread):
    season = get_seasonal_thread(st.session_state.liturgical_season)
    return {
        "seal": rule_seal(rule),
        "cross": cross_thread["practice"],
        "resurrection": season["departure"],
        "digital": digital_fast_vow(st.session_state.digital_fast),
        "body": rule["body"],
        "carry": "Lord Jesus Christ, Son of God, have mercy on me.",
        "command": exit_instruction(rule),
    }


def prayer_rope_mode(target):
    if target == 12:
        return {
            "name": "Emergency Return",
            "meaning": "A short return when the mind is scattered, tempted, or reaching for the feed.",
            "section": "Pause briefly after every 4 prayers.",
        }
    if target == 33:
        return {
            "name": "Short Cell Rule",
            "meaning": "A sober rule for gathering attention and placing the heart before Christ.",
            "section": "Pause briefly after every 11 prayers.",
        }
    return {
        "name": "Watchfulness Rule",
        "meaning": "A stronger rule for patient attention without hurry or spiritual display.",
        "section": "Pause briefly after every 10 prayers.",
    }


def father_teaching_repeats(rule, father_teaching):
    father_line = rule["father"].lower()
    return (
        father_teaching["father"].lower() in father_line
        and father_teaching["teaching"].lower() in father_line
    )


def ascetic_aim(rule, renunciation=None):
    aim = ASCETIC_AIM_BY_STATE.get(
        rule["state"],
        {"healing": "disorder in the heart", "virtue": "attention to Christ"},
    )
    healing = aim["healing"]
    if renunciation:
        healing = RENUNCIATION_AIMS.get(renunciation, healing)

    return {
        "healing": healing,
        "virtue": aim["virtue"],
    }


def lesser_obedience(rule):
    if rule["time"] == "5 minutes":
        return "Pray the Jesus Prayer three times and keep one minute of silence."
    if rule["intensity"] == "Strong":
        return "Keep the same rule for fifteen minutes instead of thirty, without resentment."
    if rule["intensity"] == "Balanced":
        return "Keep the prayer and mind discipline first; let the body discipline be simple."
    return "Do the smallest faithful version with peace."


def plain_text_rule(rule, renunciation=None):
    aim = ascetic_aim(rule, renunciation)
    posture = get_posture(st.session_state.liturgical_moment)
    examen = get_examen(rule["state"])
    prayer_name, ancient_prayer = get_ancient_prayer(st.session_state.liturgical_moment)
    father_teaching = get_father_teaching(rule["state"])
    scripture_reading = get_scripture_reading(rule["id"])
    witness = get_daily_witness(datetime.now().timetuple().tm_yday + rule["id"])
    creeds = get_creed_reflections()
    cross_thread = get_cross_resurrection_thread(rule["state"])
    seasonal_thread = get_seasonal_thread(st.session_state.liturgical_season)
    body_rule = get_body_rule(rule["intensity"], rule["time"], seasonal_thread)
    purity_rule = get_purity_rule(rule["intensity"])
    rope_mode = prayer_rope_mode(st.session_state.prayer_rope_target)
    departure = departure_rule(rule, cross_thread)
    passion_virtue = get_passion_virtue(rule["state"], st.session_state.world_pull)
    watchword = daily_watchword(rule, passion_virtue, cross_thread)
    oath = daily_oath_of_service(rule, passion_virtue, watchword)
    little_typikon = get_little_typikon(st.session_state.liturgical_moment, rule, passion_virtue)
    return "\n".join(
        [
            "The Inner Monk",
            "A daily practice of theosis.",
            "",
            "Today's Rule",
            f"{st.session_state.liturgical_moment} / {st.session_state.liturgical_season} / {rule['intensity']} / {rule['state']} / {rule['time']}",
            seasonal_thread["tone"],
            f"Watchword: {watchword}",
            "",
            "Daily Oath of Service",
            oath["love"],
            oath["allegiance"],
            oath["renunciation"],
            oath["service"],
            f"Seal: {oath['seal']}",
            "",
            "Rule of Spiritual Chivalry",
            *[f"{name}: {meaning}" for name, meaning in KNIGHTLY_RULE],
            "",
            "Ascetic Aim",
            f"Healing: {aim['healing']}",
            f"Virtue: {aim['virtue']}",
            "",
            "Opening",
            posture["invocation"],
            posture["posture"],
            posture["remembrance"],
            "",
            "Today's Little Typikon",
            *[f"{item['hour']}: {item['rule']}" for item in little_typikon],
            "",
            "Witness of the Day",
            f"{witness['name']} - {witness['title']}",
            witness["story"],
            f"Martyrdom/witness: {witness.get('martyrdom', 'This witness reveals a life offered to Christ.')}",
            f"Cross and Resurrection: {witness.get('paschal_thread', 'The witness is understood through the Cross and Resurrection of Christ.')}",
            f"Lesson: {witness['lesson']}",
            f"Deeper reading: {witness.get('depth', 'This witness reveals one concrete way the life of Christ can be formed in a human person.')}",
            f"World resisted: {witness.get('world_resisted', 'The spirit of the world that pulls the heart away from Christ.')}",
            f"Virtue: {witness.get('virtue', 'Faithfulness')}",
            f"Theosis thread: {witness.get('theosis', 'This virtue heals the heart and makes room for communion with Christ.')}",
            f"Imitation: {witness.get('imitation', 'Keep one small obedience to Christ without display.')}",
            f"Small act: {witness.get('small_act', 'Do one hidden act of prayer, mercy, or restraint today.')}",
            f"Reflection: {witness['reflection']}",
            "",
            "Prayer Corner",
            "Stand before God without images on the screen. Let the room become quiet before the heart begins to pray.",
            "",
            "Leaving the World",
            get_world_renunciation(st.session_state.world_pull),
            get_monastic_desire_word(st.session_state.monastic_longing),
            "",
            "Digital Fast Vow",
            digital_fast_vow(st.session_state.digital_fast),
            "",
            "Passion and Virtue",
            f"Passion: {passion_virtue['passion']}",
            passion_virtue["description"],
            f"Virtue: {passion_virtue['virtue']}",
            passion_virtue["virtue_description"],
            f"Small obedience: {passion_virtue['obedience']}",
            "",
            "Cross and Resurrection",
            f"Cross: {cross_thread['cross']}",
            f"Resurrection: {cross_thread['resurrection']}",
            f"Practice: {cross_thread['practice']}",
            f"Seasonal cross: {seasonal_thread['cross']}",
            f"Seasonal resurrection: {seasonal_thread['resurrection']}",
            "",
            "Scripture Reading",
            f"{scripture_reading['title']} ({scripture_reading['reference']})",
            scripture_reading["text"],
            scripture_reading["practice"],
            f"Word to carry: {scripture_reading['carry']}",
            scripture_reading["question"],
            "",
            "Prayer Focus",
            f"Ancient prayer ({prayer_name}): {ancient_prayer}",
            f"Daily Beatitude: {get_daily_beatitude(rule['id'])}",
            f"Gospel saying: {rule['scripture']}",
            f"Church Father: {rule['father']}",
            *(
                []
                if father_teaching_repeats(rule, father_teaching)
                else [f"Father teaching: {father_teaching['father']}: {father_teaching['teaching']}"]
            ),
            f"Practice: {father_teaching['practice']}",
            f"Prayer: {rule['prayer']}",
            "",
            "Creed Reflection",
            creeds["nicene"]["title"],
            creeds["nicene"]["note"],
            creeds["nicene"]["reflection"],
            creeds["apostles"]["note"],
            creeds["apostles"]["prompt"],
            "",
            "Prayer Rope",
            f"{st.session_state.prayer_rope_target} Jesus Prayers",
            rope_mode["name"],
            rope_mode["meaning"],
            rope_mode["section"],
            "Lord Jesus Christ, Son of God, have mercy on me, a sinner.",
            "",
            "Theosis Thread",
            get_theosis_thread(rule["state"]),
            "",
            "Body Discipline",
            rule["body"],
            "",
            "Purity and the Flesh",
            purity_rule["title"],
            f"Watchfulness: {purity_rule['watch']}",
            f"Body: {purity_rule['body']}",
            f"Mind: {purity_rule['mind']}",
            f"Repair: {purity_rule['repair']}",
            "",
            "Holy Diet",
            body_rule["food"]["rule"],
            body_rule["food"]["fast"],
            f"Seasonal counsel: {body_rule['food']['season']}",
            "",
            "Body Temple Workout",
            body_rule["strength"]["name"],
            *[f"- {move}" for move in body_rule["strength"]["workout"]],
            body_rule["strength"]["kettlebell"],
            body_rule["strength"]["fallback"],
            "",
            "Rest as Obedience",
            body_rule["rest"]["title"],
            *[f"- {action}" for action in body_rule["rest"]["actions"]],
            body_rule["rest"]["warning"],
            "",
            "Mind Discipline",
            rule["mind"],
            "",
            "Watchfulness",
            get_watchfulness(rule["state"]),
            "",
            "Guarding the Senses",
            get_sense_guard(rule["state"], renunciation),
            "",
            "Reflection Prompt",
            rule["reflection"],
            "",
            "Questions of Return",
            *[f"- {question}" for question in examen],
            "",
            "Seal",
            rule_seal(rule),
            "",
            "If It Feels Too Heavy",
            lesser_obedience(rule),
            "",
            "Closing",
            posture["closing"],
            "",
            "Rule of Departure",
            f"Seal: {departure['seal']}",
            f"Carry the Cross: {departure['cross']}",
            f"Carry the Resurrection: {departure['resurrection']}",
            f"Digital boundary: {departure['digital']}",
            f"Bodily obedience: {departure['body']}",
            f"Name to carry: {departure['carry']}",
            f"Command: {departure['command']}",
        ]
    )


def render_paschal_thread(cross_thread, focus):
    st.markdown(
        f"""
        <div class="paschal-thread">
            <p class="kicker">Paschal thread</p>
            <h4>{focus}</h4>
            <p><strong>Cross:</strong> {cross_thread['cross']}</p>
            <p><strong>Resurrection:</strong> {cross_thread['resurrection']}</p>
            <p><strong>Practice:</strong> {cross_thread['practice']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_seasonal_thread(seasonal_thread):
    st.markdown(
        f"""
        <div class="seasonal-thread">
            <p class="kicker">Seasonal mode</p>
            <h4>{st.session_state.liturgical_season}</h4>
            <p>{seasonal_thread['tone']}</p>
            <p><strong>Seasonal cross:</strong> {seasonal_thread['cross']}</p>
            <p><strong>Seasonal resurrection:</strong> {seasonal_thread['resurrection']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def prepare_to_receive():
    placeholder = st.empty()
    placeholder.markdown(
        """
        <div class="stillness">
            <p class="kicker">Before the rule</p>
            <h2>Be still. Breathe. Stand before God.</h2>
            <p>Let the urge to hurry pass without obeying it.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(STILLNESS_SECONDS)
    placeholder.empty()


def save_reflection(rule, reflection):
    REFLECTIONS_PATH.parent.mkdir(exist_ok=True)
    entry = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "rule_id": rule["id"],
        "liturgical_moment": st.session_state.liturgical_moment,
        "liturgical_season": st.session_state.liturgical_season,
        "world_pull": st.session_state.world_pull,
        "monastic_longing": st.session_state.monastic_longing,
        "digital_fast": st.session_state.digital_fast,
        "intensity": rule["intensity"],
        "state": rule["state"],
        "time": rule["time"],
        "reflection": reflection.strip(),
    }
    with REFLECTIONS_PATH.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry, ensure_ascii=True) + "\n")


def save_evening_examen(payload):
    EXAMEN_PATH.parent.mkdir(exist_ok=True)
    entry = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        **payload,
    }
    with EXAMEN_PATH.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry, ensure_ascii=True) + "\n")


def save_paschal_examen(rule, payload):
    EXAMEN_PATH.parent.mkdir(exist_ok=True)
    entry = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "entry_type": "paschal_rule_examen",
        "rule_id": rule["id"],
        "liturgical_moment": st.session_state.liturgical_moment,
        "liturgical_season": st.session_state.liturgical_season,
        "intensity": rule["intensity"],
        "state": rule["state"],
        "time": rule["time"],
        **payload,
    }
    with EXAMEN_PATH.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry, ensure_ascii=True) + "\n")


def read_jsonl(path):
    if not path.exists():
        return []

    entries = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    return entries


def journal_export_text(reflections, examens):
    lines = ["The Inner Monk", "Private Journal", ""]

    if reflections:
        lines.extend(["Rule Reflections", ""])
        for entry in reflections:
            lines.extend(
                [
                    entry.get("created_at", ""),
                    f"Rule: {entry.get('intensity', '')} / {entry.get('state', '')} / {entry.get('time', '')}",
                    f"Season: {entry.get('liturgical_season', '')}",
                    f"World pull: {entry.get('world_pull', '')}",
                    f"Monastic longing: {entry.get('monastic_longing', '')}",
                    entry.get("reflection", ""),
                    "",
                ]
            )

    if examens:
        lines.extend(["Evening Returns", ""])
        for entry in examens:
            if entry.get("entry_type") == "paschal_rule_examen":
                lines.extend(
                    [
                        entry.get("created_at", ""),
                        f"Paschal Rule Return: {entry.get('intensity', '')} / {entry.get('state', '')} / {entry.get('time', '')}",
                        f"Season: {entry.get('liturgical_season', '')}",
                        f"Pattern losing its hold: {entry.get('crucified', '')}",
                        f"Life Christ is calling forth: {entry.get('raised', '')}",
                        f"Next clean action: {entry.get('repair', '')}",
                        f"Call back to Christ: {entry.get('mercy', '')}",
                        "",
                    ]
                )
                continue
            lines.extend(
                [
                    entry.get("created_at", ""),
                    f"Pull resisted: {entry.get('ruling_pull', entry.get('passion', ''))}",
                    f"Attention left Christ: {entry.get('attention_departure', entry.get('fled_from_christ', ''))}",
                    f"False refuge: {entry.get('false_refuge', entry.get('comfort_over_obedience', ''))}",
                    f"Mercy needed: {entry.get('mercy_needed', entry.get('wounded', ''))}",
                    f"Call back to Christ: {entry.get('return_received', entry.get('mercy_received', ''))}",
                    f"Next clean obedience: {entry.get('next_obedience', entry.get('confess_repair_release', ''))}",
                    "",
                ]
            )

    if len(lines) == 3:
        lines.append("No private journal entries yet.")

    return "\n".join(lines)


st.set_page_config(
    page_title="The Inner Monk",
    page_icon="TIM",
    layout="centered",
    initial_sidebar_state="collapsed",
)

apply_theme()

if "rule" not in st.session_state:
    st.session_state.rule = None
if "rule_complete" not in st.session_state:
    st.session_state.rule_complete = False
if "rule_silence_active" not in st.session_state:
    st.session_state.rule_silence_active = False
if "rule_silence_started_at" not in st.session_state:
    st.session_state.rule_silence_started_at = None
if "daily_oath_taken" not in st.session_state:
    st.session_state.daily_oath_taken = False
if "last_rule_id" not in st.session_state:
    st.session_state.last_rule_id = None
if "reflection_saved" not in st.session_state:
    st.session_state.reflection_saved = False
if "renunciation" not in st.session_state:
    st.session_state.renunciation = None
if "liturgical_moment" not in st.session_state:
    st.session_state.liturgical_moment = LITURGICAL_MOMENTS[0]
if "liturgical_season" not in st.session_state:
    st.session_state.liturgical_season = LITURGICAL_SEASONS[0]
if "world_pull" not in st.session_state:
    st.session_state.world_pull = WORLD_PULLS[0]
if "monastic_longing" not in st.session_state:
    st.session_state.monastic_longing = MONASTIC_LONGINGS[0]
if "digital_fast" not in st.session_state:
    st.session_state.digital_fast = DIGITAL_FAST_OPTIONS[0]
if "cell_step" not in st.session_state:
    st.session_state.cell_step = 0
if "entered_cell" not in st.session_state:
    st.session_state.entered_cell = False
if "threshold_step" not in st.session_state:
    st.session_state.threshold_step = 0
if "threshold_renunciation" not in st.session_state:
    st.session_state.threshold_renunciation = WORLD_PULLS[0]
if "threshold_desire" not in st.session_state:
    st.session_state.threshold_desire = MONASTIC_LONGINGS[0]
if "prayer_rope_target" not in st.session_state:
    st.session_state.prayer_rope_target = PRAYER_ROPE_OPTIONS[0]
if "prayer_rope_count" not in st.session_state:
    st.session_state.prayer_rope_count = 0
if "entry_mode" not in st.session_state:
    st.session_state.entry_mode = "rule"
if "examen_saved" not in st.session_state:
    st.session_state.examen_saved = False
if "rule_examen_saved" not in st.session_state:
    st.session_state.rule_examen_saved = False

if not st.session_state.entered_cell and st.session_state.rule is None:
    threshold_steps = ["Stand at the Mouth", "Renounce", "Invoke Christ", "Name the Hunger"]
    threshold_step = max(0, min(st.session_state.threshold_step, len(threshold_steps) - 1))
    threshold_name = threshold_steps[threshold_step]
    cover_image_data_uri = get_cover_image_data_uri()
    cover_background = (
        f"background: linear-gradient(180deg, rgba(8, 7, 5, 0.04), "
        f"rgba(8, 7, 5, 0.74)), url({cover_image_data_uri});"
        if cover_image_data_uri
        else (
            "background: linear-gradient(180deg, rgba(8, 7, 5, 0.03), "
            "rgba(8, 7, 5, 0.78)), radial-gradient(circle at top, "
            "rgba(198, 161, 91, 0.22), transparent 60%), #15110c;"
        )
    )

    st.markdown(
        f"""
        <section class="monk-app cave-app" style="background: radial-gradient(circle at top, rgba(198, 161, 91, 0.12), transparent 42%), linear-gradient(180deg, rgba(29, 24, 16, 0.92), rgba(7, 6, 5, 0.98)); border: 1px solid rgba(198, 161, 91, 0.30); border-radius: 30px 30px 24px 24px; box-shadow: 0 2.2rem 5rem rgba(0, 0, 0, 0.55); margin: 0.5rem auto 1.4rem; max-width: 520px; overflow: hidden; padding: 0.9rem;">
            <div class="cave-mouth" style="background: linear-gradient(135deg, rgba(198, 161, 91, 0.20), rgba(198, 161, 91, 0.04)); border: 1px solid rgba(198, 161, 91, 0.28); border-radius: 28px; padding: 0.65rem;">
            <div class="monk-visual cave-interior opening-art" style="{cover_background} background-position: center; background-size: cover; border: 1px solid rgba(198, 161, 91, 0.24); border-radius: 22px; box-shadow: inset 0 -3rem 5rem rgba(0, 0, 0, 0.56), inset 0 1.2rem 3rem rgba(0, 0, 0, 0.35); min-height: 320px; padding: 1.2rem; position: relative; overflow: hidden;">
            </div>
            </div>
            <div class="monk-control-panel" style="padding: 0.9rem 0.1rem 0.1rem;">
                <div class="opening-threshold" style="background: rgba(8, 7, 5, 0.70); border: 1px solid rgba(198, 161, 91, 0.24); border-radius: 18px; margin-bottom: 0.85rem; padding: 1.15rem;">
                    <p class="kicker" style="color: #c6a15b; font-size: 0.76rem; letter-spacing: 0.18rem; margin-bottom: 0.6rem; text-transform: uppercase;">A daily practice of theosis</p>
                    <h1 style="color: #f3ead7; font-family: Georgia, 'Times New Roman', serif; font-size: 2rem; font-weight: 400; line-height: 1.08; margin: 0;">Enter the cave of the heart.</h1>
                <p style="color: #b9aa8d; line-height: 1.6; margin: 0.75rem 0 0;">Leave the world at the mouth of the cave. Pass through the Cross and return in the risen life of Christ.</p>
                </div>
                <div class="monk-card primary" style="background: rgba(23, 20, 15, 0.92); border: 1px solid rgba(198, 161, 91, 0.28); border-radius: 18px; padding: 1.15rem;">
                    <p class="kicker" style="color: #c6a15b; font-size: 0.78rem; letter-spacing: 0.18rem; margin-bottom: 0.6rem; text-transform: uppercase;">Entrance rite</p>
                    <h2 style="color: #f3ead7; font-family: Georgia, 'Times New Roman', serif; font-size: 1.9rem; font-weight: 400; margin: 0.25rem 0 0.45rem;">{threshold_name}</h2>
                    <p style="color: #b9aa8d; margin-bottom: 0;">Stand, renounce, invoke Christ, and bring the hunger beneath the noise into the light.</p>
                </div>
                <div class="monk-tiles" style="display: grid; gap: 0.75rem; grid-template-columns: 1fr 1fr; margin-top: 0.75rem;">
                    <div style="background: rgba(198, 161, 91, 0.08); border: 1px solid rgba(198, 161, 91, 0.18); border-radius: 16px; padding: 0.9rem;">
                        <span style="color: #b9aa8d; display: block; font-size: 0.78rem; margin-bottom: 0.25rem;">World</span>
                        <strong style="color: #f3ead7; font-family: Georgia, 'Times New Roman', serif; font-weight: 400;">{st.session_state.threshold_renunciation}</strong>
                    </div>
                    <div style="background: rgba(198, 161, 91, 0.08); border: 1px solid rgba(198, 161, 91, 0.18); border-radius: 16px; padding: 0.9rem;">
                        <span style="color: #b9aa8d; display: block; font-size: 0.78rem; margin-bottom: 0.25rem;">Desire</span>
                        <strong style="color: #f3ead7; font-family: Georgia, 'Times New Roman', serif; font-weight: 400;">{st.session_state.threshold_desire}</strong>
                    </div>
                </div>
                <div class="monk-bottom-nav cave-stones" style="align-items: center; background: rgba(8, 7, 5, 0.70); border: 1px solid rgba(198, 161, 91, 0.16); border-radius: 18px; display: grid; gap: 0.25rem; grid-template-columns: repeat(4, 1fr); margin-top: 0.75rem; padding: 0.45rem; text-align: center;">
                    <span style="background: rgba(198, 161, 91, 0.16); border-radius: 14px; color: #f3ead7; font-size: 0.78rem; padding: 0.55rem 0.2rem;">Stand</span>
                    <span style="border-radius: 14px; color: #b9aa8d; font-size: 0.78rem; padding: 0.55rem 0.2rem;">Renounce</span>
                    <span style="border-radius: 14px; color: #b9aa8d; font-size: 0.78rem; padding: 0.55rem 0.2rem;">Invoke</span>
                    <span style="border-radius: 14px; color: #b9aa8d; font-size: 0.78rem; padding: 0.55rem 0.2rem;">Hunger</span>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div class=\"threshold-path app-path\">"
        + "".join(
            f"<span class=\"{'active' if index == threshold_step else ''}\">{step}</span>"
            for index, step in enumerate(threshold_steps)
        )
        + "</div>",
        unsafe_allow_html=True,
    )

    if threshold_name == "Stand at the Mouth":
        st.markdown(
            """
            <div class="threshold-panel">
                <p class="kicker">The mouth of the cave</p>
                <h3>Leave the noise outside.</h3>
                <p>
                    Stand before Christ without performing, scrolling, defending,
                    or escaping. This is a small Christian cell for prayer,
                    repentance, Scripture, bodily discipline, chastity, and return to Jesus Christ.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif threshold_name == "Renounce":
        st.session_state.threshold_renunciation = st.radio(
            "What are you leaving at the mouth of the cave?",
            WORLD_PULLS,
            horizontal=True,
            index=WORLD_PULLS.index(st.session_state.threshold_renunciation),
        )
        st.markdown(
            f"""
            <div class="threshold-panel">
                <p>{get_world_renunciation(st.session_state.threshold_renunciation)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif threshold_name == "Invoke Christ":
        st.markdown(
            """
            <div class="threshold-panel invocation-panel">
                <p class="opening-prayer">Lord Jesus Christ, Son of God, have mercy on me.</p>
                <p>Through the Cross, joy has come into all the world.</p>
                <p>Breathe in: Lord Jesus Christ, Son of God.</p>
                <p>Breathe out: have mercy on me.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif threshold_name == "Name the Hunger":
        st.session_state.threshold_desire = st.radio(
            "What hunger are you bringing to Christ?",
            MONASTIC_LONGINGS,
            horizontal=True,
            index=MONASTIC_LONGINGS.index(st.session_state.threshold_desire),
        )
        st.markdown(
            f"""
            <div class="threshold-panel">
                <p>{get_monastic_desire_word(st.session_state.threshold_desire)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    prev_col, next_col = st.columns(2)
    if prev_col.button("Step Back", use_container_width=True, disabled=threshold_step == 0):
        st.session_state.threshold_step = max(0, threshold_step - 1)
        st.rerun()
    if threshold_step < len(threshold_steps) - 1:
        if next_col.button("Go Deeper", use_container_width=True):
            st.session_state.threshold_step = threshold_step + 1
            st.rerun()
    elif next_col.button("Enter the Cell", use_container_width=True):
        st.session_state.entered_cell = True
        st.session_state.world_pull = st.session_state.threshold_renunciation
        st.session_state.monastic_longing = st.session_state.threshold_desire
        st.rerun()
    st.stop()

st.markdown(
    """
    <section class="inner-cell-hero">
        <div>
            <p class="kicker">Inside the cell</p>
            <h1>The cave is quiet now.</h1>
            <p>Choose the chamber you need. Receive one obedience. Carry it through the Cross and depart in peace.</p>
        </div>
        <div class="cell-lamp">+</div>
    </section>
    """,
    unsafe_allow_html=True,
)

rule = st.session_state.rule

if rule is None:
    st.markdown(
        """
        <div class="chamber-selector">
            <p class="kicker">Choose a chamber</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.session_state.entry_mode = st.radio(
        "Choose a chamber",
        ["Daily Rule", "Church Fathers", "Evening Return", "Private Journal"],
        horizontal=True,
        index={"rule": 0, "fathers": 1, "examen": 2, "journal": 3}.get(st.session_state.entry_mode, 0),
        label_visibility="collapsed",
    )
    if st.session_state.entry_mode == "Church Fathers":
        st.session_state.entry_mode = "fathers"
    elif st.session_state.entry_mode == "Evening Return":
        st.session_state.entry_mode = "examen"
    elif st.session_state.entry_mode == "Private Journal":
        st.session_state.entry_mode = "journal"
    elif st.session_state.entry_mode == "Daily Rule":
        st.session_state.entry_mode = "rule"

if rule is None and st.session_state.entry_mode == "fathers":
    render_fathers_library()

    if st.button("Return to the Threshold", use_container_width=True):
        st.session_state.entered_cell = False
        st.session_state.threshold_step = 0
        st.session_state.entry_mode = "rule"
        st.rerun()

    st.stop()

if rule is None and st.session_state.entry_mode == "journal":
    reflections = list(reversed(read_jsonl(REFLECTIONS_PATH)))
    examens = list(reversed(read_jsonl(EXAMEN_PATH)))

    st.markdown(
        """
        <div class="cell-note chamber-note">
            <p class="kicker">Journal chamber</p>
            <p>
                A private spiritual notebook on this machine. No streaks, no charts,
                no public display. Read only what helps repentance, gratitude,
                honest reflection, and return to Christ.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.download_button(
        "Export Private Journal",
        data=journal_export_text(reflections, examens),
        file_name="the-inner-monk-journal.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.markdown("### Rule Reflections")
    if reflections:
        for entry in reflections[:5]:
            with st.expander(entry.get("created_at", "Reflection")):
                st.caption(
                    f"{entry.get('intensity', '')} / {entry.get('state', '')} / {entry.get('time', '')}"
                )
                st.write(entry.get("reflection", ""))
    else:
        st.write("No rule reflections saved yet.")

    st.markdown("### Evening Returns")
    if examens:
        for entry in examens[:5]:
            with st.expander(entry.get("created_at", "Evening Return")):
                if entry.get("entry_type") == "paschal_rule_examen":
                    st.caption(
                        f"Paschal Rule Return: {entry.get('intensity', '')} / {entry.get('state', '')} / {entry.get('time', '')}"
                    )
                    st.write(f"Pattern losing its hold: {entry.get('crucified', '')}")
                    st.write(f"Life Christ is calling forth: {entry.get('raised', '')}")
                    st.write(f"Next clean action: {entry.get('repair', '')}")
                    st.write(f"Call back to Christ: {entry.get('mercy', '')}")
                    continue
                st.caption(f"Pull resisted: {entry.get('ruling_pull', entry.get('passion', ''))}")
                st.write(f"Attention left Christ: {entry.get('attention_departure', entry.get('fled_from_christ', ''))}")
                st.write(f"False refuge: {entry.get('false_refuge', entry.get('comfort_over_obedience', ''))}")
                st.write(f"Mercy needed: {entry.get('mercy_needed', entry.get('wounded', ''))}")
                st.write(f"Call back to Christ: {entry.get('return_received', entry.get('mercy_received', ''))}")
                st.write(f"Next clean obedience: {entry.get('next_obedience', entry.get('confess_repair_release', ''))}")
    else:
        st.write("No evening returns saved yet.")

    if st.button("Return to the Threshold", use_container_width=True):
        st.session_state.entered_cell = False
        st.session_state.threshold_step = 0
        st.session_state.entry_mode = "rule"
        st.rerun()

    st.stop()

if rule is None and st.session_state.entry_mode == "examen":
    st.markdown(
        """
        <div class="cell-note chamber-note">
            <p class="kicker">Evening return</p>
            <p>
                Stop rehearsing the world. Gather the scattered mind and turn again
                toward Jesus Christ. Receive a sober return to attention, mercy,
                and the next clean obedience.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("evening_examen_form"):
        attention_departure = st.text_area("Where did my attention leave Christ today?")
        false_refuge = st.text_area("What false refuge promised escape but left me less free?")
        mercy_needed = st.text_area("Who needs mercy, patience, or repair from me?")
        ruling_pull = st.selectbox(
            "What most tried to rule the mind?",
            [
                "The feed",
                "Lust / Flesh",
                "Anger",
                "Fear",
                "Comfort",
                "Approval",
                "Control",
                "Despair",
                "I am not sure",
            ],
        )
        return_received = st.text_area("Where did Christ call me back to truth or mercy?")
        next_obedience = st.text_area("What clean act of obedience begins now?")
        saved = st.form_submit_button("Save Private Return", use_container_width=True)

    if saved:
        save_evening_examen(
            {
                "entry_type": "evening_return",
                "attention_departure": attention_departure.strip(),
                "false_refuge": false_refuge.strip(),
                "mercy_needed": mercy_needed.strip(),
                "ruling_pull": ruling_pull,
                "return_received": return_received.strip(),
                "next_obedience": next_obedience.strip(),
            }
        )
        st.session_state.examen_saved = True

    if st.session_state.examen_saved:
        st.success("Saved privately. Turn from the screen now and keep the next clean obedience.")
        st.caption(
            f"Saved locally to {EXAMEN_PATH}. If a pattern remains hidden, compulsive, or enslaving, "
            "bring it to a priest and a trustworthy Christian brother. The app cannot absolve, shepherd, or stand beside you."
        )

    if st.button("Return to the Threshold", use_container_width=True):
        st.session_state.entered_cell = False
        st.session_state.threshold_step = 0
        st.session_state.entry_mode = "rule"
        st.session_state.examen_saved = False
        st.rerun()

    st.stop()

if rule is None:
    st.markdown(
        """
        <div class="cell-note chamber-note">
            <p class="kicker">Rule chamber</p>
            <p>
                This is not monastic life itself, and it does not replace the Church,
                pastoral guidance, fasting guidance, or obedience to a spiritual father.
                It is a small Christian cell: receive one rule, practice it,
                and return to Christ with a quieter heart.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="pattern">
            <div>
                <span>1</span>
                <p>Enter quietly</p>
            </div>
            <div>
                <span>2</span>
                <p>Receive one rule</p>
            </div>
            <div>
                <span>3</span>
                <p>Practice and leave</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="chamber-form-title">
            <p class="kicker">Emergency passage</p>
            <h3>Tempted to scroll?</h3>
            <p>Do not negotiate with the feed. Name the pull, receive a short obedience, and let the impulse die under the Cross.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.form("scroll_form"):
        scroll_moment = st.radio(
            "Moment: when are you entering?",
            LITURGICAL_MOMENTS,
            horizontal=True,
            key="scroll_moment",
        )
        scroll_season = st.selectbox(
            "Season: what season are you entering?",
            LITURGICAL_SEASONS,
            key="scroll_liturgical_season",
        )
        scroll_state = st.radio(
            "Feed pull: what is happening right now?",
            SCROLL_STATES,
            horizontal=True,
        )
        renunciation = st.selectbox(
            "Renunciation: what are you turning from?",
            RENUNCIATIONS,
        )
        world_pull = st.selectbox(
            "Worldly pull: what is trying to capture your attention?",
            WORLD_PULLS,
            key="scroll_world_pull",
        )
        monastic_longing = st.selectbox(
            "Hunger: what holy desire is underneath it?",
            MONASTIC_LONGINGS,
            key="scroll_monastic_longing",
        )
        digital_fast = st.selectbox(
            "Fast: how long will you stay away from the feed?",
            DIGITAL_FAST_OPTIONS,
            key="scroll_digital_fast",
        )
        prayer_rope_target = st.selectbox(
            "Prayer: what prayer rope rule will you keep?",
            PRAYER_ROPE_OPTIONS,
            format_func=lambda count: f"{count} Jesus Prayers",
            key="scroll_prayer_rope",
        )
        scroll_generated = st.form_submit_button("Receive an Emergency Rule", use_container_width=True)

    if scroll_generated:
        prepare_to_receive()
        st.session_state.rule = get_scroll_rule(scroll_state, st.session_state.last_rule_id)
        st.session_state.last_rule_id = st.session_state.rule["id"]
        st.session_state.renunciation = renunciation
        st.session_state.liturgical_moment = scroll_moment
        st.session_state.liturgical_season = scroll_season
        st.session_state.world_pull = world_pull
        st.session_state.monastic_longing = monastic_longing
        st.session_state.digital_fast = digital_fast
        st.session_state.prayer_rope_target = prayer_rope_target
        st.session_state.prayer_rope_count = 0
        st.session_state.cell_step = 0
        st.session_state.rule_complete = False
        st.session_state.rule_silence_active = False
        st.session_state.rule_silence_started_at = None
        st.session_state.daily_oath_taken = False
        st.session_state.reflection_saved = False
        st.session_state.rule_examen_saved = False
        st.rerun()

    st.markdown(
        """
        <div class="chamber-form-title">
            <p class="kicker">Daily passage</p>
            <h3>Discern the Rule</h3>
            <p>Answer soberly. The rule is not a mood, a score, or a performance. It is one small obedience before Christ.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    with st.form("rule_form"):
        liturgical_moment = st.radio(
            "Moment: when are you entering the cell?",
            LITURGICAL_MOMENTS,
            horizontal=True,
            key="rule_moment",
        )
        liturgical_season = st.selectbox(
            "Season: what season are you entering?",
            LITURGICAL_SEASONS,
            key="rule_liturgical_season",
        )
        soul_state = st.selectbox("Burden: what is weighing on the soul?", SOUL_STATES)
        world_pull = st.selectbox(
            "Worldly pull: what is drawing the mind away from Christ?",
            WORLD_PULLS,
            key="rule_world_pull",
        )
        intensity = st.radio(
            "Strength: what kind of obedience can you receive today?",
            INTENSITIES,
            horizontal=True,
        )
        time_available = st.radio(
            "Time: how long can you remain faithful?",
            TIME_OPTIONS,
            horizontal=True,
        )
        monastic_longing = st.selectbox(
            "Hunger: what holy desire is underneath this?",
            MONASTIC_LONGINGS,
            key="rule_monastic_longing",
        )
        digital_fast = st.selectbox(
            "Fast: how long will you stay away from the feed?",
            DIGITAL_FAST_OPTIONS,
            key="rule_digital_fast",
        )
        prayer_rope_target = st.selectbox(
            "Prayer: what prayer rope rule will you keep?",
            PRAYER_ROPE_OPTIONS,
            format_func=lambda count: f"{count} Jesus Prayers",
            key="rule_prayer_rope",
        )
        generated = st.form_submit_button("Receive the Rule", use_container_width=True)

    if generated:
        prepare_to_receive()
        st.session_state.rule = get_rule(
            intensity,
            soul_state,
            time_available,
            st.session_state.last_rule_id,
        )
        st.session_state.last_rule_id = st.session_state.rule["id"]
        st.session_state.renunciation = None
        st.session_state.liturgical_moment = liturgical_moment
        st.session_state.liturgical_season = liturgical_season
        st.session_state.world_pull = world_pull
        st.session_state.monastic_longing = monastic_longing
        st.session_state.digital_fast = digital_fast
        st.session_state.prayer_rope_target = prayer_rope_target
        st.session_state.prayer_rope_count = 0
        st.session_state.cell_step = 0
        st.session_state.rule_complete = False
        st.session_state.rule_silence_active = False
        st.session_state.rule_silence_started_at = None
        st.session_state.daily_oath_taken = False
        st.session_state.reflection_saved = False
        st.session_state.rule_examen_saved = False
        st.rerun()

if rule:
    aim = ascetic_aim(rule, st.session_state.renunciation)
    posture = get_posture(st.session_state.liturgical_moment)
    examen = get_examen(rule["state"])
    prayer_name, ancient_prayer = get_ancient_prayer(st.session_state.liturgical_moment)
    father_teaching = get_father_teaching(rule["state"])
    scripture_reading = get_scripture_reading(rule["id"])
    witness = get_daily_witness(datetime.now().timetuple().tm_yday + rule["id"])
    creeds = get_creed_reflections()
    cross_thread = get_cross_resurrection_thread(rule["state"])
    seasonal_thread = get_seasonal_thread(st.session_state.liturgical_season)
    passion_virtue = get_passion_virtue(rule["state"], st.session_state.world_pull)
    watchword = daily_watchword(rule, passion_virtue, cross_thread)
    oath = daily_oath_of_service(rule, passion_virtue, watchword)
    little_typikon = get_little_typikon(st.session_state.liturgical_moment, rule, passion_virtue)

    if st.session_state.rule_silence_active:
        total_seconds = silence_seconds_for_rule(rule)
        started_at = st.session_state.rule_silence_started_at or time.time()
        elapsed = int(time.time() - started_at)
        remaining = max(0, total_seconds - elapsed)
        progress_value = min(1.0, elapsed / total_seconds) if total_seconds else 1.0

        st.markdown(
            f"""
            <section class="silence-screen">
                <p class="kicker">Vigil beneath the Cross</p>
                <h1>{format_silence_time(remaining)}</h1>
                <p class="silence-watchword">{watchword}</p>
                <p class="silence-instruction">{oath['seal']} Keep watch now. No browsing. No measuring. Return to the name of Jesus.</p>
            </section>
            """,
            unsafe_allow_html=True,
        )
        st.progress(progress_value)
        if remaining == 0:
            st.success("Rise and serve. Carry the Watchword into the next act of obedience.")
            if st.button("Depart", use_container_width=True):
                st.session_state.rule_silence_active = False
                st.session_state.rule_silence_started_at = None
                st.session_state.rule_complete = True
                st.rerun()
        else:
            col_a, col_b = st.columns(2)
            if col_a.button("Finish Silence", use_container_width=True):
                st.session_state.rule_silence_active = False
                st.session_state.rule_silence_started_at = None
                st.session_state.rule_complete = True
                st.rerun()
            if col_b.button("Return to Rule", use_container_width=True):
                st.session_state.rule_silence_active = False
                st.session_state.rule_silence_started_at = None
                st.rerun()
            time.sleep(1)
            st.rerun()

        st.stop()

    step_index = current_cell_step()
    steps = cell_path()
    step_name = steps[step_index]
    visible_steps = visible_path_steps(step_name)
    st.markdown(
        f"""
        <div class="cell-mode chamber-mode">
            <p class="kicker">Chamber {step_index + 1} of {len(steps)}</p>
            <h2>{step_name}</h2>
            <p>{st.session_state.liturgical_moment} / {st.session_state.liturgical_season} / {rule['intensity']} / {rule['state']} / {rule['time']}</p>
            <div class="chamber-progress"><span style="width: {((step_index + 1) / len(steps)) * 100:.1f}%"></span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div class=\"cell-path\">"
        + "".join(
            f"<span class=\"{'active' if step == step_name else ''}\">{step}</span>"
            for step in visible_steps
        )
        + "</div>",
        unsafe_allow_html=True,
    )
    st.markdown('<div class="rule-card">', unsafe_allow_html=True)

    if step_name == "Opening":
        st.markdown("#### Begin")
        st.markdown(
            f"""
            <div class="todays-path-card">
                <p class="kicker">Today's path</p>
                <h3>{rule['intensity']} rule for a {rule['state'].lower()} soul</h3>
                <div class="watchword-card compact">
                    <span>Watchword</span>
                    <p>{watchword}</p>
                </div>
                <div class="allegiance-card compact">
                    <span>Beloved and sent</span>
                    <p>{oath['love']}</p>
                    <strong>{oath['seal']}</strong>
                </div>
                <div class="path-grid">
                    <div><span>Prayer</span><strong>{st.session_state.prayer_rope_target} Jesus Prayers</strong></div>
                    <div><span>Scripture</span><strong>{scripture_reading['reference']}</strong></div>
                    <div><span>Body</span><strong>{rule['time']} of obedience</strong></div>
                    <div><span>Fast</span><strong>{st.session_state.digital_fast}</strong></div>
                </div>
                <p class="path-line">Main route: Prayer -> Scripture -> Body Temple -> Purity -> Return -> Vigil and Oath -> Depart.</p>
                <p class="path-note">Use Cave Map only when you want the deeper chambers.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_seasonal_thread(seasonal_thread)
        st.write(posture["invocation"])
        st.write(posture["posture"])
        st.write(posture["remembrance"])
        st.markdown("#### Ancient Prayer")
        st.write(f"{prayer_name}: {ancient_prayer}")
        st.markdown("#### Daily Beatitude")
        st.write(get_daily_beatitude(rule["id"]))
    elif step_name == "Cave Map":
        st.markdown("#### Cave Map")
        st.write("This is the path through the cell. Do not rush it. Move from entrance, to light, to struggle, to return.")
        current_step_name = steps[step_index]
        for stage in get_chamber_stages():
            st.markdown(
                f"""
                <div class="cave-stage">
                    <p class="kicker">{stage['stage']}</p>
                    <h3>{stage['purpose']}</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )
            for chamber in stage["chambers"]:
                target_index = chamber_step_index(chamber["name"])
                target_step_name = steps[target_index]
                active_class = " active" if target_step_name == current_step_name else ""
                st.markdown(
                    f"""
                    <div class="cave-map-node{active_class}">
                        <span>{chamber['name']}</span>
                        <p>{chamber['purpose']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if st.button(
                    "Enter",
                    key=f"enter_chamber_{stage['stage']}_{chamber['name']}",
                    use_container_width=True,
                    disabled=target_step_name == current_step_name,
                ):
                    st.session_state.cell_step = target_index
                    st.rerun()
    elif step_name == "Daily Order":
        st.markdown("#### Today's Little Typikon")
        st.write("A small order for the day. Not a tracker. Not self-improvement theater. A shape for returning to Christ.")
        for item in little_typikon:
            st.markdown(f"**{item['hour']}**")
            st.write(item["rule"])
    elif step_name == "Witness":
        st.markdown("#### Witness of the Day")
        render_paschal_thread(cross_thread, "The witness is not celebrity. The witness is a human life conformed to the Cross and Resurrection.")
        st.markdown(
            f"""
            <div class="witness-card">
                <p class="kicker">{witness['title']}</p>
                <h3>{witness['name']}</h3>
                <p>{witness['story']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### What this witness teaches")
        st.write(witness["lesson"])
        st.markdown("#### How the Witness Suffered")
        st.write(witness.get("martyrdom", "This witness reveals a life offered to Christ."))
        st.markdown("#### Cross and Resurrection")
        st.write(witness.get("paschal_thread", "This witness is understood through the Cross and Resurrection of Christ."))
        st.markdown("#### Deeper Reading")
        st.write(witness.get("depth", "This witness reveals one concrete way the life of Christ can be formed in a human person."))
        st.markdown("#### What the Witness Resisted")
        st.write(witness.get("world_resisted", "The spirit of the world that pulls the heart away from Christ."))
        st.markdown("#### Virtue")
        st.write(witness.get("virtue", "Faithfulness"))
        st.markdown("#### Theosis Thread")
        st.write(witness.get("theosis", "This virtue heals the heart and makes room for communion with Christ."))
        st.markdown("#### Imitation")
        st.write(witness.get("imitation", "Keep one small obedience to Christ without display."))
        st.markdown("#### Small Act")
        st.write(witness.get("small_act", "Do one hidden act of prayer, mercy, or restraint today."))
        st.markdown("#### Reflection")
        st.write(witness["reflection"])
    elif step_name == "Prayer Corner":
        st.markdown(
            """
            <div class="prayer-corner">
                <div class="prayer-cross">+</div>
                <p>Stand before God without images on the screen. Let the room become quiet before the heart begins to pray.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### Prayer of Attention")
        st.write("Lord Jesus Christ, gather my mind into my heart and make this place quiet before You.")
    elif step_name == "Renunciation":
        st.markdown("#### Leaving the World")
        st.write(get_world_renunciation(st.session_state.world_pull))
        st.write(get_monastic_desire_word(st.session_state.monastic_longing))
        st.markdown("#### Digital Fast Vow")
        st.write(digital_fast_vow(st.session_state.digital_fast))
        if st.session_state.renunciation:
            st.markdown("#### Particular Renunciation")
            st.write(f"Today I turn from {st.session_state.renunciation.lower()} and return to prayer.")
    elif step_name == "Passion":
        st.markdown("#### Passion")
        st.markdown(f"**{passion_virtue['passion']}**")
        st.write(passion_virtue["description"])
        st.markdown("#### Virtue")
        st.markdown(f"**{passion_virtue['virtue']}**")
        st.write(passion_virtue["virtue_description"])
        st.markdown("#### Small Obedience")
        st.write(passion_virtue["obedience"])
    elif step_name == "Cross and Resurrection":
        render_seasonal_thread(seasonal_thread)
        st.markdown("#### The Cross")
        st.write(cross_thread["cross"])
        st.markdown("#### The Resurrection")
        st.write(cross_thread["resurrection"])
        st.markdown("#### Today")
        st.write(cross_thread["practice"])
        st.markdown(
            """
            <div class="creed-response">
                <p>Through the Cross, joy has come into all the world.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif step_name == "Scripture":
        st.markdown("#### Gospel Reading")
        render_paschal_thread(cross_thread, "The Gospel is not content to consume. It is the word of Christ that judges, heals, and raises.")
        st.markdown(
            f"""
            <div class="lectio-card">
                <p class="kicker">{scripture_reading['reference']}</p>
                <h3>{scripture_reading['title']}</h3>
                <p>{scripture_reading['text']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### How to Read")
        st.write(scripture_reading["practice"])
        st.markdown("#### Word to Carry")
        st.markdown(f"**{scripture_reading['carry']}**")
        st.write(scripture_reading["question"])
        st.markdown("#### Daily Beatitude")
        st.write(get_daily_beatitude(rule["id"]))
    elif step_name == "Creed":
        st.markdown("#### Creed Chamber")
        render_paschal_thread(cross_thread, "The Creed guards the heart from inventing a private Christ.")
        st.write(creeds["nicene"]["note"])
        st.markdown("#### How to Confess")
        for instruction in creeds["nicene"]["practice"]:
            st.write(f"- {instruction}")
        with st.expander("Read the Nicene Creed slowly"):
            for line in creeds["nicene"]["lines"]:
                st.write(line)
        st.markdown("#### Reflection")
        st.write(creeds["nicene"]["reflection"])
        st.markdown(
            """
            <div class="creed-response">
                <p>Lord, I believe; help my unbelief.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### Apostles' Creed note")
        st.write(creeds["apostles"]["note"])
        st.write(creeds["apostles"]["prompt"])
    elif step_name == "Prayer":
        st.markdown("#### Prayer Focus")
        render_paschal_thread(cross_thread, "Prayer is not escape. Prayer joins the heart to the crucified and risen Lord.")
        st.markdown(
            f"""
            <div class="watchword-card">
                <span>Watchword</span>
                <p>{watchword}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(f"**Gospel saying:** {rule['scripture']}")
        st.markdown(f"**Church Father:** {rule['father']}")
        if not father_teaching_repeats(rule, father_teaching):
            st.markdown(f"**Father teaching:** {father_teaching['father']}: {father_teaching['teaching']}")
        st.markdown(f"**Practice:** {father_teaching['practice']}")
        st.markdown(f"**Prayer:** {rule['prayer']}")
        st.markdown("#### Theosis Thread")
        st.write(get_theosis_thread(rule["state"]))
    elif step_name == "Prayer Rope":
        remaining = max(0, st.session_state.prayer_rope_target - st.session_state.prayer_rope_count)
        rope_mode = prayer_rope_mode(st.session_state.prayer_rope_target)
        st.markdown("#### Jesus Prayer")
        st.markdown("#### Posture")
        st.write("Stand, sit, or kneel as you are able. Breathe naturally. Do not force feeling, imagery, or spiritual intensity. Return to the name of Jesus.")
        st.markdown("#### Mode")
        st.markdown(f"**{rope_mode['name']}**")
        st.write(rope_mode["meaning"])
        st.write(rope_mode["section"])
        st.markdown(
            f"""
            <div class="prayer-rope-panel">
                <p class="kicker">Prayer rope</p>
                <p class="opening-prayer">Lord Jesus Christ, Son of God, have mercy on me, a sinner.</p>
                <p>{st.session_state.prayer_rope_count} / {st.session_state.prayer_rope_target}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write(
            f"Prayer {min(st.session_state.prayer_rope_count + 1, st.session_state.prayer_rope_target)} "
            f"of {st.session_state.prayer_rope_target}"
        )
        st.progress(st.session_state.prayer_rope_count / st.session_state.prayer_rope_target)
        if remaining > 0:
            if st.button("Pray Next", use_container_width=True):
                st.session_state.prayer_rope_count = min(
                    st.session_state.prayer_rope_target,
                    st.session_state.prayer_rope_count + 1,
                )
                st.rerun()
        else:
            st.success("Prayer rope complete. Keep silence for a moment before continuing.")
        st.markdown("#### Guardrails")
        st.write("No score. No spiritual achievement. No forcing attention. If distracted, return to the next prayer without drama.")
        st.caption("The point is not perfect counting. The point is the heart returning to Jesus.")
    elif step_name == "Body Temple":
        body_rule = get_body_rule(rule["intensity"], rule["time"], seasonal_thread)
        st.markdown("#### Body as Temple")
        render_paschal_thread(cross_thread, "The body is disciplined under the Cross so it can rise for prayer, labor, chastity, and mercy.")
        render_seasonal_thread(seasonal_thread)
        st.write("Your body is not a project for vanity and not a thing to neglect. It is a temple of the Holy Spirit, trained to serve prayer, labor, chastity, mercy, and theosis.")
        st.markdown("#### Food as Thanksgiving")
        st.markdown(f"**{body_rule['food']['title']}**")
        st.write(body_rule["food"]["rule"])
        st.write(body_rule["food"]["fast"])
        st.write(body_rule["food"]["season"])
        st.write(body_rule["food"]["prayer"])
        st.caption("This is not medical advice. Keep any health, fasting, or dietary restrictions given by your doctor or priest.")
        st.markdown("#### Strength as Service")
        st.markdown(f"**{body_rule['strength']['name']}**")
        for move in body_rule["strength"]["workout"]:
            st.write(f"- {move}")
        st.write(body_rule["strength"]["kettlebell"])
        st.write(body_rule["strength"]["fallback"])
        st.caption("Train with humility. Strength is a skill. Never chase failure with a ballistic lift; stop before form breaks and let restraint become prayer.")
        st.markdown("#### Rest as Obedience")
        st.markdown(f"**{body_rule['rest']['title']}**")
        for action in body_rule["rest"]["actions"]:
            st.write(f"- {action}")
        st.write(body_rule["rest"]["warning"])
    elif step_name == "Purity":
        purity_rule = get_purity_rule(rule["intensity"])
        st.markdown("#### Purity and the Flesh")
        render_paschal_thread(cross_thread, "Lust is not healed by shame. Desire must be crucified with Christ and raised as chastity.")
        st.markdown(
            f"""
            <div class="watchword-card">
                <span>Watchword</span>
                <p>{watchword}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(f"**{purity_rule['title']}**")
        st.write(
            "This chamber is for men who need to break contact with the world's distorted pattern "
            "and recover a mind turned toward Christ. Do not inspect the temptation, narrate it, or build an identity around it. "
            "The body is not the enemy; slavery to images, appetite, and unreality is the enemy. Christ claims the whole man."
        )
        st.markdown("#### Immediate Return")
        st.write("- Close the image, feed, search, or private window immediately.")
        st.write("- Put the phone beyond reach and move into a public, well-lit, or active place.")
        st.write("- Stand upright and pray the Jesus Prayer without bargaining with the urge.")
        st.write("- Begin one concrete task, walk, or safe set of physical work.")
        st.write("- If the pattern keeps returning, contact a trustworthy Christian brother or priest instead of returning to secrecy.")
        st.markdown("#### Watchfulness")
        st.write(purity_rule["watch"])
        st.markdown("#### Body")
        st.write(purity_rule["body"])
        st.markdown("#### Mind")
        st.write(purity_rule["mind"])
        st.markdown("#### Repair")
        st.write(purity_rule["repair"])
        st.markdown("#### Guardrail")
        st.write(
            "Do not rehearse details or remain alone with the pattern. If it is compulsive, hidden, or enslaving, "
            "step out of isolation: speak plainly with a priest and a trustworthy Christian brother who can pray, ask hard questions, and remain present."
        )
    elif step_name == "Practice":
        st.markdown(
            f"""
            <div class="abbot-word">
                <p class="kicker">Word for the rule</p>
                <p>{COUNSEL_BY_INTENSITY.get(rule["intensity"], "Keep the rule with peace.")}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### Ascetic Aim")
        st.write(f"Healing: {aim['healing']}")
        st.write(f"Virtue: {aim['virtue']}")
        st.markdown("#### Body Discipline")
        st.write(rule["body"])
        st.markdown("#### Mind Discipline")
        st.write(rule["mind"])
        st.markdown("#### Watchfulness")
        st.write(get_watchfulness(rule["state"]))
        st.markdown("#### Guarding the Senses")
        st.write(get_sense_guard(rule["state"], st.session_state.renunciation))
    elif step_name == "Return":
        st.markdown("#### Return of the Mind")
        render_paschal_thread(cross_thread, "Do not rehearse the fall. See what ruled the mind, turn again to Christ, and keep the next obedience.")
        st.write(rule["reflection"])
        st.markdown("#### Questions of Return")
        for question in examen:
            st.write(f"- {question}")
        st.markdown("#### Private Paschal Return")
        with st.form("paschal_examen_form"):
            crucified = st.text_area("What false pattern must lose its hold?")
            raised = st.text_area("What life is Christ calling me to practice?")
            repair = st.text_area("What clean action, mercy, or repair begins now?")
            mercy = st.text_area("Where did Christ call my mind back today?")
            saved = st.form_submit_button("Save Private Paschal Return", use_container_width=True)

        if saved:
            if any([crucified.strip(), raised.strip(), repair.strip(), mercy.strip()]):
                save_paschal_examen(
                    rule,
                    {
                        "crucified": crucified.strip(),
                        "raised": raised.strip(),
                        "repair": repair.strip(),
                        "mercy": mercy.strip(),
                    },
                )
                st.session_state.rule_examen_saved = True
            else:
                st.warning("Write one honest sentence before saving.")

        if st.session_state.rule_examen_saved:
            st.success("Saved privately. Leave the analysis behind and keep the next obedience in Christ.")
    elif step_name == "Vigil and Oath":
        st.markdown("#### Vigil Before the Cross")
        st.markdown(
            f"""
            <div class="oath-foundation">
                <p class="kicker">Beloved before commanded</p>
                <h3>You stand because Christ has loved you.</h3>
                <p>{oath['love']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### Rule of Spiritual Chivalry")
        st.write(
            "This is a daily rule of service, not a formal monastic vow and not a call to violence. "
            "The struggle is against the passions, falsehood, cowardice, and the world's claim upon the mind. "
            "No human being is the enemy."
        )
        st.markdown(
            '<div class="chivalry-grid">'
            + "".join(
                f'<div class="chivalry-item"><span>{name}</span><p>{meaning}</p></div>'
                for name, meaning in KNIGHTLY_RULE
            )
            + "</div>",
            unsafe_allow_html=True,
        )
        st.markdown("#### Daily Oath of Service")
        st.markdown(
            f"""
            <div class="daily-oath">
                <p>{oath['allegiance']}</p>
                <p>{oath['renunciation']}</p>
                <p>{oath['service']}</p>
                <p><strong>Watchword:</strong> {oath['watchword']}</p>
                <footer>{oath['seal']}</footer>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if not st.session_state.daily_oath_taken:
            if st.button("Take Today's Oath", use_container_width=True):
                st.session_state.daily_oath_taken = True
                st.rerun()
        else:
            st.success("Oath received for today. Prove it through the next hidden obedience.")
        st.markdown("#### Rule Silence")
        st.write(
            f"Keep {rule['time']} of silence beneath the Watchword. Let the oath descend from language into attention, body, and action."
        )
        if st.button(
            "Begin the Vigil",
            use_container_width=True,
            disabled=not st.session_state.daily_oath_taken,
        ):
            st.session_state.rule_silence_active = True
            st.session_state.rule_silence_started_at = time.time()
            st.rerun()
        st.markdown("#### If It Feels Too Heavy")
        st.write(lesser_obedience(rule))
        st.download_button(
            "Take This Rule Offline",
            data=plain_text_rule(rule, st.session_state.renunciation),
            file_name="the-inner-monk-rule.txt",
            mime="text/plain",
            use_container_width=True,
        )
    elif step_name == "Depart":
        departure = departure_rule(rule, cross_thread)
        st.markdown("#### Closing")
        render_paschal_thread(cross_thread, "Departure carries risen obedience back into the world without surrendering to the world.")
        render_seasonal_thread(seasonal_thread)
        st.write(posture["closing"])
        st.markdown("#### Rule of Departure")
        st.markdown(
            f"""
            <div class="departure-rule">
                <p class="kicker">Leave the cave now</p>
                <h3>Depart under the Cross.</h3>
                <p><strong>Allegiance:</strong> {oath['allegiance']}</p>
                <p><strong>Oath seal:</strong> {oath['seal']}</p>
                <p><strong>Watchword:</strong> {watchword}</p>
                <p><strong>Seal:</strong> {departure['seal']}</p>
                <p><strong>Carry the Cross:</strong> {departure['cross']}</p>
                <p><strong>Carry the Resurrection:</strong> {departure['resurrection']}</p>
                <p><strong>Digital boundary:</strong> {departure['digital']}</p>
                <p><strong>Bodily obedience:</strong> {departure['body']}</p>
                <p><strong>Name to carry:</strong> {departure['carry']}</p>
                <p><strong>Command:</strong> {departure['command']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(
            "Begin the Vigil",
            use_container_width=True,
            key="depart_silence",
            disabled=not st.session_state.daily_oath_taken,
        ):
            st.session_state.rule_silence_active = True
            st.session_state.rule_silence_started_at = time.time()
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    previous_index = previous_path_step_index(step_name)
    next_index = next_path_step_index(step_name)
    prev_col, map_col, next_col = st.columns([1, 1, 1])
    if prev_col.button("Previous", use_container_width=True, disabled=previous_index == step_index):
        st.session_state.cell_step = previous_index
        st.rerun()
    if map_col.button("Full Cave Map", use_container_width=True, disabled=step_name == "Cave Map"):
        st.session_state.cell_step = steps.index("Cave Map")
        st.rerun()
    if next_col.button("Next in Path", use_container_width=True, disabled=next_index == step_index):
        st.session_state.cell_step = next_index
        st.rerun()

    if step_name == "Depart" and st.button(
        "Complete Today's Rule",
        use_container_width=True,
        disabled=not st.session_state.daily_oath_taken,
    ):
        st.session_state.rule_complete = True

    if st.session_state.rule_complete:
        departure = departure_rule(rule, cross_thread)
        st.success("The rule is received. Close the noise. Stand faithful and go serve in peace.")
        st.markdown(
            f"""
            <div class="exit-rule">
                <p class="kicker">Rule of departure</p>
                <p>{watchword}</p>
                <p>{departure['command']}</p>
                <p>{departure['digital']}</p>
                <p>{departure['resurrection']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        reflection = st.text_area(
            "What did this rule reveal?",
            placeholder="A private note. No score. No streak. No display.",
        )
        if st.button("Save Private Reflection", use_container_width=True):
            if reflection.strip():
                save_reflection(rule, reflection)
                st.session_state.reflection_saved = True
            else:
                st.warning("Write one honest sentence before saving.")

        if st.session_state.reflection_saved:
            st.caption(f"Saved locally to {REFLECTIONS_PATH}.")

        if st.button("Return to the Entrance", use_container_width=True):
            st.session_state.rule = None
            st.session_state.rule_complete = False
            st.session_state.rule_silence_active = False
            st.session_state.rule_silence_started_at = None
            st.session_state.daily_oath_taken = False
            st.session_state.reflection_saved = False
            st.session_state.rule_examen_saved = False
            st.session_state.renunciation = None
            st.session_state.cell_step = 0
            st.session_state.prayer_rope_count = 0
            st.session_state.entered_cell = False
            st.session_state.threshold_step = 0
            st.rerun()
else:
    st.markdown(
        '<p class="empty-note">Choose gently. This is medicine for attention, not a measure of worth.</p>',
        unsafe_allow_html=True,
    )
