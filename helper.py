#! /usr/bin/env python
# -*- coding: utf-8 -*-

LETTER_KA               = chr(0x1000)
LETTER_KHA              = chr(0x1001)
LETTER_GA               = chr(0x1002)
LETTER_GHA              = chr(0x1003)
LETTER_NGA              = chr(0x1004)
LETTER_CA               = chr(0x1005)
LETTER_CHA              = chr(0x1006)
LETTER_JA               = chr(0x1007)
LETTER_JHA              = chr(0x1008)
LETTER_NYA              = chr(0x1009)
LETTER_NNYA             = chr(0x100a)
LETTER_TTA              = chr(0x100b)
LETTER_TTHA             = chr(0x100c)
LETTER_DDA              = chr(0x100d)
LETTER_DDHA             = chr(0x100e)
LETTER_NNA              = chr(0x100f)
LETTER_TA               = chr(0x1010)
LETTER_THA              = chr(0x1011)
LETTER_DA               = chr(0x1012)
LETTER_DHA              = chr(0x1013)
LETTER_NA               = chr(0x1014)
LETTER_PA               = chr(0x1015)
LETTER_PHA              = chr(0x1016)
LETTER_BA               = chr(0x1017)
LETTER_BHA              = chr(0x1018)
LETTER_MA               = chr(0x1019)
LETTER_YA               = chr(0x101a)
LETTER_RA               = chr(0x101b)
LETTER_LA               = chr(0x101c)
LETTER_WA               = chr(0x101d)
LETTER_SA               = chr(0x101e)
LETTER_HA               = chr(0x101f)
LETTER_LLA              = chr(0x1020)
LETTER_A                = chr(0x1021)
LETTER_SHAN_A               = chr(0x1022)
LETTER_I                = chr(0x1023)
LETTER_II               = chr(0x1024)
LETTER_U                = chr(0x1025)
LETTER_UU               = chr(0x1026)
LETTER_E                = chr(0x1027)
LETTER_MON_E                = chr(0x1028)
LETTER_O                = chr(0x1029)
LETTER_AU               = chr(0x102a)
VOWEL_SIGN_TALL_AA              = chr(0x102b)
VOWEL_SIGN_AA               = chr(0x102c)
VOWEL_SIGN_I                = chr(0x102d)
VOWEL_SIGN_II               = chr(0x102e)
VOWEL_SIGN_U                = chr(0x102f)
VOWEL_SIGN_UU               = chr(0x1030)
VOWEL_SIGN_E                = chr(0x1031)
VOWEL_SIGN_AI               = chr(0x1032)
VOWEL_SIGN_MON_II               = chr(0x1033)
VOWEL_SIGN_MON_O                = chr(0x1034)
VOWEL_SIGN_E_ABOVE              = chr(0x1035)
SIGN_ANUSVARA               = chr(0x1036)
SIGN_DOT_BELOW              = chr(0x1037)
SIGN_VISARGA                = chr(0x1038)
SIGN_VIRAMA             = chr(0x1039)
SIGN_ASAT               = chr(0x103a)
CONSONANT_SIGN_MEDIAL_YA                = chr(0x103b)
CONSONANT_SIGN_MEDIAL_RA 	= chr(0x103c)
CONSONANT_SIGN_MEDIAL_WA                = chr(0x103d)
CONSONANT_SIGN_MEDIAL_HA 	= chr(0x103e)
LETTER_GREAT_SA             = chr(0x103f)
DIGIT_ZERO              = chr(0x1040)
DIGIT_ONE               = chr(0x1041)
DIGIT_TWO               = chr(0x1042)
DIGIT_THREE             = chr(0x1043)
DIGIT_FOUR              = chr(0x1044)
DIGIT_FIVE              = chr(0x1045)
DIGIT_SIX               = chr(0x1046)
DIGIT_SEVEN             = chr(0x1047)
DIGIT_EIGHT             = chr(0x1048)
DIGIT_NINE              = chr(0x1049)
SIGN_LITTLE_SECTION     = chr(0x104a)
SIGN_SECTION            = chr(0x104b)
SYMBOL_LOCATIVE         = chr(0x104c)
SYMBOL_COMPLETED        = chr(0x104d)
SYMBOL_AFOREMENTIONED   = chr(0x104e)
SYMBOL_GENITIVE         = chr(0x104f)

irange = lambda x,y,z=1: range(ord(x), ord(y)+1,z)

def ismyanmar (wc):
    return (wc >= LETTER_KA and wc <= SYMBOL_GENITIVE)

def ismyconsonant (wc):
    return ((wc >= LETTER_KA) and (wc <= LETTER_A)) or wc == LETTER_U

def ismymedial (wc):
    return (wc >= CONSONANT_SIGN_MEDIAL_YA) and (wc <= CONSONANT_SIGN_MEDIAL_HA)

def ismyvowel (wc):
    return ((wc >= VOWEL_SIGN_TALL_AA) and (wc <= VOWEL_SIGN_AI))

def ismytone (wc):
    return (wc == SIGN_DOT_BELOW or wc == SIGN_VISARGA)

def ismydiac (wc):
    return (ismyvowel (wc) or ismymedial (wc) or ismytone (wc) or
            wc == SIGN_ANUSVARA or wc == SIGN_ASAT)

def ismydigit (wc):
    return (wc >= DIGIT_ZERO  and wc <= DIGIT_NINE)

def ismypunct (wc):
    return (wc == SIGN_LITTLE_SECTION or wc == SIGN_SECTION)

def ismyindependvowel (wc):
    return (wc >= LETTER_I and wc <= LETTER_E) or wc == LETTER_O or wc == LETTER_AU

def ismyindependsymbol (wc):
    return (wc >= SYMBOL_LOCATIVE and
            wc <= SYMBOL_GENITIVE)

def ismyletter (wc):
    return (ismyconsonant (wc) or
            ismyindependvowel (wc) or
            wc == SYMBOL_AFOREMENTIONED)

def ismymark (wc):
    return (ismymedial (wc) or
            ismyvowel  (wc) or
            (wc >= SIGN_ANUSVARA and wc<= SIGN_ASAT))

def to_unicode_repr (string):
    x = [ r"\u%x" %ord(s) for s in string.decode("utf-8")]
    return  "".join (x)
