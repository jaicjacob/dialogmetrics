import handle

pos_lookup = {
    "CC" : "Coordinating Conjunction",
    "CD" : "Cardinal Digit",
    "DT" : "Determiner",
    "EX" : "Existential there",
    "FW" : "Foreign Word",
    "IN" : "Reposition/Subordinating Conjunction",
    "JJ" : "Adjective",
    "JJR" : "Adjective - Comparative",
    "JJS" : "Adjective - Superlative",
    "LS" : "List Marker)",
    "MD" : "Modal Could",
    "NN" : "Noun - Singular",
    "NNS" : "Noun - Plural",
    "NNP" : "Proper Noun - Singular",
    "NNPS" : "Proper Noun - Plural",
    "PDT" : "Predeterminer",
    "POS" : "Possessive",
    "PRP" : "Personal Pronoun",
    "PRP$" : "Possessive Pronoun",
    "RB" : "Adverb",
    "RBR" : "Adverb - Comparative",
    "RBS" : "Adverb - Superlative",
    "RP" : "Particle",
    "TO" : "To Go",
    "UH" : "Interjection",
    "VB" : "Verb - Base",
    "VBD" : "Verb - Past Tense",
    "VBG" : "Verb - Present Participle",
    "VBN" : "Verb - Past Participle",
    "VBP" : "Verb - Present",
    "VBZ" : "Verb - 3rd Person",
    "WDT" : "Wh-Determiner",
    "WP" : "Wh-Pronoun",
    "WP$" : "Possessive Wh-Pronoun",
    "WRB" : "Wh-Abverb",
}

chart_types = {
    'radarCharts',
    'ratioBarCharts',
    'textCharts'
}

profile_lookup = {
    "DESIGN_BOTTOM" : [
        {'radarCharts' : handle.iterative_words},
        {'radarCharts' : handle.learning_words},
        {'radarCharts' : handle.creative_words},
        {'textCharts'  : handle.curiosity_idx},
        {'textCharts'  : handle.sentiment_analysis},
        #{'radarCharts' : handle.phrase_check},
        {'radarCharts' : handle.timeliness_check},
        {'radarCharts' : handle.consistancy_check},
        {'radarCharts' : handle.motivation_check}
    ],
    "DESIGN_MIDDLE" : [
        {'radarCharts' : handle.lead_phrases},
        {'radarCharts' : handle.iterative_words},
        {'radarCharts' : handle.learning_words},
        {'radarCharts' : handle.creative_words},
        {'radarCharts' : handle.curiosity_idx},
        {'radarCharts' : handle.sentiment_analysis},
        #{'radarCharts' : handle.phrase_check},
        {'radarCharts' : handle.timeliness_check},
        {'radarCharts' : handle.consistancy_check},
        {'radarCharts' : handle.motivation_check}
    ],
    "DESIGN_TOP" : [
        {'radarCharts' : handle.manager_phrases},
        {'ratioBarCharts' : handle.i_vs_we},
        {'ratioBarCharts' : handle.past_vs_present},
        {'radarCharts' : handle.kt_check},
        {'textCharts' : handle.sentiment_analysis},
        #{'radarCharts' : handle.phrase_check},
        {'radarCharts' : handle.group_words}
    ],
    "SALES_BOTTOM" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "SALES_MIDDLE" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "SALES_TOP" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "OPERATIONS_BOTTOM" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "OPERATIONS_MIDDLE" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "OPERATIONS_TOP" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "MARKETTING_BOTTOM" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "MARKETTING_MIDDLE" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
    "MARKETTING_TOP" : [
        {'textCharts' : handle.i_vs_we},
        {'textCharts' : handle.past_vs_present},
    ],
}