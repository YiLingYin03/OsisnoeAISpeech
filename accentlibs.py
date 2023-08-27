import streamlit as st

def get_test_script():
    text = "I am the English text-to-speech assistant of 'Osisnoe' startup, " \
           "employing advanced AI to transform written content into lifelike speech. " \
           "Committed to enhancing learning accessibility, " \
           "I facilitate dynamic communication by infusing various accents, tones, and languages." \
           " As a pivotal asset to 'Osisnoe,'" \
           " I contribute to our mission of revolutionizing personalized education through innovation and inclusivity."

    return text

def get_accent(english_accent):
    accent = "n-US-JennyMultilingualNeural"
    profolio = "Default.png"
    if english_accent == "Default":
        accent = "en-US-JennyMultilingualNeural"
    elif english_accent == "Australia-Natasha":
        accent = "en-AU-NatashaNeural"
    elif english_accent == "Australia-William":
        accent = "en-AU-WilliamNeural"
    elif english_accent == "Australia-Annette":
        accent = "en-AU-AnnetteNeural"
    elif english_accent == "Australia-Carly":
        accent = "en-AU-CarlyNeural"
    elif english_accent == "Australia-Darren":
        accent = "en-AU-DarrenNeural"
    elif english_accent == "UnitedKingdom-Sonia":  # UK
        accent = "en-GB-SoniaNeural"
    elif english_accent == "UnitedKingdom-Ryan":
        accent = "en-GB-RyanNeural"
        profolio = "UnitedKingdom-Ryan.png"
    elif english_accent == "UnitedKingdom-Libby":
        accent = "en-GB-LibbyNeural"
    elif english_accent == "UnitedKingdom-Abbi":
        accent = "en-GB-AbbiNeural"
    elif english_accent == "UnitedKingdom-Alfie":
        accent = "en-GB-AlfieNeural"
    elif english_accent == "UnitedKingdom-Elliot":
        accent = "en-GB-ElliotNeural"
    elif english_accent == "UnitedKingdom-Ethan":
        accent = "en-GB-EthanNeural"
    elif english_accent == "UnitedKingdom-Hollie":
        accent = "en-GB-HollieNeural"
    elif english_accent == "UnitedKingdom-Maisie":
        accent = "en-GB-MaisieNeural"
    elif english_accent == "UnitedKingdom-Noah":
        accent = "en-GB-NoahNeural"
    elif english_accent == "UnitedKingdom-Oliver":
        accent = "en-GB-OliverNeural"
    elif english_accent == "UnitedKingdom-Olivia":
        accent = "en-GB-OliviaNeural"
    elif english_accent == "UnitedKingdom-Thomas":
        accent = "en-GB-ThomasNeural"
    elif english_accent == "HongKong-Yan":  # Hong kong
        accent = "en-HK-YanNeural"
    elif english_accent == "HongKong-Sam":
        accent = "en-HK-SamNeural"
    elif english_accent == "Ireland-Emily":  # Ireland
        accent = "en-IE-EmilyNeural"
    elif english_accent == "Ireland-Connor":
        accent = "en-IE-ConnorNeural"
    elif english_accent == "India-Neerja":  # India
        accent = "en-IN-NeerjaNeural"
    elif english_accent == "India-Prabhat":
        accent = "en-IN-PrabhatNeural"
    elif english_accent == "UnitedStates-Jenny":  # US
        accent = "en-US-JennyNeural"
    elif english_accent == "UnitedStates-Guy":
        accent = "en-US-GuyNeural"
    elif english_accent == "UnitedStates-Aria":
        accent = "en-US-AriaNeural"
    elif english_accent == "UnitedStates-Davis":
        accent = "en-US-DavisNeural"
    elif english_accent == "UnitedStates-Amber":
        accent = "en-US-AmberNeural"
    elif english_accent == "UnitedStates-Ana":
        accent = "en-US-AnaNeural"
    elif english_accent == "UnitedStates-Ashley":
        accent = "en-US-AshleyNeural"
    elif english_accent == "UnitedStates-Brandon":
        accent = "en-US-BrandonNeural"
    elif english_accent == "UnitedStates-Christopher":
        accent = "en-US-ChristopherNeural"
    elif english_accent == "UnitedStates-Cora":
        accent = "en-US-CoraNeural"
    elif english_accent == "UnitedStates-Elizabeth":
        accent = "en-US-ElizabethNeural"
    elif english_accent == "UnitedStates-Eric":
        accent = "en-US-EricNeural"
    elif english_accent == "UnitedStates-Jacob":
        accent = "en-US-JacobNeural"
    elif english_accent == "UnitedStates-Jane":
        accent = "en-US-JaneNeural"
    elif english_accent == "UnitedStates-Jason":
        accent = "en-US-JasonNeural"
    elif english_accent == "UnitedStates-Michelle":
        accent = "en-US-MichelleNeural"
    elif english_accent == "UnitedStates-Monica":
        accent = "en-US-MonicaNeural"
    elif english_accent == "UnitedStates-Nancy":
        accent = "en-US-NancyNeural"
    elif english_accent == "UnitedStates-Roger":
        accent = "en-US-RogerNeural"
    elif english_accent == "UnitedStates-Sara":
        accent = "en-US-SaraNeural"
    elif english_accent == "UnitedStates-Steffan":
        accent = "en-US-SteffanNeural"
    elif english_accent == "UnitedStates-Tony":
        accent = "en-US-TonyNeural"
    elif english_accent == "UnitedStates-Blue":
        accent = "en-US-BlueNeural"
    elif english_accent == "UnitedStates-RyanMultilingual":
        accent = "en-US-RyanMultilingualNeural"
    return accent, profolio


def get_accent_list():
    return st.selectbox(
        label="Chose You AI Assistant: :female-office-worker: :male-office-worker:",
        options=
        (
            "Default",
            "Australia-Natasha",
            "Australia-William",
            "Australia-Annette",
            "Australia-Carly",
            "Australia-Darren",
            "UnitedKingdom-Sonia",
            "UnitedKingdom-Ryan",
            "UnitedKingdom-Libby",
            "UnitedKingdom-Abbi",
            "UnitedKingdom-Alfie",
            "UnitedKingdom-Elliot",
            "UnitedKingdom-Ethan",
            "UnitedKingdom-Hollie",
            "UnitedKingdom-Maisie",
            "UnitedKingdom-Noah",
            "UnitedKingdom-Oliver",
            "UnitedKingdom-Olivia",
            "UnitedKingdom-Thomas",
            "HongKong-Yan",
            "HongKong-Sam",
            "Ireland-Emily",
            "Ireland-Connor",
            "India-Neerja",
            "India-Prabhat",
            "UnitedStates-Jenny",
            "UnitedStates-Guy",
            "UnitedStates-Aria",
            "UnitedStates-Davis",
            "UnitedStates-Amber",
            "UnitedStates-Ana",
            "UnitedStates-Ashley",
            "UnitedStates-Brandon",
            "UnitedStates-Christopher",
            "UnitedStates-Cora",
            "UnitedStates-Elizabeth",
            "UnitedStates-Eric",
            "UnitedStates-Jacob",
            "UnitedStates-Jane",
            "UnitedStates-Jason",
            "UnitedStates-Michelle",
            "UnitedStates-Monica",
            "UnitedStates-Nancy",
            "UnitedStates-Roger",
            "UnitedStates-Sara",
            "UnitedStates-Steffan",
            "UnitedStates-Tony"
        ),
    )
