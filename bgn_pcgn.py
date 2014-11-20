#! /usr/bin/env python
# -*- coding: utf-8 -*-

from helper import *

data = {
    LETTER_KA  : "k",
    LETTER_KHA : "k",
    LETTER_GA  : "g",
    LETTER_GHA : "g",
    LETTER_NGA : "ng",
    LETTER_CA  : "s",
    LETTER_CHA : "s",
    LETTER_JA  : "z",
    LETTER_JHA : "z",
    LETTER_NNYA : "ny",
    LETTER_TA  : "t",
    LETTER_THA : "t",
    LETTER_TTA : "t",
    LETTER_TTHA: "t",
    LETTER_DA  : "d",
    LETTER_DHA : "d",
    LETTER_DDA : "d",
    LETTER_DDHA: "d",
    LETTER_NA  : "n",
    LETTER_NNA : "n",
    LETTER_PA  : "p",
    LETTER_PHA : "p",
    LETTER_BA  : "b",
    LETTER_BHA : "b",
    LETTER_MA  : "m",
    LETTER_YA  : "y",
    LETTER_RA  : "y",
    LETTER_LA  : "l",
    LETTER_LLA : "l",
    LETTER_WA  : "w",
    LETTER_SA  : "th",
    LETTER_HA  : "h",
    LETTER_A   : "a",

    CONSONANT_SIGN_MEDIAL_RA : "y",
    CONSONANT_SIGN_MEDIAL_YA : "y",
    CONSONANT_SIGN_MEDIAL_WA : "w",
    CONSONANT_SIGN_MEDIAL_YA + CONSONANT_SIGN_MEDIAL_WA : "yw",
    CONSONANT_SIGN_MEDIAL_RA + CONSONANT_SIGN_MEDIAL_WA : "yw",
    LETTER_NGA + CONSONANT_SIGN_MEDIAL_HA : "hng",
    LETTER_NNYA + CONSONANT_SIGN_MEDIAL_HA : "hny",
    LETTER_NA + CONSONANT_SIGN_MEDIAL_HA : "hn",
    LETTER_MA + CONSONANT_SIGN_MEDIAL_HA : "hm",
    LETTER_YA + CONSONANT_SIGN_MEDIAL_HA : "hy",
    LETTER_RA + CONSONANT_SIGN_MEDIAL_HA : "hy",
    LETTER_LA + CONSONANT_SIGN_MEDIAL_HA : "hl",
    LETTER_WA + CONSONANT_SIGN_MEDIAL_HA : "hw",
    LETTER_KHA + CONSONANT_SIGN_MEDIAL_YA : "ch",
    LETTER_KHA + CONSONANT_SIGN_MEDIAL_RA : "ch",
    LETTER_RA + CONSONANT_SIGN_MEDIAL_HA : "sh",
    LETTER_RA + CONSONANT_SIGN_MEDIAL_WA + CONSONANT_SIGN_MEDIAL_HA : "shw",

    VOWEL_SIGN_AA : "a",
    VOWEL_SIGN_TALL_AA: "a",
    VOWEL_SIGN_E : "e",
    VOWEL_SIGN_AI : "è",
    VOWEL_SIGN_I : "i",
    VOWEL_SIGN_II : "i",
    VOWEL_SIGN_I + VOWEL_SIGN_U : "o",
    VOWEL_SIGN_U : "u",
    VOWEL_SIGN_UU : "u",
    VOWEL_SIGN_E + VOWEL_SIGN_TALL_AA : "aw",
    VOWEL_SIGN_E + VOWEL_SIGN_AA : "aw",
    VOWEL_SIGN_E + VOWEL_SIGN_TALL_AA + SIGN_ASAT : "aw",
    VOWEL_SIGN_E + VOWEL_SIGN_AA + SIGN_ASAT : "aw",

    LETTER_KA + SIGN_ASAT : "et",
    VOWEL_SIGN_I + VOWEL_SIGN_U + LETTER_KA + SIGN_ASAT : "aik",
    VOWEL_SIGN_E + VOWEL_SIGN_TALL_AA + LETTER_KA + SIGN_ASAT : "auk",
    VOWEL_SIGN_E + VOWEL_SIGN_AA + LETTER_KA + SIGN_ASAT : "auk",
    LETTER_NGA + SIGN_ASAT : "in",
    VOWEL_SIGN_I + VOWEL_SIGN_U + LETTER_NGA + SIGN_ASAT : "aing",
    VOWEL_SIGN_E + VOWEL_SIGN_TALL_AA + LETTER_NGA + SIGN_ASAT : "aung",
    VOWEL_SIGN_E + VOWEL_SIGN_AA + LETTER_NGA + SIGN_ASAT : "aung",
    LETTER_CA + SIGN_ASAT : "it",
    LETTER_NNYA + SIGN_ASAT : "i",
    LETTER_TA + SIGN_ASAT : "at",
    VOWEL_SIGN_I + LETTER_TA + SIGN_ASAT : "eik",
    VOWEL_SIGN_U + LETTER_TA + SIGN_ASAT : "ôk",
    CONSONANT_SIGN_MEDIAL_WA + LETTER_TA + SIGN_ASAT : "ut",
    LETTER_WA + LETTER_TA + SIGN_ASAT : "wut",
    VOWEL_SIGN_E + LETTER_TA + SIGN_ASAT : "it",
    LETTER_NA + SIGN_ASAT : "an",
    VOWEL_SIGN_I + LETTER_NA + SIGN_ASAT : "ein",
    VOWEL_SIGN_U + LETTER_NA + SIGN_ASAT : "ôn",
    CONSONANT_SIGN_MEDIAL_WA + LETTER_NA + SIGN_ASAT : "un",
    LETTER_WA + LETTER_NA + SIGN_ASAT : "wun",
    LETTER_PA + SIGN_ASAT : "at",
    VOWEL_SIGN_I + LETTER_PA + SIGN_ASAT : "eik",
    VOWEL_SIGN_U + LETTER_PA + SIGN_ASAT : "ôk",
    CONSONANT_SIGN_MEDIAL_WA + LETTER_PA + SIGN_ASAT : "ut",
    LETTER_MA + SIGN_ASAT : "an",
    VOWEL_SIGN_I + LETTER_MA + SIGN_ASAT : "ein",
    VOWEL_SIGN_U + LETTER_MA + SIGN_ASAT : "ôn",
    CONSONANT_SIGN_MEDIAL_WA + LETTER_MA + SIGN_ASAT : "un",
    LETTER_WA + LETTER_MA + SIGN_ASAT : "wun",
    LETTER_YA + SIGN_ASAT : "è",
    LETTER_NYA + SIGN_ASAT : "in",
    SIGN_ANUSVARA : "an",

    LETTER_DA + SIGN_ASAT : "ad",
    LETTER_U + LETTER_KA + SIGN_ASAT : "uk",

    DIGIT_ZERO : "0",
    DIGIT_ONE : "1",
    DIGIT_TWO : "2",
    DIGIT_THREE : "3",
    DIGIT_FOUR : "4",
    DIGIT_FIVE : "5",
    DIGIT_SIX : "6",
    DIGIT_SEVEN : "7",
    DIGIT_EIGHT : "8",
    DIGIT_NINE : "9",

    LETTER_E : 'e',
    SYMBOL_GENITIVE : 'e',
    LETTER_I : 'i',
    LETTER_II : 'ii',
    LETTER_U: 'u',
    LETTER_UU: 'u',

    LETTER_O : "aw",
    LETTER_AU : 'aw',
    LETTER_O + VOWEL_SIGN_E + VOWEL_SIGN_AA : 'aw',

    SIGN_VISARGA : "",
    SIGN_DOT_BELOW: "",
}