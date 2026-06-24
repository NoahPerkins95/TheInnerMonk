import streamlit as st


def apply_theme():
    st.markdown(
        """
        <style>
        :root {
            --ink: #f3ead7;
            --muted: #b9aa8d;
            --gold: #c6a15b;
            --gold-soft: rgba(198, 161, 91, 0.16);
            --ground: #0d0c0a;
            --panel: #17140f;
            --line: rgba(198, 161, 91, 0.28);
        }

        .stApp {
            background:
                radial-gradient(ellipse at 50% -8rem, rgba(198, 161, 91, 0.18), transparent 34rem),
                radial-gradient(ellipse at left 20%, rgba(0, 0, 0, 0.66), transparent 28rem),
                radial-gradient(ellipse at right 22%, rgba(0, 0, 0, 0.66), transparent 28rem),
                radial-gradient(circle at top, rgba(198, 161, 91, 0.11), transparent 34rem),
                var(--ground);
            color: var(--ink);
        }

        .block-container {
            max-width: 900px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        .monk-app {
            background:
                linear-gradient(180deg, rgba(198, 161, 91, 0.1), rgba(198, 161, 91, 0.02)),
                #0a0907;
            border: 1px solid var(--line);
            border-radius: 26px;
            box-shadow: 0 2rem 5rem rgba(0, 0, 0, 0.45);
            margin: 0.5rem auto 1.4rem;
            max-width: 460px;
            overflow: hidden;
            padding: 0.75rem;
        }

        .monk-visual {
            background:
                linear-gradient(180deg, rgba(8, 7, 5, 0.03), rgba(8, 7, 5, 0.78)),
                radial-gradient(circle at top, rgba(198, 161, 91, 0.22), transparent 60%),
                #15110c;
            background-position: center;
            background-size: cover;
            border: 1px solid rgba(198, 161, 91, 0.22);
            border-radius: 22px;
            min-height: 390px;
            padding: 1.2rem;
            position: relative;
        }

        .monk-topline {
            align-items: center;
            display: flex;
            justify-content: space-between;
        }

        .monk-topline span {
            background: rgba(8, 7, 5, 0.58);
            border: 1px solid rgba(198, 161, 91, 0.24);
            border-radius: 999px;
            color: var(--muted);
            font-size: 0.78rem;
            padding: 0.35rem 0.65rem;
        }

        .monk-title {
            bottom: 1.25rem;
            left: 1.2rem;
            max-width: 20rem;
            position: absolute;
            right: 1.2rem;
        }

        .monk-title h1 {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 2.15rem;
            font-weight: 400;
            line-height: 1.05;
            margin: 0;
            text-shadow: 0 0.25rem 1.2rem rgba(0, 0, 0, 0.62);
        }

        .monk-title p:last-child {
            color: var(--muted);
            line-height: 1.55;
            margin: 0.7rem 0 0;
        }

        .monk-control-panel {
            padding: 0.9rem 0.1rem 0.1rem;
        }

        .monk-card {
            background: rgba(23, 20, 15, 0.92);
            border: 1px solid var(--line);
            border-radius: 18px;
            padding: 1.15rem;
        }

        .monk-card h2 {
            margin: 0.25rem 0 0.45rem;
        }

        .monk-card p {
            color: var(--muted);
            margin-bottom: 0;
        }

        .monk-tiles {
            display: grid;
            gap: 0.75rem;
            grid-template-columns: 1fr 1fr;
            margin-top: 0.75rem;
        }

        .monk-tiles div {
            background: rgba(198, 161, 91, 0.08);
            border: 1px solid rgba(198, 161, 91, 0.18);
            border-radius: 16px;
            padding: 0.9rem;
        }

        .monk-tiles span {
            color: var(--muted);
            display: block;
            font-size: 0.78rem;
            margin-bottom: 0.25rem;
        }

        .monk-tiles strong {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 400;
        }

        .monk-bottom-nav {
            align-items: center;
            background: rgba(8, 7, 5, 0.7);
            border: 1px solid rgba(198, 161, 91, 0.16);
            border-radius: 18px;
            display: grid;
            gap: 0.25rem;
            grid-template-columns: repeat(4, 1fr);
            margin-top: 0.75rem;
            padding: 0.45rem;
            text-align: center;
        }

        .monk-bottom-nav span {
            border-radius: 14px;
            color: var(--muted);
            font-size: 0.78rem;
            padding: 0.55rem 0.2rem;
        }

        .monk-bottom-nav span.active {
            background: var(--gold-soft);
            color: var(--ink);
        }

        .cave-app {
            position: relative;
        }

        .cave-app::before {
            background:
                radial-gradient(circle at 20% 18%, rgba(198, 161, 91, 0.18), transparent 0.42rem),
                radial-gradient(circle at 74% 14%, rgba(198, 161, 91, 0.12), transparent 0.34rem),
                radial-gradient(circle at 48% 9%, rgba(198, 161, 91, 0.10), transparent 0.28rem);
            content: "";
            inset: 0;
            opacity: 0.7;
            pointer-events: none;
            position: absolute;
        }

        .cave-mouth,
        .cave-interior,
        .monk-control-panel {
            position: relative;
            z-index: 1;
        }

        .cave-mouth {
            box-shadow:
                inset 0 1.2rem 2rem rgba(255, 230, 171, 0.04),
                inset 0 -1.5rem 2.4rem rgba(0, 0, 0, 0.34);
        }

        .cave-interior::after {
            background:
                radial-gradient(ellipse at center 35%, transparent 30%, rgba(0, 0, 0, 0.28) 58%, rgba(0, 0, 0, 0.72) 100%),
                linear-gradient(180deg, transparent 54%, rgba(0, 0, 0, 0.72));
            content: "";
            inset: 0;
            pointer-events: none;
            position: absolute;
        }

        .cave-interior > * {
            position: relative;
            z-index: 1;
        }

        .cave-stones span {
            font-family: Georgia, "Times New Roman", serif;
        }

        .opening-art {
            aspect-ratio: 1.18 / 1;
        }

        .opening-threshold h1 {
            letter-spacing: 0;
        }

        .cave-map {
            display: grid;
            gap: 0.75rem;
            margin: 1rem 0;
        }

        .cave-stage {
            background:
                linear-gradient(135deg, rgba(198, 161, 91, 0.16), rgba(198, 161, 91, 0.04)),
                rgba(8, 7, 5, 0.82);
            border: 1px solid rgba(198, 161, 91, 0.26);
            border-radius: 22px 22px 12px 12px;
            margin: 1.35rem 0 0.55rem;
            padding: 1rem 1.1rem;
        }

        .cave-stage h3 {
            font-size: 1.15rem;
            line-height: 1.35;
            margin: 0;
        }

        .cave-map-node {
            background:
                linear-gradient(135deg, rgba(198, 161, 91, 0.12), rgba(198, 161, 91, 0.03)),
                rgba(8, 7, 5, 0.68);
            border: 1px solid rgba(198, 161, 91, 0.20);
            border-radius: 16px;
            margin-top: 0.55rem;
            padding: 0.8rem 0.95rem;
        }

        .cave-map-node.active {
            background: rgba(198, 161, 91, 0.16);
            border-color: var(--gold);
        }

        .cave-map-node span {
            color: var(--gold);
            display: block;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.05rem;
            margin-bottom: 0.25rem;
        }

        .cave-map-node p {
            color: var(--muted);
            margin: 0;
        }

        .witness-card,
        .lectio-card,
        .creed-response {
            background:
                linear-gradient(135deg, rgba(198, 161, 91, 0.13), rgba(198, 161, 91, 0.03)),
                rgba(8, 7, 5, 0.72);
            border: 1px solid rgba(198, 161, 91, 0.24);
            border-radius: 20px;
            margin: 1rem 0;
            padding: 1.25rem;
        }

        .todays-path-card {
            background:
                radial-gradient(circle at top right, rgba(198, 161, 91, 0.16), transparent 12rem),
                linear-gradient(135deg, rgba(198, 161, 91, 0.13), rgba(198, 161, 91, 0.03)),
                rgba(8, 7, 5, 0.78);
            border: 1px solid rgba(198, 161, 91, 0.30);
            border-left: 1px solid var(--gold);
            border-radius: 22px;
            box-shadow:
                inset 0 1rem 2rem rgba(255, 235, 180, 0.025),
                inset 0 -1.5rem 2.8rem rgba(0, 0, 0, 0.28);
            margin: 0.5rem 0 1.25rem;
            padding: 1.25rem;
        }

        .fathers-path-card,
        .father-profile {
            background:
                radial-gradient(circle at top right, rgba(198, 161, 91, 0.16), transparent 13rem),
                linear-gradient(135deg, rgba(198, 161, 91, 0.12), rgba(198, 161, 91, 0.025)),
                rgba(8, 7, 5, 0.78);
            border: 1px solid rgba(198, 161, 91, 0.28);
            border-left: 1px solid var(--gold);
            border-radius: 22px;
            box-shadow:
                inset 0 1rem 2rem rgba(255, 235, 180, 0.025),
                inset 0 -1.5rem 2.8rem rgba(0, 0, 0, 0.28);
            margin: 1rem 0 1.25rem;
            padding: 1.25rem;
        }

        .fathers-path-card h3,
        .father-profile h3 {
            font-size: 1.7rem;
            line-height: 1.2;
            margin: 0.15rem 0 0.75rem;
        }

        .fathers-path-card p:last-child {
            color: var(--muted);
            margin-bottom: 0;
        }

        .trail-steps {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1rem 0;
        }

        .trail-steps span {
            background: rgba(0, 0, 0, 0.24);
            border: 1px solid rgba(198, 161, 91, 0.18);
            border-radius: 999px 999px 10px 10px;
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 0.82rem;
            padding: 0.42rem 0.7rem;
        }

        .trail-steps span.read {
            background: rgba(198, 161, 91, 0.14);
            border-color: rgba(198, 161, 91, 0.34);
            color: var(--gold);
        }

        .trail-steps span.active {
            border-color: var(--gold);
            box-shadow: 0 0 0 1px rgba(198, 161, 91, 0.18);
            color: var(--ink);
        }

        .trail-progress {
            color: var(--gold) !important;
            font-family: Georgia, "Times New Roman", serif;
            margin-top: 0.8rem;
        }

        .father-theme {
            color: var(--gold) !important;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.05rem;
            margin-bottom: 1.1rem;
        }

        .father-profile section {
            border-top: 1px solid rgba(198, 161, 91, 0.16);
            padding: 0.85rem 0;
        }

        .father-profile section:last-child {
            padding-bottom: 0;
        }

        .father-profile span {
            color: var(--gold);
            display: block;
            font-size: 0.75rem;
            letter-spacing: 0.14rem;
            margin-bottom: 0.35rem;
            text-transform: uppercase;
        }

        .father-profile section p {
            color: var(--ink);
            line-height: 1.7;
            margin: 0;
        }

        .reading-list {
            display: grid;
            gap: 0.7rem;
        }

        .reading-list article {
            background: rgba(0, 0, 0, 0.22);
            border: 1px solid rgba(198, 161, 91, 0.14);
            border-radius: 14px;
            padding: 0.85rem;
        }

        .reading-list strong {
            color: var(--ink);
            display: block;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.02rem;
            font-weight: 400;
            margin-bottom: 0.35rem;
        }

        .reading-list p {
            color: var(--muted) !important;
            margin-bottom: 0.45rem !important;
        }

        .reading-list em {
            color: var(--gold);
            display: block;
            font-style: normal;
            line-height: 1.55;
        }

        .reading-list a {
            color: var(--ink);
            display: inline-block;
            font-size: 0.86rem;
            margin-top: 0.65rem;
            text-decoration-color: rgba(198, 161, 91, 0.65);
            text-underline-offset: 0.2rem;
        }

        .reading-list small {
            color: var(--muted);
            display: block;
            line-height: 1.5;
            margin-top: 0.65rem;
        }

        .todays-path-card h3 {
            font-size: 1.55rem;
            margin: 0.15rem 0 1rem;
        }

        .watchword-card {
            background:
                radial-gradient(circle at top right, rgba(198, 161, 91, 0.18), transparent 10rem),
                rgba(0, 0, 0, 0.26);
            border: 1px solid rgba(198, 161, 91, 0.30);
            border-left: 1px solid var(--gold);
            border-radius: 18px;
            box-shadow:
                inset 0 1rem 2rem rgba(255, 235, 180, 0.025),
                inset 0 -1.2rem 2.2rem rgba(0, 0, 0, 0.24);
            margin: 1rem 0 1.15rem;
            padding: 1rem 1.1rem;
        }

        .watchword-card.compact {
            margin: 0.8rem 0 1rem;
        }

        .watchword-card span {
            color: var(--gold);
            display: block;
            font-size: 0.72rem;
            letter-spacing: 0.16rem;
            margin-bottom: 0.4rem;
            text-transform: uppercase;
        }

        .watchword-card p {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.08rem;
            line-height: 1.55;
            margin: 0;
        }

        .silence-screen {
            align-items: center;
            background:
                radial-gradient(circle at center 20%, rgba(198, 161, 91, 0.16), transparent 14rem),
                radial-gradient(ellipse at 50% 100%, rgba(0, 0, 0, 0.72), transparent 20rem),
                rgba(8, 7, 5, 0.92);
            border: 1px solid rgba(198, 161, 91, 0.28);
            border-radius: 28px;
            box-shadow:
                inset 0 2rem 4rem rgba(255, 235, 180, 0.025),
                inset 0 -3rem 6rem rgba(0, 0, 0, 0.40),
                0 1.5rem 4rem rgba(0, 0, 0, 0.32);
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin: 1rem 0 1.2rem;
            min-height: 30rem;
            padding: 2rem;
            text-align: center;
        }

        .silence-screen h1 {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 4.2rem;
            font-weight: 400;
            letter-spacing: 0.04rem;
            line-height: 1;
            margin: 0.4rem 0 1rem;
        }

        .silence-watchword {
            color: var(--gold) !important;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.35rem;
            line-height: 1.55;
            max-width: 34rem;
        }

        .silence-instruction {
            color: var(--muted) !important;
            line-height: 1.7;
            max-width: 30rem;
        }

        .path-grid {
            display: grid;
            gap: 0.65rem;
            grid-template-columns: repeat(4, 1fr);
            margin: 1rem 0;
        }

        .path-grid div {
            background: rgba(0, 0, 0, 0.22);
            border: 1px solid rgba(198, 161, 91, 0.16);
            border-radius: 14px;
            padding: 0.75rem;
        }

        .path-grid span {
            color: var(--muted);
            display: block;
            font-size: 0.76rem;
            margin-bottom: 0.25rem;
        }

        .path-grid strong {
            color: var(--ink);
            display: block;
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 400;
            line-height: 1.2;
        }

        .path-line,
        .path-note {
            color: var(--muted);
            margin-bottom: 0;
        }

        .path-note {
            font-size: 0.92rem;
            margin-top: 0.4rem;
        }

        .witness-card h3 {
            margin: 0.2rem 0 0.8rem;
        }

        .witness-card p:last-child {
            color: var(--ink);
            line-height: 1.7;
            margin-bottom: 0;
        }

        .lectio-card h3 {
            margin: 0.2rem 0 0.8rem;
        }

        .lectio-card p:last-child {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.08rem;
            line-height: 1.75;
            margin-bottom: 0;
        }

        .creed-response {
            text-align: center;
        }

        .creed-response p {
            color: var(--gold);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.2rem;
            margin: 0;
        }

        .hero {
            padding: 2.5rem 0 2rem;
            border-bottom: 1px solid var(--line);
            margin-bottom: 2rem;
        }

        .opening-hero {
            border-bottom: 0;
            margin-bottom: 1rem;
            padding: 0.6rem 0 1rem;
        }

        .compact-hero {
            padding-top: 1rem;
        }

        .inner-cell-hero {
            align-items: end;
            background:
                radial-gradient(ellipse at 50% 115%, rgba(0, 0, 0, 0.62), transparent 14rem),
                radial-gradient(circle at 88% 22%, rgba(198, 161, 91, 0.14), transparent 7rem),
                linear-gradient(135deg, rgba(198, 161, 91, 0.10), rgba(8, 7, 5, 0.84));
            border: 1px solid var(--line);
            border-radius: 26px 26px 18px 18px;
            display: grid;
            gap: 1rem;
            grid-template-columns: 1fr auto;
            margin: 0.5rem 0 1.2rem;
            padding: 1.4rem;
            position: relative;
            overflow: hidden;
        }

        .inner-cell-hero::after {
            background:
                linear-gradient(90deg, rgba(0, 0, 0, 0.36), transparent 18%, transparent 82%, rgba(0, 0, 0, 0.36)),
                radial-gradient(ellipse at 50% 116%, rgba(198, 161, 91, 0.12), transparent 12rem);
            content: "";
            inset: 0;
            pointer-events: none;
            position: absolute;
        }

        .inner-cell-hero > * {
            position: relative;
            z-index: 1;
        }

        .inner-cell-hero h1 {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 2.2rem;
            font-weight: 400;
            line-height: 1.05;
            margin: 0;
        }

        .inner-cell-hero p:last-child {
            color: var(--muted);
            margin: 0.7rem 0 0;
        }

        .cell-lamp {
            align-items: center;
            background: rgba(198, 161, 91, 0.12);
            border: 1px solid var(--gold);
            border-radius: 999px 999px 12px 12px;
            color: var(--gold);
            display: flex;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.8rem;
            height: 4rem;
            justify-content: center;
            width: 3rem;
        }

        .chamber-selector {
            margin-top: 1.2rem;
        }

        .chamber-form-title {
            background:
                linear-gradient(135deg, rgba(198, 161, 91, 0.10), rgba(198, 161, 91, 0.02)),
                rgba(8, 7, 5, 0.62);
            border: 1px solid var(--line);
            border-left: 1px solid var(--gold);
            border-radius: 18px;
            margin: 1.8rem 0 0.8rem;
            padding: 1rem 1.15rem;
        }

        .chamber-form-title h3 {
            margin: 0 0 0.55rem;
        }

        .chamber-form-title p:last-child {
            color: var(--muted);
            margin-bottom: 0;
        }

        .kicker {
            color: var(--gold);
            font-size: 0.82rem;
            letter-spacing: 0.18rem;
            margin-bottom: 0.6rem;
            text-transform: uppercase;
        }

        .hero h1 {
            color: var(--ink);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 3rem;
            font-weight: 400;
            line-height: 1.08;
            margin: 0;
        }

        .opening-hero h1 {
            font-size: 2.65rem;
        }

        .subtitle,
        .vow,
        .empty-note {
            color: var(--muted);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.15rem;
            margin-top: 0.8rem;
        }

        .vow {
            max-width: 38rem;
            font-size: 1rem;
            line-height: 1.7;
        }

        .rule-card {
            background:
                linear-gradient(90deg, rgba(0, 0, 0, 0.30), transparent 7%, transparent 93%, rgba(0, 0, 0, 0.30)),
                radial-gradient(circle at top left, rgba(198, 161, 91, 0.08), transparent 18rem),
                rgba(13, 11, 8, 0.92);
            border: 1px solid var(--line);
            border-radius: 26px 26px 18px 18px;
            box-shadow:
                inset 0 -2.5rem 5rem rgba(0, 0, 0, 0.28),
                inset 0 1rem 2rem rgba(0, 0, 0, 0.24),
                0 1.2rem 3rem rgba(0, 0, 0, 0.2);
            margin-top: 1rem;
            padding: 1.55rem;
            position: relative;
        }

        .rule-card::before {
            background:
                radial-gradient(ellipse at 50% -1rem, rgba(198, 161, 91, 0.18), transparent 12rem);
            border-radius: 26px 26px 0 0;
            content: "";
            height: 4rem;
            left: 0;
            pointer-events: none;
            position: absolute;
            right: 0;
            top: 0;
        }

        .cell-note,
        .cell-mode,
        .opening-gate,
        .cover-missing,
        .exit-rule,
        .abbot-word {
            background: rgba(198, 161, 91, 0.08);
            border-left: 1px solid var(--gold);
            margin: 1.5rem 0 2rem;
            padding: 1rem 1.2rem;
        }

        .chamber-note,
        .chamber-mode {
            background:
                linear-gradient(135deg, rgba(198, 161, 91, 0.12), rgba(198, 161, 91, 0.03)),
                rgba(8, 7, 5, 0.74);
            border: 1px solid var(--line);
            border-left: 1px solid var(--gold);
            border-radius: 18px;
            margin: 1rem 0 1.2rem;
            padding: 1.15rem 1.25rem;
        }

        .chamber-mode {
            backdrop-filter: blur(10px);
            box-shadow: 0 0.85rem 2rem rgba(0, 0, 0, 0.22);
            position: sticky;
            top: 0.6rem;
            z-index: 3;
        }

        .chamber-mode h2 {
            font-size: 2rem;
            line-height: 1.05;
            margin-bottom: 0.45rem;
        }

        .chamber-progress {
            background: rgba(198, 161, 91, 0.10);
            border: 1px solid rgba(198, 161, 91, 0.16);
            border-radius: 999px;
            height: 0.45rem;
            margin-top: 0.9rem;
            overflow: hidden;
        }

        .chamber-progress span {
            background: linear-gradient(90deg, rgba(198, 161, 91, 0.55), var(--gold));
            border-radius: 999px;
            display: block;
            height: 100%;
        }

        .seasonal-thread,
        .paschal-thread {
            background:
                radial-gradient(circle at top right, rgba(198, 161, 91, 0.14), transparent 10rem),
                rgba(8, 7, 5, 0.76);
            border: 1px solid rgba(198, 161, 91, 0.26);
            border-left: 1px solid var(--gold);
            border-radius: 18px;
            margin: 0.8rem 0 1.25rem;
            padding: 1.15rem 1.25rem;
        }

        .seasonal-thread,
        .paschal-thread,
        .witness-card,
        .lectio-card,
        .creed-response,
        .departure-rule,
        .prayer-rope-panel,
        .threshold-panel,
        .abbot-word {
            box-shadow:
                inset 0 1rem 2rem rgba(255, 235, 180, 0.025),
                inset 0 -1.2rem 2.5rem rgba(0, 0, 0, 0.24);
        }

        .seasonal-thread h4,
        .paschal-thread h4 {
            margin: 0.2rem 0 0.75rem;
        }

        .seasonal-thread p,
        .paschal-thread p {
            color: var(--muted);
            margin-bottom: 0.55rem;
        }

        .seasonal-thread p:last-child,
        .paschal-thread p:last-child {
            margin-bottom: 0;
        }

        .seasonal-thread strong,
        .paschal-thread strong {
            color: var(--ink);
            font-weight: 600;
        }

        .departure-rule {
            background:
                radial-gradient(circle at top, rgba(198, 161, 91, 0.16), transparent 12rem),
                rgba(8, 7, 5, 0.82);
            border: 1px solid var(--gold);
            border-radius: 22px;
            box-shadow: inset 0 1rem 2rem rgba(0, 0, 0, 0.28);
            margin: 1rem 0;
            padding: 1.35rem;
        }

        .departure-rule h3 {
            margin: 0.2rem 0 1rem;
        }

        .departure-rule p {
            color: var(--muted);
            line-height: 1.65;
            margin-bottom: 0.6rem;
        }

        .departure-rule p:last-child {
            margin-bottom: 0;
        }

        .departure-rule strong {
            color: var(--ink);
        }

        .cell-note p,
        .cell-mode p,
        .opening-gate p,
        .cover-missing p,
        .exit-rule p,
        .abbot-word p {
            margin-bottom: 0;
        }

        .opening-gate {
            border-radius: 8px;
            margin: 0.25rem 0 1rem;
            padding: 1.2rem 1.35rem;
        }

        .opening-gate h2 {
            margin: 0.35rem 0 0;
        }

        .opening-prayer {
            color: var(--gold) !important;
            font-family: Georgia, "Times New Roman", serif;
            margin-top: 1rem !important;
        }

        .cell-mode h2 {
            margin: 0.35rem 0 0;
        }

        .cell-path {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 0.8rem 0 1rem;
        }

        .cell-path {
            background: rgba(8, 7, 5, 0.62);
            border: 1px solid rgba(198, 161, 91, 0.14);
            border-radius: 18px;
            flex-wrap: nowrap;
            overflow-x: auto;
            padding: 0.5rem;
            scrollbar-width: thin;
        }

        .threshold-path {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            justify-content: center;
            margin: 1rem 0 1rem;
        }

        .cell-path span {
            background: rgba(8, 7, 5, 0.5);
            border: 1px solid rgba(198, 161, 91, 0.18);
            border-radius: 999px 999px 10px 10px;
            color: var(--muted);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 0.78rem;
            flex: 0 0 auto;
            padding: 0.38rem 0.68rem;
        }

        .threshold-path span {
            background: rgba(8, 7, 5, 0.46);
            border: 1px solid rgba(198, 161, 91, 0.18);
            border-radius: 999px 999px 10px 10px;
            color: var(--muted);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 0.8rem;
            padding: 0.42rem 0.72rem;
        }

        .cell-path span.active {
            background: rgba(198, 161, 91, 0.18);
            border-color: var(--gold);
            color: var(--ink);
        }

        .threshold-path span.active {
            background: rgba(198, 161, 91, 0.18);
            border-color: var(--gold);
            color: var(--ink);
        }

        .threshold-panel {
            background:
                radial-gradient(circle at top left, rgba(198, 161, 91, 0.08), transparent 18rem),
                rgba(8, 7, 5, 0.72);
            border: 1px solid var(--line);
            border-radius: 18px;
            box-shadow: inset 0 1rem 2rem rgba(0, 0, 0, 0.22);
            margin: 1rem 0 1.2rem;
            padding: 1.6rem;
        }

        .threshold-panel h3 {
            margin-top: 0.35rem;
        }

        .invocation-panel {
            text-align: center;
        }

        .prayer-corner {
            display: grid;
            gap: 1rem;
            justify-items: center;
            margin: 1rem 0;
            text-align: center;
        }

        .prayer-cross {
            align-items: center;
            background: rgba(198, 161, 91, 0.08);
            border: 1px solid var(--gold);
            border-radius: 6px;
            display: flex;
            height: 4rem;
            justify-content: center;
            color: var(--gold);
            font-family: Georgia, "Times New Roman", serif;
            font-size: 2rem;
            width: 4rem;
        }

        .prayer-corner p {
            color: var(--muted);
            max-width: 30rem;
        }

        .prayer-rope-panel {
            background:
                radial-gradient(circle at top, rgba(198, 161, 91, 0.12), transparent 9rem),
                rgba(8, 7, 5, 0.78);
            border: 1px solid var(--line);
            border-radius: 20px;
            margin: 1rem 0;
            padding: 1.4rem;
            text-align: center;
        }

        .prayer-rope-panel p:last-child {
            color: var(--muted);
            font-family: Georgia, "Times New Roman", serif;
            margin-bottom: 0;
        }

        .pattern {
            border-bottom: 1px solid var(--line);
            display: grid;
            gap: 0;
            grid-template-columns: repeat(3, 1fr);
            margin: 1rem 0 2rem;
            padding-bottom: 1.5rem;
        }

        .pattern div {
            border-right: 1px solid var(--line);
            padding: 0 1rem;
        }

        .pattern div:first-child {
            padding-left: 0;
        }

        .pattern div:last-child {
            border-right: 0;
        }

        .pattern span {
            color: var(--gold);
            display: block;
            font-family: Georgia, "Times New Roman", serif;
            font-size: 1.8rem;
            margin-bottom: 0.25rem;
        }

        .pattern p {
            color: var(--muted);
            margin: 0;
        }

        .stillness {
            background: rgba(13, 12, 10, 0.94);
            border: 1px solid var(--line);
            border-radius: 8px;
            margin: 1.5rem 0;
            padding: 2rem;
            text-align: center;
        }

        .stillness h2 {
            margin-top: 0.4rem;
        }

        h2, h3, h4 {
            color: var(--ink) !important;
            font-family: Georgia, "Times New Roman", serif;
            font-weight: 400 !important;
        }

        div[data-testid="stMarkdownContainer"] h4 {
            border-top: 1px solid rgba(198, 161, 91, 0.18);
            color: var(--ink) !important;
            font-size: 1.38rem;
            margin-top: 1.6rem;
            padding-top: 1.05rem;
        }

        .rule-card > div:first-child h4,
        div[data-testid="stMarkdownContainer"] h4:first-child {
            border-top: 0;
            margin-top: 0;
            padding-top: 0;
        }

        p, li, label, div[data-testid="stMarkdownContainer"] {
            color: var(--ink);
        }

        div[data-testid="stCaptionContainer"] {
            color: var(--gold);
        }

        .stRadio, .stSelectbox, .stTextArea {
            margin-bottom: 1.1rem;
        }

        div[data-testid="stForm"] {
            background:
                linear-gradient(135deg, rgba(198, 161, 91, 0.08), rgba(198, 161, 91, 0.015)),
                rgba(8, 7, 5, 0.58);
            border: 1px solid rgba(198, 161, 91, 0.18);
            border-radius: 20px;
            padding: 1rem;
        }

        div[role="radiogroup"] {
            gap: 0.4rem;
        }

        textarea {
            background-color: var(--panel) !important;
            border-color: var(--line) !important;
            color: var(--ink) !important;
        }

        div[data-baseweb="select"] > div {
            background-color: var(--panel);
            border-color: var(--line);
            color: var(--ink);
        }

        .stButton > button,
        .stFormSubmitButton > button,
        .stDownloadButton > button {
            background:
                linear-gradient(180deg, rgba(198, 161, 91, 0.20), rgba(198, 161, 91, 0.10));
            border: 1px solid var(--gold);
            border-radius: 14px;
            box-shadow: inset 0 0.55rem 1rem rgba(255, 245, 210, 0.035);
            color: var(--ink);
            min-height: 3rem;
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover,
        .stDownloadButton > button:hover {
            background: rgba(198, 161, 91, 0.24);
            border-color: var(--gold);
            color: #fff7e7;
        }

        .stButton > button:disabled,
        .stFormSubmitButton > button:disabled {
            background: rgba(8, 7, 5, 0.44);
            border-color: rgba(198, 161, 91, 0.12);
            color: rgba(185, 170, 141, 0.45);
        }

        .stAlert {
            background: rgba(198, 161, 91, 0.14);
            border: 1px solid var(--line);
            color: var(--ink);
        }

        @media (max-width: 680px) {
            .stApp {
                background:
                    radial-gradient(ellipse at 50% -6rem, rgba(198, 161, 91, 0.16), transparent 24rem),
                    var(--ground);
            }

            .hero h1 {
                font-size: 2.35rem;
            }

            .opening-hero h1 {
                font-size: 2.15rem;
            }

            .block-container {
                padding: 0.8rem 0.8rem calc(3rem + env(safe-area-inset-bottom));
            }

            .monk-app {
                border-radius: 22px 22px 16px 16px;
                margin-top: 0;
                padding: 0.55rem;
                width: 100%;
            }

            .opening-art {
                aspect-ratio: 1 / 1;
                min-height: 260px !important;
            }

            .opening-threshold,
            .monk-card {
                padding: 1rem !important;
            }

            .chamber-mode {
                margin-top: 0.65rem;
                padding: 1rem;
                position: relative;
                top: auto;
            }

            .inner-cell-hero {
                grid-template-columns: 1fr;
                padding: 1.1rem;
            }

            .inner-cell-hero h1 {
                font-size: 1.9rem;
            }

            .entry-frame {
                padding: 0.85rem;
            }

            .cell-lamp {
                display: none;
            }

            .cell-path {
                border-radius: 14px;
                margin-bottom: 0.75rem;
                scroll-snap-type: x proximity;
            }

            .cell-path span,
            .trail-steps span {
                scroll-snap-align: start;
            }

            .threshold-path {
                flex-wrap: nowrap;
                justify-content: flex-start;
                overflow-x: auto;
                padding-bottom: 0.25rem;
            }

            .threshold-path span {
                flex: 0 0 auto;
            }

            .pattern {
                grid-template-columns: 1fr;
            }

            .pattern div {
                border-bottom: 1px solid var(--line);
                border-right: 0;
                padding: 0.8rem 0;
            }

            .pattern div:last-child {
                border-bottom: 0;
            }

            .rule-card {
                border-radius: 20px 20px 14px 14px;
                padding: 1rem;
            }

            .path-grid {
                grid-template-columns: 1fr 1fr;
            }

            .todays-path-card,
            .father-profile,
            .fathers-path-card,
            .seasonal-thread,
            .paschal-thread,
            .departure-rule,
            .threshold-panel,
            .prayer-rope-panel {
                border-radius: 16px;
                padding: 1rem;
            }

            .trail-steps {
                flex-wrap: nowrap;
                overflow-x: auto;
                padding-bottom: 0.3rem;
            }

            .trail-steps span {
                flex: 0 0 auto;
            }

            .silence-screen {
                min-height: 66vh;
                padding: 1.4rem;
            }

            .silence-screen h1 {
                font-size: 3.25rem;
            }

            .silence-watchword {
                font-size: 1.17rem;
            }

            div[data-testid="stHorizontalBlock"] {
                flex-direction: column;
                gap: 0.35rem;
            }

            div[data-testid="column"] {
                min-width: 100% !important;
                width: 100% !important;
            }

            div[role="radiogroup"] {
                align-items: stretch;
                flex-wrap: wrap;
            }

            div[role="radiogroup"] > label {
                min-height: 2.75rem;
            }

            div[data-testid="stForm"] {
                border-radius: 16px;
                padding: 0.8rem;
            }

            .stButton > button,
            .stFormSubmitButton > button,
            .stDownloadButton > button {
                min-height: 3.2rem;
                width: 100%;
            }

            p, li, label,
            .father-profile section p,
            .reading-list article {
                overflow-wrap: anywhere;
            }
        }

        @media (max-width: 420px) {
            .block-container {
                padding-left: 0.55rem;
                padding-right: 0.55rem;
            }

            .opening-threshold h1,
            .inner-cell-hero h1 {
                font-size: 1.72rem !important;
            }

            .chamber-mode h2 {
                font-size: 1.7rem;
            }

            .path-grid,
            .monk-tiles {
                grid-template-columns: 1fr;
            }

            .monk-bottom-nav {
                grid-template-columns: 1fr 1fr;
            }

            .silence-screen h1 {
                font-size: 2.75rem;
            }
        }

        header, footer, #MainMenu {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
