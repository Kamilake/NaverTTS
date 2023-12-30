import warnings

TRANSLATE_ENDPOINT = "https://dict.naver.{tld}/api/nvoice"
TRANSLATE_PARAMS = (
    "?service=dictionary&speech_fmt=mp3&text={text}&speaker={speaker}&speed={speed}"
)

LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
}

# https://apidocs.ncloud.com/en/ai-naver/clova_speech_synthesis/tts/
SPEAKERS = {
    "en": {"f": "danna", "m": "matt"},
    "es": {"f": "carmen", "m": "jose"},
    "ja": {"f": "yuri", "m": "shinji"},
    "ko": {
        "f": "kyuri",
        "m": "jinho",
        "nminsang" : "nminsang",
        "nsinu" : "nsinu",
        "njinho" : "njinho",
        "njihun" : "njihun",
        "njooahn" : "njooahn",
        "nseonghoon" : "nseonghoon",
        "njihwan" : "njihwan",
        "nsiyoon" : "nsiyoon",
        "ntaejin" : "ntaejin",
        "nyoungil" : "nyoungil",
        "nseungpyo" : "nseungpyo",
        "nwontak" : "nwontak",
        "njonghyun" : "njonghyun",
        "njoonyoung" : "njoonyoung",
        "njaewook" : "njaewook",
        "nes_c_kihyo" : "nes_c_kihyo",
        "nraewon" : "nraewon",
        "nkyuwon" : "nkyuwon",
        "nkitae" : "nkitae",
        "neunwoo" : "neunwoo",
        "nkyungtae" : "nkyungtae",
        "nwoosik" : "nwoosik",
        "dsinu-matt" : "dsinu-matt",
        "vdaeseong" : "vdaeseong",
        "ngyeongjun" : "ngyeongjun",
        "ndaeseong" : "ndaeseong",
        "njonghyeok" : "njonghyeok",
        "nian" : "nian",
        "ndonghyun" : "ndonghyun",
        "vian" : "vian",
        "vdonghyun" : "vdonghyun",
        "nmovie" : "nmovie",
        "nsangdo" : "nsangdo",
        "nreview" : "nreview",
        "nmammon" : "nmammon",
        "dara-danna" : "dara-danna",
        "nyujin" : "nyujin",
        "nara" : "nara",
        "nara_call" : "nara_call",
        "nminyoung" : "nminyoung",
        "nyejin" : "nyejin",
        "mijin" : "mijin",
        "nhajun" : "nhajun",
        "ndain" : "ndain",
        "njiyun" : "njiyun",
        "nsujin" : "nsujin",
        "ngaram" : "ngaram",
        "ngoeun" : "ngoeun",
        "neunyoung" : "neunyoung",
        "nsunkyung" : "nsunkyung",
        "dara_ang" : "dara_ang",
        "nsunhee" : "nsunhee",
        "nminseo" : "nminseo",
        "njiwon" : "njiwon",
        "nbora" : "nbora",
        "nes_c_hyeri" : "nes_c_hyeri",
        "nes_c_sohyun" : "nes_c_sohyun",
        "nes_c_mikyung" : "nes_c_mikyung",
        "ntiffany" : "ntiffany",
        "napple" : "napple",
        "njangj" : "njangj",
        "noyj" : "noyj",
        "neunseo" : "neunseo",
        "nheera" : "nheera",
        "nyoungmi" : "nyoungmi",
        "nnarae" : "nnarae",
        "nyeji" : "nyeji",
        "nyuna" : "nyuna",
        "nkyunglee" : "nkyunglee",
        "nminjeong" : "nminjeong",
        "nihyun" : "nihyun",
        "vara" : "vara",
        "vmikyung" : "vmikyung",
        "vdain" : "vdain",
        "vyuna" : "vyuna",
        "vhyeri" : "vhyeri",
        "nsabina" : "nsabina",
        "nmeow" : "nmeow",
        "nwoof" : "nwoof",
        "nyounghwa" : "nyounghwa",
        "nshasha" : "nshasha",
        "vgoeun" : "vgoeun"
    }
    "zh": {"f": "meimei", "m": "liangliang"},
}


def get_speaker(lang="ko", gender="f"):
    """Get the API name for the chosen speaker."""
    try:
        speakers = SPEAKERS[lang]
    except KeyError:
        raise ValueError(
            "No speaker for language {}. "
            "Available languages: {}".format(lang, list(SPEAKERS.keys()))
        )
    try:
        return speakers[gender]
    except KeyError:
        warnings.warn("Gender {} not available for language" " {}".format(gender, lang))
        return list(speakers.values())[0]


def translate_base(tld="com"):
    """Get the base URL."""
    return TRANSLATE_ENDPOINT.format(tld=tld)


def translate_endpoint(text, speaker="kyuri", speed=0, tld="com"):
    """Get the endpoint URL."""
    url = translate_base(tld=tld)
    return url + TRANSLATE_PARAMS.format(text=text, speaker=speaker, speed=speed)
