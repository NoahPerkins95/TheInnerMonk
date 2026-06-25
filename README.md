# The Inner Monk

The Inner Monk is a quiet, Orthodox Christian Daily Rule of Life generator for breaking free from the world's noise and returning to Jesus Christ.

Subtitle: **A daily practice of theosis.**

It is not a normal Bible app, devotional app, wellness tracker, habit tracker, dashboard, or social app. It is meant to be a small replacement for social media brain rot: a moment of prayerful resistance before the feed, the scroll, and the scattered mind.

It does not pretend to replace the Church, the sacraments, pastoral guidance, parish life, or a real spiritual father. It is a small Christian cell for people who feel the spiritual hunger for monk life: silence, repentance, simplicity, unceasing prayer, and union with Christ.

Its movement is immediate return: break contact with the world's distorted pattern, recover watchfulness, turn the mind to Jesus Christ, and keep one clean obedience. It does not ask users to rehearse or catalog failures. Persistent or enslaving patterns should be brought out of isolation to a priest and a trustworthy Christian brother.

The app asks for the kind of rule needed today, the user's state of soul, and the time available, then offers a simple rule with prayer, body discipline, mind discipline, and a reflection prompt. It also includes a "Tempted to scroll?" path for the moment when the user reaches for the feed and needs a short rule instead.

To use the branded opening artwork, place the image at `assets/the-inner-monk-cover.png`.

## Principles

- Quiet over content.
- Prayer over productivity.
- Discipline over dopamine.
- Theosis over self-optimization.
- No streaks, badges, dashboards, leaderboards, feeds, or social features.

## Current Features

- Daily Rule discernment by season, burden, passion, strength, time, holy hunger, digital fast, and prayer rope rule.
- Daily Watchword generated from the rule context and carried through Opening, Prayer, Purity, Departure, and offline export.
- Rule Silence timer for 5, 15, or 30 minutes, carrying the Watchword on a stripped-down practice screen.
- Emergency anti-scroll discernment for restless, numb, avoiding, or lonely moments.
- Opening threshold ritual before the user sees any controls: threshold, renunciation, invocation, and desire.
- Ten-second stillness pause before a rule appears.
- Monastic pattern: enter quietly, receive one rule, practice and leave.
- Cell Mode hides the setup after a rule is received, then walks through chamber-by-chamber: opening, cave map, daily order, witness, prayer corner, renunciation, passion, cross and resurrection, scripture, creed, prayer, prayer rope, body temple, practice, examen, seal, and depart.
- Staged Cave Map chamber that frames the rule as a movement through Entrance, Illumination, Struggle, and Return, with short chamber entry controls.
- Expanded Witness chamber with rotating saint, martyr, and holy witness stories, including how the witness suffered or was martyred, plus deeper reading, what the witness resisted, virtue, Cross/Resurrection meaning, theosis thread, imitation, small act, and reflection. This is an MVP rotation, not an official live Orthodox calendar.
- Cross and Resurrection chamber that makes the whole rule Paschal: what must die, what risen life Christ gives, and one concrete practice.
- Repeated Paschal Thread boxes in major chambers so Witness, Scripture, Creed, Prayer, Body Temple, Return, and Departure all return to the Cross and Resurrection.
- Rule of Departure sends the user out with a final seal, Cross practice, Resurrection act of mercy, digital boundary, bodily obedience, Jesus Prayer, and command to leave the app.
- Private Paschal Return inside the rule flow asks what false pattern must lose its hold, what life Christ is calling forth, and what clean obedience begins now.
- Church Fathers library for self-exploration outside the daily rule, with historical trails through Apostolic Fire, Blood of the Martyrs, Desert Combat, Nicene Truth, Prayer of the Heart, Mercy and Repentance, and Theosis.
- Local Fathers trail progress with Previous/Next Father, Mark as Read, and private notes saved to `data/fathers_progress.json`.
- Suggested primary readings for each Father or witness, pointing users toward Scripture, lives, letters, homilies, ascetic texts, and classic Orthodox writings.
- Creed Chamber centered on the Nicene-Constantinopolitan Creed, with an optional historical note for the Apostles' Creed.
- Prayer Rope Mode for 12, 33, or 50 Jesus Prayers with posture guidance, mode meaning, silence intervals, and guardrails against turning prayer into achievement.
- Evening Return mode gathers the mind from false refuges and saves a private next-obedience reflection to `data/examen.jsonl`.
- Private Journal view for recent local reflections and examens, with plain text export.
- Daily Order / Little Typikon page that gives the day a simple rhythm: morning, labor, body, mercy, evening, and sleep.
- Passion and Virtue page that names the pull of the heart, the Christward virtue, and one small obedience.
- Prayer Corner page with no representational artwork, just stillness before God.
- Expanded Scripture Reading page with sayings of Jesus tied to the Cross, Resurrection, watchfulness, forgiveness, hidden prayer, and mission.
- Body Temple page with a three-part bodily rule: Food as Thanksgiving, Strength as Service, and Rest as Obedience, including biblical/simple diet guidance, fasting from modern appetite-engineered foods, Pavel-inspired hardstyle kettlebell practice, bodyweight fallback, and restoration without scrolling.
- Purity chamber for breaking contact with lust and unreality through custody of the eyes, bodily action, the Jesus Prayer, clean boundaries, priestly guidance, and trustworthy brotherhood.
- Digital Fast Vow for 15 minutes, 1 hour, until evening, or until tomorrow morning.
- Liturgical moment selection: morning, midday, evening, or before sleep.
- Seasonal modes: Daily, Repentance / Lent, Cross-bearing / Holy Week, Resurrection / Pascha, and Preparation / Nativity Fast.
- Ancient prayer layer with the Trisagion, the Lord's Prayer, the Glory, and the Jesus Prayer.
- Daily Beatitude included with each rule.
- Early Church Father teaching and practice guidance by state of soul.
- Leaving-the-world prompts that name what the user is turning from.
- Monastic longing prompts: silence, purity of heart, repentance, unceasing prayer, simplicity, and union with Christ.
- Orthodox opening posture, remembrance, watchfulness, guarding the senses, and closing.
- Theosis thread that ties each state of soul to transformation in Christ.
- Short examen questions for sober reflection.
- Rule seal, a short sentence to carry after closing the app.
- Plain text download so the user can take the rule offline.
- Exit discipline that sends the user away from the app and back into practice.
- Optional private reflection saved locally to `data/reflections.jsonl`.

## Preview

First screen:

> A quiet rule before the noise.
>
> Not a feed. Not a tracker. Not a place to perform. A small monastic pause for prayer, discipline, and return to Christ.

After completing a rule:

> Exit discipline
>
> Leave this screen now. Keep the rule for 5 minutes before returning to any feed, inbox, or stream.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

If the browser shows an old import error after edits, stop the running Streamlit process and run `streamlit run app.py` again.

## Deploy and Share

The project is ready for Streamlit Community Cloud:

1. Install Git and create a GitHub repository.
2. Commit the project files. The included `.gitignore` excludes private journal, examen, Father-note, and progress data.
3. Push the repository to GitHub.
4. Open [Streamlit Community Cloud](https://share.streamlit.io/), choose the repository, and set the entrypoint to `app.py`.
5. Deploy and share the generated public URL.

The app includes `.streamlit/config.toml` and `requirements.txt` for deployment.

Important: files written under `data/` are appropriate for a local single-user MVP, but should not be treated as durable private storage on a public cloud deployment. Before adding real user accounts, move journal and progress data to authenticated persistent storage.

Official deployment guide: [Deploy your app on Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)

## Sources

See [SOURCES.md](SOURCES.md) for primary-text collections, direct reading links, and editorial guardrails.
